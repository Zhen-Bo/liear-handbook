# Research issue body template

For work that needs evidence to decide the next step.
Classification: [Work type guide](../../references/issue-types.md#research).

## Instructions

- Required fields
  - Question and decision.
  - Scope.
  - Time limit.
  - Decision criteria.
  - Evidence plan.
  - Acceptance criteria.
  - Add the adopted conclusion and locatable evidence before completion.
- Optional fields
  - Risks affecting the decision.
  - Related work with a specific purpose.

### Recommendations

1. Copy the body below and replace every placeholder.
2. Define scope by the decision that must be made.
3. Remove inapplicable optional fields.
4. Add actual findings to "Conclusions and evidence".

- The time limit is a point for reassessing scope.
  - If required evidence is still missing, obtain it or agree on a revised question that can be answered independently.
  - Listing information gaps alone does not complete the research.
- Infeasibility can be a completion conclusion.
  - Evidence must be sufficient to rule out the approach.
  - The conclusion must answer the agreed decision.
- Source records retain the verification date and section location.
  - Prefer official sources for feature facts.
  - Retain environment and data entry points for experimental results.
  - Explain how evidence leads to the conclusion when making an inference.

- Research outputs must support the agreed decision.
- Adjust the decision-maker and evidence thresholds to the adopting team.
- "Required fields" in this document are writing recommendations.
  - To enforce them at creation, configure them as required fields in a form template.

## Copyable body

```markdown
## Question and decision

`<Question to answer and the next step determined by the answer>`

## Scope

- Research subject: `<Version or scenario>`.
- Scope limit: `<Boundary of this work>`.
- Time limit: `<Deadline or effort in hours>`.

## Decision criteria

1. `<Condition and threshold the approach must meet>`.
2. `<Another condition for comparing approaches>`.

## Evidence plan

- `<Source or experiment>`: Answers `<Decision criterion>`.

## Conclusions and evidence

- Decision: `<Adopted approach or infeasibility conclusion>`.
- Reason: `<How evidence meets the criteria or rules out the approach>`.
- Evidence: `<Source section or experimental record link>`.
- Verified on: `<YYYY-MM-DD>`.
- Follow-up action: `<Specific action based on the conclusion>`.

## Acceptance criteria

- [ ] There is sufficient evidence to decide the agreed question.
- [ ] The adopted conclusion addresses each decision criterion.
- [ ] If the conclusion is infeasibility, verifiable evidence supports the reasons for exclusion.
- [ ] Required information gaps preventing the decision have been filled.
```

## Completed example: Choose the scope of a shared template

The following completed research body uses official documentation.
The requirements and time limit are example assumptions.

```markdown
## Question and decision

Should a text template shared by multiple teams be created as a workspace template or a team template?
This issue determines the shared template's scope.

## Scope

- Research subject: Linear standard issue templates.
- Scope limit: Shared text and defaults for team-specific properties.
- Time limit: One hour of official documentation review.

## Decision criteria

1. The template can be used by any team in the workspace.
2. The shared template does not need a default team-specific status.

## Evidence plan

- Read the Create standard issue templates section of Issue templates to verify scope.

## Conclusions and evidence

- Decision: Adopt a workspace template.
- Feature fact: A workspace template can be used by any team in the workspace.
- Feature limitation: A workspace template cannot preset a team-specific status.
- Inference: Shared text meets the first criterion.
- Inference: The inability to preset team-specific statuses does not affect this example's requirements.
- Evidence: [Issue templates — Create standard issue templates](https://linear.app/docs/issue-templates#create-standard-issue-templates).
- Verified on: 2026-09-13.
- Follow-up action: Configure the shared body as a workspace template.

## Acceptance criteria

- [x] Official documentation explicitly supports use across teams.
- [x] Confirmed that team-specific statuses cannot be preset.
- [x] The adopted conclusion meets both decision criteria.
```

If the requirement changes to "the same workspace template must preset a team-specific status", the official limitation above is sufficient evidence for an infeasibility conclusion.
The next decision can be to accept choosing the status at creation or create a team template for each team.

## Linear feature basis

Verified on: 2026-09-13.

- A Standard template can prefill the body. [Create standard issue templates](https://linear.app/docs/issue-templates#create-standard-issue-templates)
- A Form template can make fields required. [Create form templates](https://linear.app/docs/issue-templates#create-form-templates)

## Mapping other types

Use [Evidence and completion criteria by work type](../../references/issue-types.md#evidence-and-completion-criteria-by-work-type) to choose the closest base template, then replace its acceptance criteria.

| Work type | Base template | Acceptance focus to add |
| --- | --- | --- |
| Improvement | [Feature](feature.md) | Improvement threshold in a specified scenario |
| Technical debt | [Refactoring](refactor.md) | Target state with the known burden removed |
| Performance | [Feature](feature.md) | Measurement threshold under the same workload |
| Security | [Bug](bug.md) | Evidence that the risk scenario is blocked |
| Documentation | [Feature](feature.md) | Operation the specified reader can complete |
| Testing | [Feature](feature.md) | Tests detect the specified error |
| Incident | [Bug](bug.md) | Recovery indicators and observation period |
| Release | [Migration](migration.md) | Version and health checks in the target environment |

- Use the [Bug base template](bug.md) to restore promised behavior.
- Use the [Feature base template](feature.md) to deliver a new capability.
- Mapping a type does not mean retaining every field.
  - Remove fields that do not apply to the primary outcome.
  - Keep the actual response timeline for incidents.
  - Adapt data reconciliation fields for releases as applicable.

## Writing defaults

Follow [writing](../../references/writing.md) for formatting, evidence, and the issue's current conclusions.
