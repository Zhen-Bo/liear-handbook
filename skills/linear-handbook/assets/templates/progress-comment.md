# Issue comment template

For new progress on a single work item.
For an issue body starting point, see [Bug](bug.md) and [Feature](feature.md).

## Where and when to update

The following are recommendations.

- Issue body: Update the effective content when the goal or adopted conclusion changes.
  - Add output links.
  - Replace superseded approaches.
  - Retain open questions that still affect delivery.
- Comment: Append when there are new findings or results.
  - Progress: An intermediate output with a locatable entry point becomes available.
  - Blocker: Missing required input prevents specific work from continuing.
  - Decision: Record reasons and impact after adopting an approach.
  - Verification: New evidence is sufficient to change the assessment.
  - Completion: Record outputs and evidence after acceptance criteria are met.
- Issue status: Update the property to match the actual work stage.
  - A status change alone does not need a duplicate comment.
  - Keep the actual unfinished status while acceptance criteria remain unmet.
- Project update: When a change affects overall delivery, summarize its impact using [project-update.md](project-update.md).
- Handoff: Use [handoff.md](handoff.md) when the recipient needs execution context to resume work.

## Usage

1. Choose sections that contain new information this time.
2. Replace `{…}` and attach locatable evidence to each item.
3. Remove empty fields and inapplicable sections.
4. Update the body with the currently adopted conclusions.

Label observed results as facts.
For hypotheses, identify supporting evidence and the next verification action.
Attach source sections and verification dates to research conclusions.
Use fixed-version permalinks for code evidence.

## Concise version

```markdown
## Result summary

- Progress: {Current delivery stage.}
- Output: {Accessible output link.}

## Findings

- Fact: {Observation and evidence location.}
- Hypothesis
  - Interpretation: {Explanation awaiting verification.}
  - Basis: {Evidence supporting this explanation.}
  - Check: {Action that can determine whether the explanation holds.}

Verified on: {YYYY-MM-DD; required only for research conclusions.}

## Decision

- Adopted: {Current approach.}
- Reason: {Evidence supporting adoption.}
- Impact: {Delivery or operations requiring adjustment.}

## Blocker

- Problem: {Missing required input.}
- Impact: {Specific work that cannot continue.}
- Resolution condition: {Input that allows work to resume.}
- Owner: {Named responsible person.}

## Completed items

1. {Delivered outcome and entry point.}

## Verification results

- [x] {Actual passing result and evidence location.}
- [ ] {Actual failing result and evidence location.}

## Next steps

- {Specific action; use a native issue mention to link related work.}
```

## Completed examples

The following five comments are fictional examples.
Their filenames and results demonstrate how to fill in the template.
Replace them with accessible evidence entry points in actual use.

### Progress

```markdown
## Progress

- Output: CSV export field mapping is complete.
- Entry point: This issue's attachment export-columns.md.
- Fact: All three fields specified by requirement EXPORT-01 are mapped to source fields.

## Next steps

- Implement query inputs for the current filters.
```

### Blocker

```markdown
## Blocker

- Problem: The task API returns 403 for the test account.
- Evidence: This issue's attachment export-access.log, line 18.
- Impact: Cannot verify that the multipage export includes all filtered results.
- Resolution condition: The test account can read the test project containing 200 tasks.
- Owner: Yi-An Chen.

## Next steps

- Rerun the multipage export case after Yi-An Chen grants read access to the test project.
```

### Decision

```markdown
## Decision

- Adopted: Export uses the list's current sort order.
- Reason: EXPORT-01 acceptance criteria require CSV order to match the list.
- Impact: Query inputs must include the current sort field.
- Decision basis: Requirements owner Yi-An Chen approved this in the issue's "Export sorting" discussion.
```

### Verification

```markdown
## Verification results

- [x] CSV parsing preserves commas within titles.
  1. Run the csv-title test for version export-rc1.
  2. Check csv-title PASS in this issue's attachment export-rc1-tests.txt.
- [ ] The multipage export should contain 200 tasks but actually contains only 100.
  - Evidence: This issue's attachment export-rc1-tests.txt, pagination FAIL.

## Findings

- Hypothesis
  - Interpretation: The export query reads only the first page.
  - Basis: The result count and API page limit are both 100.
  - Check: Compare request logs to see whether the next-page cursor is missing.

## Next steps

- Inspect next-page cursor handling in the export query.
```

### Completion

```markdown
## Result summary

- Output: Currently filtered tasks can be exported as CSV.
- Remote: This issue's attachment export-rc2.zip.
- Local: dist/export-rc2.zip.

## Completed items

1. Delivered the export button.
2. Delivered the CSV query that uses the current filters.
3. Fixed missing records across pages.

## Verification results

- [x] All agreed acceptance criteria pass.
  - Evidence: This issue's attachment export-rc2-acceptance.md.

## Next steps

- Hand version export-rc2 to the deployment work item; insert its native issue mention here.
```

## Configuration notes

### Feature facts

Verified on: 2026-09-13.

- Use a threaded reply to continue discussion of the same topic.
  - Source: [Comments and reactions — Threads](https://linear.app/docs/comment-on-issues#threads).


## Writing defaults

Follow [writing](../../references/writing.md) for formatting, evidence, and the issue's current conclusions.
