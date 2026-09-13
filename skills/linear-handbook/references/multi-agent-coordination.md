# Multi-Agent claims and handoffs

Help individual developers and multiple Agents continue authorized work while reducing duplicate execution and overwrites.
The following procedures are usage recommendations.
Platform facts are collected under "Evidence and sources".
Project policy is collected under "Replaceable policy".

## Role responsibilities

- Outcome owner
  - Is responsible for the delivery result.
  - Decides scope changes requiring human judgment.
  - A human remains Assignee under native Agent delegation; see "Assign and delegate issues".
- Coordinator
  - Maintains current work assignments.
  - Arranges a sole writer for shared resources.
  - Resolves duplicate claims.
  - Checks integration results across issues.
- Executing Agent
  - Completes the assigned scope.
  - Updates its own deliverables.
  - Preserves evidence for takeover.
  - Stops affected writes when a conflict is found.
- Reviewer
  - Checks deliverables against currently effective completion criteria.
  - Records specific differences.

One person may hold several roles.
Execute assigned work directly under existing authorization.
The coordinator's assignment record confirms exclusive execution scope; it does not add a user approval step.

When external Agents share one Linear user connection, Assignee cannot distinguish execution sessions.
Record the actual executor using an identifiable session name.
Use Delegate only for an installed native Agent with the required access; see "Assign and delegate issues" and "Agents — Getting Started".

## Select an executable issue

1. Read the work specified by the user.
2. Confirm the operational scope covered by this authorization.
3. Read the target issue's current body.
4. Read the parent's overall delivery criteria.
5. Read the latest comments and follow decisions affecting this work.
6. Read the current status of prerequisite issues.
7. Open prerequisite deliverables needed for this work.
8. Check the execution conditions below.
9. If no work has been specified, choose an eligible candidate using existing priorities.
10. Assign an executor using the claim process.

Execution conditions:

1. The deliverable scope can be judged independently.
2. Completion criteria can be verified.
3. Necessary prerequisite inputs are actually available.
4. Required operations are within existing authorization.
5. The executor can access necessary deliverables.
6. No other execution assignment remains effective.
7. The write scope is compatible with concurrent work.

