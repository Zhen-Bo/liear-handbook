# linear-handbook project conventions

The first version serves individual developers working with multiple Agents, using English and preserving Linear's terminology.

## Required writing format

These conventions apply to Linear project descriptions, issue bodies, comments, documents, the handbook, and templates maintained in this project.
They capture the user's explicit corrections to project descriptions and issue bodies and carry forward across sessions.

- Break lines by meaning: complete thoughts within a topic may start on separate lines. Separate topics with blank lines instead of packing multiple sentences into one paragraph.
- Use `-` bullet points for categories and parallel items. Each point expresses one independently understandable idea.
- Split lists by information unit. Do not join multiple points with semicolons, commas, or consecutive sentences.
- When a topic contains several details, state the topic at the first level and list its details at the second level.
- List files, deliverable entry points, and related issues individually so readers can locate each item.
- When shortening content, remove unnecessary information and preserve useful list hierarchy instead of compressing several items into one sentence.
- Use numbered lists such as `1.` and `2.` for ordinary condition lists or ordered steps.
- Use numbered lists for completed work, with one delivered result per item.
- Use `- [ ]` checkboxes for acceptance criteria. This rule takes precedence over the general rule for condition lists.
- Use native Linear issue mentions when referring to related issues in Linear so their status is visible.
- If one acceptance item requires multiple steps, use a checkbox for the result and a nested numbered list for the verification steps.
- When the user supplies a complete replacement, preserve its content and structure. Platform normalization of Markdown is acceptable, but read back the result to confirm line breaks, links, and list meaning.

Example of an acceptance item with multiple steps:

```markdown
- [ ] check 1
  1. step1
  2. step2
  3. ...
```

## Content selection and work records

Describe capability constraints as general situations and choose the approach based on available tools and authorization.
When a capability is unavailable, explain how to continue, verify, and hand off the work.
Omit lists of causes that do not affect the response.
Do not use a particular harness or package as shorthand for a capability constraint in workflows or examples.

First decide whether content needs to exist, then decide how to write it well.
Apply this principle to issues, comments, documents, and instructions.

Write and revise in this order:

1. Identify the reader need served by each passage: understanding the goal, assessing the result, or taking a specific action.
2. Delete passages with no clear purpose, repetition, and routine disclaimers. Keep the deletion if it does not impair understanding or action.
3. Simplify the remaining wording and organize headings, lists, and hierarchy.
4. If the same excess wording recurs, fix the rule or template that produces it. Add content back only when a specific information gap appears.

**Work records describe only work actually performed. Unmentioned work is not completed or performed; do not add a disclaimer for every unperformed action.**

- Describe evidence with accurate verbs and scope, such as reviewed, compared, or tested. Limit conclusions to what the evidence supports.
- Remove routine statements that something was not tested, created, or published, or is awaiting review. Do not move these statements into a limitations section.
- Retain discovered documentation differences, failures, or blockers only when they affect assessment or the next action, and explain the specific impact.
- A result summary may include a short progress field. Omit explanations of what status values mean.
- Keep work records about the work itself. Omit conversation arrangements, internal delegation details, and statements about waiting for writing-style feedback.
- State the recommended next action directly and use a native Linear issue mention to link the relevant work.

Base public documents on deliverables and official sources that readers can access.
Keep private tracking in its own environment instead of making it a prerequisite for reading public documents.
Use understandable document names in citations rather than requiring readers to look up internal codes.

## Help a new reader understand quickly

Write for someone who did not participate in the conversation so they can understand the goal, findings, deliverables, and next action.

- Use short, clear headings that name the topic. Omit opening sentences that announce a start, repeat the heading, or preview the next passage.
- Put delivery goals, scope, and expected outputs directly in the issue body.
- Comments record actual progress, findings, decisions, or research results. Each comment adds information.
- Prioritize output files, deliverable entry points, and necessary findings in work records. Put recording methods in the relevant rules or deliverable document.
- When recording a finding, explain what was learned, where the evidence is, and how it affects subsequent work. Include enough context to avoid requiring the prior conversation.
- Use a short research-comment heading to identify the stage. Use “Preliminary findings” for early exploration. Put the verification date on a separate line from the content.
- Use bullets for research findings, one finding per point with its source location. State the impact on subsequent work separately in a short sentence.
- If a finding involves several sources, differences, or effects, use a first-level topic with second-level details.
- Organize completion records into result summary, completed items, verification results, and next steps. Keep only sections with content.
- Use short fields and bullets in result summaries. List remote and local output locations separately, with clickable links to remote deliverables.
- Number completed items, use checkboxes for verification results, and describe concrete next actions with links to the relevant work.

## Maintain issue bodies

The issue body is the authoritative entry point for current information.
It should let a new reader understand the goal, adopted conclusions, deliverables, and remaining questions.

- Define work around one topic and assessable completion criteria. The title expresses the intended result; the body retains the context and evidence needed to understand the problem.
- Update the body when new information, important decisions, or research conclusions appear. Replace superseded descriptions with the adopted approach and list open questions separately.
- Comments preserve discovery and decision history; the body summarizes current conclusions. Link to the relevant discussion when readers need to trace the reasoning.
- When citing related work or discussion, explain its relationship, impact, or supported conclusion so readers understand the purpose before opening the link.
- Use permanent links to fixed versions when citing code as evidence.
- On delivery, add links to outputs, documents, and verification so readers entering from the issue can find usable results.
- Decide whether to close the issue against its completion criteria. The closing comment records actual results or the reason for closure, and the body is updated accordingly.
- Treat body updates and notifications separately. When someone needs to act, state the request and context in an authorized comment, distinguishing execution responsibility from a review request.

## Where repository content belongs

- Maintain one copy of operational guides, examples, and templates in the installable skill.
- Put research evidence in `research/`, retaining sources, verification dates, and adoption rationale.
- Put architecture choices in `design/`, explaining decisions and affected entry points.
- Maintain proposals and working discussions in Linear. Incorporate adopted knowledge into the relevant documents.
- Version check scripts, fixed cases, and de-identified reports.
- Put private logs and temporary output in Git-excluded directories.
- Preserve tested versions and original judgments in historical validation. Updating hashes is not a substitute for rerunning validation.
