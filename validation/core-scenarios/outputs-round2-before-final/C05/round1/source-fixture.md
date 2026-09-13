Source: requests.md → C05

PR merged without acceptance

User request: the PR is merged. Update EXP-21’s effective body and status, and leave a directly executable next action. Updating this issue in the simulation is authorized.

- Team: Export, team-export.
- Status: Queue / backlog / exp-queue; Implementing / started / exp-implement; Validation / started / exp-validation; Done / completed / exp-done.
- EXP-21 latest status: Done / exp-done.
- EXP-21 body: export all filtered data; required acceptance: all 240 records exactly once, correct Chinese and newline fields, readable data only.
- PR #81: merged, fixed version merge-81-abc, review passed, unit tests passed.
- Automation: merging a PR with a closing relation automatically sets Done.
- Latest acceptance data: expected IDs 1 through 240; actual.csv contains only IDs 1 through 80, each once.
- Character, newline, and permission acceptance results are not available yet.
- Latest comment: reviewer Lin supplies the above data and actual.csv, requesting a missing-record fix and renewed acceptance.
- Artifact entry point: fixture://exp-21/merge-81-abc; acceptance entry point: fixture://exp-21/actual.csv.
- Parent EXP-20 status Implementing; parent/sub-issue automation off.
- Simulated tools: get_issue, list_comments, read CSV, update_issue, readback; no write capability for automation settings.
