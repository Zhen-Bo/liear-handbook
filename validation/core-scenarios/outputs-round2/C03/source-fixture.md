Source: requests.md → C03

Vague bug

User request: expenses sometimes disappear after saving. Break this into work I can hand to Agents. Only the following information is available. Produce issue drafts and an execution order.

- Promised behavior: the same expense remains visible after adding and refreshing.
- User report: occasionally on mobile, an expense of TWD 85 for Food disappeared yesterday.
- Affected product: Pocket web, version pocket-0.3.1.
- Exact device, browser version, full operation sequence, and failure rate remain to be obtained.
- Successful example: add TWD 100 Transport in desktop Chrome and refresh; data remains.
- No console, network, or localStorage snapshot exists from the failure.
- A test account and isolated browser storage are available for further investigation.
- Team discussion includes: it may be an iOS storage limit or a date-filtering problem.
- Requirements are unchanged; no cloud synchronization was requested.
- Existing Project: proj-pocket; no issue with the same outcome.
- Only drafts are authorized.
