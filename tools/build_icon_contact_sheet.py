#!/usr/bin/env python3
"""生成不联网的图标联系表；含原图的输出只保存在本机或被忽略的artifacts目录。"""
from pathlib import Path
import argparse
import base64
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]

PAGE = r'''<!doctype html>
<html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="referrer" content="no-referrer"><title>BlackBerry 10 图标联系表</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f1f3f3;color:#23282a;font:14px/1.6 system-ui,sans-serif}header{background:#232628;color:#fff;border-bottom:3px solid #00a8df;padding:24px max(24px,calc((100vw - 1320px)/2))}h1{font-size:27px;font-weight:550;line-height:1.3;margin:0 0 8px}header p{max-width:980px;color:#c9d0d3;margin:6px 0}main{max-width:1368px;margin:auto;padding:20px 24px}.controls{display:flex;flex-wrap:wrap;gap:12px;padding:15px;background:#fff;border:1px solid #d4dadd;margin-bottom:14px}.controls label{display:flex;gap:8px;align-items:center}input,select,button{font:inherit;min-height:40px;border:1px solid #aab3b8;background:#fff;color:#23282a;padding:6px 10px;border-radius:3px}input[type=search]{width:min(400px,65vw)}input[type=file]{max-width:100%;font-size:12px}button{cursor:pointer}button:active{background:#d7eef7}a{color:#006f9a;text-underline-offset:3px}a:focus-visible,input:focus-visible,button:focus-visible,select:focus-visible{outline:3px solid #00a8df;outline-offset:2px}.status{margin:12px 0;color:#4d5b62}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(225px,1fr));gap:14px}.card{background:#fff;border:1px solid #cfd6da;border-radius:4px;overflow:hidden;min-width:0}.stage{height:132px;background:#242628;display:flex;align-items:center;justify-content:center;border-top:3px solid #00a8df}.light .stage{background:#e7eaeb}.stage img{display:block;max-width:104px;max-height:104px;object-fit:contain}.missing{color:#b8c4c9;font-size:12px}.light .missing{color:#596b75}.info{padding:13px}h2{font-size:14px;overflow-wrap:anywhere;margin:0 0 7px;line-height:1.45}.summary{font-size:14px;min-height:45px;margin:0 0 9px}.meta{color:#62717a;font-size:12px;overflow-wrap:anywhere;margin:6px 0}.links{display:flex;gap:15px;flex-wrap:wrap;margin-top:9px;font-size:12px}.badge{color:#007ea8;font-size:12px}.empty{padding:30px;background:white;border:1px solid #cfd6da}footer{margin-top:24px;border-top:1px solid #cfd6da;padding-top:16px;color:#62717a;font-size:12px}@media(max-width:540px){header{padding:18px}main{padding:15px}.controls{padding:12px}.controls label{width:100%;justify-content:space-between}.controls select{max-width:70%}.controls label:last-child{flex-direction:column;align-items:stretch}.controls label:last-child input{width:100%;max-width:100%}.grid{grid-template-columns:1fr 1fr;gap:9px}.stage{height:112px}.info{padding:10px}.summary{min-height:68px}h1{font-size:22px}}@media print{.controls{display:none}header{background:white;color:#222}header p{color:#444}.grid{grid-template-columns:repeat(3,1fr)}.card{break-inside:avoid}.stage{print-color-adjust:exact}}
</style>
<header><h1>BlackBerry 10 · 图标联系表</h1><p>121 枚历史 Action 图标与 34 个去重后的仓库样例源文件。分类与中文释义用于检索，不把样例图形认定为系统标准。</p><p>整理作者：酒鬼成员。__DISPLAY_SCOPE__ 选择本机PNG目录后按SHA-256匹配显示；不上传文件、不自动请求远程图片。样例原许可随仓库保留。</p></header>
<main><div class="controls"><label>查找<input id="query" type="search" placeholder="文件名、中文语义或类别"></label><label>分类<select id="category"><option value="">全部分类</option></select></label><label>来源<select id="source"><option value="">全部来源</option></select></label><button id="background" type="button">切换样例背景</button><label>加载本机原图<input id="files" type="file" accept="image/png" multiple webkitdirectory></label></div><p id="status" class="status" role="status" aria-live="polite"></p><section class="grid" id="grid" aria-label="图标目录"></section><footer>历史包无独立再分发许可记录；官方仓库可能包含第三方素材。原图使用范围请查看来源与许可说明。联系表不改色、不描摹、不裁剪原PNG；页面显示尺寸可缩放，原文件像素保持不变。没有本机原图时可用“来源”回到固定版本或历史存档。</footer></main>
<script id="catalog" type="application/json">__CATALOG__</script>
<script id="previews" type="application/json">__PREVIEWS__</script>
<script>
'use strict';
const catalog=JSON.parse(document.querySelector('#catalog').textContent);
const previews=new Map(Object.entries(JSON.parse(document.querySelector('#previews').textContent)));
const query=document.querySelector('#query'),category=document.querySelector('#category'),source=document.querySelector('#source'),grid=document.querySelector('#grid'),status=document.querySelector('#status');
let loadingMessage='',loadingGeneration=0;
for(const [key,label] of Object.entries(catalog.categories)){const option=document.createElement('option');option.value=key;option.textContent=label;category.append(option)}
for(const [key,value] of Object.entries(catalog.sources)){const option=document.createElement('option');option.value=key;option.textContent=value.label;source.append(option)}
function node(tag,className,text){const el=document.createElement(tag);if(className)el.className=className;if(text!==undefined)el.textContent=text;return el}
function link(text,url){const el=node('a','',text);el.href=url;el.target='_blank';el.rel='noopener noreferrer';return el}
function render(){
 const term=query.value.trim().toLocaleLowerCase();
 const rank={official_action_pack_2013:0,cascades_samples:1,bbui_sample:2};
 const entries=catalog.entries.filter(e=>(!category.value||e.category===category.value)&&(!source.value||e.sourceId===source.value)&&(!term||[e.originalFilename,e.sourcePath,e.semanticSummaryZh,catalog.categories[e.category]].join(' ').toLocaleLowerCase().includes(term))).sort((a,b)=>Number(previews.has(b.sha256))-Number(previews.has(a.sha256))||rank[a.sourceId]-rank[b.sourceId]||a.sourcePath.localeCompare(b.sourcePath));
 grid.replaceChildren();
 for(const e of entries){const card=node('article','card');const stage=node('div','stage');const preview=previews.get(e.sha256);
  if(preview){const img=node('img');img.src=preview;img.alt=e.semanticSummaryZh;img.width=e.sizePx[0];img.height=e.sizePx[1];stage.append(img)}else stage.append(node('span','missing','等待本机原图'));
  const info=node('div','info');info.append(node('span','badge',catalog.categories[e.category]),node('h2','',e.originalFilename),node('p','summary',e.semanticSummaryZh),node('p','meta',catalog.sources[e.sourceId].label),node('p','meta',`${e.sizePx[0]} × ${e.sizePx[1]} px · ${e.bytes} bytes`),node('p','meta',e.sourcePath));
  info.append(node('p','meta',e.distribution==='bundled-unmodified'?'随库原图 · Apache-2.0':'仅资料索引 · 原图使用按来源处理'));
  const digest=node('p','meta',`SHA-256 ${e.sha256.slice(0,16)}…`);digest.title=e.sha256;info.append(digest);
  const links=node('div','links');links.append(link('来源',e.sourceUrl));if(preview){const original=link('保存原PNG',preview);original.download=e.originalFilename;links.append(original)}info.append(links);card.append(stage,info);grid.append(card)
 }
 if(!entries.length)grid.append(node('p','empty','没有匹配项，请清除关键词或调整筛选。'));
 status.textContent=`显示 ${entries.length} / ${catalog.entries.length} 条；原图已匹配 ${catalog.entries.filter(e=>previews.has(e.sha256)).length} / ${catalog.entries.length}。${loadingMessage}`;
}
query.addEventListener('input',render);category.addEventListener('change',render);source.addEventListener('change',render);
document.querySelector('#background').addEventListener('click',()=>grid.classList.toggle('light'));
document.querySelector('#files').addEventListener('change',async event=>{
 const generation=++loadingGeneration;loadingMessage='正在本机校验PNG…';render();
 if(!globalThis.crypto?.subtle){loadingMessage='当前浏览器不能校验SHA-256，请改用本机生成脚本。';render();return}
 const expected=new Map(catalog.entries.map(e=>[e.sha256,e]));let skipped=0;const sizes=new Set(catalog.entries.map(e=>e.bytes));
 try{for(const file of event.target.files){if(generation!==loadingGeneration)return;if(!file.name.toLowerCase().endsWith('.png')||!sizes.has(file.size)){skipped++;continue}const data=await file.arrayBuffer();if(generation!==loadingGeneration)return;const digest=Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',data)),v=>v.toString(16).padStart(2,'0')).join('');if(generation!==loadingGeneration)return;const e=expected.get(digest);if(!e){skipped++;continue}const current=previews.get(digest);if(current?.startsWith('blob:'))URL.revokeObjectURL(current);previews.set(digest,URL.createObjectURL(new Blob([data],{type:'image/png'})))}loadingMessage=`已完成本机校验；忽略 ${skipped} 个非目录匹配文件。`}catch{loadingMessage='有文件无法读取；已成功匹配的原图仍保留。'}if(generation===loadingGeneration)render();
});
render();
</script></html>'''


