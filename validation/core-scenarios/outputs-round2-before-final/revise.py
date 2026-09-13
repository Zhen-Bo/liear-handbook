from pathlib import Path
import shutil,json,hashlib,re,difflib
ROOT=Path(__import__('sys').argv[1]).resolve()
SRC=ROOT/'outputs'; DST=ROOT/'outputs-round2'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,t):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(t.encode('utf-8'))
def save(c,n,t): write(DST/c/n,t)
def load(c,n): return (DST/c/n).read_text(encoding='utf-8')
def jsave(c,n,v): save(c,n,json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def jload(c,n): return json.loads(load(c,n))
for c in ['C01','C02','C03','C04','C05','C06']:
    shutil.copytree(SRC/c,DST/c,dirs_exist_ok=True)

save('C01','environment.md','''# Pocket minimum environment

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
  - Actual subscription fields for new issues were not provided.
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
''')
save('C01','project-brief.md','''# Personal expense tracker v1

## Goal

Allow individuals to add expense amounts and categories.
Users can view the monthly total and find saved expenses after refreshing.
Requirement basis: requests.md C01.

## Adopted scope

- Storage: localStorage in one browser.
- Amount: positive integer TWD.
- Category
  - Food.
  - Transport.
  - Other.
- Version 1 capabilities
  - Add an expense.
  - View the current monthly total.
- Working baseline
  - Repository: pocket-web.
  - Version: fixture-base-01.
  - Technology: Vite + TypeScript.
  - Test tool: Vitest.
- Engineering conventions for this round, adjustable during implementation
  - Record the time when adding.
  - Determine the current month from the browser’s local year and month.
  - Inject the clock to verify cross-month behavior.

## Success criteria

- [ ] After adding TWD 85 Food and TWD 100 Transport, the monthly total is TWD 185.
  1. Use isolated localStorage.
  2. Fix the clock in the current month.
  3. Add the two expenses above through the interface.
  4. Check the displayed total is TWD 185.
- [ ] After refresh, both expense amounts and categories match the added content.
  1. Add TWD 85 Food and TWD 100 Transport through the interface.
  2. Refresh.
  3. Compare saved contents record by record.
- [ ] After refresh, the monthly total is still TWD 185.
- [ ] An amount of 0 does not add an expense.
- [ ] A negative amount does not add an expense.
- [ ] A fractional amount does not add an expense.
- [ ] A blank amount does not add an expense.
- [ ] Invalid amounts display corrective guidance.
- [ ] Exclude previous-month expenses from the current monthly total.
- [ ] Empty data has a monthly total of 0.
- [ ] Display the failure result when storage fails.
- [ ] Do not report a successful addition when storage fails.

## Responsibilities and entry points

- Project lead: Owner/user-owner.
- Requirement decision-maker: Owner/user-owner.
- Outcome reviewer: Owner/user-owner.
- Simulated Project: sim-pocket-v1.
- Team: team-pocket.
- Initial work
  - [PKT-1](PKT-1.md): data functions.
    - Executor: session A.
  - [PKT-2](PKT-2.md): expense interface.
    - Executor: session B.
    - Prerequisite: usable PKT-1 contract and data functions.
  - [PKT-3](PKT-3.md): workflow integration.
    - Executor: session A.
    - Prerequisite: PKT-1 artifact.
    - Prerequisite: PKT-2 artifact.

## Next steps

1. A checks the repository state for PKT-1.
2. Deliver the data contract.
3. Complete the data functions and their verification.
''')
save('C01','PKT-1.md','''# Deliver expense persistence and monthly-total data functions

- Outcome owner: Owner/user-owner.
- Planned executor: session A.
- Project: sim-pocket-v1.

## Inputs and scope

- Input
  - [Project brief](project-brief.md).
  - Pocket-web/fixture-base-01.
- Exclusive write scope
  - src/expenses/.
  - Corresponding Vitest checks.
  - docs/expense-contract.md.
- Data contract
  - Expense identity.
  - Amount.
  - Category.
  - Creation time.
  - Storage key.
  - Data version.
  - Error results.
- Function deliverables
  - Add an expense.
  - Reread.
  - Current monthly total.
- Documentation deliverable: complete call examples.
- Clock: injectable.
- Month determination: browser local year and month.

## Acceptance

- [ ] After saving and rereading, TWD 85 Food and TWD 100 Transport match their original values.
- [ ] Nonpositive or noninteger amounts are not written.
- [ ] Write failures return an error the interface can display.
- [ ] TWD 85 and TWD 100 in the same month total TWD 185.
- [ ] Previous-month data is excluded from the current monthly total.
- [ ] Empty data has a monthly total of 0.
- [ ] The contract is sufficient for B to integrate using the call examples.
  1. Read the contract’s input and output definitions.
  2. Call data functions using the success example.
  3. Check error outcomes against error examples.
- [ ] Relevant Vitest checks pass.
- [ ] Verification records identify the tested version.

## Next steps

1. Read the empty Vite repository.
2. Check the existing test configuration.
3. Define the complete contract.
4. Complete the data functions.
5. Run verification and save the record.
''')
save('C01','PKT-2.md','''# Provide expense entry and monthly-total interface

- Outcome owner: Owner/user-owner.
- Planned executor: session B.
- Project: sim-pocket-v1.

## Inputs and scope

- Required inputs
  - PKT-1’s docs/expense-contract.md.
  - PKT-1’s callable data functions.
- Exclusive write scope
  - src/ui/expenses/.
  - Corresponding interface checks.
- Interface contents
  - Amount field.
  - Category choices: Food/Transport/Other.
  - Save action.
  - Current monthly total.
- Interface verification: use a contract-compatible adapter.
- Integration entry-point maintainer: PKT-3.

## Acceptance

- [ ] Successful addition displays the latest monthly total.
- [ ] Invalid amounts display corrective guidance.
- [ ] Invalid amounts do not submit an addition.
- [ ] Display an error on save failure.
- [ ] Allow retrying after a save failure.
- [ ] Empty data displays a total of 0.
- [ ] Keyboard operation can complete the add flow.
- [ ] Interface verification results are saved.
- [ ] The integration successor can locate the interface export entry point.

## Next steps

1. Confirm the PKT-1 artifact version.
2. Check the calling contract.
3. Build the interface.
4. Check behavior against each acceptance criterion.
''')
save('C01','PKT-3.md','''# Complete expense workflow integration and verify persistence after refresh

- Outcome owner: Owner/user-owner.
- Planned executor: session A.
- Project: sim-pocket-v1.

## Inputs and scope

- Required inputs
  - Usable version of PKT-1 data functions.
  - Usable version of the PKT-2 interface.
- Exclusive write scope
  - Actual Vite startup entry point.
  - Required integration changes.
  - verification/pocket-v1.md.
- Connect real localStorage.
- Connect the expense interface.
- Fix gaps caused by integration.
- Perform browser acceptance against the Project brief.

## Acceptance

- [ ] After adding TWD 85 for Food and TWD 100 for Transport in the browser, the monthly total is TWD 185.
- [ ] After refresh, both expenses match the added content.
- [ ] After refresh, the monthly total is still TWD 185.
- [ ] Previous-month expenses are excluded from the current monthly total.
- [ ] Empty data totals 0.
- [ ] Amount 0 does not add an expense.
- [ ] Negative amounts do not add an expense.
- [ ] Fractional amounts do not add an expense.
- [ ] Blank amounts do not add an expense.
- [ ] Invalid amounts display corrective guidance.
- [ ] Display the failure result on storage failure.
- [ ] Do not report a successful addition when storage fails.
- [ ] Acceptance records identify the tested version.
- [ ] Acceptance records identify the browser.
- [ ] Acceptance records identify isolated data.
- [ ] Owner can locate each acceptance result from the record.

## Next steps

1. Read both artifacts.
2. Check version and interface-contract compatibility.
3. Connect the startup entry point.
4. Perform the browser acceptance above.
5. Save individual results.
''')
save('C02','environment.md','''# Ledger takeover state

Baseline: requests.md C02.
Verified on: 2026-09-13.

- Workspace
  - Name: Ledger.
  - ID: ws-ledger.
  - Plan: Business.
- Team
  - Name: Finance.
  - ID: team-finance.
  - Identifier: FIN.
  - Time zone: Asia/Taipei.
- Project
  - Name: Ledger.
  - ID: proj-ledger.
  - Archived: false.
- Search results
  - Page 1: archived Ledger 2024/proj-archive.
  - Page 1 next-page cursor: ledger-next.
  - Page 2: Ledger/proj-ledger.
  - Page 2 hasNextPage: false.
- Owner: Mina/user-mina.
- Session B
  - Use Mina’s connection.
  - Can read the Project.
  - Can read artifacts.
- Default: fin-queue.
- Estimates
  - Retain Fibonacci 1/2/3/5/8.
  - Original values for each issue were not provided.
- Cycles
  - Period: two weeks.
  - Current: cycle-24.
  - FIN-10 Cycle membership is unknown.
- Priority
  - Blocked expense entry: High.
  - Others: follow the existing order.
- Labels
  - Team Bug: label-fin-bug/team-finance.
  - Workspace Bug: label-workspace-bug/workspace.
  - No documentation label was provided for FIN-10.
- Automation
  - PR merged → Checking.
  - Parent/sub-issue auto-close: off.
  - Auto-archive: 180 days.
  - Auto-close: off.

| Stage | Status | Category | ID |
| --- | --- | --- | --- |
| Unscheduled | Queue | backlog | fin-queue |
| Ready to execute | Ready | unstarted | fin-ready |
| Execution | Building | started | fin-building |
| Acceptance | Checking | started | fin-checking |
| Complete | Shipped | completed | fin-shipped |
| Stopped | Stopped | canceled | fin-stopped |

## Takeover decision

- The current Project ID supersedes old proj-ledger-legacy.
- The old Ready/old-ready mapping does not match the current status list.
- This round uses Checking as the acceptance stage.
- Project order: fix monthly totals first, then complete category filtering.
- FIN-9
  - Executor: session A, still active.
  - Writes: src/totals.ts.
- FIN-8
  - Wait for FIN-9 artifacts.
  - Mina’s latest comment supersedes the old ”FIN-8 first” suggestion.
- B’s first draft: FIN-10.
  - No blockedBy.
  - No active executor.
  - Write target: docs/import-date-contract.md.
  - Compatible with A’s write scope.
- docs/ledger-brief.md
  - Version: fixture-ledger-02.
  - The fixture provides a readable location but not the full text.
- Basis for current conclusions
  - Latest Project body.
  - Latest FIN-10 body.
  - Mina’s latest Project comment.
''')
save('C02','FIN-10.md','''# Complete the import date contract for monthly-report integration

## Goal

Let the monthly-report integration successor use one contract to determine import dates and cross-month assignment.

- Type: documentation.
- Project: Ledger/proj-ledger.
- Current state: Ready/fin-ready.
- Outcome owner: Mina/user-mina.
- Suggested successor: session B.
- Source
  - Latest FIN-10 body in Requests.md C02.
  - Mina’s latest Project comment.

## Adopted conclusions

- Use the user-selected time zone.
- Express date inputs in ISO format.
- Provide the completed document to monthly-report integration.

## Deliverables

- docs/import-date-contract.md
  - Acceptance rules for ISO date-only.
  - Acceptance rules for timestamps with offsets.
  - How to obtain the selected time zone.
  - Time-zone application order.
  - Missing-time-zone handling.
  - Invalid-ISO handling.
  - Cross-month examples.
  - Comparison examples across different browser time zones.
- To confirm
  - Currently accepted ISO subset.
  - Missing-time-zone handling.
- Confirmation method: inspect existing import and user time-zone settings contracts.
- Keep ambiguous content as open decisions.

## Acceptance

- [ ] Each accepted ISO form has a determinable result.
- [ ] Cross-month examples determine month assignment.
- [ ] The same input and selected time zone yield the same month assignment across different browser time zones.
- [ ] Invalid-input handling is usable by integration.
- [ ] Missing-time-zone handling is usable by integration.
- [ ] The monthly-report integration successor can locate the document.
- [ ] The document identifies the applicable version.

## Next steps

1. Open docs/ledger-brief.md/fixture-ledger-02.
2. Inspect the existing import contract.
3. Inspect the user time-zone contract.
4. Document accepted ISO forms.
5. Add cross-month cases.
6. Hand the completed document to monthly-report integration.

Schedule FIN-8 once the FIN-9 artifact is usable.
''')
save('C03','parent-bug.md','''# Fix expenses occasionally disappearing after saving

## Problem

- Type: Bug.
- Project: proj-pocket.
- Promise: the same expense remains visible after adding and refreshing.
- Mobile report: expenses occasionally disappear.
- Reported case: a TWD 85 Food expense disappeared.
- Reported time: ”yesterday”; exact date unknown.
- Version: Pocket web/pocket-0.3.1.
- Successful control: desktop Chrome retains a TWD 100 Transport expense after adding and refreshing.
- Evidence: requests.md C03.

## Current gaps

- Exact device unknown.
- Browser version unknown.
- Complete failure steps are unknown.
- Failure rate unknown.
- Observation time unknown.
- Console logs at failure are missing.
- Network logs at failure are missing.
- The localStorage snapshot at failure is missing.
- Hypotheses to investigate
  - iOS storage limitations.
  - Date-filtering problem.
- No causal evidence currently supports these hypotheses.

## Outcomes and order

1. Deliver the diagnostic evidence from [investigation-issue.md](investigation-issue.md).
2. Determine the fix location from evidence.
3. Define regression cases.
4. Draft the fix issue.
5. Perform overall acceptance on the fixed version.

## Overall acceptance

- [ ] The identified original failure scenario retains the same expense after the fix.
  1. Restore the affected environment from the investigation results.
  2. Add TWD 85 for Food using the failure steps.
  3. Refresh.
  4. Check that stored and displayed values match.
  5. Save the tested version and results.
- [ ] The desktop Chrome TWD 100 Transport control still passes.
- [ ] Regression checks pass for affected paths involved in the root cause.
- [ ] Regression records identify the tested version.

This item restores the existing persistence promise; the investigation determines the fix.
''')
save('C03','investigation-issue.md','''# Find why expenses disappear and define the fix scope

## Question and decision

Determine which processing stage causes mobile expense loss in pocket-0.3.1, with enough evidence to choose the fix location.

- Type: research.
- Relation: prerequisite for parent ”Fix expenses occasionally disappearing after saving”.
- Investigation path
  - Save.
  - Reread.
  - Display filtering.

## Inputs and deliverables

- Input
  - Requests.md C03 report.
  - Desktop successful control.
  - Test account.
  - Isolated browser storage.
- Diagnostic output: investigation/expense-disappearance.md.
- Reproduction data: fixtures/expense-disappearance/.
  - Environment.
  - Operation steps.
  - Observation records.
- Suggested review point: check evidence gaps after one controlled reproduction attempt.
- Time limit: not yet agreed.

## Evidence plan

1. Obtain exact phone details.
2. Obtain the browser version.
3. Obtain the date at the time.
4. Obtain the complete operation sequence.
5. Add the reported TWD 85 Food expense in isolated storage.
6. Save data snapshots before and after storage.
7. Refresh and save data snapshots.
8. Save the corresponding screen state.
9. Compare console logs.
10. Trace actual save calls.
11. Compare date-filtering results.
12. Record network requests related to the failure.
13. Rerun the desktop Chrome successful control with the same inputs.
14. Test hypotheses individually; establish causality through repeatable observations or fixed-version code evidence.
15. Define the fix scope from evidence.
16. Define regression cases.
17. Update the parent with conclusions.

## Acceptance

- [ ] The successor can reproduce the failure or obtain equivalent failure observations.
- [ ] Conclusions have sufficient evidence to define the fix boundary.
- [ ] Each adopted reason distinguishes observation from inference.
- [ ] Reasons for rejected hypotheses are verifiable.
- [ ] The original failure has been converted into a determinable regression case.
- [ ] The successful control has been converted into a determinable regression case.

When only hypotheses exist or decision evidence is missing, save progress and continue this investigation.
''')

# Backend, parent, and integration use the same acceptance source, preserving each independently failing result.
csv_checks='''- [ ] Cross-page export contains all readable data matching the date range.
- [ ] The export contains only data matching the category filter.
- [ ] Each matching record appears exactly once.
- [ ] Column order matches the contract.
- [ ] Data sorting matches the contract.
- [ ] Chinese notes match their original values after parsing.
- [ ] Comma-containing notes match their original values after parsing.
- [ ] Double-quote notes match their original values after parsing.
- [ ] Newline notes match their original values after parsing.
- [ ] 5000  records download completely.
- [ ] 5001  records display a prompt to narrow the range.
- [ ] 5001  records create no file.
- [ ] No matches downloads a CSV with only the four-column header.
- [ ] Unreadable data never appears in the output.
'''
save('C04','parent-feature.md','''# Allow users to download CSV for all filtered expenses

## Requirements

- Project: Pocket Reporting/proj-report.
- Filter by date range.
- Filter by category.
- The export includes matching data from other pages.
- Permissions: include only expenses readable by the current user.
- Download mode: synchronous.
- Record limit: 5000.
- Limit handling
  - Prompt narrowing the range.
  - Do not create a file.
- Column order: date → amount → category → notes.
- No matches downloads a header-only CSV.
- Source: requests.md C04.

## Deliverables and sub-issues

- [contract.md](contract.md): shared export contract.
- [backend.md](backend.md): CSV generation for the complete data set.
- [frontend.md](frontend.md): filtered download interface.
- [integration.md](integration.md): real download workflow integration.
- [plan.md](plan.md): execution schedule.

## Overall acceptance

'''+csv_checks+'''- [ ] Acceptance records identify the tested version.
- [ ] Acceptance records identify the browser.
- [ ] Acceptance records identify the data baseline.
- [ ] Each acceptance result has an evidence entry point.

## Verification order

1. Prepare a known multi-page data set.
2. Add data outside the date range.
3. Add data from other categories.
4. Add unreadable data.
5. Select filters in the browser.
6. Download the file.
7. Parse CSV.
8. Check each acceptance result above.
9. Save evidence.
''')
save('C04','contract.md','''# Deliver the complete shared frontend/backend export contract

## Inputs and scope

- Input: [parent-feature.md](parent-feature.md).
- Existing API limitation: current-page response only.
- Executor: Agent A.
- Delivery location: docs/export-contract.md.
- Readers: frontend/backend implementation successors.
- Filter contract
  - Date boundaries.
  - Time zone.
  - Category representation.
- Sorting contract
  - Primary sort.
  - Tie-breaker for equal sort values.
- Query contract
  - Interface for retrieving the complete filtered data set.
  - Connection to the existing paginated API.
  - Location of current-user permission checks.
  - Limit-detection method.
- Response contract
  - Successful file.
  - Empty header file.
  - Limit-exceeded error.
  - General errors.
- CSV contract
  - Encoding.
  - Special-character escaping rules.
  - Chinese example.
  - Comma example.
  - Quote example.
  - Newline example.
- Current gap: these detailed contracts have not been supplied.
- Confirmation method: check choices against existing data and APIs.
- The maintainer decides unresolved semantic conflicts.

## Acceptance

- [ ] Frontend can be implemented independently against the request/response examples.
- [ ] Backend can be implemented independently against the same contract version.
- [ ] Cross-page data sets have determinable results.
- [ ] Date boundaries have determinable results.
- [ ] Tied sort values have a determinable result.
- [ ] Unreadable data has a determinable result.
- [ ] 0 -record case defines a header-file result.
- [ ] 5000 -record case defines a complete-file result.
- [ ] 5001 -record case defines a prompt to narrow the range.
- [ ] 5001 -record case explicitly creates no file.
- [ ] Chinese text round-trips through contract serialization and parsing.
- [ ] Commas round-trip through contract serialization and parsing.
- [ ] Quotes round-trip through contract serialization and parsing.
- [ ] Newlines round-trip through contract serialization and parsing.
- [ ] The complete query is not restricted to the current page.
- [ ] Both successors can locate the adopted version.

## Next steps

1. Inspect existing data.
2. Inspect the API.
3. Complete the shared contract.
4. Add examples.
5. The maintainer reviews the contract.
6. Unblock both implementations once the contract is usable.
''')
save('C04','backend.md','''# Fetch all readable filtered expenses and generate CSV

## Inputs and scope

- Blocked by: the usable contract from contract.md.
- Executor: Agent A.
- Write location
  - src/export/.
  - Corresponding verification.
- Implementation contents
  - Complete query.
  - Permission filtering.
  - Stable sorting.
  - 5000 -record limit.
  - CSV encoding.
- Empty data: output a header.
- Over the limit: produce no file.
- Delivery entry point: implementation version callable by integration.
- Verification deliverable: data comparison evidence.

## Acceptance

'''+csv_checks.replace('Downloads completely','Generates completely')+'''- [ ] General error responses match the contract.

## Next steps

1. Read the reviewed contract version.
2. Create known multi-page data.
3. Implement the complete query.
4. Implement CSV serialization.
5. Check each acceptance criterion.
6. Save the integration entry point and verification evidence.
''')
save('C04','frontend.md','''# Provide an interface to download CSV by date and category

## Inputs and scope

- Blocked by: the usable request/response contract from contract.md.
- Executor: Agent B.
- Write location
  - src/ui/export/.
  - Corresponding interface verification.
- Submit the date range.
- Submit the category filter.
- Handle successful downloads.
- Handle error responses.
- Verification method: contract response doubles.
- integration.md handles connection to the real backend.

## Acceptance

- [ ] The request includes the current date range.
- [ ] The request includes the current category filter.
- [ ] Full export requests are not restricted to the current page.
- [ ] A successful response triggers a file download.
- [ ] Empty results still download a header file.
- [ ] Exceeding the limit displays a prompt to narrow the range.
- [ ] Exceeding the limit does not trigger a download.
- [ ] General failures display understandable errors.
- [ ] Allow retrying after failure.
- [ ] Verification records state the response-double scope.
- [ ] Verification records identify the delivered version.

## Next steps

1. Read the contract.
2. Prepare success responses.
3. Prepare empty-data responses.
4. Prepare limit-exceeded responses.
5. Prepare general failure responses.
6. Implement the interface.
7. Check each acceptance behavior.
''')
save('C04','integration.md','''# Connect the real export service and verify browser CSV downloads

## Inputs and scope

- Blocked by
  - The usable implementation version from Backend.md.
  - The usable implementation version from Frontend.md.
- Executor: Agent A.
- Shared entry point: src/app/export.ts.
- Sole writer for the shared entry point: Agent A.
- Deliverables
  - Integration version.
  - verification/csv-export.md.
- Connect the complete-query functions.
- Connect the download interface.
- Perform all overall acceptance checks in parent-feature.md.

## Acceptance

'''+csv_checks+'''- [ ] The results above come from an actual browser download.
- [ ] Each result identifies the integration version.
- [ ] Each result identifies the actual data baseline.

Mark the parent complete only after all required acceptance criteria pass.

## Next steps

1. Check the backend entry point.
2. Check the frontend entry point.
3. Check the contract version used by both.
4. Connect src/app/export.ts.
5. Prepare multi-page data.
6. Perform browser acceptance.
''')
save('C04','plan.md','''# Execution order

1. Agent A completes contract.md.
2. The maintainer reviews the contract.
3. Start implementation once the contract is usable.
   - Agent A: backend.md.
   - Agent B: frontend.md.
4. The maintainer reviews one item at a time.
5. Agents prioritize rework.
6. Once both implementations are usable, A completes integration.md.
7. Check outcomes against the overall acceptance in parent-feature.md.

## Capacity and allocation

- Each Agent executes one item at a time.
- The aggregate parent does not occupy another execution slot.
- Deliverables awaiting review still count toward WIP.
- Do not open new work before review capacity is released.
- Backend waits for the shared contract.
- Frontend waits for the shared contract.
- Backend and frontend have no artifact dependency on each other.
- Integration waits for the backend artifact.
- Integration waits for the frontend artifact.
- A alone maintains src/app/export.ts.
- Determine artifact dependencies from actual required inputs.
- This round uses corresponding filenames as work identifiers.
- Identifiers not provided
  - Actual Team.
  - Status ID.
  - New issue IDs.
''')
save('C05','EXP-21.md','''# Export all filtered data

## Current results

- PR #81 is merged.
- Artifact version: [merge-81-abc](fixture://exp-21/merge-81-abc).
- PR review passed.
- Unit tests passed.
- Lin’s latest acceptance data
  - Expected IDs: 1–240.
  - Actual.csv IDs: 1–80.
  - Each actual ID appears once.
- Missing IDs: 81–240.
- Missing count: 160.
- Full export acceptance failed.
- Acceptance evidence: [actual.csv](fixture://exp-21/actual.csv).
- Data source: latest acceptance summary in requests.md C05.
- Current stage: Implementing/exp-implement.
- Follow-up work: fix missing records.

## Required acceptance

- [ ] The export contains all 240 records.
- [ ] Each record appears exactly once.
- [ ] Chinese fields are correct.
- [ ] Newline fields are correct.
- [ ] Include only data readable by the current user.

## Next steps

1. Open the export query path in merge-81-abc.
2. Compare actual.csv IDs with query responses stage by stage to locate missing data.
3. Fix missing records based on evidence.
4. Rerun export with the same 240 records.
5. Check ID-set completeness.
6. Check occurrences of each ID.
7. Check Chinese fields.
8. Check newline fields.
9. Check permission cases.
10. Save individual results tied to the tested version.
11. Determine completion from all required acceptance criteria.

## Relations and workflow

- Parent EXP-20: Implementing.
- Parent waits for this required export artifact.
- Merge automation using a PR closing relation set this issue to Done.
- Automatic closure preceded product acceptance.
- The settings maintainer should check whether to map merging to acceptance.
- Current tools support issue updates only.
''')

doc=load('C06','docs/export-spec.md')
doc=doc.replace('- Requirement basis: PAY-16 current body and latest user comment, fully replacing the old CSV specification.','- Requirement basis\n  - PAY-16 current body.\n  - Latest user comment.\n- Current approach: JSON specification fully replaces the old CSV specification.')
doc=doc.replace('- `id` is the source’s unique string, used for stable sorting and excluded from the three output fields.','- Source `id` is a unique string.\n- `id` is used for stable sorting.\n- Output fields exclude `id`.')
doc=doc.replace('- The sorting example covers both cross-date ordering and same-date ID ordering.','- The sorting example covers cross-date ordering.\n- The sorting example covers same-date ID ordering.')
doc=doc.replace('- Example output parses as JSON and objects match the three-field definition.','- Example output parses as JSON.\n- Example objects match the three-field definition.')
doc=doc.replace('- Check record: ../verification.json, including this document’s SHA-256 and individual results.','- Check record: [verification.json](../verification.json).\n  - SHA-256 of this document’s actual bytes.\n  - Check each result.')
save('C06','docs/export-spec.md',doc)
hash6=sha(DST/'C06/docs/export-spec.md')
save('C06','PAY-16.md','''Deliver the JSON export specification.

- Fields
  - Date.
  - Amount.
  - Category.
- Amount is an integer.
- Sort data by date ascending.
- Sort by id ascending within a date.
- Artifact: [docs/export-spec.md](docs/export-spec.md).
- Prerequisite source: PAY-15/fixture://pay-15/data-contract-v2.
- For PAY-11’s JSON export implementation.

## Completed items

1. Completely replace with a JSON specification.
2. Define the three output fields.
3. Add a cross-date sorting example.
4. Add a same-date id sorting example.
5. Specify empty-array output.

## Verification results

- [x] The date definition matches data-contract-v2.
- [x] The amount definition matches the integer contract.
- [x] The category definition matches the string contract.
- [x] Sorting example JSON parses successfully.
- [x] The example sorts date ascending.
- [x] The example sorts id ascending within the same date.
- [x] Empty-data output is explicitly [].

- Evidence: [verification.json](verification.json).
- Tested document SHA-256:'''+hash6+'''
- Hash baseline: actual saved file bytes.
- Local simulated artifact links are relative to this directory.

## Continuation entry point

1. The PAY-11 implementation successor reads docs/export-spec.md.
2. Implement output according to field definitions.
3. Check results against the sorting example.
'''.replace('  - Date.','  - date.').replace('  - Amount.','  - amount.').replace('  - Category.','  - category.'))

# Read back the document and check JSON examples, then generate evidence from the actual bytes.
raw=(DST/'C06/docs/export-spec.md').read_bytes()
parsed=raw.decode('utf-8')
inp,out=[json.loads(x) for x in re.findall(r'```json\n(.*?)\n```',parsed,re.S)]
expected=[{k:r[k] for k in ('date','amount','category')} for r in sorted(inp,key=lambda r:(r['date'],r['id']))]
assert out==expected
assert all(set(r)=={'date','amount','category'} for r in out)
assert all(type(r['amount']) is int for r in out)
assert 'Empty-data example: input `[]`, output `[]`.' in parsed
assert hashlib.sha256(raw).hexdigest()==hash6
oldv=json.loads((SRC/'C06/verification.json').read_text(encoding='utf-8'))
newv={'source':'docs/export-spec.md','sha256':hash6,'hashBasis':'hashlib.sha256(Path.read_bytes())','basis':'Current body, latest comment, and embedded PAY-15 data-contract-v2 contents in requests.md C06','checks':[
{'name':'The YYYY-MM-DD date definition matches the prerequisite contract','passed':True},
{'name':'The integer amount definition matches the prerequisite contract','passed':True},
{'name':'The string category definition matches the prerequisite contract','passed':True},
{'name':'JSON examples parse successfully','passed':True},
{'name':'Example dates ascending','passed':True},
{'name':'Example IDs ascending within the same date','passed':True},
{'name':'Output fields are date, amount, category','passed':True},
{'name':'Empty-data output [] explicitly stated','passed':True},
{'name':'Document byte hash matches the declared hash','passed':True}],
'scope':'Document content and specification-example checks',
'correction':{'round1DeclaredSha256':oldv['sha256'],'round1ActualBytesSha256':sha(SRC/'C06/docs/export-spec.md'),'finding':'Round 1 hashed LF text re-encoded after text readback, differing from the CRLF file bytes written on Windows. Round 2 reads the saved file bytes directly.'}}
jsave('C06','verification.json',newv)

# Synchronize the local simulated authoritative state; preserve the first-round snapshot in the round1 subdirectory for exact comparison.
for c in ['C01','C02','C03','C04','C05','C06']:
    shutil.copytree(SRC/c,DST/c/'round1',dirs_exist_ok=True)
    jsave(c,'route.json',{'round':2,'skillRoot':'../../linear-handbook','paths':[{'path':'SKILL.md','mode':'reused'},{'path':'references/writing.md','mode':'loaded'}],'priorRoute':'round1/route.json','action':'Follow first-round effective requirements and workflow; reread writing.md to review deliverables.'})
    if c=='C01':
        state=jload(c,'workspace.json')
        state['project']['description']=load(c,'project-brief.md')
        for i in state['issues']: i['body']=load(c,i['identifier']+'.md')
        jsave(c,'workspace.json',state)
    elif c in ['C05','C06']:
        state=jload(c,'workspace.json')
        state['issue']['body']=load(c,'EXP-21.md' if c=='C05' else 'PAY-16.md')
        jsave(c,'workspace.json',state)
    diffs=[]; manifest=[]
    for p in sorted((DST/c).rglob('*.md')):
        if 'round1' in p.relative_to(DST/c).parts or p.name=='source-fixture.md': continue
        rel=p.relative_to(DST/c).as_posix()
        before=(SRC/c/rel).read_text(encoding='utf-8')
        after=p.read_text(encoding='utf-8')
        assert after.strip()
        diffs.extend(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='round1/'+rel,tofile=rel))
        manifest.append({'file':rel,'sha256':sha(p),'changed':before!=after,'checkboxCount':len(re.findall(r'^- \[[ x]\]',after,re.M))})
    save(c,'revision.diff',''.join(diffs))
    findings={
    'C01':['Several environment and write-scope details are compressed into one bullet.','Monthly total, previous-month exclusion, and empty-data results are combined in one checkbox.','Invalid-input blocking and error guidance are combined in one checkbox.','Persistence after refresh and correct total were not checked separately.'],
    'C02':['Environment mappings, access, and execution choices contain several independent information units.','Invalid ISO and missing-time-zone handling are combined into one acceptance check.'],
    'C03':['Product type and Project are combined in one bullet.','Unknown environment details and observation gaps were not listed separately.','Regression cases for the original failure and successful control are combined into one acceptance check.'],
    'C04':['5000  and 5001-record results are combined into one acceptance check.','Special-character, sorting, and permission results are combined into one acceptance check.','Limit guidance and absence of a file are combined into one acceptance check.','Frontend/backend delivery scopes and capacity rules contain multiple information units.'],
    'C05':['PR review and unit-test results are combined in one description.','Data completeness and exactly-once occurrence are combined into one acceptance check.','Chinese and newline checks are combined.'],
    'C06':['JSON parsing and both sorting results are combined into one acceptance check.','Multiple delivered document contents are combined in one completed item.','First-round hashes used normalized text and differed from actual bytes.']}
    readback={'round':2,'files':manifest,'checks':[]}
    if c=='C01':
        actual=jload(c,'workspace.json')
        assert actual['project']['description']==load(c,'project-brief.md')
        assert all(i['body']==load(c,i['identifier']+'.md') for i in actual['issues'])
        readback['checks'].append({'name':'Project description and three issue bodies synchronized','passed':True})
    if c in ['C05','C06']:
        actual=jload(c,'workspace.json')
        expected_status='exp-implement' if c=='C05' else 'pay-done'
        assert actual['issue']['statusId']==expected_status
        assert actual['issue']['body']==load(c,'EXP-21.md' if c=='C05' else 'PAY-16.md')
        readback['checks'].append({'name':'Issue body synchronized; status matches the effective requirements','passed':True})
    if c=='C06':
        v=jload(c,'verification.json'); b=load(c,'PAY-16.md')
        assert v['sha256']==sha(DST/c/'docs/export-spec.md')
        assert v['sha256'] in b and v['sha256'] in jload(c,'workspace.json')['issue']['body']
        readback['checks'].append({'name':'Hashes agree across document bytes, verification, PAY-16, and simulated body','passed':True})
    readback['checks'].append({'name':'Documents read back individually; unchanged snapshots preserved in round1/','passed':True})
    jsave(c,'readback.json',readback)
    jsave(c,'operations.json',{'round':2,'simulationOnly':True,'priorOperations':'round1/operations.json','findings':findings[c],
    'operations':[{'operation':'read','source':['requests.md#'+c,'../outputs/'+c,'linear-handbook/references/writing.md'],'result':'Retain original requirements, reread writing rules, and inspect first-round documents'},
    {'operation':'save_revision','target':c,'result':'Separated independent information and acceptance results and saved revised Markdown'},
    {'operation':'preserve_original','target':'round1/','result':'Copy first-round data as file bytes for exact comparison'},
    {'operation':'sync_local_simulation' if c in ['C01','C05','C06'] else 'save_drafts','target':'workspace.json' if c in ['C01','C05','C06'] else 'Markdown for this case','result':'Synchronized and read back' if c in ['C01','C05','C06'] else 'Saved and read back drafts'},
    {'operation':'readback','target':'readback.json','result':'Checked documents, simulated bodies, and applicable evidence; revision.diff preserves line-by-line differences'}]})
save('','README.md','''# Round 2 deliverables

- [C01](C01/project-brief.md): environment and initial work.
- [C02](C02/FIN-10.md): takeover draft.
- [C03](C03/parent-bug.md): Bug plan.
- [C04](C04/parent-feature.md): CSV export decomposition.
- [C05](C05/EXP-21.md): issue body for the missing-record fix.
- [C06](C06/PAY-16.md): JSON document completion record.

Per-case check entry points:

- operations.json: revision findings and actual operations.
- route.json: second-round skill routing.
- readback.json: readback checks and document byte hashes.
- revision.diff: line-by-line changes.
- round1/: unchanged copies of first-round files.
''')
print(json.dumps({'round':2,'output':str(DST),'C06Sha256':hash6,'result':'All six cases revised, synchronized, and checked by readback'},ensure_ascii=False))
