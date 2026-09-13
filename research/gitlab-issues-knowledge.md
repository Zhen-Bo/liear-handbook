# GitLab Issues: knowledge extraction and adoption decisions

## Source and reading scope

- Source: [GitLab Handbook — Communication / Issues](https://handbook.gitlab.com/handbook/communication/#issues).
- Retrieved: 2026-09-12.
- [Full source excerpt](sources/gitlab-communication-issues.md), [original HTML](sources/gitlab-communication-issues.html), [retrieval record](sources/gitlab-communication-issues.metadata.json).
- Read all content from the Issues heading to the next heading of the same level: purposes and focus, the first set of 3 rules, the automatic closure tip, the second set of 16 rules, and the good and bad linking examples.
- Locations below use “opening,” “first set,” “tip,” and “second set,” preserving the source’s two separately numbered lists.
- The following contains extracted findings and adoption decisions. The source excerpt and these notes retain attribution and licensing information under the source’s [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

## Findings by source location

| Source location | Main point (paraphrased) | Applicable knowledge and boundaries |
|---|---|---|
| Opening: purposes | Issues can support research proposals, design exploration, delivery decomposition, and progress tracking. | Issues are not limited to bugs and features; research and decisions can also close with clear deliverables. This is work-modeling guidance; it need not all appear in body-maintenance rules. |
| Opening: focus | Each issue needs one topic and an outcome that permits closure; avoid open-ended discussion. | The body needs an understandable goal and completion criteria. Create and link bounded work when a new independent problem arises. |
| First set 1 | A closing comment explains why the issue is closing and the discussion’s MVC outcome, including whether it was implemented. | MVC means minimum viable change. Record actual results or the reason for cancellation to support closure; there is no need to explain the meaning of Done. This fits the user’s deletion principles. |
| First set 2 | External commitments require internal agreement. | Distinguish proposals, decisions, and external commitments. This is an authorization and collaboration policy; an Agent cannot infer permission to make commitments. |
| First set 3 | Keep external stakeholders informed and give the next update date when needed to avoid unexpected delays. | Explain changes that affect others’ plans, their impact, and the next update point. Frequency depends on context; the source does not require a comment for every tool operation. |
| Tip | GitLab can automatically close issues with MR closing keywords; some projects disable this. | This is GitLab behavior. Linear’s GitHub integration requires separate research. Do not present the syntax as universal or equate merging with all work being complete. |
| Second set 1 | Find an existing issue for an enhancement request, or create one and clarify the first deliverable. | Check for duplicates, then clarify the request and smallest deliverable scope. |
| Second set 2 | Cross-link related issues, MRs, and reports; report back or transfer responsibility when complete. | Record request sources, related changes, and relationships in the body. Completion notifications and handoffs must remain within existing authorization. |
| Second set 3 and two examples | Summarize linked content beside the link so readers can understand the relationship without navigating away. | A native mention only points to work. Explain its specific relationship alongside it, such as a similar performance problem, blocking condition, or verification result. |
| Second set 4 | Cite code lines with permalinks to a fixed commit. | Point evidence to a reproducible version so branch updates cannot shift the reference. |
| Second set 5 | Prioritize issues in the current milestone. | This is scheduling policy. It cannot be applied to every workspace automatically or override actual priority and blocking relationships. |
| Second set 6 | GitLab uses public issue trackers and designated organization groups. | This reflects GitLab’s transparency culture and tooling; it does not establish a default requirement to make Linear data public. |
| Second set 7 | Claim work when starting it and reassign it when someone else needs to take over. | Assignee should reflect actual execution responsibility; claim timing must fit the team’s assignment practices. |
| Second set 8 | Titles state the desired outcome, including for bugs. | Make the intended result visible in the title. Keep symptoms and reproduction evidence in the body rather than reducing the bug to an abstract improvement slogan. |
| Second set 9 | Update the description with new information and important decisions so it remains the authoritative entry point. | Update the body when decisions and conclusions emerge, without waiting for closure. Replace superseded descriptions and retain comment links for tracing the process. |
| Second set 10 | Request review with a comment mention rather than by changing the assignee. | Separate execution responsibility from review requests. Mentioning people and sending notifications requires authorization. |
| Second set 11 | Notifications and assignments need contextual comments describing the requested action; mentioning someone only in the description is insufficient. | Maintaining the body and notifying someone are separate actions. A message should directly state what the recipient should do and why. |
| Second set 12 | Close work only when it is truly done; discuss further iteration or a subsequent change as needed. | Judge closure by actual completion criteria. Creating a follow-up issue does not complete necessary work that remains in scope. |
| Second set 13 | Add documentation links to the description when a feature is done so readers arriving from search can find them. | Put delivery links in the issue body so third parties can locate results, usage documentation, and verification evidence. Applying this to research documents is an extension proposed in these notes. |
| Second set 14 | Minimize private information in issues and use confidential issues when necessary; the source also discusses access roles and external documents. | Adopt data minimization. GitLab’s confidential permissions and Google Docs advice do not imply equivalent protection in Linear; verify actual access controls. |
| Second set 15 | Adjust visibility when public content becomes confidential. | Recheck access when sensitivity changes; an existing public location is not necessarily appropriate forever. |
| Second set 16 | Public discussions that violate the code of conduct may be locked or moderated. | This concerns community governance and administrative permissions, outside an ordinary Agent’s automatic text-editing operations. |

## Core rules for maintaining issue bodies

1. Use the title, goal, and completion criteria together to define one work outcome.
2. Update the effective version of the body when new information, decisions, or conclusions emerge.
3. Preserve sources, related work, and discussion evidence through contextual links.
4. Add delivered documents and result links to the body on completion.
5. Support closure with met completion criteria, and explain the result or closure reason in a comment.
6. Handle body updates, execution responsibility, and notification requests separately.

Source locations: opening, first set 1, second set 2–4 and 7–13.
AGENTS.md includes only rules directly related to these behaviors; the remaining findings stay in the table for later research.

## Additions when converting the source into operating rules

- “Comments preserve the process; the body preserves current conclusions” is an operating interpretation of second set 9, not a verbatim requirement.
- Separating unresolved questions from conclusions helps prevent proposals from being presented as decisions.
- Reading the latest body before making a targeted update protects against concurrent edits by people or Agents.
- Markdown heading, bullet, numbered-list, and checkbox choices come from the user’s formatting requirements.
- The closure reason in first set 1 should support judgment; the user’s requirements call for omitting repeated field values and explanations of status names.
- The source’s policies on publicity, milestones, assignment, mention notifications, and platform automation do not authorize broader operations.