def safe_json(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')


def collect(catalog, roots, action_zip=None):
    expected = {e['sha256']: e for e in catalog['entries']}
    previews = {}
    sizes = {e['bytes'] for e in expected.values()}
    def accept(data):
        digest = hashlib.sha256(data).hexdigest()
        if digest in expected:
            previews[digest] = 'data:image/png;base64,' + base64.b64encode(data).decode('ascii')
    for e in catalog['entries']:
        if e['distribution'] == 'bundled-unmodified':
            file = (ROOT / 'icons' / e['assetPath']).resolve()
            if not file.is_relative_to(ROOT / 'icons/assets'):
                raise ValueError('不安全的随库资源路径')
            raw = file.read_bytes()
            if hashlib.sha256(raw).hexdigest() != e['sha256']:
                raise ValueError('随库样例原图哈希不符')
            accept(raw)
    for root in roots:
        if not root.is_dir():
            raise ValueError('原图目录不存在')
        for file in root.rglob('*'):
            if file.is_file() and file.suffix.lower() == '.png' and file.stat().st_size in sizes:
                accept(file.read_bytes())
    if action_zip:
        package = catalog['sources']['official_action_pack_2013']
        data = action_zip.read_bytes()
        if hashlib.sha256(data).hexdigest() != package['sha256']:
            raise ValueError('Action ZIP与固定来源哈希不一致')
        with zipfile.ZipFile(action_zip) as archive:
            if archive.testzip() is not None:
                raise ValueError('Action ZIP未通过CRC检查')
            for e in catalog['entries']:
                if e['sourceId'] == 'official_action_pack_2013':
                    raw = archive.read(e['sourcePath'])
                    if hashlib.sha256(raw).hexdigest() != e['sha256']:
                        raise ValueError('Action ZIP成员与索引不一致')
                    accept(raw)
    return previews


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--asset-root', type=Path, action='append', default=[], help='本机已取得的原PNG目录，可重复指定')
    parser.add_argument('--action-zip', type=Path, help='本机已取得的历史Action原ZIP')
    parser.add_argument('--output', type=Path, default=ROOT / 'artifacts/icon-contact-sheet.html', help='输出HTML；默认在被忽略的artifacts中')
    args = parser.parse_args()
    catalog = json.loads((ROOT / 'icons/catalog.json').read_text(encoding='utf-8'))
    try:
        previews = collect(catalog, args.asset_root, args.action_zip)
        output = args.output.resolve()
        distributable = {e['sha256'] for e in catalog['entries'] if e['distribution'] == 'bundled-unmodified'}
        if set(previews) - distributable and output.is_relative_to(ROOT) and not output.is_relative_to(ROOT / 'artifacts'):
            raise ValueError('含未随库分发原图的联系表只能输出到仓库外或被忽略的artifacts目录')
        scope = f'本机参考版已包含{len(previews)}枚原图；请勿将本文件上传公开仓库。' if set(previews) - distributable else '公开目录版自带6个Apache-2.0样例原图，其余149条仅提供资料。'
        page = PAGE.replace('__CATALOG__', safe_json(catalog)).replace('__PREVIEWS__', safe_json(previews)).replace('__DISPLAY_SCOPE__', scope)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(page, encoding='utf-8')
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        parser.exit(1, f'生成失败：{error}\n')
    print(json.dumps({'entries': len(catalog['entries']), 'matched': len(previews), 'outputContainsOriginals': bool(previews)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
