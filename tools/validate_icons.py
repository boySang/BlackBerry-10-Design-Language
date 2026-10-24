#!/usr/bin/env python3
"""核对图标索引结构；可额外核对本机原PNG与历史ZIP，不联网下载。"""
from collections import Counter
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit
import argparse
import hashlib
import json
import re
import struct
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def validate_catalog(root=ROOT, asset_root=None, action_zip=None):
    errors = []
    def check(condition, text):
        if not condition:
            errors.append(text)
    data = json.loads((root / 'icons/catalog.json').read_text(encoding='utf-8'))
    entries = data['entries']
    check(data['packageVersion'] == json.loads((root / 'tokens.source.json').read_text())['packageVersion'], '图标目录版本与规范不一致')
    check(len(entries) == 155 and data['counts']['entries'] == 155, '图标目录数量不是155')
    check(len({e['id'] for e in entries}) == len(entries), '图标ID重复')
    counts = dict(Counter(e['sourceId'] for e in entries))
    check(counts == data['counts']['sourceCounts'] == {'official_action_pack_2013': 121, 'cascades_samples': 6, 'bbui_sample': 28}, '来源计数不符')
    check(dict(Counter(e['category'] for e in entries)) == data['counts']['categoryCounts'], '分类计数不符')
    check(len({e['sha256'] for e in entries}) == data['counts']['uniqueContentHashes'] == 155, '图标哈希重复或数量不符')
    for e in entries:
        check(e['category'] in data['categories'], '未定义的图标分类')
        check(e['sourceId'] in data['sources'] and e['sourceId'] != 'subway', '官方来源目录混入其他来源')
        check(e['originalFilename'] == PurePosixPath(e['sourcePath']).name, '没有保留原文件名')
        check(not PurePosixPath(e['sourcePath']).is_absolute() and '..' not in PurePosixPath(e['sourcePath']).parts, '不安全的来源路径')
        check(e['id'] == e['sourceId'] + ':' + e['sourcePath'], '图标ID与原路径不符')
        check(re.fullmatch('[0-9a-f]{64}', e['sha256']) is not None, '图标SHA-256格式错误')
        check(len(e['sizePx']) == 2 and all(type(v) is int and 0 < v < 4096 for v in e['sizePx']), 'PNG尺寸错误')
        check(type(e['bytes']) is int and e['bytes'] > 0, '图标字节数错误')
        check(bool(e['semanticSummaryZh']) and bool(e['semanticEvidence']), '图标缺少语义依据')
        check(urlsplit(e['sourceUrl']).scheme == 'https', '图标来源链接不是HTTPS')
        if e['sourceId'] == 'cascades_samples':
            check(e['distribution'] == 'bundled-unmodified' and e['licenseStatus'] == 'Apache-2.0-project-license', '样例原图缺少明确许可映射')
            check(e['assetPath'] == 'assets/cascades_samples/' + e['sourcePath'], '随库资源路径不符')
            file = root / 'icons' / e['assetPath']
            check(file.is_file(), '随库样例原图缺失')
            if file.is_file():
                raw = file.read_bytes()
                check(hashlib.sha256(raw).hexdigest() == e['sha256'] and len(raw) == e['bytes'], '随库原图字节改变')
                check(len(raw) >= 24 and raw[:8] == b'\x89PNG\r\n\x1a\n', '随库文件不是有效PNG头')
                if len(raw) >= 24:
                    check(list(struct.unpack('>II', raw[16:24])) == e['sizePx'], '随库原图尺寸改变')
                check(hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == e['gitBlob'], '样例Git blob不符')
            license_path = root / 'icons' / e['licensePath']
            check(license_path.is_file(), '随库样例缺少原许可证')
        else:
            check(e['distribution'] == 'metadata-only' and 'assetPath' not in e, '不应随库分发的原图被捆绑')
        source = data['sources'][e['sourceId']]
        if e['sourceId'] != 'official_action_pack_2013':
            check(re.fullmatch('[0-9a-f]{40}', source['commit']) is not None and source['commit'] in e['sourceUrl'], '样例链接未固定完整提交')
    for item in data['sources']['cascades_samples']['licenseEvidence'].values():
        file = root / 'icons' / item['path']
        check(file.is_file() and hashlib.sha256(file.read_bytes()).hexdigest() == item['sha256'], '原LICENSE字节不符')
    check(sum(e['distribution'] == 'bundled-unmodified' for e in entries) == data['counts']['bundledOriginalPngs'] == 6, '随库原PNG计数不符')
    check(sum(e['distribution'] == 'metadata-only' for e in entries) == data['counts']['metadataOnlyEntries'] == 149, '仅索引计数不符')
    expected = {e['sha256']: e for e in entries}
    matched = set()
    if asset_root:
        check(asset_root.is_dir(), '本机原图目录不存在')
        for file in asset_root.rglob('*.png'):
            raw = file.read_bytes()
            digest = hashlib.sha256(raw).hexdigest()
            if digest not in expected:
                continue
            e = expected[digest]
            check(raw[:8] == b'\x89PNG\r\n\x1a\n' and len(raw) >= 24, '匹配文件不是PNG')
            if len(raw) >= 24:
                check(list(struct.unpack('>II', raw[16:24])) == e['sizePx'], '本机原图尺寸不符')
            check(len(raw) == e['bytes'], '本机原图字节数不符')
            matched.add(digest)
        check(len(matched) == len(expected), '本机原图不完整或有字节变化')
    if action_zip:
        source = data['sources']['official_action_pack_2013']
        raw = action_zip.read_bytes()
        check(len(raw) == source['bytes'] and hashlib.sha256(raw).hexdigest() == source['sha256'], 'Action ZIP哈希或大小不符')
        if not errors:
            with zipfile.ZipFile(action_zip) as archive:
                check(archive.testzip() is None and len(archive.infolist()) == source['zipEntryCount'], 'Action ZIP CRC或成员数不符')
                check(len([n for n in archive.namelist() if n.endswith('.png')]) == 121, 'Action PNG成员不完整')
                for e in entries:
                    if e['sourceId'] == 'official_action_pack_2013':
                        check(hashlib.sha256(archive.read(e['sourcePath'])).hexdigest() == e['sha256'], 'Action PNG与原ZIP不一致')
                xls = archive.read(source['xls']['filename'])
                check(hashlib.sha256(xls).hexdigest() == source['xls']['sha256'] and len(xls) == source['xls']['bytes'], 'XLS与来源校验不符')
    return {'entries': len(entries), 'sourceCounts': counts, 'matchedOriginals': len(matched), 'actionZipChecked': bool(action_zip), 'errors': errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--asset-root', type=Path)
    parser.add_argument('--action-zip', type=Path)
    args = parser.parse_args()
    try:
        result = validate_catalog(asset_root=args.asset_root, action_zip=args.action_zip)
    except (OSError, KeyError, TypeError, ValueError, zipfile.BadZipFile) as error:
        result = {'errors': [str(error)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return bool(result['errors'])


if __name__ == '__main__':
    raise SystemExit(main())
