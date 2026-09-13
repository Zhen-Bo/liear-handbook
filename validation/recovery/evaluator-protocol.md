# Independent exercise input

Use `skills/linear-handbook/SKILL.md` and references as needed to complete the six requests in `requests.json`.

- Obtain original requirements and existing tool responses only from `requests.json`.
- Choose operations according to the skill and complete the executable scope.
- Real Linear, network, and external service operations are prohibited.
- Keep all output in a newly created isolated temporary directory.
- Do not read `fixtures.json`, the `simulator.py` source, `*-state.json`, or `expected.json`.
- Simulator CLI responses are the only readable current service state.
- Save `outcome.md` with actual results, loaded routes, and necessary resumption points.

## Tool contract

Pass `case`, `tool`, and `args` in a JSON file.
`case` is `claim`, `human`, `timeout`, `partial`, `permission`, or `untrusted`.

```powershell
python simulator.py --fixtures fixtures.json --run run --request request.json
```

| Tool | Arguments and effects |
| --- | --- |
| get_issue | `id`; read the current issue |
| list_comments | `issueId`; read current comments |
| get_connection | Empty object; read connection information |
| get_request | `id`; inspect an earlier request |
| list_issues | `team`, `project`, `parentId`, `includeArchived`, optional `cursor`; continue using the returned cursor |
| save_issue | Update when `id` is present, otherwise create; `description` and `blockedBy` replace their existing fields |
| save_comment | `issueId`, `body`; add a comment |
| record_decision | Any JSON; save a local decision without a remote write |

Each simulator call saves its request/response to `run/transcript.jsonl`.
When another action is needed, use `record_decision` to save the specific action and reason, and save drafts separately.

## Replay

1. Copy this directory to a new temporary directory.
2. Preserve the existing `raw/` as evidence of the original exercise.
3. Replay requests from `raw/run/transcript.jsonl` using a different `--run` directory.
4. Compare each response and the final state with the original evidence.

Replay checks only the deterministic effects of the same decisions.
To reassess the skill, use a fresh Agent and provide only this document, `requests.json`, and the skill path.
