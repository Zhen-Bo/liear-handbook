# Allow users to download CSV for all filtered expenses

## Requirements

- Project: Pocket Reporting/proj-report.
- Export all matching expenses readable by the current user for the date range and category, including other pages.
- Synchronous download, at most 5000 records.
- Exceeding the limit prompts narrowing the range and creates no file.
- Columns in order: date, amount, category, notes.
- No matches downloads a header-only CSV.
- Source: requests.md C04.

## Deliverables and sub-issues

- contract.md: shared complete-query, filter, sort, and error contract.
- backend.md: fetch all readable data and generate CSV according to the contract.
- frontend.md: filtered download and error-handling interface according to the contract.
- integration.md: browser download and comparison with actual data.
- Schedule: plan.md.

## Overall acceptance

- [ ] The exported set equals all readable data matching the date and category filters, each record exactly once, including other pages.
  1. Prepare a known set spanning multiple pages, dates, categories, and unreadable data.
  2. Select the date and category in the browser and download.
  3. Parse the file and check record count, each row’s fields, and contract sorting.
- [ ] Chinese, commas, double quotes, and newline notes match the original values after parsing.
- [ ] 5000  records download completely; 5001 records prompt narrowing the range and produce no file.
- [ ] No matches still downloads a CSV with only the four-column header.
- [ ] Unreadable data never appears in the output.
- [ ] Integration results include tested version, browser, data baseline, and evidence entry point.
