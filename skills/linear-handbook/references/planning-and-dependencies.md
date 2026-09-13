# Milestones and dependency scheduling

Context: An individual developer working with multiple Agents.
Verified on: 2026-09-13.

- Planning input: [Build a Project from requirements](project-planning.md).
- Outcome fields: [Project brief](../assets/templates/project-brief.md).

## Feature selection

| Question to answer | Choice | Scope |
| --- | --- | --- |
| Which outcome stage has this Project reached? | Milestone | Stages and their issues within a Project. [Project milestones](https://linear.app/docs/project-milestones) |
| What work has the Team scheduled for this period? | Cycle | Work scheduled in a fixed time interval. [Cycles](https://linear.app/docs/use-cycles) |
| Which issue must supply its output first? | Issue dependency | `Blocks` and `Blocked by` express direction. [Issue relations](https://linear.app/docs/issue-relations) |
| Which Project must end before another can start? | Project dependency | Project-level end → start relationships. [Project dependencies](https://linear.app/docs/project-dependencies) |
| How much work can be undertaken simultaneously? | WIP management | Workload policy recommended in this guide; see below. |

### Feature facts

- Milestone
  - Create milestones and add descriptions in Project overview. [Project milestones](https://linear.app/docs/project-milestones)
  - Target dates are optional. [Project milestones](https://linear.app/docs/project-milestones)
  - One milestone cannot be shared across Projects. [Project milestones](https://linear.app/docs/project-milestones)
  - Progress percentages reflect the statuses of member issues. [Project milestones](https://linear.app/docs/project-milestones)
  - Multiple milestones can proceed in parallel; the yellow focus can be disregarded. [Project milestones](https://linear.app/docs/project-milestones)
- Cycle
  - Enable Cycles in Team Settings. [Cycles](https://linear.app/docs/use-cycles)
  - Cycles use a recurring schedule. [Cycles](https://linear.app/docs/use-cycles)
  - They are not tied to releases. [Cycles](https://linear.app/docs/use-cycles)
  - Assigned unfinished issues normally move automatically into the next cycle. [Cycles](https://linear.app/docs/use-cycles)
  - Issues moved to backlog during cooldown do not move into the next cycle. [Cycles](https://linear.app/docs/use-cycles)
  - Issues moved to triage during cooldown do not move into the next cycle. [Cycles](https://linear.app/docs/use-cycles)
  - Issues canceled or completed during cooldown do not move into the next cycle. [Cycles](https://linear.app/docs/use-cycles)
- Issue dependency
  - Add relationships from the issue menu. [Issue relations](https://linear.app/docs/issue-relations)
  - Official UI documentation says the relationship moves to Related when the blocker is resolved. [Issue relations](https://linear.app/docs/issue-relations)
- Project dependency
  - Create from Dependencies in the Project menu. [Project dependencies](https://linear.app/docs/project-dependencies)
  - Timeline can display blocking relationships. [Project dependencies](https://linear.app/docs/project-dependencies)

## Schedule work from outcomes

The workflow below is a handbook recommendation.

### 1. Define milestone outcomes

- Inputs
  - Brief success criteria.
  - Confirmed scope.
- Actions
  1. Name milestones as stages that can be accepted.
  2. State the completion result for each stage.
  3. List the verification method.
  4. Keep overall acceptance criteria in the milestone description.
  5. Set target dates according to the scheduling basis.
- Completion criteria
  - [ ] Each milestone outcome is assessable.
  - [ ] Dates serve as delivery targets only when supported by a basis.

### 2. Split out issues that can be handed off

- Inputs
  - Milestone outcomes and acceptance criteria.
- Actions
  1. Split issues by independently acceptable deliverables.
  2. List input entry points.
  3. Assign responsible roles.
  4. State output locations.
  5. Write acceptance steps.
  6. Place each issue in the corresponding milestone.
- Completion criteria
  - [ ] The next session can find necessary context.
  - [ ] Each issue has an assessable completion result.

### 3. Identify real blockers

Check each prerequisite individually:

1. Which specific missing input would prevent this item from delivering?
2. Which work item supplies that input?
3. When is the input usable, and which conditions must it meet?
4. Can an independent part be split out and done first?

- Create `Blocked by` when usable input must be awaited.
- Use `Related` for background relationships only.
- Sharing a milestone is insufficient to establish a dependency.
- Lower priority is insufficient to establish a dependency.
- When multiple Agents edit the same file, coordinate execution scope first.
  - Handle write conflicts through work assignment.
  - If later work needs the earlier work's new interface, record an output dependency.
- When a prerequisite is only partly complete, split out an acceptable shared contract.
  - Link work depending on that contract to the contract issue.
  - Integration acceptance still depends on complete implementation.
- If dependencies form a cycle, first check whether a blocker was set incorrectly.
  - If both sides need the same specification, extract a shared contract as the prerequisite.
  - Recheck relationships and confirm that at least one work item can start.

When taking over through tools, read each prerequisite's current status and inspect its outputs.
A nonempty relationship list still requires checking current status and outputs to determine whether the necessary input is usable.
If a prerequisite is canceled, confirm that another output replaces its input or that the requirement was removed.

### 4. Select executable work and control WIP

In this guide, WIP means execution work that has started and is not yet complete.
Deliverables under review still consume capacity.
Label work waiting for a blocker with its waiting reason and continue counting it as started work, so opening more items cannot hide congestion.

1. Read the latest issue content.
2. Check necessary prerequisites' statuses and outputs.
3. Confirm that the executor has the necessary access and authorization.
4. Confirm there is no duplicate claimant.
5. Confirm remaining execution capacity.
6. Confirm downstream review capacity.
7. From executable work, choose the item that most effectively unblocks later work.
8. If unblocking benefits are similar, choose by delivery deadline and priority.

- Adopters set the WIP limit.
  - Start with one item per executor and adjust according to actual throughput.
  - When multiple Agents share one reviewer, jointly control the review queue.
  - More Agents do not imply more review capacity.
- At the limit, prioritize completing or unblocking existing work.
- When urgent work must be inserted, record the resumption conditions for deferred items.
- Count actual execution issues for capacity; do not count an aggregating parent again.

### 5. Add work to a Cycle and replan

This section applies to Teams already using Cycles.
Otherwise, schedule work using the outcome and capacity criteria above.

- Inputs
  - Executable work list.
  - Confirmed WIP limit.
  - Team Cycle settings.
- Actions
  1. Select work for the current period according to available capacity.
  2. Clearly state start conditions for candidate work still needing prerequisites.
  3. Recheck prerequisite outputs when completed, then take on candidate work.
  4. Update affected issues when delays appear.
  5. If milestone delivery is affected, update its target and reason.
  6. At Cycle end, inspect each unfinished item moved into the next period.
  7. Reassess whether those items should continue consuming capacity.
- Completion criteria
  - [ ] Current-period work has enough inputs to start.
  - [ ] Candidate work is distinguishable from work already taken on.
  - [ ] Capacity is rechecked after rollover.

## Example across milestones: Time-log CSV export

This hypothetical schedule illustrates the selection method through a tabletop walkthrough.
Work IDs are example labels.
WIP limits and timing are illustrative settings.

- Project outcome: Users obtain a time-log CSV for a specified date range.
- "CSV data capability available".
  - [ ] Known time-log data matches API-generated CSV record by record.
- "Users can complete the download".
  - [ ] Users obtain the specified date-range CSV through the interface.
    1. Prepare known data spanning several date ranges.
    2. Select one date range in the interface.
    3. Download and check file contents.
- Roles
  - Agent A: API and integration verification.
  - Agent B: Interface.
  - Maintainer: Delivery review.
- Example capacity
  - One execution item per Agent at a time.
  - At most one deliverable in the review queue.

| ID | Milestone | Acceptable deliverable | Required prerequisite | Responsible role |
| --- | --- | --- | --- | --- |
| A | "CSV data capability available" | CSV API contract with field definitions and response examples | Brief | Agent A |
| B | "CSV data capability available" | API output passes comparison with known data | A's usable contract | Agent A |
| C | "Users can complete the download" | Interface sends dates and handles mock responses according to the contract | A's usable contract | Agent B |
| D | "Users can complete the download" | Interface uses the actual API and passes "Users can complete the download" acceptance | Outputs of B and C | Agent A |

### Cycle 1

1. Agent A completes A and the maintainer confirms the contract is usable.
2. B and C start simultaneously.
3. B and C each use the confirmed contract.
4. When review capacity is full, complete existing review or rework first.
5. Keep the other deliverable awaiting review and count it in WIP.
6. Submit it for review after capacity is released.

- Real blockers
  - Before A is usable, B lacks the output specification.
  - Before A is usable, C lacks the API contract to follow.
  - Before B completes, D lacks a usable API.
  - Before C completes, D lacks an interface ready for integration.
- Parallel work
  - After A completes, B and C have no output dependency on one another.
  - C belongs to "Users can complete the download" and can still proceed before "CSV data capability available" is complete.
  - C's acceptance using mock responses covers only interface behavior.
  - D still performs acceptance for the complete download outcome.

### Hypothetical state at Cycle 1 end

- B is complete and passes data comparison.
- C still lacks error-response handling.
- D has not started.

Assessment from this state:

1. The "CSV data capability available" outcome is achieved.
2. The "Users can complete the download" outcome is not yet achieved.
3. C moves into the next cycle under normal rollover behavior. [Cycles](https://linear.app/docs/use-cycles)
4. D still awaits C and retains its start conditions.
5. The maintainer reconfirms C's remaining scope.
6. Complete C first in Cycle 2, then take on D.
7. If the target date for "Users can complete the download" is affected, update delivery expectations.

### Cycle end and outcome completion

| Assessment target | Basis | Follow-up action |
| --- | --- | --- |
| Cycle ends | The time interval ends. [Cycles](https://linear.app/docs/use-cycles) | Check work capacity after rollover. |
| Issue completes | This item's acceptance results and output evidence. | Add outputs and update status. |
| Milestone outcome completes | Stage acceptance criteria are met. | Verify the overall result and record output links. |
| Project completes | Brief success criteria are met. | Close through the adopter's acceptance workflow. |

Outcome assessments and follow-up actions in this table are handbook recommendations.
Milestone percentages help track status, but still check whether stage acceptance covers actual outcomes.

## Adopter configuration

Adopters confirm the following choices and record them as their own work policy.

- WIP limit.
- Review capacity.
- How urgent work is inserted.
- Resumption conditions for waiting work.
- Cycle cadence.
- Outcome acceptance responsibility.

## Source record

All publishers are Linear.
Verified on: 2026-09-13.
Evidence status: Confirmed in documentation.

- [Project milestones](https://linear.app/docs/project-milestones)
  - `Create milestones`: Creation and optional dates.
  - `Milestones progress`: Progress displayed from issue statuses.
  - `FAQ`: Parallel work across milestones.
  - `FAQ`: Milestones cannot be shared across Projects.
- [Cycles](https://linear.app/docs/use-cycles)
  - Page introduction: Team work time intervals.
  - `Configure`: Team settings entry point.
  - `Cycle duration`: Recurring schedule.
  - `Issues rollover`: Unfinished work rollover and exceptions.
- [Issue relations](https://linear.app/docs/issue-relations)
  - `Add relationships`: Relationship creation.
  - `Blocked / blocking`: Direction and UI display after resolution.
- [Project dependencies](https://linear.app/docs/project-dependencies)
  - `Overview`: End → start limitation.
  - `Create a project dependency`: Menu entry point.
  - `View project dependencies`: Timeline display.