- Even when a prerequisite shows Done, open its deliverable to confirm availability.
- When a prerequisite is canceled, follow its replacement deliverable before judging.
- When a prerequisite is marked duplicate, follow the canonical issue before judging.
- If tools still list a completed blockedBy relationship, judge using current status and deliverables.
- If an aggregation parent only summarizes child items, select the child carrying the actual deliverable.
- For an actual input gap, record resolution conditions using the [blocking process](issue-lifecycle.md#2-blocked).

When lists are paginated:

1. Keep the same filters.
2. Keep the same ordering.
3. Save the returned cursor.
4. Read subsequent pages using the current tool's next-page parameter.
5. Continue until hasNextPage is false.
6. Deduplicate by issue ID.
7. Directly reread the selected issue.

Completing the list does not prove nothing changed during the query.
Use paginated data to select candidates and direct reads to confirm current execution conditions.
Use API pagination and MCP fields according to their respective interfaces; see "Pagination".

## Work claims

By default, one coordinator maintains work assignments.
Assign only one executor to each shared write scope at a time.
Without a coordinator, let the single executor in the existing schedule handle shared writes.
When the sole executor cannot be confirmed, first complete independent reads and drafts.

1. The coordinator rereads current assignments.
2. Confirm the candidate issue still meets execution conditions.
3. Check whether shared resources already have a writer.
4. Designate the execution session.
5. Record necessary assignment information.
6. The executing Agent reads that assignment.
7. Check that no conflicting assignment exists.
8. Update the stage when starting, following [Starting work](issue-lifecycle.md#1-starting-work).

Assignment information:

- Issue: unique ID.
- Outcome owner: person responsible for delivery.
- Executor: identifiable session.
- Write scope: files or remote objects.
- Shared resources: entry points requiring coordination with other work.
- Execution baseline: version read at the start.
- Resumption point: location from which work can recover after interruption.

Reuse an existing readable assignment entry point.
When a Linear write is necessary to preserve assignments across sessions, put the current assignment in the body under existing write authorization.
Comments add only new decisions affecting collaboration.

Assignee and Delegate express responsibility or delegation.
Status expresses the work stage.
These fields and claim text are not atomic locks.
Reading, writing a claim, and reading back your own name can still be followed immediately by another executor overwriting it.
The process reduces race risk but cannot guarantee exclusivity.
Check whether the current tool provides corresponding guarantees before operating.

If the work requires strict exclusivity, use a verified external scheduling mechanism.
It must reject writes from a second effective executor.
Replacing an executor must also remove the previous executor's write capability.
Coordination text or an expiry time alone cannot provide this guarantee.

## Reread before updating

Reread the target object at these points:

- Before starting this execution.
- Before writing a shared object.
- Before recording results after a long analysis.
- After receiving a user correction.
- After taking over another session's work.
- Before retrying an operation with an uncertain tool result.

1. Read the latest body.
2. Read new comments affecting this operation.
3. Check the current execution assignment.
4. Check whether status changed.
5. Check current completion criteria.
6. Compare the latest content with your read baseline.
7. Reassess affected judgments when differences exist.
8. Produce the smallest necessary change using the latest content.
9. Write within existing authorization.
10. Read back target fields.
11. Check necessary relationships.
12. Check that others' additions remain intact.

- updatedAt can indicate an object changed.
  - It is not a version condition enforced by the server when accepting writes.
  - Read comments separately; issue timestamps alone are insufficient.
- When replacing a complete body, assemble new content from the version just read.
  - Preserve others' still-effective changes.
  - Resolve semantic conflicts before writing.
- When a tool provides patch, first check its targeting and failure contract.
  - A successful patch does not mean the entire issue is locked.
- A race window remains between rereading and writing.
  - Continue assigning a single writer for shared objects.
- If readback differs, use [tool recovery](tool-recovery.md) to establish current effects.

## Concurrency and scope conflicts

Different issues may still modify the same deliverable.
Compare scope by actual resource when claiming work.

| Shared resource | Arrangement |
| --- | --- |
| Same file | Designate one writer to combine changes |
| Same issue body | Designate one writer to maintain current conclusions |
| Same parent acceptance | Have the coordinator combine child evidence |
| Same project description | Have the maintainer integrate summaries |
| Same deployment environment | Follow the existing release schedule |
| Shared test data | Confirm isolation or serialize checks that modify data |

1. When overlapping scope is discovered, stop the affected writes.
2. Save each draft in a location that cannot overwrite the other.
3. Read the latest shared deliverable.
4. Compare the purpose of both parties' changes.
5. If a priority already exists, choose the writer according to that decision.
6. If no applicable decision exists, have the coordinator decide the order.
7. Give the other party's necessary changes to the writer for integration.
8. Integrate against the current version.
9. Verify the merged deliverable.
10. Update the assignment entry point.

Independent research can run concurrently.
Independently verifiable deliverables can be handed over separately.
Shared outputs need an explicit write order.

## Handoff and recovery

Use the [handoff template](../assets/templates/handoff.md).
The issue body preserves currently effective requirements.
The handoff entry point preserves information needed to resume execution.

Handing off work:

1. Update the body with adopted conclusions.
2. Save an identifiable deliverable version.
3. Preserve existing changes.
4. Record verified results.
5. Record remaining work.
6. State resolution conditions for actual blockers.
7. Preserve the source and scope of existing authorization.
8. Identify the first directly executable operation.
9. Stop your own writes to the transferred scope.
10. Have the coordinator update the successor assignment.

Taking over work:

1. Open the handoff entry point.
2. Reread the current issue.
3. Read the latest user corrections.
4. Check the currently effective assignment.
5. Check necessary prerequisite deliverables.
6. Compare existing changes in the working location.
7. Check whether tool capabilities apply.
8. For remote operations with uncertain outcomes, inspect current effects first.
9. Continue the first executable step under existing authorization.

When an executor has not responded for a long time, the coordinator first checks whether work is still running.
Inactivity alone does not invalidate a claim.
Before taking over shared writes, confirm the previous executor has stopped or lost write capability for that scope.
If this cannot be confirmed, hold shared writes and continue nonconflicting work.
A resumed old session must reread assignments before writing back its old draft.

When necessary acceptance has not been met, keep the work at its actual incomplete stage.
After completion, record deliverables according to the [lifecycle](issue-lifecycle.md#5-completion).

## Examples

The following are fictional scenario walkthroughs.

### Two Agents claim simultaneously

| Point | Agent A | Agent B |
| --- | --- | --- |
| 1 | Reads no executor | Reads no executor |
| 2 | Writes A's claim | Has not written |
| 3 | Reads back A's claim | Has not written |
| 4 | Prepares to edit the shared file | Writes B's claim |
| 5 | Still holds the earlier read result | Reads back B's claim |

Both Agents successfully read back their own claims.
If they continue on that basis, both will edit the shared file concurrently.

1. When either party discovers another effective executor, stop shared writes.
2. Save A's existing draft.
3. Save B's existing draft.
4. The coordinator checks existing assignment decisions.
5. In this example, the coordinator designates A as the sole writer for the scope.
6. B stops modifying that scope.
7. A integrates B's necessary deliverables against the latest version.
8. Read back the shared deliverable and check the merged result.

- [x] The sequence explains why read-write-read cannot establish an atomic lock.
- [x] Conflict handling preserves both parties' deliverables.
- [x] A sole writer is explicitly designated before resumption.

### Human rewrite during execution

- Original body: deliver CSV export.
- Agent draft: an existing CSV implementation plan.
- The user provides a complete replacement body during work.
  - Deliver JSON export.
  - Preserve the user's list structure.
- Existing authorization: modify local deliverables and update that issue.

1. After receiving the correction, the Agent rereads the latest body.
2. Compare the CSV draft with JSON requirements.
3. Update execution scope to JSON export.
4. Preserve investigation results usable for JSON work.
5. Modify the deliverable according to new completion criteria.
6. Reread the body before updating it.
7. Add actual deliverable links to the user's version.
8. Read back and confirm JSON requirements remain.
9. Check that list semantics are preserved.

- [x] New instructions sufficiently define scope, allowing continuation under existing authorization.
- [x] The old draft does not overwrite the user's complete replacement.
- [x] Verification follows currently effective completion criteria.

If new requirements involve operations outside the original authorization, first complete independent preparation.
Assess actual missing operational authorization using [Agent boundaries](agent-boundaries.md).

## Evidence and sources

Verification date: 2026-09-13.
The following are official Linear documents.

- [Assign and delegate issues](https://linear.app/docs/assigning-issues)
  - Section: [Overview](https://linear.app/docs/assigning-issues#overview).
    - An issue has one Assignee at a time.
  - Section: [Delegating to agents](https://linear.app/docs/assigning-issues#delegating-to-agents).
    - The human Assignee retains outcome responsibility when delegating to an Agent.
    - The Agent needs access to the target Team.
- [Agents — Getting Started](https://linear.app/developers/agents)
  - Section: [Actor and scopes](https://linear.app/developers/agents#actor-and-scopes).
    - actor=app uses the App installation identity.
  - Section: [Mention + assign scopes](https://linear.app/developers/agents#mention-+-assign-scopes).
    - app:assignable allows an App to become an issue Delegate.
  - Section: [Management](https://linear.app/developers/agents#management).
    - Admins can change or revoke an App's Team access.
- [Issue relations](https://linear.app/docs/issue-relations)
  - Section: [Blocked / blocking](https://linear.app/docs/issue-relations#blocked-blocking).
    - After a blocker is resolved, the relationship appears under Related.
- [Pagination](https://linear.app/developers/pagination)
  - Location: page introduction and first issues query example.
    - GraphQL lists use cursor pagination.
    - Use endCursor as after to fetch the next page.
    - hasNextPage indicates whether another page remains.

## Replaceable policy

Responsibility and assignment sources follow [policy](policy.md).
Writing and complete replacement versions follow [writing](writing.md).
