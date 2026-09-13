# Connect the real export service and verify browser CSV downloads

## Inputs and scope

- Blocked by
  - The usable implementation version from Backend.md.
  - The usable implementation version from Frontend.md.
- Executor: Agent A.
- Shared entry point: src/app/export.ts.
- Sole writer for the shared entry point: Agent A.
- Deliverables
  - Integration version.
  - verification/csv-export.md.
- Connect the complete-query functions.
- Connect the download interface.
- Perform all overall acceptance checks in parent-feature.md.

## Acceptance

- [ ] The cross-page exported set equals the complete filtered set matching date range, category, and current-user read permission.
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
- [ ] The results above come from an actual browser download.
- [ ] Each result identifies the integration version.
- [ ] Each result identifies the actual data baseline.

Mark the parent complete only after all required acceptance criteria pass.

## Next steps

1. Check the backend entry point.
2. Check the frontend entry point.
3. Check the contract version used by both.
4. Connect src/app/export.ts.
5. Prepare multi-page data.
6. Perform browser acceptance.
