"""Replay recorded requests in a fresh temporary directory and compare effects."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

base = Path(__file__).resolve().parent
rows = [json.loads(line) for line in (base / 'raw/run/transcript.jsonl').read_text(encoding='utf-8-sig').splitlines()]
results = []
with tempfile.TemporaryDirectory(prefix='linear-recovery-replay-') as temp:
    root = Path(temp)
    for number, row in enumerate(rows, 1):
        request = root / 'request.json'
        request.write_text(json.dumps(row['request'], ensure_ascii=False), encoding='utf-8')
        process = subprocess.run([sys.executable, str(base / 'simulator.py'), '--fixtures', str(base / 'fixtures.json'), '--run', str(root / 'run'), '--request', str(request)], capture_output=True, encoding='utf-8', env={**os.environ, 'PYTHONIOENCODING': 'utf-8'}, check=True)
        actual = json.loads(process.stdout)
        results.append({'step': number, 'case': row['request']['case'], 'responseMatches': actual == row['response']})
    states = []
    for path in sorted((base / 'raw/run').glob('*-state.json')):
        original = json.loads(path.read_text(encoding='utf-8-sig'))
        replayed = json.loads((root / 'run' / path.name).read_text(encoding='utf-8-sig'))
        states.append({'file': path.name, 'matches': original == replayed})
result = {'requests': len(rows), 'responsesMatch': all(r['responseMatches'] for r in results), 'statesMatch': bool(states) and all(s['matches'] for s in states), 'steps': results, 'states': states}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(0 if result['responsesMatch'] and result['statesMatch'] else 1)
