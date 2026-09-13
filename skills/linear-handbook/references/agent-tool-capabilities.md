# Linear API, MCP, and GitHub integration capabilities

Official documentation verification date: 2026-09-12.
Pinned API schema: `23f11eb41ef63ba219ec582911079c19d1abbf62`.
This document preserves the scope of official evidence; check the current interface before operating.

## Evidence levels

- Official product documentation supports features and usage conditions.
- The API schema supports field declarations at the pinned version.
- The current tool schema determines which parameters can be sent in this operation.
- Actual readback supports only that account, object, and operation.

## Capability matrix

- Issue and comment reading and writing
  - Official basis
    - API queries/mutations: [Getting started — GraphQL](https://linear.app/developers/graphql).
    - MCP use cases: [MCP server](https://linear.app/docs/mcp).
  - Confirm before operating
    - Creation tool.
    - Update tool.
    - Readback tool.

- Parent
  - Official basis
    - Parent feature: [Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues).
    - parentId schema: [Official schema — IssueUpdateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L22348).
  - Confirm before operating
    - Parent creation field.
    - Parent removal method.
    - Child-query method.

- Dependencies
  - Official basis
    - Blocking, Related, and Duplicate: [Issue relations](https://linear.app/docs/issue-relations).
    - Relation mutation: [Official schema — IssueRelationCreateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L20623).
  - Confirm before operating
    - Relationship direction.
    - Append or replace semantics.

- Document
  - Official basis
    - Document placement: [Documents](https://linear.app/docs/documents).
    - Document mutation: [Official schema — DocumentCreateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L10446).
  - Confirm before operating
    - Supported parent types.
    - Patch contract.
    - Readback method.

- Pagination
  - Official basis: GraphQL Relay cursor, [Pagination](https://linear.app/developers/pagination).
  - Confirm before operating: each tool's page parameters and response locations.

- GitHub
  - Official basis: Team PR status mapping, [GitHub](https://linear.app/docs/github).
  - Confirm before operating
    - App installation.
    - PR relationship type.
    - Workflow.

### Parent-child relationships and dependencies

- Team settings configure parent/sub-issue automatic closure.[Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues)
- IssueCreateInput and IssueUpdateInput in the pinned schema include parentId.[Official schema — IssueUpdateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L22348)
- The API supports creating and deleting relations.[Official schema — IssueRelationCreateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L20623)
- Read each prerequisite's current status and deliverable.
  - A relationship list is not a completion criterion.
  - For canceled or duplicate work, follow through to the replacement deliverable.
- Read back both ends after relationship writes, checking direction and preserved relationships.

### Documents

- Document parent types listed in product documentation: [Documents](https://linear.app/docs/documents).
  - Project.
  - Initiative.
  - Team.
  - Issue.
  - Cycle.
- Some parent fields in the pinned schema are marked Internal.[Official schema — DocumentCreateInput](https://github.com/linear/linear/blob/23f11eb41ef63ba219ec582911079c19d1abbf62/packages/sdk/src/schema.graphql#L10446)
- Confirm required placement using the current interface; product documentation alone cannot establish connector support.
- Check available operations separately for document restoration and reassignment.
- For attachments, select the applicable protocol under [Attachment delivery in tool recovery](tool-recovery.md#attachment-delivery).

### Pagination

- GraphQL uses first/after and pageInfo.endCursor.[Pagination](https://linear.app/developers/pagination)
- hasNextPage determines whether another page remains.[Pagination](https://linear.app/developers/pagination)
- Connectors may use different fields; inspect each tool's schema and actual responses.
- Preserve filters and ordering, save the cursor, and deduplicate by ID.
- Even after reading the full list, reread selected targets; the list is not a snapshot from a single instant.

## Permissions, plans, and identities

- API keys can restrict operations and Teams.[API and Webhooks](https://linear.app/docs/api-and-webhooks)
- OAuth separates scopes: [OAuth 2.0 authentication](https://linear.app/developers/oauth-2-0-authentication).
  - read.
  - write.
  - issues:create.
  - comments:create.
  - admin.
- A successful read does not guarantee writing or access to another Team.
- The official MCP read-only endpoint exposes only read tools.[MCP server](https://linear.app/docs/mcp)
- OAuth user and actor=app are different identities.[OAuth 2.0 authentication](https://linear.app/developers/oauth-2-0-authentication)[OAuth actor authorization](https://linear.app/developers/oauth-actor-authorization)
- Native Agent delegation and session lifecycle have separate interfaces.[Agents — Getting Started](https://linear.app/developers/agents)
  - A Delegate field does not mean an external MCP connection automatically becomes a native Agent.
  - Confirm connection identity and Team access before operating.
- Confirm plans and App approvals in the target environment.[Third-Party App Approvals](https://linear.app/docs/third-party-application-approvals)[Pricing](https://linear.app/pricing)
  - When extracted plan-comparison text lacks checkmark states, do not infer availability on every plan.
  - Uploads also require checking the current interface's per-file limit.

## Interface boundaries for writes, pagination, and recovery

1. Inspect the current tool's version conditions, patch, idempotency, and transaction scope.
2. Do not infer undeclared guarantees.
3. GraphQL responses can include both data and errors; HTTP 200 alone does not prove success.[Getting started — GraphQL](https://linear.app/developers/graphql)
4. Reading updatedAt can reveal changes but is not a server-enforced version condition.
5. Even if a single patch has an atomic contract, do not extend it to cross-tool transactions or exclusive claims.
6. Strict exclusivity requires a verified scheduling mechanism that rejects a second executor and removes the previous executor's write capability.
7. When the outcome is unknown, inspect remote effects first and recover using [tool-recovery](tool-recovery.md).

API headers provide quotas and reset times.
Requests, endpoints, and complexity may each have limits.[Rate limiting](https://linear.app/developers/rate-limiting)
A connector may not expose headers; use bounded backoff based on actual responses.
Coordinate request volume when multiple Agents share a quota.

## GitHub adoption conditions

The following conditions are supported by official documentation reviewed on 2026-09-12.[GitHub](https://linear.app/docs/github)

- Team PR/commit automations determine status mapping.
- The target branch may affect rules.
- Closing relationships can trigger merge status.
- Non-closing relationships retain other workflow updates but do not apply merge status.
- Relation creates only a relationship.
- For multiple PRs, check status against official multiple-link rules and current settings.
- Ready for merge also requires checking
  - Checks.
  - Review.
  - Branch protection.
- Confirm GitHub Issues Sync direction and Team/repo mapping separately.
- Before cancellation or marking duplicate, check [Platform behavior in the issue lifecycle](issue-lifecycle.md#platform-behavior).

Record before adoption:

- GitHub host.
- Repository where the App is installed.
- Linear Team.
- Event-to-status mapping.
- PR relationship type.
- Representative event and expected result.

Use authorized representative work to read back the required PR and issue stages.
Merging supplies integration evidence.
Judge deployment and deliverable acceptance using their own evidence.

## Sources

All publishers are Linear; all sources were reviewed on 2026-09-12.
API schema references use a pinned commit; other references point to official product or developer documentation.

- [API and Webhooks](https://linear.app/docs/api-and-webhooks).
  - API: reading and writing data.
  - API Keys: permission scope.
  - API Keys: Team restrictions and administrative permissions.
- [Getting started — GraphQL](https://linear.app/developers/graphql).
  - Endpoint and Authentication: API request method.
  - Error handling: partial data and errors may coexist.
  - Creating & Editing Issues: issueCreate and issueUpdate examples.
- [MCP server](https://linear.app/docs/mcp).
  - General: MCP endpoint and transport.
  - FAQ: read-only access methods.
  - Common use cases: supported objects and parent-child examples.
  - Actual tool declarations govern field contracts.
- [Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues).
  - Create a sub-issue: creating parent-child relationships.
  - Status automation: automatic completion settings.
  - Converting issues: parent-child conversion.
- [Issue relations](https://linear.app/docs/issue-relations).
  - Related issues: related-work semantics.
  - Blocked / blocking: blocking relationships and UI display.
  - Duplicate: duplicate-work semantics.
- [Documents](https://linear.app/docs/documents).
  - Page introduction: possible document parents.
  - Edit documents: collaborative editing.
  - Version history: version records.
- [Pagination](https://linear.app/developers/pagination).
  - Page introduction: Relay cursor.
  - orderBy example: query ordering.
  - Default page size: 50 records.
- [GitHub](https://linear.app/docs/github).
  - Permissions: GitHub installation permissions.
  - GitHub Enterprise options: plan requirements.
  - Magic words: PR relationship types.
  - Link multiple issues: linking multiple work items.
  - Workflow automation: status mapping.
  - Configure GitHub Issues Sync: issue synchronization setup.
- [OAuth 2.0 authentication](https://linear.app/developers/oauth-2-0-authentication).
  - Redirect user access requests to Linear: OAuth scopes.
  - Actor parameter: default user identity.
- [OAuth actor authorization](https://linear.app/developers/oauth-actor-authorization).
  - Page introduction: user and app operation identities.
- [Agents — Getting Started](https://linear.app/developers/agents).
  - Developer Preview: maturity label in the reviewed documentation.
  - Actor and scopes: native Agent authorization.
  - Management: App access management.
  - Agent session lifecycle: native Agent session boundaries.
- [Third-Party App Approvals](https://linear.app/docs/third-party-application-approvals).
  - Page introduction: paid-plan conditions.
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
  - Plan summary: Team and issue quotas.
  - File upload: upload conditions.
  - API and webhook access: API access comparison row.
  - MCP access: MCP access comparison row.
  - The text extraction at review time lacked per-plan checkmark states.
- [Rate limiting](https://linear.app/developers/rate-limiting).
  - API request limits: hourly request quota.
  - Query- and mutation-specific request limits: operation-specific quotas.
  - Complexity limits: complexity restrictions.
  - Response headers: remaining quota and reset.
