# Small to-do product: from environment initialization to the first issues

This fictional plan uses a paper walkthrough to demonstrate work allocation for an individual developer with multiple Agents.
All identifiers and configurations are examples.

- Initialization: [Workspace initialization and takeover](workspace-setup.md).
- Project planning: [Build a Project from requirements](project-planning.md).
- Brief fields: [Project brief template](../assets/templates/project-brief.md).
- Scheduling: [Milestones and dependency scheduling](planning-and-dependencies.md).
- Decomposition: [Single-session deliverables](issue-decomposition.md).

## Scenario and inputs

- Requirement record
  - The user opens the same computer daily and wants to quickly record a few to-dos.
  - To-do text and completion state must remain after refreshing the webpage.
  - The first version must support adding to-dos.
  - The first version must support toggling completion state.
- Environment inventory
  - The maintainer already has a Linear Workspace for personal development.
  - The existing Product Team handles personal product development.
  - Search found no Project or issues delivering the same result.
  - Product repository `pocket-tasks` has a runnable blank webpage and test commands.
- Requirement decisions
  - Use local storage in the same browser.
  - Provide a persistence-failure message and retry method.
  - Accounts are outside the first version.
  - Cross-device synchronization is outside the first version.
  - Deletion is outside the first version.
  - Reason: the core outcome in the requirement record needs only local creation and completion marking.

## Workspace and object choices

### Reasons for the choices

- Workspace: reuse the personal-development Workspace in the inventory.
  - Reason: the same maintainer manages the product, with no new organizational boundary.
- Team: reuse the Product Team.
  - Reason: the first batch shares a workflow and access scope.
- Project: create "Preserve to-dos and completion state locally".
  - Reason: coordinate four deliverables through a shared brief and track the first version's overall result.
- Milestones: use "To-do data can be saved reliably" and "The user can complete the to-do flow" to express two assessable outcomes.
  - See "Milestones" for specific outcomes and issues.
- Issues: each of four work items provides a deliverable usable downstream.
  - See "First issues" for specific boundaries.
- Parent: the Project retains overall acceptance in this example; all four issues belong directly to the Project.
  - Reason: the four items cover the same first-version result; an additional parent would duplicate its acceptance criteria.
- Cycle: begin with deliverable dependencies.
  - Reason: no capacity records for a fixed cadence exist yet.

### Configuration adopted from the inventory

