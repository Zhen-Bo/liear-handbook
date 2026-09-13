from pathlib import Path
import json, hashlib, re

ROOT=Path(__import__('sys').argv[1]).resolve()
OUT=ROOT/'outputs'
request=(ROOT/'requests.md').read_text(encoding='utf-8-sig')
def put(case,name,value):
    p=OUT/case/name; p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(value if isinstance(value,str) else json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
    return p
def read(case,name):
    return (OUT/case/name).read_text(encoding='utf-8')
def fixture(case):
    return request.split('## '+case+' ',1)[1].split('\n## C',1)[0]
routes={
'C01':['SKILL.md','references/workspace-setup.md','references/policy.md','references/project-planning.md','assets/templates/project-brief.md','references/issue-types.md','references/writing.md','assets/templates/feature.md','references/issue-decomposition.md','references/planning-and-dependencies.md','references/multi-agent-coordination.md'],
'C02':['SKILL.md','references/workspace-setup.md','references/policy.md','references/multi-agent-coordination.md','references/issue-lifecycle.md','references/issue-types.md','references/writing.md','assets/templates/feature.md'],
'C03':['SKILL.md','references/issue-types.md','references/issue-decomposition.md','references/decomposition-edge-cases.md','references/writing.md','assets/templates/bug.md','assets/templates/research.md','references/planning-and-dependencies.md'],
'C04':['SKILL.md','references/issue-decomposition.md','references/planning-and-dependencies.md','references/feature-decomposition.md','references/issue-types.md','references/writing.md','assets/templates/feature.md'],
'C05':['SKILL.md','references/issue-lifecycle.md','references/policy.md','references/writing.md'],
'C06':['SKILL.md','references/multi-agent-coordination.md','assets/templates/handoff.md','references/issue-lifecycle.md','references/documentation.md','references/writing.md']}
seen=set()
for c,paths in routes.items():
    entries=[]
    for p in paths:
        entries.append({'path':p,'mode':'reused' if p in seen else 'loaded'})
        seen.add(p)
    put(c,'route.json',{'skill_root':'../../linear-handbook','paths':entries,'note':'Shared batch reads were applied per case; loaded means the first applicable case, reused means using previously read content. Initial bulk output was truncated, so core workflows and templates were reread in smaller batches; feature-decomposition was loaded in a batch but its examples were not used to infer requirements.'})
    put(c,'source-fixture.md','Source: requests.md → '+c+'\n\n'+fixture(c))

put('C01','environment.md','''# Pocket minimum environment

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
''')
brief='''# Personal expense tracker v1

## Goal

Allow individuals to add expense amounts and categories, view this month’s total, and retain data after refresh.
Requirement basis: requests.md C01.

## Adopted scope

- Persist expenses in localStorage within one browser.
- Amounts are positive integer TWD.
- Categories: Food, Transport, Other.
- Version 1 provides expense addition and the monthly total.
- Working baseline: pocket-web/fixture-base-01, Vite + TypeScript, Vitest.
- Engineering conventions for this round: record time when adding; determine the current month from browser local year/month; inject the clock to verify cross-month behavior. These are adjustable implementation choices.

## Success criteria

- [ ] After adding TWD 85 Food and TWD 100 Transport, the monthly total is TWD 185.
  1. Use isolated localStorage and a fixed current-month clock.
  2. Add two expenses through the interface.
  3. Check categories and amounts, then refresh.
  4. Confirm both records remain and the total is still TWD 185.
- [ ] 0, negative, fractional, and blank amounts do not add an expense; the interface displays corrective guidance.
- [ ] Previous-month expenses are excluded; empty data produces a monthly total of 0.
- [ ] Display the failure result when storage fails; do not report a successful addition.

## Responsibilities and entry points

- Project lead, requirement decisions, and outcome acceptance: Owner/user-owner.
- Simulated Project: sim-pocket-v1, Team team-pocket.
- Initial work
  - PKT-1: data contract, localStorage persistence, and monthly total; session A.
  - PKT-2: expense entry and monthly total interface; session B, waiting for a usable PKT-1 contract.
  - PKT-3: connect the real persistence flow and perform acceptance; session A, waiting for PKT-1 and PKT-2 artifacts.
- Next step: A checks the repository state for PKT-1, delivers a readable data contract and verified data functions.
'''
put('C01','project-brief.md',brief)
c1=[('PKT-1','Deliver expense persistence and monthly-total data functions','A',[],'''## Inputs and scope

- Input: Project brief, pocket-web/fixture-base-01.
- Exclusive write scope: src/expenses/, corresponding Vitest checks, docs/expense-contract.md.
- Define expense identity, amount, category, creation time, storage key/version, and error results.
- Deliver add, reload, and monthly-total functions with complete call examples.
- Use an injectable clock; determine the current month from the browser’s local year and month.

## Acceptance

- [ ] 85  TWD for Food and TWD 100 for Transport can be saved and reread with matching amounts and categories.
- [ ] Nonpositive or noninteger amounts are not written; write failures return an error the interface can display.
- [ ] Monthly total is 185; previous-month data excluded; empty data is 0.
- [ ] The contract includes inputs, outputs, errors, and call examples that B can integrate directly.
- [ ] Relevant Vitest checks pass; save the version and execution results.

## Next steps

1. Read the empty Vite repository and existing test configuration.
2. Define the complete contract and finish the data functions and verification.
'''),('PKT-2','Provide expense entry and monthly-total interface','B',['PKT-1'],'''## Inputs and scope

- Required inputs: PKT-1’s docs/expense-contract.md and callable data functions; check versions at completion.
- Exclusive write scope: src/ui/expenses/ and corresponding interface checks.
- Amount field, Food/Transport/Other category choices, save action, and monthly total.
- Verify the interface with a contract-compatible adapter; PKT-3 maintains the integration entry point.

## Acceptance

- [ ] Successful addition displays the latest monthly total.
- [ ] Invalid amounts receive understandable, actionable guidance and do not submit an addition.
- [ ] Display an error on save failure and allow retrying after correction.
- [ ] Empty data displays 0; keyboard operation supports fields and saving.
- [ ] Save interface verification results and the export entry point for integration.

## Next steps

1. Confirm PKT-1 artifacts are readable and match the calling contract.
2. Build the interface and check behavior against success, empty-data, and failure responses.
'''),('PKT-3','Complete expense workflow integration and verify persistence after refresh','A',['PKT-1','PKT-2'],'''## Inputs and scope

- Input: usable versions of PKT-1 data functions and the PKT-2 interface.
- Exclusive write scope: actual Vite startup entry point, required integration changes, verification/pocket-v1.md.
- Connect real localStorage and the interface, fixing integration gaps.
- Complete browser operations and data comparison against the Project brief’s success criteria.

## Acceptance

- [ ] Add TWD 85 Food and TWD 100 Transport in the actual browser; after refresh both remain and the total is 185.
- [ ] Previous-month exclusion, empty data, invalid amounts, and storage failure match the Project brief.
- [ ] Record the tested version, browser, isolated data, and individual results.
- [ ] Owner can assess the overall Project outcome from the evidence entry point.

## Next steps

1. Read both artifacts and check versions and interfaces.
2. After connecting the startup entry point, execute the full flow and save acceptance records.
''')]
issues=[]
for ident,title,agent,deps,body in c1:
    text=f'# {title}\n\n- Outcome owner: Owner/user-owner.\n- Planned executor: session {agent}.\n- Project: sim-pocket-v1.\n\n'+body
    put('C01',ident+'.md',text)
    issues.append({'id':'sim-'+ident.lower(),'identifier':ident,'teamId':'team-pocket','projectId':'sim-pocket-v1','assigneeId':'user-owner','statusId':'st-todo' if not deps else 'st-backlog','priority':'No priority','labels':[],'estimate':None,'body':text,'blockedBy':['sim-'+d.lower() for d in deps]})
state={'simulation':True,'id_allocation':'sim-* IDs are allocated by the local simulator; PKT-* identifiers are simulated sequential allocations after an empty issue list.','project':{'id':'sim-pocket-v1','name':'Personal expense tracker v1','teamIds':['team-pocket'],'leadId':'user-owner','description':brief},'issues':issues}
put('C01','workspace.json',state)

put('C02','environment.md','''# Ledger takeover state

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
''')
put('C02','FIN-10.md','''# Complete the import date contract for monthly-report integration

## Goal

Let the monthly-report integration successor use one contract to determine import dates and cross-month assignment.

- Type: documentation.
- Project: Ledger/proj-ledger.
- Current state: Ready/fin-ready.
- Outcome owner: Mina/user-mina.
- Suggested successor: session B.
- Source: latest FIN-10 body and Mina’s Project comment in requests.md C02.

## Adopted conclusions

- Use the user-selected time zone.
- Express date inputs in ISO format; the contract must specify the accepted forms.
- Provide the completed document to monthly-report integration.

## Deliverables

- docs/import-date-contract.md.
  - Explicit rules for accepting ISO date-only and timestamps with offsets.
  - How to obtain and apply the selected time zone, in order.
  - Determine missing-time-zone and invalid-ISO handling.
  - Input/expected-result examples across months and different browser time zones.
- Current data does not define the accepted ISO subset or missing-time-zone handling; inspect existing import and user time-zone settings contracts first, keeping ambiguities as open decisions.

## Acceptance

- [ ] Each accepted ISO form includes input, selected time zone, and an explicit result.
- [ ] Cross-month examples determine month assignment.
- [ ] The same input and selected time zone yield the same month assignment across different browser time zones.
- [ ] Invalid-input and missing-time-zone handling are directly usable by integration.
- [ ] The monthly-report integration successor can locate the document and applicable version.

## Next steps

1. Open docs/ledger-brief.md/fixture-ledger-02 and inspect existing import and time-zone contracts.
2. Document accepted ISO forms and cross-month cases in the draft.
3. Provide the completed document to monthly-report integration; schedule FIN-8 once FIN-9 artifacts are usable.
''')

put('C03','parent-bug.md','''# Fix expenses occasionally disappearing after saving

## Problem

- Type: Bug; Project: proj-pocket.
- Promise: the same expense remains visible after adding and refreshing.
- User report: occasionally on mobile; one TWD 85 Food expense disappeared ”yesterday” in the report; exact date unknown.
- Version: Pocket web/pocket-0.3.1.
- Successful control: desktop Chrome retains a TWD 100 Transport expense after adding and refreshing.
- Evidence: requests.md C03.

## Current gaps

- Device and browser versions unknown.
- Complete failure steps, rate, and observation time are unknown.
- Console, network, and localStorage snapshots at failure are missing.
- iOS storage limitations and date filtering are discussion hypotheses without causal evidence.

## Outcomes and order

1. First deliver reproduction and diagnostic evidence in investigation-issue.md.
2. Determine the fix location and regression cases from evidence, then draft the fix issue.
3. Perform this item’s overall acceptance on the fixed version.

## Overall acceptance

- [ ] The identified original failure scenario retains the same expense after the fix.
  1. Reproduce using the device, version, and steps from the investigation.
  2. Add TWD 85 for Food on the fixed version and refresh.
  3. Check that stored and displayed values match; record the tested version and results.
- [ ] The desktop Chrome TWD 100 Transport control still passes.
- [ ] Regression checks pass for affected paths involved in the root cause, with version evidence.

This item restores the existing persistence promise; the investigation determines the fix.
''')
put('C03','investigation-issue.md','''# Find why expenses disappear and define the fix scope

## Question and decision

Determine whether mobile expense loss in pocket-0.3.1 occurs during saving, rereading, or display filtering, with enough evidence to choose the fix location.
This diagnosis is a research prerequisite for the parent ”Fix expenses occasionally disappearing after saving”.

## Inputs and deliverables

- Input: requests.md C03 report, successful control, test account, and isolated browser storage.
- Output: investigation/expense-disappearance.md.
- Reproduction data: fixtures/expense-disappearance/, preserving environment, steps, and observations.
- Check evidence gaps after one controlled reproduction attempt; no time limit has been agreed.

## Evidence plan

1. Obtain the exact phone, browser version, date, and complete operation sequence.
2. Add the reported TWD 85 Food expense in isolated storage; save data snapshots and screen states before/after saving and after refresh.
3. Compare console logs, actual save calls, and date-filtering results; record only relevant network requests.
4. Rerun the desktop Chrome successful control with the same inputs.
5. Test hypotheses individually; establish causality through repeatable observations or fixed-version code evidence.
6. List the fix scope and regression cases from evidence, and update the parent.

## Acceptance

- [ ] The successor can reproduce the failure using the environment and data, or equivalent failure observations exist.
- [ ] Conclusions have traceable evidence sufficient to define the fix boundary.
- [ ] Each adopted reason distinguishes observation from inference; rejection reasons are verifiable.
- [ ] The original failure and successful control have been converted into determinable regression cases.

When only hypotheses exist or decision evidence is missing, save progress and continue this investigation.
''')
put('C03','sequence.json',{'draftOnly':True,'ready':['investigation-issue.md'],'parent':'parent-bug.md','later':[{'deliverable':'Fix and regression-test against the accepted diagnosis','blockedBy':'Traceable diagnostic conclusion','bodyStatus':'Draft after evidence is available'},{'deliverable':'Verify the complete flow on the fixed version','blockedBy':'Testable fixed version','acceptance':'Overall acceptance in parent-bug.md'}]})

put('C04','parent-feature.md','''# Allow users to download CSV for all filtered expenses

## Requirements

- Project: Pocket Reporting/proj-report.
- Export all matching expenses readable by the current user for the date range and category, including other pages.
- Synchronous download, at most 5000 records.
- Exceeding the limit prompts narrowing the range and creates no file.
- Columns in order: date, amount, category, notes.
- No matches downloads a header-only CSV.
- Source: requests.md C04.

## Deliverables and sub-issues

- contract.md: shared complete-query, filter, sort, and error contract.
- backend.md: fetch all readable data and generate CSV according to the contract.
- frontend.md: filtered download and error-handling interface according to the contract.
- integration.md: browser download and comparison with actual data.
- Schedule: plan.md.

## Overall acceptance

- [ ] The exported set equals all readable data matching the date and category filters, each record exactly once, including other pages.
  1. Prepare a known set spanning multiple pages, dates, categories, and unreadable data.
  2. Select the date and category in the browser and download.
  3. Parse the file and check record count, each row’s fields, and contract sorting.
- [ ] Chinese, commas, double quotes, and newline notes match the original values after parsing.
- [ ] 5000  records download completely; 5001 records prompt narrowing the range and produce no file.
- [ ] No matches still downloads a CSV with only the four-column header.
- [ ] Unreadable data never appears in the output.
- [ ] Integration results include tested version, browser, data baseline, and evidence entry point.
''')
put('C04','contract.md','''# Deliver the complete shared frontend/backend export contract

## Inputs and scope

- Input: parent-feature.md; the existing query API provides only current-page responses.
- Executor: Agent A.
- Delivery location: docs/export-contract.md, used by both implementation sub-issues.
- Define date boundaries, time zone, category representation, stable sorting, and tie-breakers.
- Define the interface for retrieving all filtered data and its connection to the existing paginated API.
- Define where current-user permission checks occur and how limits are detected.
- Define successful file responses, empty header files, limit-exceeded responses, and general errors.
- Define CSV encoding and special-character escaping; provide Chinese, comma, quote, and newline cases.
- These contract details are missing; inspect existing data/APIs and record choices first. The maintainer decides unresolved conflicts constrained by existing product semantics.

## Acceptance

- [ ] Frontend and backend can be implemented independently against the same request/response examples.
- [ ] Cross-page data, date boundaries, sort ties, and unreadable data all have determinable results.
- [ ] 0, 5000, and 5001 records have explicit file or error outcomes.
- [ ] Special characters round-trip through contract serialization and parsing.
- [ ] The contract does not treat the current page as the complete data set; both implementation sub-issues can locate the adopted version.

## Next steps

1. Inspect existing data and APIs, then complete the shared contract and examples.
2. Unblock both implementations after the maintainer reviews the usable version.
''')
put('C04','backend.md','''# Fetch all readable filtered expenses and generate CSV

## Inputs and scope

- Blocked by: the usable contract and examples from contract.md.
- Executor: Agent A.
- Write location: src/export/ and corresponding verification.
- Implement complete queries, permission filtering, stable sorting, the 5000 limit, and CSV encoding.
- Empty data outputs a header; exceeding the limit produces no file.
- Deliver an implementation version callable by the integration entry point and data comparison evidence.

## Acceptance

- [ ] The multi-page data set exactly matches the expected complete readable set, each record once.
- [ ] Column order and sorting match the contract.
- [ ] Chinese, commas, quotes, and newlines match the original values after parsing.
- [ ] 0, 5000, and 5001 records meet the contract; exceeding the limit produces no file.
- [ ] Unreadable data is excluded, and applicable error checks pass.

## Next steps

1. Read the reviewed contract version and create known multi-page data.
2. Implement and verify complete queries and serialization; preserve the entry point for integration.
''')
put('C04','frontend.md','''# Provide an interface to download CSV by date and category

## Inputs and scope

- Blocked by: the usable request/response contract from contract.md.
- Executor: Agent B.
- Write location: src/ui/export/ and corresponding interface verification.
- Submit the date range and category according to the contract; handle successful downloads and errors.
- Verify independently with contract response doubles; hand off to integration.md to connect the real backend.

## Acceptance

- [ ] The operation includes current date and category filters; full export is unaffected by current pagination.
- [ ] A successful response triggers a file download; an empty result still downloads a header file.
- [ ] Exceeding the limit prompts narrowing the range and does not trigger a download.
- [ ] General failures are understandable and allow retrying.
- [ ] Verification records state the response-double scope and delivered version.

## Next steps

1. Read the contract and prepare success, empty-data, limit-exceeded, and failure responses.
2. Implement the interface and check input/response behavior.
''')
put('C04','integration.md','''# Connect the real export service and verify browser CSV downloads

## Inputs and scope

- Blocked by: usable implementation and verification versions from backend.md and frontend.md.
- Executor: Agent A.
- Sole shared-entry writer: Agent A, src/app/export.ts.
- Delivery location: verification/csv-export.md and the integration version.
- Connect the complete query and interface; run all overall acceptance checks in parent-feature.md.

## Acceptance

- [ ] The actual browser download matches every record in the known complete readable set.
- [ ] Special characters, sorting, permissions, and 0/5000/5001 boundaries match the parent.
- [ ] Each result identifies the integration version and actual data baseline.
- [ ] Mark the overall outcome complete only after all required parent acceptance criteria pass.

## Next steps

1. Check the actual backend/frontend entry points and contract versions.
2. Connect src/app/export.ts, prepare multi-page data, and perform browser acceptance.
''')
put('C04','plan.md','''# Execution order

1. Agent A completes contract.md first; the maintainer reviews the contract.
2. Once the contract is usable, A handles backend.md and B handles frontend.md.
3. The maintainer reviews one item at a time; the other pending item still counts toward WIP. Agents prioritize rework and do not start another item.
4. Once both implementations are usable, A alone maintains src/app/export.ts and completes integration.md.
5. Check outcomes against the overall acceptance in parent-feature.md.

- Each Agent executes one item at a time; the aggregate parent does not occupy another slot.
- Backend and frontend wait for the shared contract and have no artifact dependency on each other.
- Integration waits for both implementations.
- Assigning a sole writer prevents shared-entry conflicts; artifact dependencies follow actual inputs.
- This round is planning; the filenames above identify work. Actual Team, status IDs, and new issue IDs were not supplied.
''')

c5body='''# Export all filtered data

## Current results

- PR #81 is merged; version [merge-81-abc](fixture://exp-21/merge-81-abc).
- PR review and unit tests passed.
- Lin’s latest acceptance data expects IDs 1–240; actual.csv contains only IDs 1–80, each once.
- IDs 81–240 are missing, 160 records total; full export acceptance failed.
- Evidence: [actual.csv](fixture://exp-21/actual.csv), from the latest comment and acceptance data in requests.md C05.
- Current stage: Implementing/exp-implement, for the missing-record fix.

## Required acceptance

- [ ] 240  records complete, each exactly once.
- [ ] Chinese and newline fields are correct.
- [ ] Include only data readable by the current user.

## Next steps

1. Open the export query path in merge-81-abc; compare actual.csv IDs with query responses stage by stage to locate missing data.
2. Fix missing records using traceable evidence; rerun the same 240 records and check count, ID set, and duplicates.
3. Check Chinese, newline, and permission cases; link each result to the tested version before declaring completion.

## Relations and workflow

- Parent EXP-20: Implementing, waiting for this required export artifact.
- Merge automation using a PR closing relation set this issue to Done before product acceptance.
- The automation settings maintainer should check whether to map merging to acceptance; current tools only support issue updates.
'''
put('C05','EXP-21.md',c5body)
put('C05','workspace-before.json',{'issue':{'identifier':'EXP-21','statusId':'exp-done','body':'Export all filtered data; required acceptance: all 240 records exactly once, correct Chinese and newline fields, readable data only.'},'parent':{'identifier':'EXP-20','status':'Implementing'},'automation':{'closingMerge':'Done','parentSubIssue':False}})

spec='''# JSON export specification

## Scope

- For PAY-11’s JSON export implementation.
- Authoritative document: docs/export-spec.md.
- Requirement basis: PAY-16 current body and latest user comment, fully replacing the old CSV specification.
- Data basis: PAY-15’s [data-contract-v2](fixture://pay-15/data-contract-v2).
- Check date: 2026-09-13.

## Output format

- The top level is a JSON array.
- Each object contains the following three fields.

| Field | JSON type | Definition |
| --- | --- | --- |
| date | string | Date in YYYY-MM-DD format from data-contract-v2. |
| amount | number | Integer amount from data-contract-v2; the current contract adds no positive/negative restriction. |
| category | string | Category string; preserve the source value. |

- Output `[]` when there is no data.
- `id` is the source’s unique string, used for stable sorting and excluded from the three output fields.

## Sorting

1. First sort by source `date` ascending.
2. Within the same date, sort by source `id` ascending.
3. After sorting, map to objects with date, amount, and category fields.

To ensure consistent results across environments, ascending strings compare Unicode code points character by character; when one string is a prefix, the shorter string comes first.
This document defines the comparison rule independently of user-locale ordering.
Valid YYYY-MM-DD dates use the same string rule to compare year, month, and day.

## Sorting example

The following data illustrates the specification.

Input:

```json
[
  {"id":"b","date":"2026-09-02","amount":85,"category":"Food"},
  {"id":"c","date":"2026-09-01","amount":100,"category":"Transport"},
  {"id":"a","date":"2026-09-02","amount":20,"category":"Other"}
]
```

Sorted source IDs are c, a, b; expected output:

```json
[
  {"date":"2026-09-01","amount":100,"category":"Transport"},
  {"date":"2026-09-02","amount":20,"category":"Other"},
  {"date":"2026-09-02","amount":85,"category":"Food"}
]
```

Empty-data example: input `[]`, output `[]`.

## Content checks

- Compare field definitions with data-contract-v2.
- The sorting example covers both cross-date ordering and same-date ID ordering.
- Example output parses as JSON and objects match the three-field definition.
- Check record: ../verification.json, including this document’s SHA-256 and individual results.
'''
put('C06','docs/export-spec.md',spec)
put('C06','workspace-before.json',{'issue':{'id':'pay-16','identifier':'PAY-16','statusId':'pay-doing','assigneeId':'user-ren','parent':'PAY-11','body':'Deliver the JSON export specification; fields date, amount, category; integer amounts; ascending date, then ascending id within a date; artifact docs/export-spec.md; acceptance covers field definitions, sorting examples, and empty output [].'},'parent':{'identifier':'PAY-11','body':'Deliver JSON export; the specification is an implementation prerequisite.'},'allocation':{'writer':'session B','scope':['PAY-16','docs/export-spec.md'],'sessionAStopped':True,'updatedAt':'2026-09-13T10:00:00+08:00'},'prerequisite':{'identifier':'PAY-15','status':'Done','artifact':'fixture://pay-15/data-contract-v2','content':{'date':'YYYY-MM-DD','amount':'Integer','category':'String','id':'Unique string'}},'parentAutomation':False})

# Read back saved contents before deciding simulated issue updates and saving operation evidence.
for c in routes:
    logs=[{'operation':'read_fixture','source':'requests.md#'+c,'result':'Read the authoritative data supplied for this case; source-fixture.md preserves its location'}]
    if c=='C01':
        actual=json.loads(read(c,'workspace.json'))
        assert len(actual['issues'])==3
        assert all(x['projectId']==actual['project']['id'] and x['teamId']=='team-pocket' and x['assigneeId']=='user-owner' for x in actual['issues'])
        assert actual['issues'][2]['blockedBy']==['sim-pkt-1','sim-pkt-2']
        logs += [{'operation':'plan_fields','source':'environment.md; project-brief.md; PKT-1.md–PKT-3.md','fields':state,'result':'Use existing fixture IDs; allocate new object IDs in the local simulation'}, {'operation':'create_local_simulation','target':'workspace.json','result':'Wrote one Project and three issues'}, {'operation':'readback','source':'workspace.json','result':'Read back and checked Project, Team, Assignee, status, and blockedBy; first item Todo, others Backlog'}]
    elif c in ('C02','C03','C04'):
        names={'C02':['environment.md','FIN-10.md'],'C03':['parent-bug.md','investigation-issue.md','sequence.json'],'C04':['parent-feature.md','contract.md','backend.md','frontend.md','integration.md','plan.md']}[c]
        for n in names:
            assert read(c,n).strip()
        logs += [{'operation':'interpret','source':'requests.md#'+c,'result':{'C02':'Read both listing pages and select proj-ledger; latest instructions prioritize FIN-10. Ready means ready to execute, not acceptance; FIN-9 has an active executor and FIN-8 lacks prerequisite artifacts.','C03':'Restoring promised behavior is a Bug; evidence is insufficient to select a root cause, so provide an independently transferable diagnosis draft first.','C04':'Define the shared contract first, then parallel frontend/backend work; preserve full browser acceptance and capacity for one review at a time.'}[c]}, {'operation':'save_drafts','targets':names,'result':'Saved and read back usable drafts'}, {'operation':'planned_remote_fields','fields':None,'result':'This case authorizes preparation/drafts only; statuses and relations in deliverables describe current state or plans, with no simulated remote writes'}]
    elif c=='C05':
        before=json.loads(read(c,'workspace-before.json'))
        expected=set(range(1,241)); actual=list(range(1,81))
        missing=sorted(expected-set(actual))
        assert len(missing)==160 and len(set(actual))==80
        put(c,'verification.json',{'basis':'Latest acceptance summary in requests.md C05; actual.csv contents were not attached; the following set calculation uses that summary','expectedCount':240,'actualCount':80,'missingIds':missing,'duplicatesInReportedActual':[],'complete':False,'characters':None,'permissions':None})
        before['issue'].update(statusId='exp-implement',body=c5body)
        put(c,'workspace.json',before)
        after=json.loads(read(c,'workspace.json'))
        assert after['issue']['statusId']=='exp-implement' and after['issue']['body']==read(c,'EXP-21.md')
        assert after['parent']['status']=='Implementing'
        logs += [{'operation':'compare_reported_ids','source':'requests.md#C05 → latest acceptance; verification.json','result':'Calculate 160 missing records from the provided summary; do not describe the fixture summary as rereading the original actual.csv file'}, {'operation':'reread_before_update','source':'workspace-before.json','result':'Read the local simulated prior state; Done came from PR automation, while required acceptance failed'}, {'operation':'planned_fields','target':'EXP-21','fields':{'statusId':'exp-implement','bodyFile':'EXP-21.md'},'result':'Repair the original promise gap; reopen the original issue for rework'}, {'operation':'update_local_simulation','target':'workspace.json','result':'Saved simulated body and status updates'}, {'operation':'readback','source':'workspace.json','result':'Read back and confirmed exp-implement, complete body, and EXP-20 still Implementing; parent automation off'}]
    else:
        before=json.loads(read(c,'workspace-before.json'))
        assert before['allocation']['sessionAStopped'] and before['allocation']['writer']=='session B'
        doc=read(c,'docs/export-spec.md')
        blocks=re.findall(r'```json\n(.*?)\n```',doc,re.S)
        inp,out=map(json.loads,blocks)
        sorted_rows=sorted(inp,key=lambda x:(x['date'],x['id']))
        assert out==[{k:r[k] for k in ('date','amount','category')} for r in sorted_rows]
        assert all(set(r)=={'date','amount','category'} and isinstance(r['amount'],int) for r in out)
        assert 'Empty-data example: input `[]`, output `[]`.' in doc
        assert doc.startswith('# JSON export specification') and 'Output first-row header' not in doc
        sha=hashlib.sha256(doc.encode('utf-8')).hexdigest()
        put(c,'verification.json',{'source':'docs/export-spec.md','sha256':sha,'basis':'Current body, latest comment, and embedded PAY-15 data-contract-v2 contents in requests.md C06','checks':[{'name':'Compare date YYYY-MM-DD, integer amount, and string category with the source','passed':True},{'name':'Parse JSON examples and compare expected date/id sorting results','passed':True},{'name':'The three output fields exclude the sorting id','passed':True},{'name':'Empty input and output [] explicitly stated','passed':True},{'name':'Title and format changed to JSON; old header rule removed','passed':True}],'scope':'Document content and example checks'})
        body='''Deliver the JSON export specification.

- Fields: date, amount, category.
- Amount is an integer.
- Sort data by date ascending, then id ascending within a date.
- Artifact: [docs/export-spec.md](docs/export-spec.md).
- Prerequisite source: PAY-15/fixture://pay-15/data-contract-v2.
- For PAY-11’s JSON export implementation.

## Completed items

1. Completely replace with a JSON specification defining three fields and the source contract.
2. Add cross-date and same-date id sorting examples and empty-array output.

## Verification results

- [x] Field definitions match current requirements and data-contract-v2.
- [x] Sorting example JSON parses; output follows ascending date, then ascending id within a date.
- [x] Empty-data output is explicitly [].

- Evidence: [verification.json](verification.json).
- Tested document SHA-256:'''+sha+'''
- Local simulated artifact links are relative to this directory.

## Continuation entry point

The PAY-11 implementation successor reads the fields and sorting examples in docs/export-spec.md first, then implements JSON export accordingly.
'''
        put(c,'PAY-16.md',body)
        # Before updating, reread the latest fixture decisions and local prior state, then write within the explicit allocation.
        assert 'Completely replace with JSON' in fixture(c)
        current=json.loads(read(c,'workspace-before.json'))
        current['issue'].update(body=body,statusId='pay-done')
        put(c,'workspace.json',current)
        after=json.loads(read(c,'workspace.json'))
        assert after['issue']['statusId']=='pay-done' and after['issue']['assigneeId']=='user-ren'
        assert after['issue']['parent']=='PAY-11' and after['issue']['body']==read(c,'PAY-16.md')
        logs += [{'operation':'resolve_current_scope','source':'requests.md#C06 → latest body/comment/allocation/PAY-15/current file','result':'JSON replaces CSV; A has stopped, B is the sole writer; existing authorization permits completing the document and updating the issue'}, {'operation':'edit_document','target':'docs/export-spec.md','result':'Wrote JSON fields, sorting, and empty-data specification'}, {'operation':'verify_document','source':'docs/export-spec.md; verification.json','result':'Read back, compared with the contract, parsed examples, and checked sorting and output fields'}, {'operation':'reread_before_update','source':'requests.md#C06; workspace-before.json','result':'Recheck effective requirements and exclusive allocation before updating'}, {'operation':'planned_fields','target':'pay-16','fields':{'statusId':'pay-done','bodyFile':'PAY-16.md'},'result':'Required documentation completion criteria checked; the environment requires no additional human review'}, {'operation':'update_local_simulation','target':'workspace.json','result':'Saved simulated PAY-16 body/status update'}, {'operation':'readback','source':'workspace.json','result':'Confirmed pay-done, user-ren, PAY-11 relation, and JSON body; PAY-11 still owns the parent’s overall implementation outcome'}]
    put(c,'operations.json',{'simulationOnly':True,'source':'requests.md#'+c,'operations':logs,'mentionHandling':'No native mention tool contract or actual issue URLs were provided; documents use known identifiers, simulated relations preserve supplied IDs, and do not claim native mentions were created.'})

put('','README.md','''# Deliverables for six cases

1. C01: environment.md, project-brief.md, PKT-1.md through PKT-3.md; workspace.json stores the created local simulated Project and issues.
2. C02: environment.md and FIN-10.md; current state and first draft.
3. C03: parent-bug.md, investigation-issue.md, and sequence.json; diagnose first, then define the fix from evidence.
4. C04: parent-feature.md, contract.md, backend.md, frontend.md, integration.md, and plan.md; preserves the shared contract and full integration acceptance.
5. C05: EXP-21.md, verification.json, and workspace.json; simulates reopening the original issue as Implementing.
6. C06: docs/export-spec.md, verification.json, PAY-16.md, and workspace.json; completes the JSON specification and simulates updating to Done.

Each route.json preserves skill routing; operations.json records actual isolated operations and planned fields.
''')
print(json.dumps({'output':str(OUT),'cases':list(routes),'result':'Saved six cases and completed in-script readback checks'},ensure_ascii=False))
