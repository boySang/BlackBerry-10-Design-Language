#!/usr/bin/env python3
"""检查轻量规范的结构、来源与引用；不会自动下载外部资料。"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PAPER_URL = 'https://developer.blackberry.com/devzone/files/design/bb10/UI_Guidelines_BlackBerry_10.pdf'
parser = argparse.ArgumentParser(description='检查中文设计规范及可选的本地PDF')
parser.add_argument('--pdf', type=Path, help='另行下载的官方PDF路径，可选')
args = parser.parse_args()
errors = []

def require(ok, message):
    if not ok:
        errors.append(message)

def read_json(name):
    try:
        return json.loads((ROOT / name).read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        errors.append(f'无法读取JSON：{name}，{exc}')
        return None

def check_structure():
    source = read_json('tokens.source.json')
    kit = read_json('tokens.kit-reference.json')
    visual = read_json('tokens.visual-profile.json')
    profile = read_json('PROJECT_PROFILE.template.json')
    coverage = read_json('source-map.json')
    if any(x is None for x in (source, kit, visual, profile, coverage)):
        return {}
    require(source['source']['url'] == PAPER_URL, '官方PDF链接与预期不符')
    require(source['source']['file'] == PAPER_URL, '轻量版来源标识必须指向官方PDF')
    require(source['source']['pages'] == 156, '官方PDF页数不符')
    require(source['distribution'] == visual['distribution'] == 'external-references', '分发方式不一致')
    require(visual['packageVersion'] == source['packageVersion'] == kit['packageVersion'] == profile['designLanguageVersion'], '版本不一致')
    require(visual['sourcePdfSha256'] == source['source']['sha256'], '原图量测与来源PDF哈希不一致')
    require(re.fullmatch(r'[0-9a-f]{64}', source['source']['sha256']) is not None, 'PDF哈希格式不正确')
    rules = set(re.findall(r'`([A-Z]+-\d+)`', (ROOT / 'DESIGN_LANGUAGE.md').read_text(encoding='utf-8')))
    for name, token in source['tokens'].items():
        require(token.get('value') is not None, f'来源参数缺值：{name}')
        require(bool(token.get('unit')), f'来源参数缺单位：{name}')
        require(bool(token.get('pages')), f'来源参数缺页码：{name}')
        require(all(type(p) is int and 1 <= p <= 156 for p in token.get('pages', [])), f'来源页码无效：{name}')
        require(token.get('evidence') in ('source-text', 'source-figure'), f'来源证据混用：{name}')
        if token.get('rule'):
            require(token['rule'] in rules, f'来源规则入口不存在：{name}')
    for name, token in kit['tokens'].items():
        require(token.get('evidence') == 'kit-reference', f'第三方证据类别缺失：{name}')
        require(token.get('approvedForProject') is False, f'第三方候选被当成批准值：{name}')
        require(kit['source']['commit'] in token.get('source', ''), f'第三方链接未固定提交：{name}')
    for name, token in profile['projectTokens'].items():
        require(token.get('value') is None and token.get('status') == 'unresolved', f'项目模板被写入确定值：{name}')
    pages = []
    for section in coverage['sections']:
        start, end = section['pages']
        require(start <= end, f'章节页码倒置：{section["heading"]}')
        require(all(rule in rules or rule in ('SOURCE_MAP', 'SOURCES') for rule in section.get('rules', [])), f'章节规则入口缺失：{section["heading"]}')
        pages.extend(range(start, end + 1))
    require(sorted(pages) == list(range(1, 157)), '章节覆盖缺页或重叠')
    for name, figure in visual['figures'].items():
        expected = PAPER_URL + '#page=' + str(figure['page'])
        require(figure['file'] == figure['sourceUrl'] == expected, f'图示外部页码链接不符：{name}')
        require(1 <= figure['page'] <= 156, f'图示页码无效：{name}')
        require(re.fullmatch(r'[0-9a-f]{64}', figure['extractedImageSha256']) is not None, f'原提取图哈希格式无效：{name}')
    for name, value in visual['measurements'].items():
        require(value['evidence'] == 'derived-from-source-figure', f'量测来源类别错误：{name}')
        require(value['figure'] in visual['figures'], f'量测图示索引缺失：{name}')
        require(value['sourceFigureWidth'] > 0, f'量测画布宽度无效：{name}')
        if value['sourceFigureWidth'] > 0:
            require(abs(value['value'] - value['measuredPixels'] / value['sourceFigureWidth']) < 1e-10, f'归一化比例不符：{name}')
    checked_pdf = False
    if args.pdf:
        require(args.pdf.is_file(), '指定的本地PDF不存在')
        if args.pdf.is_file():
            require(hashlib.sha256(args.pdf.read_bytes()).hexdigest() == source['source']['sha256'], '指定PDF与固定来源哈希不一致')
            checked_pdf = True
    return dict(source_tokens=len(source['tokens']), kit_candidate_tokens=len(kit['tokens']),
                unresolved_project_tokens=len(profile['projectTokens']), source_pages_covered=len(pages),
                rule_ids=len(rules), visual_measurements=len(visual['measurements']),
                visual_source_figures=len(visual['figures']), source_pdf_sha256=source['source']['sha256'],
                local_pdf_checked=checked_pdf)

try:
    result = check_structure()
except (KeyError, TypeError, ValueError, OSError) as exc:
    errors.append(f'数据结构异常：{exc}')
    result = {}
local_links = external_links = total_bytes = file_count = 0
for file in ROOT.rglob('*'):
    if not file.is_file() or '.git' in file.relative_to(ROOT).parts or '__pycache__' in file.parts:
        continue
    if file.name != 'validation-report.json':
        file_count += 1
        total_bytes += file.stat().st_size
    require(file.stat().st_size < 1024 * 1024, f'文件超过轻量上限：{file.relative_to(ROOT)}')
    require(file.suffix.lower() not in {'.pdf', '.png', '.jpg', '.jpeg', '.zip', '.ttf', '.otf', '.woff', '.woff2'}, f'混入外部资料或二进制资产：{file.name}')
    try:
        text = file.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        errors.append(f'存在非UTF-8文本文件：{file.name}')
        continue
    if file.suffix in ('.md', '.json'):
        require('/Users/' not in text and 'file://' not in text, f'包含本机路径：{file.name}')
    if file.suffix == '.json':
        try:
            json.loads(text)
        except ValueError as exc:
            errors.append(f'无法解析JSON：{file.name}，{exc}')
    if file.suffix == '.md':
        require('酒鬼成员' in text, f'缺少整理署名：{file.name}')
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
            parts = urlsplit(target)
            if parts.scheme:
                require(parts.scheme == 'https', f'引用不使用HTTPS：{file.name}')
                external_links += 1
            elif not target.startswith('#'):
                require((file.parent / unquote(parts.path)).resolve().is_file(), f'相对引用不存在：{file.name}：{target}')
                local_links += 1
require(total_bytes < 1024 * 1024, '规范文本总量超过1MiB，请检查是否误入大文件')
report = dict(status='pass' if not errors else 'fail', **result,
              local_links_checked=local_links, external_links_checked=external_links,
              published_files=file_count, published_bytes=total_bytes,
              errors=errors, limits=['生成的校验报告不计入文件数量和字节统计。', '不自动下载或验证外链可用性。', '不证明目标应用、第三方库或实机已通过验收。'])
print(json.dumps(report, ensure_ascii=False, indent=2))
sys.exit(bool(errors))
