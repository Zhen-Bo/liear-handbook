# Allow users to download CSV for all filtered expenses

## Requirements

- Project: Pocket Reporting/proj-report.
- Filter by date range.
- Filter by category.
- The export includes matching data from other pages.
- Permissions: include only expenses readable by the current user.
- Download mode: synchronous.
- Record limit: 5000.
- Limit handling
  - Prompt narrowing the range.
  - Do not create a file.
- Column order: date → amount → category → notes.
- No matches downloads a header-only CSV.
- Source: requests.md C04.

## Deliverables and sub-issues

- [contract.md](contract.md): shared export contract.
- [backend.md](backend.md): CSV generation for the complete data set.
- [frontend.md](frontend.md): filtered download interface.
- [integration.md](integration.md): real download workflow integration.
- [plan.md](plan.md): execution schedule.

## Overall acceptance

- [ ] Cross-page export contains all readable data matching the date range.
- [ ] The export contains only data matching the category filter.
- [ ] Each matching record appears exactly once.
- [ ] Column order matches the contract.
- [ ] Data sorting matches the contract.
- [ ] Chinese notes match their original values after parsing.
- [ ] Comma-containing notes match their original values after parsing.
- [ ] Double-quote notes match their original values after parsing.
- [ ] Newline notes match their original values after parsing.
- [ ] 5000  records download completely.
- [ ] 5001  records display a prompt to narrow the range.
- [ ] 5001  records create no file.
- [ ] No matches downloads a CSV with only the four-column header.
- [ ] Unreadable data never appears in the output.
- [ ] Acceptance records identify the tested version.
- [ ] Acceptance records identify the browser.
- [ ] Acceptance records identify the data baseline.
- [ ] Each acceptance result has an evidence entry point.

## Verification order

1. Prepare a known multi-page data set.
2. Add data outside the date range.
3. Add data from other categories.
4. Add unreadable data.
5. Select filters in the browser.
6. Download the file.
7. Parse CSV.
8. Check each acceptance result above.
9. Save evidence.
