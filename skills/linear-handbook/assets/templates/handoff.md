# Handoff template

For another executor or a later session to continue the work.
For choosing the authoritative document location, see [Documentation placement guide](../../references/documentation.md#authoritative-version-and-links).

## Usage

The following are recommendations.

1. First update the issue body with the currently effective conclusions.
2. Specify one handoff entry point the recipient can read.
3. Copy the concise version and replace `{…}`.
4. Remove fields that do not affect continuation.
5. Check that the inputs required for the next steps are present.

Leave a recoverable work state before ending the handoff.
When an actual blocker exists, record the condition for resolving it and who is responsible.
When acceptance criteria are met, record the result with a [completion comment](progress-comment.md#completion).
Completing a handoff does not complete the work while required acceptance criteria remain unmet.

## Concise version

```markdown
## Continuation goal

{The specific outcome the recipient must deliver in this session.}

- Issue: {Native issue mention.}
- Current stage: {Assessable progress.}
- Completion criteria: {Location of acceptance criteria in the issue body.}

## Required inputs

- Authoritative requirements: {Entry point and applicable section.}
- Work location: {Repository or directory.}
- Execution baseline: {Branch and commit, or identifiable file version.}
- Existing changes: {Changes and files not yet saved in version control.}
- Environment: {Versions or configuration required for the next step.}
- Test data: {How to obtain it and prerequisites.}
- Existing authorization: {Explicit scope and basis for permitted operations.}

## Completed items

1. {Delivered outcome.}
   - Remote: {Clickable output link.}
   - Local: {File location.}

## Verification results

- [x] {Actual passing result.}
  - Baseline: {Tested version.}
  - Evidence: {Record link and location.}
- [ ] {Actual failing result.}
  - Evidence: {Record link and location.}

## Adopted conclusions

- Decision: {Current approach.}
- Reason: {Evidence supporting adoption.}
- Discussion: {Necessary link for tracing the decision.}

## Remaining work and blockers

- Remaining work: {Specific remaining outcome.}
- Blocker
  - Gap: {Missing required input.}
  - Impact: {Operation that cannot continue.}
  - Resolution condition: {Result that allows work to resume.}
  - Owner: {Named responsible person.}
- Hypothesis
  - Interpretation: {Unconfirmed explanation affecting the next step.}
  - Basis: {Supporting evidence.}
  - Check: {Next verification action.}

## Next steps

1. {First directly executable action.}
2. {Action after success.}

## Acceptance

- [ ] {Observable result when this continuation is complete.}
```

## Completed example

The following is a fictional handoff example.
Replace evidence names with accessible entry points in actual use.

```markdown
## Continuation goal

Fix missing records in CSV exports spanning multiple pages.

- Issue: Insert the native issue mention for the pagination fix here.
- Current stage: The likely query scope has been identified.
- Completion criteria: EXPORT-01, "Export all filtered results".

## Required inputs

- Authoritative requirements: This issue's attachment export-requirements.md, EXPORT-01.
- Work location: `<Actual working directory>`/task-export.
- Execution baseline: This issue's attachment task-export-rc1.zip.
- Existing changes: Cursor logging added to src/export.ts, saved in attachment task-export-working.zip.
- Environment: Node.js 22.
- Test data: fixtures/tasks-200.json.
- Existing authorization: The issue body's "Execution scope" permits local fixes and tests.

## Completed items

1. Created a reproduction case with 200 tasks.
   - Remote: This issue's attachment task-export-working.zip.
   - Local: tests/export-pagination.test.ts.

## Verification results

- [ ] The export should contain 200 records but actually contains only 100.
  - Baseline: export-rc1.
  - Evidence: This issue's attachment export-rc1-tests.txt, pagination FAIL.

## Adopted conclusions

- Decision: Limit the fix to the export query using the existing API.
- Reason: The requirement changes only export behavior.
- Discussion: This issue's "Export query scope" decision thread.

## Remaining work and blockers

- Remaining work: Locate the missing data using request logs, then fix the issue.
- Hypothesis
  - Interpretation: The current result contains only the first page.
  - Basis: 100 records matches the API page limit.
  - Check: Inspect cursor logs in src/export.ts.

## Next steps

1. Read src/export.ts in task-export-working.zip.
2. Run npm test -- export-pagination.
3. Use cursor logs to check whether the next-page request is missing.
4. Based on the findings, fix the query operation causing missing records.
5. Rerun export-related tests.

## Acceptance

- [ ] The export contains all 200 filtered results.
- [ ] Each task ID appears exactly once.
- [ ] CSV order matches the list sort order.
```

## Evidence and policy

### Recommendations

- Attach official source sections to research conclusions.
- Put the verification date on its own line.
- Link code evidence to a fixed version.
- Retain only uncertainty that affects continuation.
- When access is required, provide the access request entry point instead of including credentials.
- Return lasting conclusions to the authoritative document and keep the summary needed for continuation in the handoff.


## Writing defaults

Follow [writing](../../references/writing.md) for formatting, evidence, and the issue's current conclusions.
