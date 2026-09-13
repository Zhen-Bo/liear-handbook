# Decompose work into outcomes deliverable in one session

For individual developers collaborating with multiple Agents.
This guide's decomposition workflow is a recommendation.
Session size depends on the work and verification scope the recipient can complete.

- Type selection: [Work type guide](issue-types.md#choosing-an-issue-parent-or-project).
- Requirement starting point: [Feature template](../assets/templates/feature.md).
- Scheduling basis: [Milestones and dependency scheduling](planning-and-dependencies.md#3-identify-real-blockers).
- Complete example: [Task CSV export decomposition](feature-decomposition.md).

## Decomposition workflow

### 1. Fix the overall outcome

1. Describe what users can do after completion.
2. List the adopted scope.
3. Write observable acceptance results for the primary workflow.
4. Write expected results for failure scenarios that affect delivery.
5. Assess whether one issue can contain implementation and verification.
6. When multiple handoff outputs are needed, retain overall acceptance in a parent.

### 2. Identify outputs that can be handed off

1. Work backward from parent acceptance to the outputs needed.
2. For each candidate child, describe the deliverable and who can use it after completion.
3. Keep small implementation and verification tasks needed for the same output together.
4. When different parts need a shared specification, first check whether an existing specification is sufficient.
5. When an unknown approach must be resolved before implementation, split out research that supports the decision.
6. When specifications are insufficient and needed by several children, split out a contract deliverable with examples and usability conditions.
7. Retain integration work that connects the parts into the user workflow promised by the parent.

Avoid splitting the same small deliverable into "write code" and "add tests".
Create a separate testing issue only when an independent testing capability has its own users and completion criteria.

### 3. Make the next session ready to start

Keep the following information in each child's body.

- Inputs
  - Location of adopted requirements.
  - Version or fixed entry point of required prerequisite outputs.
  - Environment and permissions needed to take over.
- Outputs
  - Capability or document with assessable acceptance criteria.
  - Planned delivery location.
- Scope
  - Behavioral boundary owned by this item.
  - Handoff boundary with adjacent children.
- Acceptance
  - Observable successful result.
  - Applicable failure scenarios.
  - Numbered steps when actions are required.

Add non-goals only when something could easily be mistaken for a commitment.
For example, synchronous export and background export imply different architectures, so explicitly specify which approach is adopted.

### 4. Assess session size

| Signal | Assessment | Adjustment |
| --- | --- | --- |
| One item contains several independently acceptable capabilities | Too large | Split by user outcome or handoff component |
| The key approach is undecided, preventing implementation acceptance criteria | Too large or not yet executable | First deliver research supporting the decision |
| Taking over requires rebuilding substantial scattered context | Too much context | Consolidate adopted conclusions and required sources, then check scope |
| Implementation is expected to fill the session, leaving no time for required verification | Too large | Reduce to a deliverable that can still be fully accepted |
| A child only changes one line and must be combined with others for an assessable outcome | Too small | Merge it back into the issue for the same outcome |
| A child only creates an empty file or adds fields individually | Usually too small | Accept a complete, usable data contract |
| A small change independently fixes a complete behavior | Can remain one item | Judge by the outcome; do not merge based on line count |

The criteria do not assume a fixed number of minutes or tokens.
Before starting, estimate both context-reading and implementation time.
Also reserve capacity for required verification and output handoff.

### 5. Map real dependencies

1. For each child, ask: "Which missing output would prevent it from passing acceptance?"
2. Make the issue supplying that output a prerequisite.
3. State when the input counts as usable.
4. Check each prerequisite's output and current status.
5. If a cycle appears, check whether to extract a shared contract.
6. Confirm that at least one item has the inputs needed to start.

- Can run in parallel
  - Two items use the same confirmed contract.
  - Each can pass acceptance without the other's output.
  - Execution and review capacity are sufficient.
- Writes requiring coordination
  - Assign modification scope before multiple items edit the same file.
  - A conflict over shared files does not itself imply an output dependency.
- Prerequisite status
  - Done: Still verify that the required input is usable.
  - Canceled: Verify a replacement output or adopted requirement change.

Follow [WIP criteria](planning-and-dependencies.md#4-select-executable-work-and-control-wip) for capacity.
A parent's aggregation role does not count as another execution item.

## Handling work that exceeds a session

When new findings mean the remaining work cannot be fully accepted in the current session, proceed in order.

1. Save files or the working tree in a state the recipient can use.
2. Record the exact output location.
3. Record an identifiable version or file hash.
4. Retain actual verification results and evidence links.
5. Organize remaining work into follow-up issues with independent outputs and acceptance criteria.
6. Add required inputs to the follow-up issues.
7. Update real dependencies so integration waits for outputs still missing.
8. Update the original issue body with the effective scope and reasons for adoption.
9. Retain the original overall commitment in the parent or record a confirmed scope change.
10. Write the first action the recipient can start directly.

When an independent deliverable can reasonably be separated, assess the original issue against its revised acceptance criteria.
If the original output is still unusable, retain its unfinished status and hand off the same issue.
Do not claim delivery of the original commitment merely by moving failing acceptance criteria elsewhere.

### Required handoff record content

- Saved outputs
  - File or working-tree entry point.
  - Version identification.
- Verification results
  - Checks actually performed.
  - Corresponding result entry points.
- Findings affecting takeover
  - Specific gaps.
  - Their impact on delivery.
- Next steps
  - Follow-up issue.
  - First action.
  - Conditions needed to resume.

Remove fields that have no content.

## Parent integration acceptance

1. Confirm the effective output entry point for every child.
2. Verify the actual integrated version.
3. Compare each original parent acceptance criterion with child coverage.
4. Run the primary workflow across children.
5. Run the agreed overall failure scenarios.
6. Assign fixes for gaps and retain unfinished acceptance criteria.
7. When the output meets the criteria, add integration evidence and close according to work policy.

- [ ] Child outputs are connected into the capability promised by the parent.
- [ ] All parent acceptance criteria have locatable evidence.
- [ ] Delivery-scope gaps are resolved or covered by a confirmed scope decision.
- [ ] The usable entry point is directly reachable from the parent.

## Linear feature facts

Verified on: 2026-09-13.
Evidence method: Reviewed official Linear documentation.

- Sub-issues break a larger parent into smaller work items.
  - Source: [Parent and sub-issues — Overview](https://linear.app/docs/parent-and-sub-issues#overview).
- Create children from the parent's `+ Add sub-issues`.
  - Source: [Create a sub-issue](https://linear.app/docs/parent-and-sub-issues#create-a-sub-issue).
- `Blocked by` indicates that this item is waiting for another issue.
  - Source: [Issue relations — Blocked / blocking](https://linear.app/docs/issue-relations#blocked-blocking).
- Parent and sub-issue automatic closure is an optional team setting.
  - Source: [Parent and sub-issues — Status automation](https://linear.app/docs/parent-and-sub-issues#status-automation).
  - All children being Done can trigger parent auto-close.
  - A parent being Done can trigger sub-issue auto-close.

Before adopting status automation, confirm that it fits the parent integration acceptance arrangement.
This check is a handbook recommendation.


## User policy

Work granularity follows [Work granularity and authorization in policy](policy.md#work-granularity-and-authorization).
Follow [writing](writing.md) for wording and current conclusion maintenance.
