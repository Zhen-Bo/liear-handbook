# Build a Project from requirements

Context: An individual developer working with multiple Agents.
Verified on: 2026-09-13.

- Template: [Project brief](../assets/templates/project-brief.md).
- Modeling basis: [Object relationships and feature selection](object-model.md).
- Work classification: [Work types and parent issue selection](issue-types.md).

## Feature facts

- Create a Project with `+` on the Workspace or Team Projects page. [P1](https://linear.app/docs/projects#create-a-project)
- The name is the only required field at creation. [P1](https://linear.app/docs/projects#create-a-project)
- The Project lead field holds one member. [P1](https://linear.app/docs/projects#faq)
- Projects can span Teams. [P1](https://linear.app/docs/projects#multi-team-projects)
- An issue can belong to only one Project at a time. [P1](https://linear.app/docs/projects#add-issues-to-a-project)
- A Project does not need a completion date. [P1](https://linear.app/docs/projects#faq)
- The detailed description can be edited in Overview. [P2](https://linear.app/docs/project-overview#detailed-description)
- External links can be added to Resources. [P2](https://linear.app/docs/project-overview#external-links)
- Project documents can be created in Resources. [P2](https://linear.app/docs/project-overview#project-documents)
- Converting a parent to a Project changes the original structure. [P3](https://linear.app/docs/parent-and-sub-issues#turn-issues-into-projects)
  - The original parent is renamed.
  - The original parent and children become independent issues.
  - Original parent-child relationships are removed.

## Planning workflow

The following are handbook recommendations.
The platform requires less information to create a Project than is needed for a plan that can be handed off for execution.

### 1. Organize requirement inputs

- Inputs
  - The requester's original wording.
  - Evidence of the current usage scenario.
  - Existing output entry points.
- Actions
  1. State who encounters which problem in what scenario.
  2. Link to a locatable requirement basis.
  3. Separate proposals from adopted requirements.
  4. When introducing the process midstream, inventory existing work using the section below.
- Completion criteria
  - [ ] The next reader can understand the problem and its basis.
  - [ ] Assumptions remain marked as unconfirmed.

### 2. Define outcomes and boundaries

- Inputs
  - Problem statement.
  - Confirmed requirements.
  - Known constraints.
- Actions
  1. Describe the expected outcome as a task users can complete.
  2. List the delivery scope.
  3. List exclusions easily mistaken for included scope.
  4. Link each constraint to its basis.
  5. Define each success criterion and verification method.
- Completion criteria
  - [ ] Each deliverable has an assessable completion result.
  - [ ] Thresholds are confirmed requirements or explicitly marked as undecided proposals.

### 3. Choose the work container

- Inputs
  - Outcomes and success criteria.
  - Scope of work needing coordination.
- Actions
  1. Use an Issue when a single outcome can be delivered directly.
  2. Use a parent and sub-issues when parts of an outcome need separate handoffs.
  3. Choose a Project when a shared Brief and ongoing project progress management are needed.
  4. Search existing Projects for an entry point serving the same outcome.
  5. Record each repository work location.
- Completion criteria
  - [ ] Coordination needs justify the container choice.
  - [ ] The number of Agents or repositories does not directly cause additional Projects.

### 4. Assign roles and handle uncertainty

- Inputs
  - Draft Brief.
  - Questions still requiring answers.
- Actions
  1. Assign a Project lead to maintain overall scope.
  2. Assign a requirements decision-maker.
  3. Assign an acceptance reviewer.
  4. Record the impact of each unresolved requirement.
  5. Assign responsibility and a method for obtaining answers.
  6. Set the point by which a decision is required.
  7. Schedule work independent of the answer first.
  8. Specify each Agent's execution scope within the work.
- Completion criteria
  - [ ] Each unresolved requirement has a confirmation path.
  - [ ] Work awaiting an answer is identifiable.
  - [ ] The first executable batch does not treat assumptions as commitments.

### 5. Create or update the Project

- Inputs
  - An executable Brief.
  - Selected Workspace and Team.
  - Search results for existing Projects.
- Actions
  1. Update the existing Project entry point when one matches.
  2. If a new Project is needed, select `+` on the Projects page and enter the outcome name. [P1](https://linear.app/docs/projects#create-a-project)
  3. Set the Team that will actually perform the work.
  4. Set the confirmed lead.
  5. Record progress using the environment's actual status options.
  6. If dates are unconfirmed, retain the question and confirmation method in the Brief.
  7. Put the Brief in Overview's detailed description or link its authoritative document. [P2](https://linear.app/docs/project-overview#detailed-description)
  8. Add each work resource to Resources. [P2](https://linear.app/docs/project-overview#external-links)
  9. Read back the content and check access to required links.
- Completion criteria
  - [ ] The Project's outcome scope matches the Brief.
  - [ ] The authoritative document entry point is identifiable.
  - [ ] Executors can find required resources.

### 6. Hand off the first batch

- Inputs
  - Project entry point.
  - Confirmed deliverables.
  - Impact of open questions.
- Actions
  1. List the first batch by independently acceptable outcomes.
  2. Record delivery and acceptance for each item.
  3. List required prerequisites for each item.
  4. Link existing issues back to the Brief.
  5. Create missing work and add its entry points.
  6. State an action the next executor can perform immediately.
  7. When confirmed requirements change, revise acceptance criteria in affected work.
- Completion criteria
  - [ ] The next session can continue the first batch.
  - [ ] Overall success criteria remain at Project level.

## Introducing the process midstream

1. Record the inventory date and version.
2. Confirm completed scope using output evidence.
3. List issues still in progress.
4. Compare requirement documents with current behavior.
5. Create open questions for conflicting or unsupported statements.
6. Prefer updating existing issues to preserve original tracking entry points.
7. Before changing Project membership, confirm the original Project's delivery responsibility.
8. When a shared output already has a primary Project, reference it from the Brief.
9. If independent adoption or acceptance is needed, create work with a distinct deliverable.
10. Read back updated relationships and statuses.

If considering converting a parent to a Project, first save overall acceptance criteria and the parent-child list.
After conversion, verify each structural change described in [P3](https://linear.app/docs/parent-and-sub-issues#turn-issues-into-projects).
To preserve a local parent-child structure, create a Project and add the existing issues.

## Example 1: Build CSV export from scratch

This hypothetical example uses illustrative requirements and thresholds.

- Inputs
  - Simulated interview record: Users manually copy time logs every week.
  - Adopted requirement: Export time logs for a specified date range as CSV.
- Problem: Manual copying easily misses records.
- Outcome: Users can obtain a verifiable time-log CSV.
- This scope
  - Date range selection.
  - CSV download.
- Exclusions
  - Scheduled delivery.
- Constraint: Reuse the existing time-log data format.
- Work locations
  - Example repository: `time-log`.
    - `app/`: Export interface.
    - `api/`: Data queries and CSV generation.
- Roles
  - Project lead: Product maintainer.
  - Requirements decision-maker: Product maintainer.
  - Acceptance reviewer: Product maintainer.
  - API executor: Agent A.
  - Interface executor: Agent B.
- Open question: Are custom fields needed?
  - Status: Unconfirmed.
  - Impact: The custom-field interface must await an answer.
  - Confirmation method: The maintainer obtains usage examples from the requester.
  - Decision point: Before planning custom-field work.
  - Work that can proceed: Fixed-field export.
- Success criteria
  - [ ] The fixed-field CSV matches time-log records within the specified dates.
    1. Prepare known records spanning several date ranges.
    2. Export one date range.
    3. Check record count and each field value.
- Modeling: Create the "Provide time-log CSV export" Project.
  - Reason: A shared Brief coordinates API and interface delivery.
- First batch
  - Generate a fixed-field CSV.
    - Acceptance: Known data and output match record by record.
  - Provide a download interface.
    - Prerequisite: CSV API contract.
    - Acceptance: Users obtain the file for the specified range.
  - Verify the complete export workflow.
    - Prerequisites: Usable API and interface.
    - Acceptance: Project success criteria pass.
- Next step: Define the CSV API contract first for both execution items.

## Example 2: Introduce notification preferences midstream

This hypothetical example uses evidence labels to represent entry points that must be obtained during takeover.

- Inventory baseline: Current test version `v0.4`.
- Inputs
  - Output A: Notification delivery API verification report.
  - Work B: Preference interface issue currently under development.
  - Proposal C: SMS suggestion in a chat record.
- Problem: Users cannot stop weekly summary emails themselves.
- Outcome: Users can save preferences and control subsequent summary emails.
- This scope
  - Email summary toggle.
  - Delivery service respects preferences.
- Constraint: Keep the current Email provider.
- Work locations
  - Example repository: `notifications`.
    - `settings/`: Preference interface.
    - `mailer/`: Delivery decision.
- Handling existing work
  - Output A: Record as a completed foundational capability and retain its report link.
  - Work B: Keep the original issue and add success criteria.
  - Proposal C: Retain as an unconfirmed requirement.
- Roles
  - Project lead: Product maintainer.
  - Requirements decision-maker: Product maintainer.
  - Acceptance reviewer: Product maintainer.
  - Interface executor: Original executor of work B.
  - Delivery decision executor: Agent C.
- Open question: Should SMS be included?
  - Status: Unconfirmed.
  - Impact: SMS provider selection and implementation must await an answer.
  - Confirmation method: The maintainer asks the requester to confirm the usage scenario.
  - Decision point: Before adding SMS work.
  - Work that can proceed: Email preferences.
- Success criteria
  - [ ] The next scheduled run sends no summary email after summaries are disabled.
    1. Save the disabled preference.
    2. Run the test schedule.
    3. Verify from delivery logs that no summary email was generated.
  - [ ] The next scheduled run resumes summary emails after re-enabling them.
- Modeling: Search for and reuse the "Provide notification preferences" Project.
- First batch
  - Complete work B's preference-saving interface.
    - Acceptance: Preference values persist after reload.
  - Add preference checks to the delivery service.
    - Prerequisite: Preference data contract.
    - Acceptance: Skip delivery when the preference is disabled.
  - Verify the next scheduled run's behavior.
    - Prerequisites: Usable interface and delivery checks.
    - Acceptance: Both Project success criteria pass.
- Next step: Check the preference data contract adopted by work B, then add the delivery-service work.

## Adoption configuration

Adopters configure the following according to their authorization and work practices.

- Decide whether the lead also acts as requirements decision-maker.
- Decide whether the same person also performs acceptance review.
- Specify authorization scope for remote changes.

## Source record

All publishers are Linear.
Verified on: 2026-09-13.
Evidence status: Confirmed in documentation.
Scope: Product feature descriptions in the sections below.

- P1: [Projects](https://linear.app/docs/projects)
  - `Create a project`: Creation entry point and required name.
  - `Add issues to a project`: One Project per issue.
  - `Multi-team projects`: Cross-Team Projects.
  - `FAQ`: Single lead and optional completion date.
- P2: [Project overview](https://linear.app/docs/project-overview)
  - `Detailed description`: Editing the detailed description.
  - `External links`: Resources links.
  - `Project documents`: Document creation.
- P3: [Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues)
  - `Turn issues into projects`: Structural changes during parent conversion.
