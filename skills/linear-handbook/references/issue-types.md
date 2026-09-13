# Guide to work types and parent issue selection

Context: An individual developer working with multiple Agents.
Verified on: 2026-09-13.

- Object relationship basis: [object-model.md](object-model.md).
- Policy for this edition: [Writing rules](writing.md).

## Choose the outcome before the type

The classifications and completion criteria below are handbook recommendations.
Replace example thresholds with verifiable values or results for actual work.

1. State the result to deliver when this item ends.
2. Select one work type based on the primary completion criterion.
3. Use additional labels for dimensions that need to be searchable.
4. When different outputs require separate acceptance, split them into issues and state their dependencies.
5. Finally, decide whether a parent or project is needed.

| Primary outcome | Suggested type |
| --- | --- |
| Restore promised behavior | Bug |
| Provide a capability that did not exist | Feature |
| Improve the usability of an existing capability | Improvement |
| Change internal structure while preserving external behavior | Refactoring |
| Remove a known ongoing maintenance burden | Technical debt |
| Answer an unresolved question with evidence | Research |
| Meet a measurable resource or speed target | Performance |
| Reduce a specific security risk | Security |
| Move users or data to a new foundation | Migration |
| Enable readers to understand or perform a specified operation | Documentation |
| Add a lasting ability to detect errors | Testing |
| Restore a service currently affected | Incident |
| Deliver a specified version to target users | Release |

### Resolving overlap

- Bug and improvement
  - Choose Bug when a specification or accepted behavior establishes a deviation.
  - Choose improvement when the existing behavior meets the commitment but should be easier to use.
- Refactoring and technical debt
  - Choose refactoring when the deliverable centers on internal structural changes.
  - Choose technical debt when it centers on removing a known burden.
  - Refactoring may address technical debt; select the type by the issue's primary acceptance criterion.
- Research and implementation
  - Create a research issue first when feasibility must be decided before proceeding.
  - Diagnose the cause of a known Bug within the same issue.
  - Diagnosis itself does not require a separate research issue.
- Performance and Bug
  - A fix for violating an established latency commitment can use Bug.
  - Add a performance label and retain benchmark acceptance criteria.
- Security and incident
  - Choose incident when a service is currently affected and restoration is the primary goal.
  - Accept the permanent fix in a separate security issue linked to incident evidence.
- Documentation and testing
  - Small supporting work required for Feature completion can remain in the original issue.
  - Split out documentation or testing issues when they have independent deliverables and responsibility.
- Migration and release
  - Choose migration when the work handles a transition between old and new states.
  - Choose release when acceptance concerns the version rollout result.

## Evidence and completion criteria by work type

### Bug

- Purpose: Correct a deviation between actual and promised behavior.
- Required evidence
  - Specification or existing acceptance basis for expected behavior.
  - Locatable failing case and affected version.
  - Reproduction steps or observations demonstrating the problem.
- Completion criteria
  - [ ] The original failing case meets expected behavior.
  - [ ] Regression checks for affected paths pass.

### Feature

- Purpose: Deliver a new capability users could not previously use.
- Required evidence
  - Target users and their task.
  - Adopted requirements and scope.
  - Expected results of key workflows.
- Completion criteria
  - [ ] Target users can complete the specified workflow.
  - [ ] Listed failure scenarios are handled as required.

### Improvement

- Purpose: Improve usability of an existing capability.
- Required evidence
  - Specific examples of current friction.
  - Desired improvement in user outcomes.
  - A comparable current baseline.
- Completion criteria
  - [ ] The specified scenario meets the predefined improvement standard.
  - [ ] Existing core tasks can still be completed.

### Refactoring

- Purpose: Improve internal structure while preserving external behavior.
- Required evidence
  - Code locations for specific structural problems.
  - External behavior contracts to preserve.
  - An inspectable description of the target structure.
- Completion criteria
  - [ ] The target structure is implemented within the specified scope.
  - [ ] Relevant external behavior contract checks pass.

### Technical debt

