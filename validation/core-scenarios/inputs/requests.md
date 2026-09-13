# Fixed requirements and simulated environment

The six cases in this file are independent.
Each case’s fixture is the simulated environment’s current authoritative data.
Use the linear-handbook skill to complete the requirements; write usable content and simulated operation records to the isolated output directory.
The operation log records each data read, planned field change, result decision, and source location.
All Linear IDs, products, versions, and links are synthetic.
Do not turn facts missing from the simulation into claimed results.

## C01 Blank initialization

User request: I just created a Workspace and want to use Linear to manage a personal expense web app with two Agents. The first version should accept expense amounts and categories, show this month’s total, and retain data after refresh. Prepare a minimal environment configuration, Project brief, and initial issues ready for handoff. You may create the Project and issues in this simulation.

- Workspace: Pocket, ID ws-pocket, Free.
- The native interface created the same-name default Team: Pocket, ID team-pocket, identifier PKT, time zone Asia/Taipei.
- Acting identity: Owner, ID user-owner, the human outcome owner.
- Agents: external sessions A and B share the Owner connection and can both access Pocket.
- Statuses: Backlog / backlog / st-backlog; Todo / unstarted / st-todo; Doing / started / st-doing; Done / completed / st-done; Canceled / canceled / st-canceled.
- Default status: st-backlog.
- All Project search results: empty.
- All issue search results: empty.
- Labels: empty.
- Estimates: off.
- Cycles: off.
- Automations: PR, parent/sub-issue, auto-close, and auto-archive are all off.
- Owner’s notification entry point: Inbox, checked daily; subscribes to owned issues.
- Requirement decisions: localStorage in one browser; positive integer TWD expenses; Food/Transport/Other categories; version 1 only supports addition and monthly total.
- Environment: an empty Vite + TypeScript repository pocket-web exists, version fixture-base-01, test tool Vitest.
- Simulated tools can read the above data, create a Project and issues, and read back new objects; no Workspace/Team/settings creation tools are provided.

## C02 Taking over an existing project

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

## C03 Vague bug

User request: expenses sometimes disappear after saving. Break this into work I can hand to Agents. Only the following information is available. Produce issue drafts and an execution order.

- Promised behavior: the same expense remains visible after adding and refreshing.
- User report: occasionally on mobile, an expense of TWD 85 for Food disappeared yesterday.
- Affected product: Pocket web, version pocket-0.3.1.
- Exact device, browser version, full operation sequence, and failure rate remain to be obtained.
- Successful example: add TWD 100 Transport in desktop Chrome and refresh; data remains.
- No console, network, or localStorage snapshot exists from the failure.
- A test account and isolated browser storage are available for further investigation.
- Team discussion includes: it may be an iOS storage limit or a date-filtering problem.
- Requirements are unchanged; no cloud synchronization was requested.
- Existing Project: proj-pocket; no issue with the same outcome.
- Only drafts are authorized.

## C04 Large feature

User request: break ”allow users to export all filtered expenses as CSV” into work for two Agents, preserving overall acceptance. This round needs only planning and issue bodies.

- Project: Pocket Reporting, proj-report.
- New capability: export all matching data by date range and category, including other pages.
- Decision: synchronous download, at most 5000 records; exceeding the limit prompts narrowing the range and creates no file.
- CSV columns: date, amount, category, notes.
- Notes may contain Chinese, commas, double quotes, and newlines.
- No matches: still download a header-only CSV.
- Permissions: include only expenses readable by the current user.
- The existing query API returns only the current page; no complete-query contract is available for export.
- Frontend and export backend need a shared filter, sort, and error-response contract.
- Implementation can split into src/export/ and src/ui/export/, with integration at src/app/export.ts.
- Each of two Agents can handle one item; the maintainer can review one item at a time.
- Delivery includes browser download and comparison with actual data.
- No launch date is specified.
- No issue has the same outcome.

## C05 PR merged without acceptance

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

## C06 A second Agent takes over

User request: you are session B, taking over PAY-16. Continue the currently authorized documentation work and update the simulated issue. Read the current data first.

- Issue PAY-16, current status Doing, id pay-16, assignee user-ren.
- Current body: deliver JSON export specification; fields date, amount, category; integer amounts; ascending date, then ascending id within a date; artifact docs/export-spec.md; acceptance covers field definitions, sorting examples, and empty-data output [].
- Parent PAY-11: deliver JSON export; the specification is an implementation prerequisite.
- Latest user comment: fully replace the old CSV specification with JSON requirements; complete the document and update this issue under the original authorization.
- Old handoff: session A was working on CSV; saved docs/export-spec.md draft draft-csv-01; confirmed date, amount, category fields; no acceptance record.
- Current file docs/export-spec.md: # CSV export specification; fields date date-string, amount integer, category category-string; first output row is a header; sorting undecided.
- Current coordinator allocation: session A has stopped writing PAY-16 and docs/export-spec.md; session B is the sole writer for both; updated 2026-09-13T10:00:00+08:00.
- Prerequisite PAY-15: Done; artifact fixture://pay-15/data-contract-v2 readable; defines date YYYY-MM-DD, integer amount, string category, and unique string id.
- Environment: status Doing / started / pay-doing; Review / started / pay-review; Done / completed / pay-done.
- Parent/sub-issue automatic closing: off.
- Existing authorization: edit the local specification, update PAY-16 body/status after content verification, no additional human review required; may save a findings comment.
- Simulated tools: read the above data, edit isolated docs/export-spec.md, update_issue, readback.
