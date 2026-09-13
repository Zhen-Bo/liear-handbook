# Pocket minimum environment

Verification baseline: requests.md C01.
Verified on: 2026-09-13.

- Workspace
  - Name: Pocket.
  - ID: ws-pocket.
  - Plan: Free.
- Team
  - Reuse the native default Team.
  - Name: Pocket.
  - ID: team-pocket.
  - Identifier: PKT.
  - Time zone: Asia/Taipei.
- Human outcome owner: Owner/user-owner.
- External executors
  - Session A.
  - Session B.
  - Connection: shared Owner connection.
  - Access: both can access Pocket.
- Allocation record
  - Issue body records the actual session.
  - Issue body records the exclusive write scope.
  - Use user-owner as Assignee.
- Notifications
  - Owner checks Inbox daily.
  - Owner subscribes to issues they own.
- Priority: No priority for this round.
- Execution order: arrange by prerequisite artifacts.
- Labels: empty.
- Estimates: keep off.
- Cycles: keep off.
- Automations
  - PR: off.
  - Parent/sub-issue: off.
  - Auto-close: off.
  - Auto-archive: off.
- All search results
  - Projects: empty.
  - Issues: empty.

| Stage | Name | Category | ID |
| --- | --- | --- | --- |
| Unscheduled | Backlog | backlog | st-backlog |
| Ready to start | Todo | unstarted | st-todo |
| Execution and acceptance | Doing | started | st-doing |
| Accepted | Done | completed | st-done |
| Stopped | Canceled | canceled | st-canceled |

- Default status: st-backlog.
- Creation capability: this round may create a Project and issues.
- Settings: retain the state above.
- Suggested capacity: one item per Agent at a time.
- Coordinator: Owner.
  - Arrange writes to the shared entry point.
  - Check overall acceptance.
- Working baseline
  - Repository: pocket-web.
  - Version: fixture-base-01.
  - Technology: Vite + TypeScript.
  - Test tool: Vitest.