The following records example decisions using the [environment record](workspace-setup.md#environment-record) fields.

- Workspace
  - Name: Personal Product Development.
  - Settings administrator: product maintainer.
- Team
  - Name: Product.
  - Identifier: TASK.
  - Time zone: Asia/Taipei.
  - Access scope: maintainer and this execution connection.
- Issue status
  - Awaiting scheduling: Backlog.
  - Ready to execute: Todo.
  - Executing: In Progress.
  - Review and acceptance: retain In Progress.
  - Complete: Done.
  - Canceled: Canceled.
  - Default status: Backlog.
  - Reason: default work stages sufficiently express this example's progress.
- Automations
  - Update status manually after acceptance is complete.
  - Check every existing status-changing rule before reusing the environment.
- Priority: No priority.
  - Reason: no additional urgency differences exist; arrange work around actual prerequisites first.
- Estimates: disabled.
  - Reason: manage this batch using assessable deliverable boundaries and WIP first.
- Labels: empty.
  - Reason: these four items currently have no recurring classification need.
- Execution identity
  - Human Assignee: product maintainer.
  - Agent A: execute TASK-A, then storage and integration work.
  - Agent B: execute interface work.
  - Connection method: existing authorized MCP connection.
  - Operational scope: specified issues and their deliverable files only.
  - Reason: the human owns outcomes, and each Agent's scope can be handed off clearly.
- Notifications
  - Viewing entry point: Inbox.
  - Subscription: the maintainer subscribes to this batch's real work.
  - Reason: the same person follows the first batch throughout.

### From inventory to the first work batch

1. Check the inventory's actual values using the [existing-environment takeover checklist](workspace-setup.md#existing-environment-takeover-checklist).
2. Save actual Workspace identifiers.
3. Save the Team UUID.
4. Save each status ID and category.
5. Confirm the execution connection can read the target Team.
6. Have the maintainer confirm settings-administration permissions.
7. Confirm how to start and test the repository.
8. Create the Project using the brief below.
9. Create "To-do data can be saved reliably" and "The user can complete the to-do flow", filling each with its stage acceptance criteria.
10. Create each initial issue and record its actual entry point.
11. Set the relationships in "Dependencies and execution order".
12. Read back Team and Project placement for the first issues.
13. Check milestone placement.
14. Check initial statuses and optional fields.
15. Add an environment record ready for handoff to the TASK-A body.

When adapting this example to a blank environment, first complete the [blank-environment initialization checklist](workspace-setup.md#blank-environment-initialization-checklist), then proceed to Project planning above.

## Project brief: preserve to-dos and completion state locally

### Problem and outcome

- Target user: an individual managing a few to-dos in the same browser.
- Problem: the user in the requirement record needs to continue working with to-dos after reopening the webpage.
- Requirement basis: "Requirement record" in this document.
- Expected outcomes
  - The user can add to-dos.
  - The user can toggle completion state.
  - Reloading preserves results.

### Scope

- This delivery
  - Add to-dos.
  - Toggle completion state.
  - Persist locally.
  - Handle errors when local data cannot be read or written.
- Exclusions
  - Accounts: no such need yet in the requirement record.
  - Cross-device synchronization: no such need yet in the requirement record.
  - Delete to-dos: awaits confirmation of usage needs.
- Constraints
  - Use only within the same browser profile, following the requirement decisions in this document.
  - Use the existing web project and test tools in the inventory.
- Work locations
  - Example repository: `pocket-tasks`.
    - `docs/task-contract.md`: data and interface contract.
    - `src/tasks/`: storage capability.
    - `src/ui/`: to-do interface.
    - `src/app/`: assembly entry point.
    - `tests/`: behavioral verification using existing tools.
    - `docs/acceptance.md`: overall acceptance evidence.

### Success criteria

- [ ] After adding two to-dos, reloading preserves their text and order.
  1. Start with empty data.
  2. Add "Buy milk" and "Tidy the desk".
  3. Reload and check both texts and their order.
- [ ] Completion state can be toggled and persisted.
  1. Mark "Buy milk" complete.
  2. Reload and check its completed state.
  3. Mark it incomplete, reload, and check its incomplete state.
- [ ] Blank text is rejected and existing to-dos remain intact.
- [ ] A write failure displays an error and preserves input for retry.
- [ ] A read failure or corrupted data format displays an error, preserves original data, and stops writes.

### Roles and execution entry points

- Project lead: product maintainer.
- Requirements decision-maker: product maintainer.
- Acceptance reviewer: product maintainer.
- Execution allocation
  - Agent A
    - TASK-A.
    - TASK-B.
    - TASK-D.
  - Agent B: TASK-C.
  - The maintainer owns every deliverable's outcome.
- Team: Product Team from the inventory.
- Project: use this brief as the authoritative description when creating it, then record the actual URL.
- First batch: TASK-A through TASK-D below.
- Dates: arrange by deliverables; no delivery date yet.
- Next step: confirm environment replacement values and assign TASK-A's contract work to the first execution session.

### Open question

- Whether cross-device synchronization warrants inclusion in a later version.
  - Source: first-version exclusions in this document.
  - Impact: planning for accounts and remote data storage.
  - Confirmation method: the maintainer collects actual cross-device usage scenarios.
  - Decision point: before planning the next version.
  - Work that can proceed: the entire first batch in this example.

## Milestones

- "To-do data can be saved reliably".
  - Issues
    - TASK-A.
    - TASK-B.
  - Reason: the shared contract and storage capability form a deliverable ready for interface integration.
  - [ ] Storage capability passes data and error-scenario acceptance.
  - [ ] TASK-C and TASK-D can find usage instructions in the contract.
- "The user can complete the to-do flow".
  - Issues
    - TASK-C.
    - TASK-D.
  - Reason: interface and integration jointly deliver the Project's user outcome.
  - [ ] The actual assembled version passes every success criterion in the brief.

Interface work for "The user can complete the to-do flow" can start using the confirmed contract before "To-do data can be saved reliably" is complete.
Judge milestone outcomes by their respective acceptance criteria.

## First issues

All items share the repository and existing test tools from the inventory.
On takeover, read in this order:

1. This brief.
2. The issue's latest body.
3. Pinned versions of prerequisite deliverables.

Each item aims to deliver the following output and verification within one session.
If the scope cannot be fully accepted, preserve deliverables and split again using [Handling work that exceeds a session](issue-decomposition.md#handling-work-that-exceeds-a-session).

### TASK-A: provide a to-do contract shared by storage and interface

- Milestone: "To-do data can be saved reliably".
- Executor: Agent A.
- Input: this brief and the requirement decisions in the requirement record.
- Prerequisite: environment inventory complete and repository usable.
- Deliverable: `docs/task-contract.md`.
- Scope
  - Define data fields
    - Stable identifier.
    - Text.
    - Completion state.
    - Creation order.
  - Define operation interfaces
    - Add.
    - Toggle completion state.
    - Read the list.
  - Define rules for rejecting blank text.
  - Define error responses
    - Write failure.
    - Read failure.
    - Corrupted data.
- Reason for a separate item: TASK-B and TASK-C need the same data and error semantics for independent acceptance.
- Acceptance
  - [ ] The contract includes complete data examples.
  - [ ] Every operation has an input specification.
  - [ ] Every operation has an output specification.
  - [ ] Creation order has a checkable example.
  - [ ] State toggling has a checkable example.
  - [ ] Blank text has an explicit response.
  - [ ] Write failure has an explicit response.
  - [ ] The read-failure response prohibits subsequent overwriting of original data.
  - [ ] The corrupted-data response prohibits subsequent overwriting of original data.
  - [ ] The maintainer confirms the contract supports both storage implementation and interface mock data.

### TASK-B: implement verifiable local to-do storage

- Milestone: "To-do data can be saved reliably".
- Executor: Agent A.
- Input: the confirmed TASK-A contract version.
- Blocked by: TASK-A.
- Deliverables
  - Storage capability in `src/tasks/`.
  - Behavioral verification in `tests/tasks/`.
- Scope
  - Read and write to-do data according to the contract.
  - Verify persistence of additions and completion state.
  - Verify failures do not overwrite existing data.
- Reason for a separate item: storage behavior can be verified directly through the contract and provides integration input for TASK-D.
- Acceptance
  - [ ] After adding two items, a new storage instance reads back the same text and order.
  - [ ] After marking complete, readback shows the completed state.
  - [ ] After marking incomplete, readback shows the incomplete state.
  - [ ] Blank text creates no new item.
  - [ ] An injected write failure returns the contract error and preserves original data.
  - [ ] An injected read failure leaves original data intact.
  - [ ] Injected corrupted data leaves original data intact.

### TASK-C: provide a contract-compliant to-do interface

- Milestone: "The user can complete the to-do flow".
- Executor: Agent B.
- Input: the confirmed TASK-A contract version.
- Blocked by: TASK-A.
- Deliverables
  - To-do interface in `src/ui/`.
  - Mock-response verification in `tests/ui/`.
- Scope
  - Display the list and accept additions.
  - Provide completion-state toggling.
  - Simulate success and failure responses using the contract.
- Reason for a separate item: interface interactions can be accepted with simulated responses without waiting for storage implementation.
- Acceptance
  - [ ] An empty list has an understandable message.
  - [ ] The input has an identifiable name.
  - [ ] Action controls have identifiable names.
  - [ ] Adding sends the operation required by the contract.
  - [ ] State toggling sends the operation required by the contract.
  - [ ] The keyboard can complete an addition.
  - [ ] The keyboard can toggle state.
  - [ ] An addition write failure preserves text for retry.
  - [ ] A state-toggle failure preserves the original completion state for retry.
  - [ ] A write failure displays an error.
  - [ ] A read failure displays an error and disables write operations.
  - [ ] Corrupted data displays an error and disables write operations.

### TASK-D: integrate and verify a to-do flow for continued use

- Milestone: "The user can complete the to-do flow".
- Executor: Agent A.
- Inputs
  - TASK-B's accepted storage version.
  - TASK-C's accepted interface version.
- Blocked by
  - TASK-B: provides real storage capability.
  - TASK-C: provides an interface ready for assembly.
- Deliverables
  - Assembly entry point in `src/app/`.
  - Complete-flow verification in `tests/integration/`.
  - Overall acceptance record in `docs/acceptance.md`.
- Reason for a separate item: separately passing the simulated interface and storage still requires confirming the assembled user outcome.
- Acceptance
  - [ ] The actual assembled version passes every success criterion in the brief.
    1. Record the integration version.
    2. Record the browser used.
    3. Execute each operation in the brief's success criteria.
    4. Record each result in `docs/acceptance.md`.
  - [ ] Error responses travel through the actual storage interface to the screen and meet TASK-C's error acceptance criteria.
  - [ ] The Project deliverable entry point locates the integration version and acceptance record.

## Dependencies and execution order

- Dependency graph: `TASK-A → {TASK-B, TASK-C} → TASK-D`.
- TASK-A availability: contract acceptance complete and a pinned deliverable version accessible.
- Conditions for TASK-B and TASK-C to run concurrently
  - Both use the same contract version.
  - Each stays within its storage or interface paths.
  - Execution and review capacity are sufficient.
- TASK-D readiness: both TASK-B and TASK-C deliverables pass acceptance.
- If shared configuration files need changes, assign a single writer first.
  - Coordinate change conflicts by write scope.
  - If changes affect the contract, revise affected inputs and acceptance criteria first.
- Example WIP
  - One executing item per Agent at a time.
  - At most one deliverable under active review.
  - Waiting for review and rework still count toward the original executor's WIP.

1. The first session executes TASK-A.
2. After the maintainer confirms the contract, take on TASK-B and TASK-C separately.
3. When both deliveries arrive together, finish one review first; the other remains awaiting review and occupies WIP.
4. Read both deliverables and statuses, and take on TASK-D only after its inputs are complete.
5. After TASK-D passes, check acceptance for "To-do data can be saved reliably".
6. Check acceptance for "The user can complete the to-do flow".
7. Check Project success criteria.

## Settings to replace when adapting

- Environment
  - Actual Workspace.
  - Actual Team.
  - Required permissions.
  - Search results for existing Projects.
  - Search results for existing issues.
  - Actual issue-workflow names and status categories.
- Work locations
  - Repository URL.
  - Identifiable version.
  - Real source paths.
  - Test commands.
  - Actually supported browsers.
  - Storage limits.
- Roles and policy
  - Project lead.
  - Requirements decision-maker.
  - Acceptance reviewer.
  - Each issue's assignee.
  - Each Agent's execution scope.
  - Remote-operation authorization.
  - Deliverable publication method.
  - WIP.
  - Review capacity.
  - Whether Cycles are enabled and existing settings.
- Requirements and tracking
  - Replace the requirement record with real requirement evidence.
  - Replace the environment inventory with the actual inventory record.
  - Confirm first-version scope and decision points for unknown requirements.
  - Replace TASK identifiers with native issue mentions after creation.
  - Replace "To-do data can be saved reliably" with the actual milestone.
  - Replace "The user can complete the to-do flow" with the actual milestone.
  - Add an accessible Project link.
  - Add accessible prerequisite-deliverable links.
  - Add an accessible acceptance-record link.

## Feature basis

Verification date: 2026-09-13.
Evidence method: review of official Linear documentation.
Object choices and capacity arrangements in this document are usage recommendations.

- An issue can belong to only one Project at a time.
  - Source: [Projects — Add issues to a project](https://linear.app/docs/projects#add-issues-to-a-project).
- Milestone dates are optional.
  - Source: [Project milestones — Create milestones](https://linear.app/docs/project-milestones#create-milestones).
- Multiple milestones can run concurrently.
  - Source: [Project milestones — FAQ](https://linear.app/docs/project-milestones#faq).
- `Blocked by` expresses that this item waits for a prerequisite issue.
  - Source: [Issue relations — Blocked / blocking](https://linear.app/docs/issue-relations#blocked-blocking).
