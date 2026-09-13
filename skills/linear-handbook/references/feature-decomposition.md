# Decomposing a large Feature: Task CSV export

The following is a tabletop exercise for a fictional product.
It uses the requirements from the [Feature template's completed example](../assets/templates/feature.md#completed-example).
Paths name planned artifacts.
Acceptance lists describe results to verify during implementation.

Method: [Single-session decomposition guide](issue-decomposition.md).
Dependency criteria: [Milestones and dependency scheduling](planning-and-dependencies.md#3-identify-real-blockers).

This case extracts a shared contract so the API and interface can be handed off separately.
If a usable contract already exists and one session can complete implementation and verification, combine the work into one Feature issue.
The four-sub-issue structure applies only to this case's delivery needs.

## Parent: Let project managers export the currently filtered tasks

- User: a project manager with project read permission.
- Scenario: preparing weekly meeting materials after filtering the task list.
- Outcome: a complete CSV of the current filtered results.
- Adopted scope
  - Export all tasks matching the current filters.
  - Preserve the current list ordering.
  - Use UTF-8.
  - Output fields
    - Task ID.
    - Title.
    - Status.
  - Disable the export button for empty results.
  - Offer retry after request failure.
- Additional decisions for this case
  - Use a synchronous download request.
  - Handle at most 1,000 records per request.
  - Prompt narrowing the range when the limit is exceeded.
  - Do not return a truncated file when the limit is exceeded.
  - Retry with the failed request's filters and sorting.
  - Prevent duplicate submissions while a request is in flight.
  - Recheck project read permission at the download endpoint.
- Non-goals
  - Large background exports need a job queue and completion notifications; plan them separately.

These quantities and behaviors are assumptions for this case.

### Integration acceptance

- [ ] The interface downloads a correctly filtered CSV.
  1. Prepare 3 pending tasks and 2 completed tasks.
  2. Set the list page size to 2.
  3. Filter pending tasks and sort by ID ascending.
  4. Export from the first page.
  5. Use a CSV parser to verify all 3 pending tasks.
- [ ] Data follows ascending ID order.
- [ ] Each record has exactly the 3 specified fields.
- [ ] Chinese titles match their original values after UTF-8 decoding.
- [ ] Titles containing commas remain in one field after CSV parsing.
- [ ] Empty results cannot trigger an export.
- [ ] A failed export can be retried with the original conditions.
  1. Make the download endpoint return 500.
  2. Confirm “Export failed. Please retry.” is displayed.
  3. Restore the service and select retry.
  4. Check the file against the original filters and sorting.
- [ ] More than 1,000 records displays “Narrow the filters before exporting.”
- [ ] Exactly 1,000 matching records download completely.
- [ ] A limit-exceeded response provides no truncated CSV.
- [ ] Requests without project read permission cannot obtain task contents.
- [ ] Repeated clicks during a request do not create a second request.

## Sub-issue 1: Confirm the download contract

- Inputs
  - The parent's adopted requirements.
  - Filter semantics of the existing task query interface.
  - Existing permission-check entry point.
- Outputs
  - `contracts/task-export.md`: request and response specification.
  - `fixtures/task-export/`: normal and failure response examples.
- Scope
  - Fix the request's filter parameters.
  - Fix the sorting parameters.
  - Fix CSV fields and encoding.
  - Define empty-result handling.
  - Define limit-exceeded responses.
  - Define permission-error responses.
  - Define service-failure responses.
- Acceptance
  - [ ] The document identifies the request or response rule for each parent requirement.
  - [ ] Examples cover successful downloads.
  - [ ] Examples cover empty results.
  - [ ] Examples cover limit-exceeded errors.
  - [ ] Examples cover permission errors.
  - [ ] Examples cover service failures.
  - [ ] API and interface successors can implement independently against the same contract.

When this sub-issue is complete, update the issue with the contract version and example locations.
An empty file or a list of field names alone is insufficient delivery.

## Sub-issue 2: Make the download endpoint produce the correct CSV

- Inputs
  - Confirmed download contract.
  - Response examples from sub-issue 1.
  - Task data read entry point.
  - Project permission-check entry point.
- Outputs
  - `src/task-export/api/`: download endpoint implementation.
  - `tests/task-export-api/`: contract and data verification.
- Scope
  - Apply the requested filters.
  - Apply the requested sorting.
  - Export all matching data.
  - Check read permission.
  - Generate UTF-8 CSV.
  - Return empty results and errors according to the contract.
- Acceptance
  - [ ] Output across pages contains exactly 3 pending tasks.
  - [ ] Output ordering matches the request.
  - [ ] Parsed CSV has exactly the 3 specified fields.
  - [ ] Chinese titles match their original values after parsing.
  - [ ] Titles containing commas match their original values after parsing.
  - [ ] Empty results match the contract.
  - [ ] 1,000 records export completely.
  - [ ] 1,001 records return a limit-exceeded error.
  - [ ] A limit-exceeded response provides no truncated file.
  - [ ] Unauthorized requests cannot read task contents.
  - [ ] Service-failure responses match the contract.

## Sub-issue 3: Make the interface handle exports according to the contract

- Inputs
  - Confirmed download contract.
  - Simulated responses from sub-issue 1.
  - Current task-list filter state.
  - Current task-list sorting state.
- Outputs
  - `src/task-export/ui/`: export interactions.
  - `tests/task-export-ui/`: interface verification with simulated responses.
- Scope
  - Submit filters and sorting from the list.
  - Receive successful responses and start downloads.
  - Disable the button for empty results.
  - Prevent duplicate submissions during requests.
  - Display limit-exceeded guidance.
  - Display permission-error guidance.
  - Offer a retry action after service failure.
- Acceptance
  - [ ] Requests include the current filters.
  - [ ] Requests include the current sorting.
  - [ ] A successful response triggers one download.
  - [ ] The button is disabled for empty results.
  - [ ] Repeated clicks during a request do not create a second request.
  - [ ] Exceeding the limit displays the parent's specified message.
  - [ ] Permission errors do not trigger a download.
  - [ ] Service failures display the parent's specified message.
  - [ ] Retry uses the failed request's original filters.
  - [ ] Retry uses the failed request's original sorting.

Acceptance with simulated responses establishes interface behavior only.
The download endpoint and integration acceptance together verify actual CSV contents.

## Sub-issue 4: Integrate the real download flow

- Inputs
  - Usable download endpoint from sub-issue 2.
  - Interface ready for integration from sub-issue 3.
  - Confirmed download contract.
  - Reproducible parent acceptance data.
  - Access to the test environment.
- Outputs
  - An integration version connecting the actual interface to the download endpoint.
  - `tests/task-export-e2e/`: overall flow checks.
  - `verification/task-export.md`: version and acceptance evidence entry points.
- Scope
  - Connect the interface and actual endpoint.
  - Verify the parent's complete user flow.
  - Fix contract gaps found during integration.
- Acceptance
  - [ ] All parent integration acceptance criteria in this document pass.
  - [ ] Verification records identify the actual integration version.
  - [ ] Each parent acceptance criterion has corresponding evidence.
  - [ ] The parent body includes usable artifact entry points.

The integration sub-issue performs verification across components and provides evidence.
The parent reviewer determines overall completion after checking the original commitment and integration evidence.
The integration sub-issue being Done is a required input to parent closure.

## Real dependencies and parallel work

| Waiting work | Required prerequisite | Specific impact when missing |
| --- | --- | --- |
| Download endpoint | Usable download contract | Cannot determine request and response acceptance specifications |
| Export interface | Usable download contract | Cannot verify interactions against consistent simulated responses |
| Real download integration | Usable download endpoint | Cannot obtain actual CSV |
| Real download integration | Interface ready for integration | Cannot complete a download from the list |

- Once the contract is confirmed, the download endpoint and interface can proceed in parallel.
  - Interface acceptance uses simulated responses.
  - Download endpoint acceptance directly compares data.
  - Each has a determinable outcome.
- Allocate write scopes, then use WIP limits to decide whether to take both on simultaneously.
- The order of parent sub-issues does not imply dependencies.
- Integration waits for both the download endpoint and interface to be usable.

## Tabletop exercise: Work exceeds the session

Suppose the download endpoint was planned for delivery in one session.
Execution reveals that the existing query can retrieve only the first list page.
Fulfilling “all filtered results” first requires data retrieval across pages.

1. Save the completed endpoint skeleton and data-verification cases.
2. Record the worktree location and version identifier in the handoff.
3. Record verification performed, preserving evidence that only 2 records were output when 3 were expected.
4. Keep the download endpoint issue unfinished.
5. Create a follow-up sub-issue, “Let the export query retrieve all matching tasks.”
6. Set the download endpoint to wait for data retrieval across pages.
7. Preserve acceptance for all filtered results in the parent.
8. The successor first reproduces the case where 3 records produce only 2 results.

### Follow-up sub-issue: Complete data retrieval across pages

- Inputs
  - Saved failing case.
  - Existing query entry point.
  - Download contract filter and sorting rules.
- Outputs
  - Complete data retrieval for the download endpoint.
  - Verification results for data across pages.
- Scope
  - Retrieve all matching tasks.
  - Preserve the specified ordering.
  - Provide information needed to detect the limit.
- Acceptance
  - [ ] All 3 matching tasks are retrieved with a page size of 2.
  - [ ] Combining pages produces no duplicate tasks.
  - [ ] Combined ordering matches the request.
  - [ ] 1,001 records can be identified as over the limit.

After the new sub-issue is complete, the original download endpoint connects the data retrieval and completes its own acceptance.
The interface can continue against the existing contract.
This decomposition preserves the parent's full commitment and gives the successor a reproducible first step.