- Purpose: Remove a known burden that continually adds cost or risk.
- Required evidence
  - Specific component or workflow containing the burden.
  - Observed maintenance cost or risk.
  - An assessable target state with the burden removed.
- Completion criteria
  - [ ] The target scope no longer depends on the listed burden.
  - [ ] Verification of original usage scenarios passes.

### Research

- Purpose: Provide sufficient evidence for the next decision.
- Required evidence
  - Specific question to answer.
  - Criteria for comparing approaches.
  - Locatable primary sources or experimental data.
- Completion criteria
  - [ ] The research answer has enough evidence to make the agreed decision.
  - [ ] If infeasibility is adopted, sufficient evidence rules out the approach.
  - [ ] The recommended conclusion explains the reasons for adoption.
  - [ ] Required information gaps preventing the decision are filled.

### Performance

- Purpose: Meet a specified performance or resource usage target.
- Required evidence
  - Metric definitions and target thresholds.
  - Measurement environment and workload.
  - Reproducible baseline results.
- Completion criteria
  - [ ] Target thresholds are met under comparable conditions.
  - [ ] Results record measurement methods and samples.
  - [ ] Specified correctness checks pass.

### Security

- Purpose: Eliminate or reduce a specific security risk.
- Required evidence
  - Affected assets and applicable versions.
  - Conditions under which the risk exists.
  - Vulnerability evidence or threat scenarios verifiable in an authorized environment.
- Completion criteria
  - [ ] The specified risk scenario is blocked or the explicit mitigation target is met.
  - [ ] Legitimate usage workflows can still be completed.
  - [ ] Any residual risk has a disposition record from a named decision-maker.

Link sensitive evidence to a location with appropriate access permissions.
Keep the risk summary needed to understand the work in the issue.

### Migration

- Purpose: Switch data or usage workflows to a new system state.
- Required evidence
  - Mapping rules between old and target states.
  - Affected scope and cutover sequence.
  - Data consistency check method.
  - Conditions for rollback or forward repair.
- Completion criteria
  - [ ] The specified scope operates in the target state.
  - [ ] Reconciliation or consistency checks pass.
  - [ ] The recovery plan has the agreed verification evidence.
  - [ ] The old system has been handled according to this item's retirement conditions.

### Documentation

- Purpose: Enable specified readers to understand content or perform operations.
- Required evidence
  - Problem the reader needs to solve.
  - Applicable version or verification date.
  - Sources supporting operations and feature conclusions.
- Completion criteria
  - [ ] The document answers the specified question.
  - [ ] Operational content is checked using the agreed method.
  - [ ] Readers can locate outputs and references.

### Testing

- Purpose: Establish verification that continually detects specified errors.
- Required evidence
  - Behavior to protect or a previously missed case.
  - Coverage gap in current checks.
  - Planned execution location and timing.
- Completion criteria
  - [ ] Tests detect the specified error.
  - [ ] Correct behavior passes the tests.
  - [ ] Tests run reproducibly from the specified entry point.

### Incident

- Purpose: Restore a service currently affected.
- Required evidence
  - Start time and scope of impact.
  - Observations of current service state.
  - Timeline of actions taken.
- Completion criteria
  - [ ] The service meets prespecified recovery indicators.
  - [ ] The agreed observation period passes.
  - [ ] Remaining permanent improvements have traceable work entry points.

Service restoration and permanent fixes may have different completion times.
If a postmortem requires independent delivery, create related work and link it to the timeline.

### Release

- Purpose: Deliver a specified version to target users.
- Required evidence
  - Identifiable version or build artifact.
  - Target environment and rollout scope.
  - Release entry criteria.
  - Criteria for rollback or stopping rollout.
- Completion criteria
  - [ ] The target environment runs the specified version.
  - [ ] Post-release health checks pass.
  - [ ] Agreed delivery notifications or release information are provided.

## Native fields, labels, and templates

The following feature facts are confirmed by official Linear documentation.

