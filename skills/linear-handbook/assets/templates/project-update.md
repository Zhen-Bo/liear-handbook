# Project update template

For explaining changes to overall project delivery.
Put individual operation details in an [issue comment](progress-comment.md).

## When to use

The following are recommendations.

- Scheduled update date: Summarize changes affecting delivery since the last update.
  - If there is no new information, a progress check is sufficient.
- Key milestone reached: Explain the outputs now available for use.
- Delivery risk changes: Explain affected goals and response actions.
- Scope or date finalized: Explain the new commitment and reasons for adoption.
- Project completed: Summarize overall outputs and acceptance evidence links.

The project lead determines update frequency based on collaboration needs.
Link individual issue details to support the overall assessment.
Keep the overview updated with the currently effective project scope.
Update each issue body with its current conclusions.

## Usage

1. Select health in the update interface.
2. Copy the concise version and replace `{…}`.
3. Retain content affecting overall delivery.
4. Remove inapplicable sections.

The following health assessment recommendations should be adjusted to the project's commitments.

- On track: Current evidence supports meeting the commitment.
- At risk: A specific risk could prevent meeting the commitment.
- Off track: Work has already deviated from the commitment and requires a revised approach or target.

Provide a reason for the health assessment.
The proportion of completed items does not directly determine health.
Express estimates separately from observed results.

## Concise version

```markdown
## Result summary

- Period: {Dates from the last update to this update.}
- Health rationale: {Specific evidence supporting the selected health.}
- Target: {Currently committed delivery date or milestone.}

## Completed items

1. {Delivered outcome affecting the project, with an entry point.}

## Risks and decisions

- {Risk topic.}
  - Fact: {Observed result and evidence.}
  - Estimated impact: {Delivery impact that has not yet occurred.}
  - Response: {Adopted action.}
  - Reason: {Basis for adoption.}
  - Owner: {Named responsible person.}
  - Checkpoint: {Date or event for reassessing the risk.}

## Next steps

- {Next specific outcome.}
  - Work: {Insert a native issue mention.}
  - Owner: {Named responsible person.}
  - Expected: {Completion date.}
```

## Completed example

The following is a fictional example.
Replace evidence names with accessible entry points in actual use.

Interface selection: At risk.

```markdown
## Result summary

- Period: 2026-09-07 to 2026-09-11.
- Health rationale: Multipage exports still omit records, which may affect the trial date.
- Target: Provide a trial of task CSV export on 2026-09-16.

## Completed items

1. Integrated the export button into the list page; see "CSV trial demo" in project Resources.
2. Confirmed field formats; see "EXPORT-01 approved requirements" in project Resources.

## Risks and decisions

- Missing records across pages
  - Fact: export-rc1 outputs only 100 of the 200 test records.
  - Evidence: Export issue attachment export-rc1-tests.txt, pagination FAIL.
  - Estimated impact: If unresolved by September 14, the September 16 trial may be delayed.
  - Response: Locate the missing records using request logs, then perform trial acceptance after the fix.
  - Reason: Complete filtered results are required acceptance criteria for EXPORT-01.
  - Owner: Yi-An Chen.
  - Checkpoint: Multipage acceptance results on 2026-09-14.

## Next steps

- Complete the multipage export fix.
  - Work: Insert the native issue mention for the pagination fix here.
  - Owner: Yi-An Chen.
  - Expected: 2026-09-14.
```

## Configuration notes

### Feature facts

Verified on: 2026-09-13.

- A Project update includes a health indicator and rich text description.
  - Source: [Initiative and Project updates — Overview](https://linear.app/docs/initiative-and-project-updates#overview).
- Health options
  - On track.
  - At risk.
  - Off track.
  - Source: [Create Initiative and Project updates](https://linear.app/docs/initiative-and-project-updates#create-initiative-and-project-updates).
- The latest update appears in Project Overview.
  - Source: [View Initiative and Project updates](https://linear.app/docs/initiative-and-project-updates#view-initiative-and-project-updates).
- Past updates are available in the Updates tab.
  - Source: [View Initiative and Project updates](https://linear.app/docs/initiative-and-project-updates#view-initiative-and-project-updates).


## Writing defaults

Follow [writing](../../references/writing.md) for formatting, evidence, and the issue's current conclusions.
