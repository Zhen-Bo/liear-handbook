# Write verification and tool recovery

Help Agents identify completed operations when results are incomplete and continue from confirmed progress.
Applies to individual developers and multiple Agents using Linear.

- For work claims and concurrency conflicts, see [Multi-Agent coordination](multi-agent-coordination.md).
- For authorization and sensitive information, see [Agent boundaries](agent-boundaries.md).
- For interface capabilities and verification methods, see [Tool capability research](agent-tool-capabilities.md).

The recovery steps in this document are recommended procedures.
Official feature facts have separate sources.
Confirm connector fields against current declarations.

## Outcome classification

| Judgment | Required evidence | Next step |
| --- | --- | --- |
| Confirmed success | Readback by target ID shows required fields match this operation's expectations | Save evidence and continue |
| Confirmed failure | Explicit rejection or evidence of nonapplication, with success of other steps ruled out | Fix the cause, then decide whether to retry |
| Unknown outcome | Timeout, disconnection, or missing required response prevents confirming application | Verify remote effects and pause writes depending on the result |
| Partial success | At least one step is confirmed successful; other steps failed or remain unknown | Check each step and recover only unfinished steps |

HTTP 200 is insufficient to establish GraphQL success.
The official API may return both data and `errors`.
Check error paths and required fields.[Getting started](https://linear.app/developers/graphql)
If a connector does not expose HTTP or GraphQL details, use available tool errors and object readback results without guessing missing fields.

Work completion requires meeting the issue's acceptance criteria.
Do not describe failed or unknown outcomes as complete or use Done to hide steps awaiting recovery.

## Prepare before writing

1. Read the authorized operational scope.
2. Inspect the latest declarations of actually callable tools.
3. Read the target object by known ID.
4. Compare the returned workspace and Team.
5. Compare the object's purpose and parent or Project placement.
6. Read the latest fields this operation will modify.
7. Preserve this operation's changes.
8. List success conditions that can be read back for each write step.

Names are only for finding candidate objects.
If names collide or scope differs, stop that write and obtain the correct ID.
Official API issue operations support UUIDs or issue identifiers; handle other objects according to each interface contract.[Getting started](https://linear.app/developers/graphql)

For work that may be interrupted, save a recovery record where the next session can read it:

- Operation identifier: stable identifier for this work and step.
- Target: resolved object ID.
- Expectation: field values or content changes intended by this operation.
- Baseline: read time and remote `updatedAt`, when available.
- Progress: last confirmed successful step.
- Response: obtained new object ID.
- Error: error code and reason with sensitive information removed.
- Verification: readback result and time.
- Recovery: next executable action.

Short-lived signed URLs are not permanent deliverable entry points.
Recovery records do not store tokens or signatures.
Obtain a fresh valid URL when file access is needed.

## Deduplicate before creating

1. If the target ID is already known, read that object directly.
2. Without an ID, search the correct scope for candidates serving the same purpose.
3. Complete necessary queries using "Complete pagination".
4. Read candidate bodies and check their goals.
5. When the same work exists, reuse the confirmed ID.
6. If multiple candidates cannot be distinguished, stop creation and clarify correspondence.
7. After confirming an initial creation is necessary, save the operation identifier and query scope before submitting it.
8. Save the returned ID immediately and read back by that ID.

Identical titles do not imply identical work.
A search miss also does not prove absence; visibility permissions or search scope may affect results.
Official API pagination hides archived data by default.
Include archived data when needed for deduplication; confirm connector parameters separately.[Getting started](https://linear.app/developers/graphql)

A deduplication identifier only assists investigation.
Without an explicit interface contract, it is neither a server-side idempotency key nor a uniqueness constraint.
Deduplication before the first creation also cannot prevent another Agent from creating simultaneously.
Complete claims according to the coordination protocol.

## Updates and readback

1. Reread the target before updating.
2. Compare it with the saved baseline.
3. If someone changed the same content, merge differences or resolve the conflict using the coordination protocol.
4. Submit only the necessary changes for this operation.
5. Check the tool response for errors.
6. Read back required fields by target ID.
7. For content writes, check the full text, preserving list hierarchy and link semantics.
8. For relationship changes, read both ends as needed and confirm direction.
9. Once readback matches, record the step as confirmed successful.

When writing a full description, incorporate others' additions into the latest version.
When using patch, check that the anchor still matches current content.
Before patching, inspect the current tool's version conditions, idempotency, and failure contract.
Without an explicit contract, do not assume a write is safe to replay.
Neither a prewrite comparison nor a patch guarantees freedom from races between writes.

If readback fails, classify the write outcome as unknown and retry reading.
If readback differs from expectations, first identify differences caused by platform formatting normalization or other writes.
If conflicts persist, stop writing that field and hand off the latest remote content and this operation's changes to avoid repeated overwrites.

## Complete pagination

Official GraphQL uses `first/after`; the next page comes from `pageInfo.endCursor`, and `hasNextPage` determines whether to continue.[Pagination](https://linear.app/developers/pagination)
Check list parameters and response structure for each connector tool.

1. Save complete filters and ordering settings.
2. Read the first page and check response completeness.
3. Deduplicate by object ID and save this page's results.
4. Save the successful page's next-page cursor.
5. When another page exists, continue with the original query conditions and returned cursor.
6. Mark the query fully traversed only after explicitly reading that no next page exists.
7. If data may change during the query, reread candidate targets or data updated during that interval.

- Intermediate page timeout.
  1. Reread the failed page using the last successful page's next-page cursor.
  2. Merge results by ID.
- Invalid cursor.
  1. Restart from the first page with the same conditions.
  2. Deduplicate against existing IDs.
- Repeated or nonadvancing cursor.
  1. Stop the loop and preserve the abnormal response.
  2. Retry the query once.
  3. If still abnormal, hand off the query gap.
- Next page indicated but cursor missing.
  1. Classify the query as incomplete.
  2. Reread that page.
  3. If still missing, stop operations requiring the complete set.
- Empty page with another page indicated.
  1. Check that the cursor is valid and advances.
  2. Continue querying; an empty page does not establish the end.
- Insufficient permissions.
  1. Recover using "Insufficient permissions".
  2. Preserve visibility gaps; do not treat invisible data as absent.

Traversing every page does not produce a snapshot from one instant.
When continuously changing data prevents stable comparison, preserve the query interval and gaps without claiming a complete export.

## Timeouts and connection failures

### Unknown creation outcome

1. Pause creation retries.
2. Check whether the original request is still running and obtain any available final response.
3. If an ID was returned, read directly by ID.
4. Without an ID, list candidates in the original creation scope and traverse all necessary pages.
5. Narrow candidates using the operation identifier and creation time.
6. Check each candidate's target content and placement.
7. When a created object is found, save its ID and continue from the next step.
8. With multiple candidates, stop creation and hand off duplicate objects for judgment.
9. If still not found, perform one supplementary check using a delayed read or an authorized direct object list.
10. If creation cannot be ruled out, preserve "unknown outcome" and hand off verification.

Resubmit the same creation intent only with explicit evidence of nonapplication or a verifiable safe-replay contract from the interface.
Do not recreate solely because search found no match.
Adding comments and creating attachment rows follow the same rule.

### Unknown update outcome

1. Read the latest fields by the original target ID.
2. If expectations are met, record success without resubmitting.
3. If fields match the baseline and nonapplication can be confirmed, recheck authorization and current content, then retry necessary changes.
4. If fields differ from both baseline and expectations, handle an update conflict.
5. If reading remains impossible, save the unknown state and stop dependent operations.

Appending comments or producing non-idempotent side effects cannot use the ordinary field-rewrite strategy.
Server 5xx responses or connector interruptions do not automatically prove a mutation did not execute.

## Rate limiting

Official GraphQL represents rate limiting with HTTP 400 and `RATELIMITED` in `errors`.[Rate limiting](https://linear.app/developers/rate-limiting)
API request and complexity quotas have separate reset headers.
Specific endpoints may also have independent limits.[Rate limiting](https://linear.app/developers/rate-limiting)
A connector may transform error formats; inspect actual responses instead of checking only HTTP 429.

1. Pause subsequent requests using the same credentials, including verification reads.
2. Save completed steps and cursors.
3. If a usable reset time is returned, convert its units and wait until the relevant limit clears.
4. If reset information is missing, use a bounded number of backoff attempts.
5. After resumption, first verify the last write's outcome.
6. Continue from the unfinished step.

Prefer the environment's existing backoff policy.
Without one, use these adjustable recommended values, adding a random delay of 0–5 seconds each time:

1. Wait 5 seconds on the first attempt.
2. Wait 15 seconds on the second attempt.
3. Wait 30 seconds on the third attempt.

If still limited after three consecutive attempts, save progress and hand off to a later scheduled run or someone who can manage the connection.
These values are procedure recommendations, not reset times guaranteed by Linear.

If a single query's complexity is too high, reduce required fields or page size before retrying.
Waiting cannot fix a query that consistently exceeds the per-query complexity limit.[Rate limiting](https://linear.app/developers/rate-limiting)
Coordinate lower request volume when multiple Agents share the same user's API-key quota.
Replacing a key for the same user does not separate that quota.[Rate limiting](https://linear.app/developers/rate-limiting)

## Insufficient permissions and input errors

### Insufficient permissions

1. Save the sanitized error and target ID.
2. Confirm the current connection's identity and workspace.
3. Confirm the scope required by the operation.
4. Confirm the target object is visible to the connection.
5. For official MCP, check whether the connection uses the read-only endpoint.[MCP server](https://linear.app/docs/mcp)
6. Have someone authorized to manage the connection restore the necessary access.
7. After access is restored, first read the target's latest state.
8. Continue from an unfinished, authorized step.

OAuth read and write scopes are separate; creating issues and adding comments also have separate scopes.[OAuth 2.0 authentication](https://linear.app/developers/oauth-2-0-authentication)
A successful read does not establish write access.
When an object cannot be found, check its ID and visibility first; do not automatically create a substitute in another Team.
Do not elevate privileges or switch identities to bypass denial.

### Input or schema errors

1. Inspect current tool declarations and specific field errors.
2. Resolve the correct target ID again.
3. Correct necessary inputs using the latest content.
4. If an anchor mismatch caused the error, reread the full text before producing a patch.
5. Submit the corrected version only after confirming nonapplication.

When the same input is explicitly rejected by validation, retries do not replace correction.

## Partial success

1. Divide the overall operation into steps that can be read back.
2. Mark each step as successful, failed, or unknown.
3. Save new object IDs from successful steps.
4. Verify unknown steps.
5. Fix failure causes.
6. Execute only necessary unfinished steps.
7. Recheck overall acceptance criteria.

For example, an issue was created but relationship setup failed:

1. Read back the issue using the obtained ID.
2. Read current relationships.
3. Confirm the tool's append or replace semantics.
4. Add missing authorized relationships.
5. Read back both ends to confirm direction.

Cross-tool operations have no confirmed overall transaction guarantee.
Do not rerun the whole creation sequence because a later step failed, or automatically delete successful objects as rollback.
Check compensating operations separately for their effects and existing authorization.

### Attachment delivery

Use this procedure only when the current connector explicitly provides a prepare → raw PUT → attachment row protocol.
For a single-step upload interface, follow its contract and read back the file.
If upload capability is missing, preserve the local deliverable and concrete delivery requirements.

1. Save the local file size and SHA-256.
2. Prepare to obtain the upload request.
3. PUT the raw bytes using returned headers exactly.
4. After confirming PUT success, create the attachment row using assetUrl.
5. Save the attachment ID.
6. Read back the issue's attachments.
7. Download that attachment and compare size and SHA-256.

- Prepare succeeded; PUT explicitly failed or the URL expired.
  1. Prepare the same file again.
  2. Complete PUT using the new response.
- PUT outcome unknown.
  1. Pause finalize.
  2. Check whether the asset is readable and its bytes match.
  3. If upload success cannot be proved, prepare and PUT again.
  4. Record that the old asset may remain.
- PUT succeeded; finalize explicitly failed.
  1. Preserve the uploaded asset identifier.
  2. Fix the failure cause.
  3. Resume only attachment-row creation.
- Finalize outcome unknown.
  1. Read the target attachments.
  2. Locate candidates by the asset's stable path; an identical name alone does not establish success.
  3. Download and compare content.
- Download URL expired.
  1. Obtain a fresh download URL for that attachment ID.
- Downloaded content differs.
  1. Preserve failure evidence and stop claiming successful delivery.
  2. Confirm source bytes.
  3. Repair the attachment.

Confirm URL validity and headers from the current prepare response, processing each file as prepare → PUT → finalize.
A URL from prepare means only that uploading can begin.
A finalized row that has not been read back also does not establish completed file delivery.

## Sources

Verification date: 2026-09-13.
All official documents are published by Linear.

- [Getting started](https://linear.app/developers/graphql).
  - Error handling.
    - HTTP 200 may include partial data and errors.
  - Queries & Mutations.
    - Queries support object IDs.
  - Creating & Editing Issues.
    - Creation responses include the new issue ID.
  - Archived resources.
    - API pagination excludes archived data by default.
- [Pagination](https://linear.app/developers/pagination).
  - Relay cursor example.
    - `pageInfo` controls the next page.
  - `orderBy` example.
    - Sorting by `updatedAt` is supported.
- [Rate limiting](https://linear.app/developers/rate-limiting).
  - API request limits.
    - API keys for the same user share a quota.
    - Response headers provide reset information.
  - Query- and mutation-specific request limits.
    - Endpoints may have independent limits.
  - Complexity limits.
    - Complexity has its own quota.
  - Maximum complexity.
    - Queries consistently exceeding the per-query limit are rejected.
  - Handling rate limit errors.
    - GraphQL rate limiting returns HTTP 400.
    - The error code is `RATELIMITED`.
- [MCP server](https://linear.app/docs/mcp).
  - Setup → General.
    - The read-only endpoint exposes only read tools.
    - `read` scope restricts write access.
- [OAuth 2.0 authentication](https://linear.app/developers/oauth-2-0-authentication).
  - Redirect user access requests to Linear → scope.
    - Operations have separate scopes.
