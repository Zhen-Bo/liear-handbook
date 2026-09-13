"""Inventory Markdown links in a complete review copy, preserving historical gaps."""
import argparse
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt


def inspect(root):
    root = root.resolve()
    parser = MarkdownIt()
    if (root / '.git').exists():
        names = subprocess.check_output(['git', '-c', 'core.quotepath=false', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'], cwd=root).decode('utf-8').split('\0')
        files = sorted({root / name for name in names if name.endswith('.md')})
    else:
        files = sorted(root.rglob('*.md'))
    anchors = {}
    links = {}
    for path in files:
        tokens = parser.parse(path.read_text(encoding='utf-8-sig'))
        found, references, counts = set(), [], {}
        for i, token in enumerate(tokens):
            if token.type == 'heading_open':
                heading = tokens[i + 1].content
                slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
                count = counts.get(slug, 0)
                found.add(slug if count == 0 else f'{slug}-{count}')
                counts[slug] = count + 1
            for child in token.children or []:
                if child.type == 'link_open':
                    references.append(child.attrGet('href'))
                elif child.type == 'image':
                    references.append(child.attrGet('src'))
        anchors[path] = found
        links[path] = references
    gaps, checked, simulated = [], 0, []
    for path, references in links.items():
        for reference in references:
            parsed = urlsplit(reference)
            if parsed.scheme or parsed.netloc:
                continue
            checked += 1
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if path.relative_to(root).as_posix() == 'validation/recovery/raw/permission-body.md' and reference == 'artifacts/auth-report.md':
                simulated.append({'file': path.relative_to(root).as_posix(), 'link': reference, 'reason': 'Synthetic remote artifact referenced by the permission-error fixture'})
                continue
            reason = None
            if not target.is_relative_to(root):
                reason = 'outside repository'
            elif not target.exists():
                reason = 'missing target'
            elif parsed.fragment and unquote(parsed.fragment) not in anchors.get(target, set()):
                reason = 'missing anchor'
            if reason:
                gaps.append({'file': path.relative_to(root).as_posix(), 'link': reference, 'reason': reason})
    return {'markdown_files': len(files), 'local_links': checked, 'simulated_artifact_links': simulated, 'gaps': gaps}


if __name__ == '__main__':
    cli = argparse.ArgumentParser()
    cli.add_argument('root', type=Path)
    cli.add_argument('--output', type=Path)
    args = cli.parse_args()
    result = inspect(args.root)
    if args.output:
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(bool(result['gaps']))
