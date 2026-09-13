Source: requests.md → C02

Taking over an existing project

User request: take over the existing Ledger Project, document the current environment and draft the first issue to work on, preserving our workflow. Prepare only; do not create or update remote objects.

- Workspace: Ledger, ws-ledger, Business.
- Team: Finance, team-finance, FIN, Asia/Taipei.
- Old policy: Project id proj-ledger-legacy; acceptance status name Ready, status id old-ready; suggests the Agent start FIN-8 first.
- Project search page 1: proj-archive, name Ledger 2024, archived true; hasNextPage true, cursor ledger-next.
- Project search page 2: proj-ledger, name Ledger, archived false; hasNextPage false.
- Status: Queue / backlog / fin-queue; Ready / unstarted / fin-ready; Building / started / fin-building; Checking / started / fin-checking; Shipped / completed / fin-shipped; Stopped / canceled / fin-stopped.
- Default: fin-queue.
- Estimates: enabled, Fibonacci 1/2/3/5/8; retain existing values.
- Labels: Bug / label-fin-bug / team-finance; Bug / label-workspace-bug / workspace.
- Cycles: enabled with two-week periods; current Cycle cycle-24.
- Priority: High for blocked expense entry; otherwise follow the existing order.
- Automation: PR merged → Checking; parent/sub-issue auto-close off; auto-archive 180 days; auto-close off.
- Owner: Mina, user-mina; Agent session B uses Mina’s connection and can read the Project and artifacts.
- Latest Project body: fix monthly totals, then complete category filtering; deliver the monthly-total fix first.
- Latest FIN-8: category filtering, Ready, blockedBy FIN-9, no active executor.
- Latest FIN-9: fix monthly totals, Building, executor session A, writes src/totals.ts, still active.
- Latest FIN-10: complete the import date contract; Ready, no blockedBy, no active executor; artifact docs/import-date-contract.md; acceptance requires determinable ISO-date and cross-month examples.
- Latest Project comment: Mina asks B to draft FIN-10 first, then schedule FIN-8 after FIN-9 is delivered.
- Latest FIN-10 body: adopt the user-selected time zone instead of the browser time zone; hand off to monthly-report integration when complete.
- Existing artifact: docs/ledger-brief.md, version fixture-ledger-02, readable.
- Simulated tools: read-only listings, get, comments, and artifacts.
