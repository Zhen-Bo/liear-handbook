"""Offline stateful tool double. No network or real Linear calls."""
import argparse
import copy
import json
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--fixtures', required=True)
p.add_argument('--run', required=True)
p.add_argument('--request', required=True, help='JSON file: case, tool, args')
a = p.parse_args()
fixtures = json.loads(Path(a.fixtures).read_text(encoding='utf-8-sig'))
request = json.loads(Path(a.request).read_text(encoding='utf-8-sig'))
run = Path(a.run).resolve()
run.mkdir(parents=True, exist_ok=True)
case = request['case']
statefile = run / (case + '-state.json')
state = json.loads(statefile.read_text(encoding='utf-8')) if statefile.exists() else copy.deepcopy(fixtures[case]['state'])
tool, args = request['tool'], request.get('args', {})
if tool == 'get_issue':
    result = state['issues'].get(args['id'], {'error': 'NOT_FOUND'})
elif tool == 'list_comments':
    result = {'comments': state.get('comments', []), 'hasNextPage': False}
elif tool == 'get_connection':
    result = state.get('connection', {'actor': 'agent-A', 'workspace': 'sim-workspace', 'scopes': ['read', 'write']})
elif tool == 'get_request':
    result = {'requestId': args['id'], 'running': False, 'result': 'unavailable'}
elif tool == 'list_issues':
    ids = state.get('pages', [list(state['issues'])])
    index = int(args.get('cursor', '0'))
    result = {'issues': [state['issues'][i] for i in ids[index]], 'hasNextPage': index + 1 < len(ids), 'cursor': str(index + 1) if index + 1 < len(ids) else None}
elif tool == 'save_issue':
    if state.get('connection', {}).get('scopes') == ['read']:
        result = {'error': 'FORBIDDEN', 'applied': False, 'requiredScope': 'write'}
    else:
        id_ = args.get('id') or ('SIM-NEW-' + str(len(state['issues'])))
        target = state['issues'].setdefault(id_, {'id': id_})
        target.update(args)
        target['updatedAt'] = '2026-09-13T02:00:00Z'
        if 'blockedBy' in args:
            for upstream in args['blockedBy']:
                other = state['issues'][upstream]
                other['blocks'] = sorted(set(other.get('blocks', []) + [id_]))
        result = {'success': True, 'id': id_}
elif tool == 'save_comment':
    entry = {'id': 'comment-' + str(len(state.get('comments', []))), **args}
    state.setdefault('comments', []).append(entry)
    result = {'success': True, **entry}
elif tool == 'record_decision':
    state.setdefault('decisions', []).append(args)
    result = {'saved': True}
else:
    result = {'error': 'UNSUPPORTED_OPERATION', 'tool': tool}
with (run / 'transcript.jsonl').open('a', encoding='utf-8') as f:
    f.write(json.dumps({'request': request, 'response': result}, ensure_ascii=False) + '\n')
statefile.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
