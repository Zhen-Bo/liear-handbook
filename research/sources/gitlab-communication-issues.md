# GitLab Communication — Issues source excerpt

- Author/publisher: GitLab
- Source: https://handbook.gitlab.com/handbook/communication/#issues
- Retrieved: 2026-09-12 (UTC; see metadata.json for the full timestamp)
- Scope: from the Issues heading to the next heading of the same level.
- License: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/), as indicated on the source page.
- Processing: the source text was neither translated nor summarized. HTML was converted to Markdown, preserving paragraphs, lists, and links; relative links were made absolute. The original HTML is stored separately for comparison.

---

### Issues

Issues are valuable when there isn’t a specific code change that is being proposed, such as:

- Crafting a research proposal to validate a problem or solution
- Ideating on designs in order to solve a particular problem
- Breaking down implementation tasks in order to deliver a solution iteratively
- Tracking progress of particular tasks, especially when an issue board is needed

When utilizing issues, it is still important to maintain focus by defining a single specific topic of discussion and the desired outcome that would result in the resolution of the issue. Issues should not be open-ended or go stale due to lack of resolution. For example, a team member may open an issue to track the progress of a blog post with associated to-do items that need to be completed by a certain date (e.g. first draft, peer review, publish). Once the specific items are completed, the issue can successfully be closed.

Below are a few things to remember when creating issues:

1. When **closing** an issue leave a comment explaining why you are closing the issue and what the MVC outcome was of the discussion (if it was implemented or not).
2. We keep our **promises** and do not make external promises without internal agreement.
3. Be proactive and consistent with communication on discussions that have external stakeholders such as customers. It’s important to keep communication flowing to keep everyone up to date. Issues can appear stale if there aren’t recent discussions and no clear definition on when another update will be provided, based on feedback. This leaves those subscribed in the dark, causing unnecessary surprise if something ends up delayed and suddenly jumps to the next milestone. It is important that issues are closed in a timely manner. One way of doing this is having the current assignee set a due date for when they will provide another update. This can be days or weeks ahead depending on the situation, prioritization, and available capacity that we may have.

***Pro Tip:*** When creating a Merge Request you can add `closes: #[insert issue number here]` and when the Merge Request is merged, the issue will automatically close. You can see an example of this [here](https://gitlab.com/gitlab-com/people-group/peopleops-eng/employment-automation/-/merge_requests/60). **Note:** [Automatic issue closing](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#disable-automatic-issue-closing) is disabled on some projects.

1. If a user suggests an enhancement, try and find an existing issue that addresses their concern, or create a new one. Ask if they’d like to elaborate on their idea in an issue to help define the first MVC via a subsequent MR.
2. **Cross link** issues or MRs with related conversations. Another example is to add “Report: " lines to the issue description with links to relevant issues and feature requests. When done, add a comment to relevant issues (and close them if you are responsible for reporting back, or reassign if you are not). This prevents internal confusion and us failing to report back to the reporters.
3. When cross-linking issues or MRs, include a preview of the content you are linking, to facilitate [low-context communication](https://handbook.gitlab.com/handbook/communication/#low-context):
   1. Good: `this would cause performance issue similar to #123456`. The reader has full information on first read and can refer to the link for more.
   2. Avoid: `this would cause issue similar to #123456`. The reader needs to click the link and find the relevant information among other discussion threads, before switching back to the original discussion.
4. When providing links to specific lines of code relevant to the issue, **always use a permalink** (a link to a specific commit for the file). This ensures that the reference is still valid if the file changes. For more information, see [Link to specific lines of code](https://docs.gitlab.com/ee/development/documentation/styleguide/#link-to-specific-lines-of-code).
5. Prioritize your work on issues in the current [milestone](https://gitlab.com/groups/gitlab-org/-/milestones).
6. Use the public issue trackers on GitLab.com for everything since [we work out in the open](https://about.gitlab.com/blog/2015/08/03/almost-everything-we-do-is-now-open/). Issue trackers that can be found on the relevant page in the handbook and in the projects under [the gitlab-com group](https://gitlab.com/gitlab-com/).
7. Assign an issue to yourself as soon as you start to work on it, but not before that time. If you complete part of an issue and need someone else to take the next step, **re-assign** the issue to that person.
8. Ensure the issue **title** states what the desired outcome should be. For instance, for bugs make sure the issue states the desired result, not the current behavior.
9. **Regularly update** the issue description with the latest information and its current status, especially when important decisions were made during the discussion. The issue description should be the **single source of truth**.
10. If you want someone to review an issue, do not assign them to it. Instead, @-mention them in an issue comment. Being assigned to an issue is a signal that the assignee should or intends to work on it. So you should not assign someone to an issue and misrepresent this with a false signal.
11. If you’d like to inform someone about an issue or assign a task to them, do so via an issue comment, not only by adding them to the description. The to-do item generated when you mention someone in an issue description provides little context for the action you’re requesting. But using a comment to explicitly inform someone of the action you’d like them to take ensures that when they read the associated to-do item they won’t need to read the entire issue to gather the context they need to complete the work.
12. Do not close an issue until it is [**done**](https://docs.gitlab.com/ee/development/contributing/merge_request_workflow.html#definition-of-done). It’s okay to explicitly ask if everyone is on board and in agreement on how to move forward, whether to iterate, close the open issue, or create a subsequent MR to implement a MVC.
13. Once a feature is [**done**](https://docs.gitlab.com/ee/development/contributing/merge_request_workflow.html#definition-of-done), update the description to add a link to the corresponding documentation. When using a Search Engine, issues often appear before documentation pages, which makes it harder to find the relevant information about the feature.
14. Write issues so that they exclude private information. This way, the issue can be public. Only use confidential issues, if the issue must contain [non-public information](https://handbook.gitlab.com/handbook/communication/confidentiality-levels/#not-public). **Note:** Confidential issues are [accessible to all members of the project with Reporter access and above](https://docs.gitlab.com/ee/user/project/issues/confidential_issues.html#permissions-and-access-to-confidential-issues). You may consider using a Google Doc for items that require a stricter level of confidentiality.
15. If the content within a public issue transitions to become what is deemed confidential [non-public information](https://handbook.gitlab.com/handbook/communication/confidentiality-levels/#not-public), the issue may be made confidential.
16. If the content of a public issue draws comments that are deemed in violation of our [code of conduct](https://about.gitlab.com/community/contribute/code-of-conduct/) the issue may be locked and may [undergo moderation](https://handbook.gitlab.com/handbook/marketing/developer-relations/workflows-tools/code-of-conduct-enforcement/#overview).
