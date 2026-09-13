"""Check a standalone skill's Markdown link closure and source preservation.

Markdown tokens (including reference links) are parsed with markdown-it-py.
This checks document structure, not Agent behavior or remote URL availability.
"""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from collections import Counter
import argparse, hashlib, json, re, unicodedata
from markdown_it import MarkdownIt

def slug(text):
    text = text.lower()
    return ''.join(c for c in text if c in '-_' or c.isspace() or unicodedata.category(c)[0] in 'LN').replace(' ', '-')

def inspect(root):
    root=root.resolve()
    parser=MarkdownIt('commonmark',{'html':True}).enable('table')
    files=sorted(root.rglob('*.md'))
    anchors={}; links={}; errors=[]; remote=0; local=0
    for p in files:
        tokens=parser.parse(p.read_text(encoding='utf-8-sig'))
        counts=Counter(); found=set(); refs=[]
        for i,t in enumerate(tokens):
            if t.type=='heading_open':
                inline=tokens[i+1]
                plain=''.join(c.content for c in (inline.children or []) if c.type in ['text','code_inline','html_inline'])
                s=slug(re.sub('<[^>]*>','',plain))
                actual=s if counts[s]==0 else f'{s}-{counts[s]}'
                found.add(actual);counts[s]+=1
            for c in t.children or []:
                if c.type=='link_open':refs.append(c.attrGet('href'))
                elif c.type=='image': refs.append(c.attrGet('src'))
            if t.type in ['html_inline','html_block']:
                found.update(re.findall(r'(?:id|name)=[\"\']([^\"\']+)',t.content))
        anchors[p]=found;links[p]=refs
    edges={p:set() for p in files}
    for p,refs in links.items():
        for ref in refs:
            parsed=urlsplit(ref)
            if parsed.scheme or parsed.netloc:remote+=1;continue
            local+=1
            target=(p.parent/unquote(parsed.path)).resolve() if parsed.path else p
            if not target.is_relative_to(root):errors.append(f'{p.name}: escapes package: {ref}');continue
            if not target.is_file():errors.append(f'{p.name}: missing file: {ref}');continue
            if parsed.fragment and unquote(parsed.fragment) not in anchors.get(target,set()):
                errors.append(f'{p.name}: missing anchor: {ref}')
            if target in edges:edges[p].add(target)
    entry=root/'SKILL.md'; reachable=set();queue=[entry]
    while queue:
        p=queue.pop()
        if p in reachable:continue
        reachable.add(p);queue.extend(edges.get(p,()))
    missing=set(files)-reachable
    errors.extend('unreachable: '+str(p.relative_to(root)) for p in sorted(missing))
    direct=edges.get(entry,set())
    errors.extend('not directly routed: '+str(p.relative_to(root)) for p in files if p!=entry and p not in direct)
    for p in files:
        t=p.read_text(encoding='utf-8-sig')
        for pattern in [r'KEV-\d+',r'KevinSun',r'AGENTS\.md',r'uploads\.linear\.app',r'[A-Z]:[/\\]']:
            if re.search(pattern,t):errors.append(f'{p.name}: personal/package-external metadata: {pattern}')
    return {'files':len(files),'local_links':local,'remote_links':remote,'reachable':len(reachable),'directly_routed':len(direct-{entry}),'errors':errors}

if __name__=='__main__':
    cli=argparse.ArgumentParser();cli.add_argument('root',type=Path);cli.add_argument('--source-manifest',type=Path);cli.add_argument('--source-revisions',type=Path);cli.add_argument('--output',type=Path)
    args=cli.parse_args();result=inspect(args.root)
    if args.source_manifest:
        manifest=json.loads(args.source_manifest.read_text(encoding='utf-8'))
        repo=args.source_manifest.parent.parent
        revisions=json.loads(args.source_revisions.read_text(encoding='utf-8')) if args.source_revisions else {}
        changed=[];revised=[]
        for name,h in manifest.items():
            actual=hashlib.sha256((repo/name).read_bytes()).hexdigest() if (repo/name).is_file() else None
            if actual==h:continue
            revision=revisions.get(name,{})
            if revision.get('original_sha256')==h and revision.get('current_sha256')==actual:revised.append(name)
            else:changed.append(name)
        result['source_files']=len(manifest);result['unchanged_sources']=len(manifest)-len(revised)-len(changed)
        result['revised_sources']=revised;result['unexpected_changed_sources']=changed
        result['errors']+=['unexpected source change: '+x for x in changed]
    if args.output:args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    raise SystemExit(bool(result['errors']))
