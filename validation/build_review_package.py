"""Build and verify the complete local review deliverable."""
import hashlib
import json
import tempfile
import zipfile
import subprocess
from pathlib import Path

from check_repository_links import inspect

ROOT = Path(__file__).resolve().parents[1]
DIRECTORIES = {'design', 'docs', 'examples', 'handbook', 'research', 'skills', 'templates', 'validation'}
EXCLUDED_PARTS = {'.git', '.tmp', 'Temp', 'temp', '__pycache__', 'drafts', 'deliverables'}
MANIFEST = ROOT / 'validation/generated/repository-manifest.json'
LINKS = ROOT / 'validation/generated/repository-links.json'
OUTPUT = ROOT / 'deliverables/linear-handbook-review.zip'


def payload_files():
    names = subprocess.check_output(['git', '-c', 'core.quotepath=false', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'], cwd=ROOT).decode('utf-8').split('\0')
    return sorted({ROOT / name for name in names if name and (ROOT / name).is_file()})


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    OUTPUT.parent.mkdir(exist_ok=True)
    for metadata in (MANIFEST, LINKS):
        if not metadata.exists():
            save(metadata, {})
    with tempfile.TemporaryDirectory(prefix='linear-handbook-review-') as temporary:
        staging = Path(temporary) / 'source'
        staging.mkdir()
        for path in payload_files():
            target = staging / path.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(path.read_bytes())
        links = inspect(staging)
        save(LINKS, links)
        files = [path for path in payload_files() if path != MANIFEST]
        manifest = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
        save(MANIFEST, {'algorithm': 'SHA-256', 'scope': 'All payload files except this manifest', 'files': manifest})
        files = payload_files()
        with zipfile.ZipFile(OUTPUT, 'w', zipfile.ZIP_DEFLATED) as archive:
            for path in files:
                archive.write(path, 'linear-handbook/' + path.relative_to(ROOT).as_posix())
        extracted = Path(temporary) / 'extracted'
        with zipfile.ZipFile(OUTPUT) as archive:
            archive.extractall(extracted)
        restored = extracted / 'linear-handbook'
        expected = {path.relative_to(ROOT).as_posix() for path in files}
        actual = {path.relative_to(restored).as_posix() for path in restored.rglob('*') if path.is_file()}
        mismatches = [name for name in sorted(expected & actual) if (ROOT / name).read_bytes() != (restored / name).read_bytes()]
        extracted_links = inspect(restored)
        result = {
            'archive': OUTPUT.name,
            'sha256': hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
            'bytes': OUTPUT.stat().st_size,
            'files': len(files),
            'file_set_matches': expected == actual,
            'byte_mismatches': mismatches,
            'links_match': links == extracted_links,
            'links': extracted_links,
        }
        save(ROOT / 'validation/generated/repository-review-delivery.json', result)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        raise SystemExit(bool(mismatches) or expected != actual or links != extracted_links or bool(links['gaps']))
