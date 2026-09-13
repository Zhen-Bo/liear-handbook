# Linear API, MCP, and GitHub integration capabilities

Verified: 2026-09-12.
Editorial revision: 2026-09-13.

- Environment: an individual developer with multiple Agents.
- Research baseline: [scope-and-sources.md](scope-and-sources.md).
- Policy interface: [extension-model.md](extension-model.md).

## Adopted conclusions

- Choose operations according to the evidence level.
  - Product documentation supports features and conditions of use.
  - Tool declarations support accepted fields.
  - Operational evidence supports actual results for specific accounts and objects.
- Reread the issue and prerequisite states at every handoff.
  - `blockedBy` may retain completed work.
  - Readiness to take over depends on prerequisite statuses and deliverables.
- Include GitHub Team settings and PR relationship types in environment policy.
  - A PR merge event provides evidence of code integration.
  - Deployment results and acceptance each retain their own evidence.

See [AGENTS.md](../AGENTS.md) for workflow policy.

## Evidence levels

| Label | Supported scope |
| --- | --- |
| Documented | Product behavior and conditions stated on official pages |
| Declared | Interface contracts in a pinned API schema or tool snapshot |
| Operational evidence | Requests and readback results recorded under “Observed operations and verification” below |

- Official documentation was read on 2026-09-12.
- The API schema is pinned to commit `23f11eb41ef63ba219ec582911079c19d1abbf62`.
- Historical tool snapshot: [linear-tool-schema-2026-09-12.json](sources/linear-tool-schema-2026-09-12.json).
  - Dated 2026-09-12; contains 14 tool declarations.
  - Operation records use the then-available `mcp__linear__*` tools.
  - Short tool names below refer to this snapshot.
- Maintenance operations for this document on 2026-09-13 used `mcp__codex_apps__linear_*`.
  - Later sessions should recheck the tools and fields actually exposed.
  - The historical snapshot preserves the evidence scope at that time.

## Capability matrix

