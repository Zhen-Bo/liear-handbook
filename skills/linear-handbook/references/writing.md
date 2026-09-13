# Writing and body maintenance

Default to English and retain Linear terminology.
An explicitly specified user language, complete replacement version, or applicable policy takes precedence.

## Content selection

1. Assess whether each section helps readers understand the goal, judge the result, or take a specific action.
2. Remove purposeless content, repetition, and routine statements.
3. Arrange wording, headings, and list hierarchy for retained content.
4. Fix templates when the same unnecessary content recurs.
Add information back when a specific gap appears.

Retain necessary evidence, completion criteria, and actual problems.
Judge by whether readers can understand and act; do not set a deletion quota.

## Formatting

- Use names readers can understand and link sources directly to documents and sections.
- Use reader-accessible evidence in public content; private tracking IDs must not be a reading prerequisite.

- Break lines at complete units of meaning within a topic.
- Separate different topics with blank lines.
- Use `-` bullets for ordinary categories.
  - Each bullet expresses one independently understandable piece of information.
  - For a topic with multiple details, put the topic at the first level and individual details at the second.
  - Do not join independent points with semicolons, commas, or consecutive sentences.
  - Preserve necessary hierarchy when simplifying; do not compress multiple pieces of information into one sentence.
- Use numbered lists for ordinary conditions or ordered steps.
- Number completed items, with each item describing one delivered outcome.
- Use checkboxes for acceptance criteria.
  - When one acceptance item requires several actions, express the result in an outer checkbox and the steps in an inner numbered list.
- Provide an entry point for each file and related work item.
- Headings directly identify their topic.

```markdown
- [ ] The specified result holds.
  1. Obtain verification inputs.
  2. Perform the operation.
  3. Compare results and retain evidence.
```

## Issue body and comments

- Write for readers who did not participate in the discussion and provide the context needed to understand the goal and act.
- Turn abstract requests into concrete deliverables and observable acceptance results.
- Explain which output this work needs from each prerequisite link.
- Maintain common execution rules centrally instead of repeating them in every issue.
- When a capability is unavailable, directly explain how to continue execution, verification, and handoff.
  - Omit lists of causes that do not affect handling.
  - Describe workflows in terms of capabilities, without using a particular tool brand as shorthand for a limitation.

- The title directly expresses the expected outcome.
- The body is the authoritative entry point for currently effective work information.
  - Goal and scope.
  - Adopted conclusions.
  - Delivered outputs and verification links.
  - Open questions still affecting operations.
- Update the body when new information or important decisions emerge.
  - Replace superseded approaches.
  - List unresolved questions separately.
- Comments retain new findings, decision reasons, or outputs.
  - Link the body to the corresponding discussion when traceability is needed.
  - Do not post a separate comment merely to announce starting or waiting.
- The Project description retains shared delivery scope.
- A Project update summarizes changes affecting the overall commitment.

## Evidence and output links

- Use precise verbs such as "reviewed", "compared", and "tested".
- Limit conclusions to the scope supported by evidence.
- Work records describe only work actually performed.
  - Unmentioned work is not implied complete.
  - Do not add a statement for each action not performed.
  - When actual differences or blockers affect assessment, explain their specific impact.
- Attach source locations to research findings.
  - Put the verification date on its own line.
  - Use "Initial investigation" as a heading for early exploration.
- Use fixed-version permalinks for code evidence.
- Use native issue mentions when referring to related issues in Linear.
  - Use native UI selection or the mention format supported by the current tool.
  - Build mentions from actual target IDs and URLs; do not invent IDs.
  - Explain the relationship or supported conclusion beside the mention.
  - Read back after writing to verify the target and meaning.
- Provide accessible entry points for remote outputs.
  - Locate attachments using a stable issue page and attachment name.
  - Do not use signed download URLs as permanent entry points.

## Completion and feedback

1. Assess closure against the currently effective completion criteria.
2. Add usable output and verification links.
3. Divide completion records into result summary, completed items, verification results, and next steps, retaining only sections with content.
4. Describe concrete actions directly in next steps and link to the corresponding work.

When the user supplies a complete replacement version, preserve its content and structure.
Platform normalization of Markdown is acceptable, but read back to verify line breaks, links, and list meaning.
Apply corrections only within their relevant scope; do not turn a single case into permanent policy.

Handle body updates and notifications separately.
Authorized notifications must explain the requested action and context.
Express assignee responsibility separately from review requests.
