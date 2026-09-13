# Ledger takeover state

Baseline: requests.md C02, 2026-09-13.

- Workspace: Ledger/ws-ledger/Business.
- Team: Finance/team-finance/FIN/Asia/Taipei.
- Project: Ledger/proj-ledger, not archived.
  - Search page 1 contains only archived Ledger 2024/proj-archive.
  - Continue to page 2 using cursor ledger-next; hasNextPage false.
  - Old proj-ledger-legacy is no longer the current mapping.
- Owner: Mina/user-mina; B uses Mina’s connection and can read the Project and artifacts.
- Default: fin-queue.
- Estimates: retain Fibonacci 1/2/3/5/8; original issue values are unavailable, so the draft does not supply values.
- Cycles: two weeks, currently cycle-24; the draft does not assume FIN-10 belongs to the Cycle.
- Priority: High for blocked expense entry; otherwise follow the existing order.
- Labels
  - Team Bug: label-fin-bug/team-finance.
  - Workspace Bug: label-workspace-bug/workspace.
  - FIN-10 delivers documentation; no corresponding existing label was provided.
- Automation
  - PR merged → Checking.
  - Parent/sub-issue auto-close off.
  - Auto-archive: 180 days.
  - Auto-close off.

| Stage | Status | Category | ID |
| --- | --- | --- | --- |
| Unscheduled | Queue | backlog | fin-queue |
| Ready to execute | Ready | unstarted | fin-ready |
| Execution | Building | started | fin-building |
| Acceptance | Checking | started | fin-checking |
| Complete | Shipped | completed | fin-shipped |
| Stopped | Stopped | canceled | fin-stopped |

- Old policy treats Ready/old-ready as awaiting acceptance, conflicting with current category and ID; this round uses Checking for acceptance.
- The Project currently delivers the monthly-total fix before category filtering.
- Session A is working on FIN-9 and writes src/totals.ts.
- FIN-8 waits for FIN-9; Mina’s latest comment supersedes the old suggestion to start FIN-8 first.
- B’s first draft is FIN-10: no blockedBy or active executor; writes docs/import-date-contract.md, compatible with A’s write scope.
- docs/ledger-brief.md/fixture-ledger-02 provides only a readable location and version, with no full text in the fixture; conclusions use the current Project body and latest FIN-10 body.