| Mechanism | Purpose | Documentation |
| --- | --- | --- |
| Native issue fields | Record platform-defined work properties | [Create issues — Apply pre-set properties](https://linear.app/docs/creating-issues#apply-pre-set-properties) |
| Label | Organize issues by custom classification | [Issue labels — Labels](https://linear.app/docs/labels#labels) |
| Label group | Select at most one label in the same group | [Issue labels — Label groups](https://linear.app/docs/labels#label-groups) |
| Standard template | Prefill issue properties and body | [Issue templates — Create standard issue templates](https://linear.app/docs/issue-templates#create-standard-issue-templates) |
| Form template | Collect structured information when creating an issue | [Issue templates — Create form templates](https://linear.app/docs/issue-templates#create-form-templates) |

- Native properties each have their own purpose.
  - Status expresses workflow stage. [Create issues — Overview](https://linear.app/docs/creating-issues#overview)
  - Priority expresses urgency. [Priority — Overview](https://linear.app/docs/priority#overview)
  - A parent relationship expresses work decomposition. [Parent and sub-issues — Overview](https://linear.app/docs/parent-and-sub-issues#overview)
- Labels can be created for a workspace or a specific team. [Issue labels — Labels](https://linear.app/docs/labels#labels)
- Official documentation uses `Type/Bug` to demonstrate creating a label group and label. [Issue labels — Create a label during add label workflow](https://linear.app/docs/labels#create-a-label-during-add-label-workflow)
- Official Jira documentation lists Issue Type as a feature Linear does not adopt. [Jira — Limitations](https://linear.app/docs/jira#limitations)
- A Workspace template cannot preset team-specific issue statuses. [Issue templates — Create standard issue templates](https://linear.app/docs/issue-templates#create-standard-issue-templates)
- A Workspace template cannot preset team-specific labels. [Same section](https://linear.app/docs/issue-templates#create-standard-issue-templates)
- A Form template can make fields required. [Issue templates — Create form templates](https://linear.app/docs/issue-templates#create-form-templates)
- Issues can be filtered by the template used at creation. [Issue templates — Template based Insights](https://linear.app/docs/issue-templates#template-based-insights)

### Recommended configuration

1. Start with existing labels and templates and check whether they express the primary outcome.
2. Use a single-select `Type` label group when consistent filtering by work type is needed.
3. Create only the type labels actually needed.
4. Express secondary dimensions with an ungrouped label or a label group for a different dimension.
5. Choose templates by the evidence to collect and verify their default properties.

- This guide's thirteen types are recommended work classifications.
  - `Type/Bug` in the official example above is a label configuration.
  - Do not describe these thirteen types as a mandatory list of native issue types supplied by Linear.
- Type only determines how to describe the outcome.
  - Set Priority for security work according to actual impact.
  - A parent can also be labeled Feature or another primary work type.
  - Revise acceptance content when changing the type.

## Choosing an issue, parent, or project

The decisions below are handbook recommendations, extending [Feature selection in object-model.md](object-model.md#feature-selection-table).

| Scenario | Choice | Basis |
| --- | --- | --- |
| One output can be independently delivered and accepted | Issue | One body can define the work |
| One outcome needs parts that can each be handed off | Parent + sub-issues | Parent verifies the overall outcome |
| A shared outcome needs independent project progress management | Project | Dedicated context and progress entry points are needed |
| A local outcome within a Project needs decomposition | Parent within a Project | Local integration has independent completion criteria |
| Different outputs only have sequencing dependencies | Issues + blocked by | A dependency alone does not imply a parent-child relationship |

1. State overall completion criteria.
2. Keep a single issue when it can deliver the outcome.
3. Use a parent to aggregate parts that can be independently handed off.
4. Use a project when ongoing project-level coordination is needed.
5. Give every child its own output and acceptance criteria, and retain integration conditions in the parent.

### Feature basis and operational considerations

- Official documentation recommends sub-issues for work between a single issue and a project in size. [Parent and sub-issues — Overview](https://linear.app/docs/parent-and-sub-issues#overview)
- A Project organizes issues around a shared outcome. [Projects — Overview](https://linear.app/docs/projects#overview)
- A Project provides a dedicated progress graph. [Same section](https://linear.app/docs/projects#overview)
- An issue can belong to only one project at a time. [Projects — Add issues to a project](https://linear.app/docs/projects#add-issues-to-a-project)
- Use blocked by when waiting for another output. [Issue relations — Blocked / blocking](https://linear.app/docs/issue-relations#blocked-blocking)
- Sub-issues do not inherit parent labels at creation. [Parent and sub-issues — Copy properties](https://linear.app/docs/parent-and-sub-issues#copy-properties)
- Parent and sub-issue automatic status closure is an optional team setting. [Parent and sub-issues — Status automation](https://linear.app/docs/parent-and-sub-issues#status-automation)
  - Parent auto-close can close the parent after all children are Done.
  - Sub-issue auto-close can close remaining children after the parent is Done.
- Converting a parent into a project changes the original structure. [Parent and sub-issues — Turn issues into projects](https://linear.app/docs/parent-and-sub-issues#turn-issues-into-projects)
  - The original parent and children become independent issues in the project.
  - The original parent is renamed.
  - Parent-child relationships are removed.

### Operational recommendations

- Confirm each child's type based on its own outcome.
- Before using status automation to drive closure, confirm that the setting fits the integration acceptance method.
- Save overall acceptance criteria before converting a parent into a project.
- After conversion, place overall acceptance criteria back in the appropriate output entry point.

### Selection examples

| Scenario | Type | Structure | Assessable result |
| --- | --- | --- | --- |
| Show an error message for an expired token | Bug | Single issue | Original failing case shows the required message |
| Deliver API and frontend separately to complete subscriptions | Feature | Parent + sub-issues | Parent verifies the end-to-end subscription workflow |
| Move customers to a new login system in phases | Migration | Project | Each phase passes cutover and consistency checks |
| Restore an interrupted service | Incident | Independent issue | Service meets recovery indicators |
| Permanently fix a vulnerability exposed by an incident | Security | Issue linked to the incident | Specified vulnerability scenario is blocked |

## Source record

All sources below are published by Linear.
Verified on: 2026-09-13.
Evidence method: Reviewed official documentation and checked sections.

| Document | Section | Supported conclusion |
| --- | --- | --- |
| [Create issues](https://linear.app/docs/creating-issues) | Overview | Issue as the basic work unit and required properties |
| [Create issues](https://linear.app/docs/creating-issues#apply-pre-set-properties) | Apply pre-set properties | Properties the platform can preset |
| [Issue labels](https://linear.app/docs/labels#labels) | Labels | Classification and scope |
| [Issue labels](https://linear.app/docs/labels#label-groups) | Label groups | Single selection within a group |
| [Issue labels](https://linear.app/docs/labels#create-a-label-during-add-label-workflow) | Create a label during add label workflow | Type/Bug example |
| [Issue templates](https://linear.app/docs/issue-templates#create-standard-issue-templates) | Create standard issue templates | Prefill and team property limits |
| [Issue templates](https://linear.app/docs/issue-templates#create-form-templates) | Create form templates | Required form fields |
| [Issue templates](https://linear.app/docs/issue-templates#template-based-insights) | Template based Insights | Filtering by template |
| [Priority](https://linear.app/docs/priority#overview) | Overview | Urgency |
| [Jira](https://linear.app/docs/jira#limitations) | Limitations | Product difference for Issue Type |
| [Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues#overview) | Overview | Decomposition purpose |
| [Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues#copy-properties) | Copy properties | Labels are not inherited |
| [Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues#status-automation) | Status automation | Optional automatic closure |
| [Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues#turn-issues-into-projects) | Turn issues into projects | Conversion result |
| [Projects](https://linear.app/docs/projects#overview) | Overview | Project purpose |
| [Projects](https://linear.app/docs/projects#add-issues-to-a-project) | Add issues to a project | One project per issue |
| [Issue relations](https://linear.app/docs/issue-relations#blocked-blocking) | Blocked / blocking | Work dependencies |

## User policy

Work granularity follows [Work granularity and authorization in policy](policy.md#work-granularity-and-authorization).
Follow [writing](writing.md) for wording and current conclusion maintenance.