| Capability | Linear product | Official API | Official MCP | Historical tool evidence |
| --- | --- | --- | --- | --- |
| Read/write | Object operations [API and Webhooks](https://linear.app/docs/api-and-webhooks) | query/mutation [Getting started — GraphQL](https://linear.app/developers/graphql) | Operations on issues and other objects [MCP server](https://linear.app/docs/mcp) | Issue and comment writes read back |
| Parent relationships | Parent/sub-issues [Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues) | `parentId` [Official schema — IssueUpdateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L22348) | Parent/sub-issue use cases [MCP server](https://linear.app/docs/mcp) | Parent read and sub-issue list query |
| Dependencies | Blocking and other relationships [Issue relations](https://linear.app/docs/issue-relations) | Relation mutation [Official schema — IssueRelationCreateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L20623) | Related use cases [MCP server](https://linear.app/docs/mcp) | Dependency reads |
| Documents | Document editing [Documents](https://linear.app/docs/documents) | Document mutation [Official schema — DocumentCreateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L10446) | General feature page [MCP server](https://linear.app/docs/mcp) | Project document list query |
| Pagination | List interface | Relay cursor [Pagination](https://linear.app/developers/pagination) | Tool contract | Four-page results compared with a single-page query |
| GitHub PR sync | Team status mappings [GitHub](https://linear.app/docs/github) | General issue mutation | Issue update interface [MCP server](https://linear.app/docs/mcp) | Diff tools: declaration only |

### Read/write

- Official GraphQL documentation provides `issueCreate` and `issueUpdate` examples. [Getting started — GraphQL](https://linear.app/developers/graphql)
- Official MCP documentation lists supported objects. [MCP server](https://linear.app/docs/mcp)
  - Issues.
  - Projects.
  - Comments.
- Historical declarations provide `get_issue` and `list_issues`.
- `save_issue` supports issue creation and updates.
- `save_comment` supports comment creation and updates.
- The observed operations read back the updated status, description, and comment.

### Parent relationships

- The product supports setting and removing a parent. [Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues)
- Teams can configure parent/sub-issue auto-close. [Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues)
- API `IssueCreateInput` and `IssueUpdateInput` declare `parentId`. [Official schema — IssueUpdateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L22348)
- Historical tool declarations:
  - `save_issue.parentId` accepts a string or null.
  - `list_issues.parentId` filters sub-issues.
- Operational evidence:
  - Read back the tested issue’s parent.
  - Queried the same parent and listed four sub-issues.

### Dependencies

- Product relationship semantics: [Issue relations](https://linear.app/docs/issue-relations)
  - Blocking means this work prevents another item from proceeding.
  - Blocked means another item prevents this work from proceeding.
  - Related means associated work.
  - Duplicate means duplicate work.
- The API supports `issueRelationCreate` and `issueRelationDelete`. [Official schema — IssueRelationCreateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L20623)
- Historical tool declarations:
  - `get_issue(includeRelations=true)` reads relationships.
  - `save_issue.blocks` specifies blocked work.
  - `save_issue.blockedBy` specifies prerequisites.
  - `save_issue.relatedTo` specifies related work.
  - `duplicateOf` specifies the duplicated issue.
  - `removeBlocks` removes specified blocks relationships.
  - `removeBlockedBy` removes specified blockedBy relationships.
  - `removeRelatedTo` removes specified related relationships.
- The observed operations read back parent and blockedBy relationships.
- Before adopting relationship writes, use an authorized object to establish whether arrays append or replace.

### Documents

- The product supports collaborative editing and version history. [Documents](https://linear.app/docs/documents)
- A Document can belong to the following objects. [Documents](https://linear.app/docs/documents)
  - Project.
  - Initiative.
  - Team.
  - Issue.
  - Cycle.
- The API provides `documentCreate` and `documentUpdate`. [Official schema — DocumentCreateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L10446)
  - Some parent fields are marked Internal.
  - Check support for the required parent against the deployed interface.
- Historical `save_document` declaration:
  - Creation requires a title and exactly one parent.
  - Updates can specify a new parent.
  - `patch` supports targeted content changes.
- The observed operations queried a Project’s document list.
- Attachment delivery follows a separate workflow; see “Attachment delivery” below.

### Pagination

- The API uses Relay cursors. [Pagination](https://linear.app/developers/pagination)
  - Use `first` and `after` for subsequent pages.
  - Use `last` and `before` for backward queries.
  - `pageInfo.hasNextPage` and `endCursor` provide continuation information.
  - The default page size is 50.
- Historical list tool declarations:
  - `list_issues` provides `cursor` and `limit`.
  - `list_comments` provides the same pagination fields.
  - `list_documents` provides the same pagination fields.
  - `limit` defaults to 50, with a maximum of 250.
- Paginated responses expose `hasNextPage` and `cursor` at the top level.
- Assess completeness by exhausting pagination and comparing IDs.

### GitHub PR status sync

- Official documentation supports PR links and Team status mappings. [GitHub](https://linear.app/docs/github)
- Historical tool declarations:
  - `get_diff` accepts a GitHub PR URL.
  - `merge_diff` provides a merge method.
  - `save_issue.links` adds links.
- Sync capability depends on GitHub App installation and workflow configuration.
- See “GitHub adoption conditions” below.

## Permissions, plans, and identity

### Access permissions

- Personal API keys can restrict permissions and Teams. [API and Webhooks](https://linear.app/docs/api-and-webhooks)
  - Read.
  - Write.
  - Admin.
  - Create issues.
  - Create comments.
  - Admins can control whether Members can create keys.
- OAuth scopes control separate capabilities. [OAuth 2.0 authentication](https://linear.app/developers/oauth-2-0-authentication)
  - `read`.
  - `write`.
  - `issues:create`.
  - `comments:create`.
  - `admin`.
- A successful read establishes access only for that operation.
- Confirm the corresponding scopes and object permissions before accessing another Team or writing.

### MCP and Agent identity

- The MCP endpoint affects the tool set. [MCP server](https://linear.app/docs/mcp)
  - `/mcp/readonly` exposes only read tools.
  - Standard `/mcp` can use read scope or a restricted key.
  - Streamable HTTP is the primary transport.
  - SSE is a deprecated fallback.
- The default OAuth actor is user. [OAuth 2.0 authentication](https://linear.app/developers/oauth-2-0-authentication)
- `actor=app` uses app identity. [OAuth actor authorization](https://linear.app/developers/oauth-actor-authorization)
  - App installation requires an Admin.
  - `actor=app` cannot request admin scope.
- Native Agent delegate and mention scopes are separate. [Agents — Getting Started](https://linear.app/developers/agents)
  - App access can be changed or revoked.
  - The `save_issue.delegate` declaration establishes only a setting interface.
  - Agent session creation and lifecycle use the separate native Agent API.
  - The documentation was marked Developer Preview on 2026-09-12.
- Identity observations from the session:
  - `get_user(query="me")` returned the signed-in user.
  - `isAdmin=true`.
  - `isGuest=false`.
  - The comment author matched the signed-in user, with `onBehalfOf=null`.
  - These results support conclusions about the displayed identity.

### Plans and administration

- Third-party app approvals can be enabled on paid plans. [Third-Party App Approvals](https://linear.app/docs/third-party-application-approvals)
  - Workspace owners manage them on Enterprise.
  - Admins manage them on other paid plans.
- Free plan allowances shown on Pricing on 2026-09-12: [Pricing](https://linear.app/pricing)
  - 2 Teams.
  - 250 issues.
  - 10MB file uploads.
- Basic and above list unlimited issues and file uploads. [Pricing](https://linear.app/pricing)
- Business provides private teams and guests. [Pricing](https://linear.app/pricing)
- Uploads remain subject to each interface’s per-file limits.
- The Pricing text extraction retained API and MCP comparison rows but omitted per-plan checkmarks.
  - Check the target plan and actual access directly before adoption.
- GitHub installation permissions: [GitHub](https://linear.app/docs/github)
  - Organization-level installation requires a GitHub organization owner.
  - A repository administrator can install at repository level.
  - The integration requires repository read/write and other read permissions.
  - GitHub Enterprise options require Linear Enterprise.

## Interface boundaries for writes, pagination, and recovery

- GraphQL can return partial data alongside `errors`. [Getting started — GraphQL](https://linear.app/developers/graphql)
  - Inspect mutation results even with HTTP 200.
  - Read back the required fields to confirm the write.
- Historical `save_document.patch` declares sequential, atomic application.
  - Failure of any operation aborts the entire save.
  - Anchors must match uniquely by default.
  - `replace_all` can change replacement behavior.
  - Atomicity applies only to that save.
- Historical `save_issue` declares neither version preconditions nor an idempotency key.
  - `updatedAt` can support readback comparisons.
  - The [multi-Agent coordination guide](../skills/linear-handbook/references/multi-agent-coordination.md) reduces conflicts through coordination and readback.
  - These steps do not guarantee atomic exclusion.
- Default official API request allowances: [Rate limiting](https://linear.app/developers/rate-limiting)
  - API keys: 2,500 requests per user per hour.
  - OAuth Apps: 5,000 requests per user or App User per hour.
  - Endpoints and complexity have separate limits.
- API headers expose remaining allowance and reset information. [Rate limiting](https://linear.app/developers/rate-limiting)
  - The observed MCP responses did not include these headers, so remaining allowance could not be read from them.
  - Base recovery waits on the actual error and available reset information.

Operation sequence:

1. Read the issue and all prerequisite statuses.
2. Select the fields to change.
3. Keep filters and ordering consistent across pages.
4. Save each cursor until `hasNextPage=false`.
5. Deduplicate by issue ID.
6. Requery necessary objects in changing result sets, or supplement with an `updatedAt` filter.
7. Read back target fields and required relationships after writing.
8. On timeout or incomplete results, check whether the operation succeeded before retrying.
9. Complete the bytes PUT before creating the attachment row, retaining results from each stage.

## GitHub adoption conditions

The following conditions come from official documentation read on 2026-09-12. [GitHub](https://linear.app/docs/github)

- Team Pull request and commit automations determine status mappings.
  - Rules can vary by target branch.
- Magic words determine the purpose of a PR relationship.
  - Closing can trigger the post-merge status.
  - Non-closing retains other workflow updates but does not apply the merge status.
  - Relation only creates a relationship.
- When one issue has multiple PRs, wait for the last relevant PR to reach the required state.
- Ready for merge depends on:
  - GitHub mergeability and check results.
  - Review automation.
  - Branch protection.
- Canceling or marking duplicate may close certain linked PRs.
  - Read relationships and confirm side effects before acting.
- GitHub Issues Sync requires separate configuration.
  - Confirm one-way or bidirectional sync.
  - Confirm Team/repo mapping.
  - Confirm the synced thread.

Record environment settings before adoption:

- GitHub host.
- Repos with the App installed.
- Linear Team.
- Event-to-status mappings.
- PR relationship type.
- Representative PR and expected events.

Use authorized representative work to observe the required PR stages, then read back both PR and issue states.
Confirm deployment and acceptance independently through their result evidence.

## Observed operations and verification

Operation date: 2026-09-12.

- Issue write and readback.
  - Updated the tested issue’s status and body with `save_issue`.
  - Read back In Progress and the full body with `get_issue`.
  - Native issue mentions were preserved.
  - Paragraphs and checkboxes were preserved.
- Parent and dependency reads.
  - Used `get_issue` with `includeRelations` to read the tested issue’s parent.
  - `blockedBy` contained one prerequisite issue.
  - Read that prerequisite separately and confirmed its status was Done.
- Four-page cursor pagination.
  - Filtered sub-issues by the same parent with `limit=1` and `orderBy="createdAt"`.
  - Passed each returned cursor to retrieve four distinct sub-issues.
  - The final response returned `hasNextPage=false`.
  - Queried again with `limit=250` and confirmed the same four IDs.
  - All four belonged to the specified parent.
- Document list and comments.
  - Queried documents for the tested Project with `limit=1`; the result was an empty array.
  - `hasNextPage=false`.
  - Created an initial investigation comment with `save_comment`.
  - Read back its content and author with `list_comments`.
- Attachment delivery.
  1. Obtained upload locations for two artifacts.
  2. Uploaded file bytes; both PUTs returned HTTP 200.
  3. Created attachment records.
  4. Downloaded the attachments and confirmed their SHA-256 hashes matched the local files at that time.
  - The capability document was then 17,849 bytes.
  - The tool declaration snapshot was 21,851 bytes.

Difference found in parent and dependency reads:

- Official Issue relations documentation says a resolved blocker moves to Related in the UI. [Issue relations](https://linear.app/docs/issue-relations)
- The tool output still listed the completed prerequisite in `blockedBy`.
- Read prerequisite statuses and deliverables before taking over; `blockedBy` alone cannot determine whether work is blocked.

## Open questions and handoff

- Environment inventory.
  - Confirm token scopes.
  - Confirm the target plan and remaining allowance.
  - Confirm GitHub App installation and sync settings.
- Relationship writes.
  - Establish append-versus-replace semantics with authorized objects.
  - Check auto-close settings before clearing a parent.
  - Read back both ends after writing a relationship.
- Document writes.
  - Confirm support for the required parent.
  - Use a reversible patch to check success and failure behavior.
- Tool updates.
  - Compare declarations in a new session.
  - Include transaction scope and retry behavior in recovery design.

Follow-up protocol entry points:

- [Claiming and handoff](../skills/linear-handbook/references/multi-agent-coordination.md): use identity and prerequisite-state evidence.
- [Tool recovery](../skills/linear-handbook/references/tool-recovery.md): use write readback and upload stages.
- [Authorization and operating boundaries](../skills/linear-handbook/references/agent-boundaries.md): use permission and identity boundaries.
- [Skill architecture](../design/skill-architecture.md): account for tool capability differences in environment adaptation.

## Sources

All publishers are Linear; all sources were read on 2026-09-12.
API schema references use a fixed commit; other links point to official product or developer documentation.

- [API and Webhooks](https://linear.app/docs/api-and-webhooks).
  - API: reading and writing data.
  - API Keys: permission scopes.
  - API Keys: Team restrictions and administrative permissions.
- [Getting started — GraphQL](https://linear.app/developers/graphql).
  - Endpoint and Authentication: API requests.
  - Error handling: partial data and errors can coexist.
  - Creating & Editing Issues: issueCreate and issueUpdate examples.
- [MCP server](https://linear.app/docs/mcp).
  - General: MCP endpoints and transport.
  - FAQ: read-only access.
  - Common use cases: supported objects and parent/sub-issue use cases.
  - Actual tool declarations determine field contracts.
- [Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues).
  - Create a sub-issue: creating parent relationships.
  - Status automation: automatic completion settings.
  - Converting issues: parent/sub-issue conversion.
- [Issue relations](https://linear.app/docs/issue-relations).
  - Related issues: semantics of related work.
  - Blocked / blocking: blocking relationships and UI display.
  - Duplicate: duplicate-work semantics.
  - “Observed operations and verification” above records the difference between tool output and the UI description.
- [Documents](https://linear.app/docs/documents).
  - Page introduction: supported document parents.
  - Edit documents: collaborative editing.
  - Version history: version records.
- [Pagination](https://linear.app/developers/pagination).
  - Page introduction: Relay cursors.
  - orderBy example: query order.
  - Default page size: 50 records.
- [GitHub](https://linear.app/docs/github).
  - Permissions: GitHub installation permissions.
  - GitHub Enterprise options: plan requirements.
  - Magic words: PR relationship types.
  - Link multiple issues: linking multiple work items.
  - Workflow automation: status mappings.
  - Configure GitHub Issues Sync: issue sync configuration.
- [OAuth 2.0 authentication](https://linear.app/developers/oauth-2-0-authentication).
  - Redirect user access requests to Linear: OAuth scopes.
  - Actor parameter: default user identity.
- [OAuth actor authorization](https://linear.app/developers/oauth-actor-authorization).
  - Page introduction: user and app identities.
- [Agents — Getting Started](https://linear.app/developers/agents).
  - Developer Preview: the documentation’s maturity label at the time.
  - Actor and scopes: native Agent authorization.
  - Management: App access management.
  - Agent session lifecycle: native Agent session boundaries.
- [Third-Party App Approvals](https://linear.app/docs/third-party-application-approvals).
  - Page introduction: paid-plan requirements.
  - Configure: approval settings and administrative roles.
- [Official schema — IssueUpdateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L22348).
  - L22348 IssueUpdateInput: parentId.
  - L22348 IssueUpdateInput: delegateId.
  - Same file, L18598 IssueCreateInput: creation fields.
- [Official schema — IssueRelationCreateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L20623).
  - L20623 IssueRelationCreateInput: issueId.
  - L20623 IssueRelationCreateInput: relatedIssueId.
  - L20623 IssueRelationCreateInput: type.
  - Same file, L26109: relation creation mutation.
  - Same file, L26122: relation deletion mutation.
- [Official schema — DocumentCreateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L10446).
  - L10446 DocumentCreateInput: content and parent fields.
  - L10446 DocumentCreateInput: Internal annotations.
  - Same file, L24335: documentCreate.
  - Same file, L24362: documentUpdate.
- [Pricing](https://linear.app/pricing).
  - Plan summaries: Team and issue allowances.
  - File upload: upload conditions.
  - API and webhook access: API comparison row.
  - MCP access: MCP comparison row.
  - The text extraction omitted per-plan checkmarks.
- [Rate limiting](https://linear.app/developers/rate-limiting).
  - API request limits: hourly allowances.
  - Query- and mutation-specific request limits: operation-specific allowances.
  - Complexity limits: complexity restrictions.
  - Response headers: remaining allowance and reset.
