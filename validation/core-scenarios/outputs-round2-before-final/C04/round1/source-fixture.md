Source: requests.md → C04

Large feature

User request: break ”allow users to export all filtered expenses as CSV” into work for two Agents, preserving overall acceptance. This round needs only planning and issue bodies.

- Project: Pocket Reporting, proj-report.
- New capability: export all matching data by date range and category, including other pages.
- Decision: synchronous download, at most 5000 records; exceeding the limit prompts narrowing the range and creates no file.
- CSV columns: date, amount, category, notes.
- Notes may contain Chinese, commas, double quotes, and newlines.
- No matches: still download a header-only CSV.
- Permissions: include only expenses readable by the current user.
- The existing query API returns only the current page; no complete-query contract is available for export.
- Frontend and export backend need a shared filter, sort, and error-response contract.
- Implementation can split into src/export/ and src/ui/export/, with integration at src/app/export.ts.
- Each of two Agents can handle one item; the maintainer can review one item at a time.
- Delivery includes browser download and comparison with actual data.
- No launch date is specified.
- No issue has the same outcome.
