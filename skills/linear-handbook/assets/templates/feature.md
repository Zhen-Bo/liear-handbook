# Feature issue body template

For delivering a new capability that users could not previously use.
Classification: [Work type guide — Feature](../../references/issue-types.md#feature).

## Usage

1. Enter the title in the issue title field.
2. Copy the concise version as the issue body and replace `{…}`.
3. For multiple key workflows, add observable acceptance results for each.
4. After filling in the template, remove empty fields and instructions that no longer serve a purpose.

Prefer the target project's existing issue template.
Retain impact and related work only when they contain specific information; do not routinely enter "None".
List requirements that have not been adopted as open questions and explain which outcomes they affect.
For independently deliverable parts, use the [Work decomposition guide](../../references/issue-types.md#choosing-an-issue-parent-or-project) to decide whether to create sub-issues.

## Concise version

Title: `Enable {user} to {complete a new task}`

```markdown
## Need

{The limitation target users currently face.}

- User: {Specific role.}
- Scenario: {When this capability is needed.}
- Outcome: {What users can do after delivery.}

## Approach

{The planned interaction and user-visible behavior.}

## Scope

- {Boundary of the capability being delivered.}

## Acceptance

- [ ] {Observable result of the primary workflow.}
- [ ] {Handling result for a specified failure scenario.}

## Verification method

{Data and actions used to assess the acceptance results above. Do not repeat steps already included in checkboxes.}

## Impact

- {Existing behavior, compatibility, or migration needs affected. Include only specific impacts.}

## Basis

- {Source and location of the adopted requirement.}
```

## Completed example

This fictional product example shows a completed requirement and acceptance criteria.

Title: `Enable project managers to export currently filtered tasks as CSV`

```markdown
## Need

Project managers need to share a weekly task list with external partners and currently must copy tasks individually.

- User: Project managers with project read access.
- Scenario: Preparing weekly meeting material after filtering the task list.
- Outcome: A CSV file containing the current filter results.

## Scope

- Export all tasks matching the current filters.
- Use the current list sort order.
- Use UTF-8 encoding.
- Output fields
  - Task ID.
  - Title.
  - Status.
- Disable the export button when the filter returns no results.
- Offer a retry action when export fails.

## Acceptance

- [ ] The CSV contains only the 3 pending tasks matching the filter.
  1. Create 3 pending tasks and 2 completed tasks.
  2. Filter for pending tasks and sort by ID ascending.
  3. Run the export.
  4. Read the file with a CSV parser and confirm that it contains exactly those 3 pending tasks.
- [ ] The task order in the CSV matches the list's ascending ID order.
- [ ] Every record contains the 3 specified fields.
- [ ] Chinese titles match their original values after UTF-8 decoding.
- [ ] Commas within titles remain in the same field after CSV parsing.
- [ ] The export button is disabled when no tasks match.
- [ ] Export can succeed on retry after a failure.
  1. Make the export request return 500.
  2. Confirm that "Export failed. Please retry." appears.
  3. Restore the service and select retry.
  4. Confirm that the resulting file matches the original filters.

## Basis

- Requirement record: "Weekly meeting task list", approved version dated 2026-09-10.
```

## Configuration notes

### Feature facts

Verified on: 2026-09-13.

- A Standard template can prefill issue properties and the description.
  - Source: [Linear Issue templates — Create standard issue templates](https://linear.app/docs/issue-templates#create-standard-issue-templates).
- A Workspace template cannot preset team-specific labels.
  - Source: [Same section](https://linear.app/docs/issue-templates#create-standard-issue-templates).
- A Workspace template cannot preset team-specific issue statuses.
  - Source: [Same section](https://linear.app/docs/issue-templates#create-standard-issue-templates).

### Recommendations

- Use this file's concise version as the starting point for the body.
- Choose labels according to the actual work.
- Check the scope of default properties when configuring a template.
- Add links to outputs to the body after delivery.
- Keep links to actual verification results in the body.


## Writing defaults

Follow [writing](../../references/writing.md) for formatting, evidence, and the issue's current conclusions.
