# Pocket minimum environment

Verification baseline: requests.md C01, 2026-09-13.

- Workspace: Pocket/ws-pocket/Free.
- Team: Pocket/team-pocket/PKT/Asia/Taipei; reuse the native default Team.
- Human outcome owner: Owner/user-owner.
- Executors: external sessions A and B share the Owner connection and can access Pocket.
  - Record the session and write scope in the issue body.
  - Use user-owner as Assignee.
- Notifications: Owner checks Inbox daily and subscribes to owned issues; actual new-issue subscription fields were not provided.
- Priority: No priority for this round; order work by prerequisite artifacts.
- Labels: empty.
- Estimates: keep off.
- Cycles: keep off.
- Automations: PR, parent/sub-issue, auto-close, and auto-archive are all off.
- Project and issue searches: all results empty.

| Stage | Name | Category | ID |
| --- | --- | --- | --- |
| Unscheduled | Backlog | backlog | st-backlog |
| Ready to start | Todo | unstarted | st-todo |
| Execution and acceptance | Doing | started | st-doing |
| Accepted | Done | completed | st-done |
| Stopped | Canceled | canceled | st-canceled |

- Default status: st-backlog.
- This round uses existing Project/issue creation capabilities and retains the environment above.
- Suggested capacity: one item per Agent at a time; Owner coordinates shared entry points and overall acceptance.
- Working baseline: pocket-web, fixture-base-01, Vite + TypeScript, Vitest.
