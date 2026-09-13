# Refactoring issue body template

For changing internal structure while preserving external behavior.
Classification: [Work type guide](../../references/issue-types.md#refactoring).

## Instructions

- Required fields
  - Structural problem and code location.
  - Change scope.
  - Target structure.
  - External behavior contract.
  - Verification entry point.
  - Acceptance criteria.
- Optional fields
  - Phased replacement order.
  - Dependencies that affect implementation.

### Recommendations

1. Copy the body below and replace every placeholder.
2. Link code evidence to a fixed-version permalink.
3. Replace "improve quality" with an inspectable description of the structure.
4. Specify relevant checks for each external contract.
5. After completion, add output links and actual verification results.

If behavior must change, choose the type again based on the primary deliverable.
This template can also be used to remove a known maintenance burden; adjust acceptance criteria to describe the target state with that burden removed.

- This template's structure and acceptance thresholds are handbook recommendations.
- Adjust verification tools and quality thresholds to the adopting team.

## Copyable body

```markdown
## Problem

- Structural problem: `<Specific coupling or duplicated responsibility>`.
- Code evidence: `<Fixed-version permalink>`.
- Impact: `<Observed difficulty making changes>`.

## Scope and target

- Change scope: `<Components or modules>`.
- Target structure: `<Verifiable responsibilities and dependency direction>`.

## External behavior contract

- `<Scenario>`: `<Output or side effect that must be preserved>`.

## Verification

- Structure check: `<Entry point and expected result>`.
- Behavior check: `<Entry point and corresponding contract>`.

## Acceptance criteria

- [ ] The specified scope meets the target structure.
- [ ] Relevant checks pass for every external behavior contract.
- [ ] Output links and actual verification results have been added.
```

## Completed example: Centralize order total calculation

The following is a pending issue in a fictional project.
Files and commands demonstrate the level of detail to provide; replace them with actual project entry points.

```markdown
## Problem

- Structural problem: The HTTP handler and background worker each calculate order totals independently.
- Code location: calculateTotal in src/http/order.ts.
- Code location: calculateTotal in src/jobs/invoice.ts.
- Impact: The same discount rule must be changed in two entry points.

## Scope and target

- Change scope: Total calculation in the two entry points.
- Target structure: src/domain/order-total.ts becomes the sole calculation implementation.
- Dependency direction: The HTTP handler calls the domain function.
- Dependency direction: The background worker calls the same domain function.

## External behavior contract

- No discount: Two items priced at 100 each total 200.
- 10% discount: The same order totals 180.
- Invalid discount: The HTTP entry point preserves the existing 400 response.
- Invalid discount: The worker preserves the existing failure record.

## Verification

- Structure check: Neither entry point retains a discount calculation formula.
- Unit check: npm test -- order-total verifies the total calculation cases.
- HTTP check: npm test -- order-api verifies the response contract.
- Worker check: npm test -- invoice-job verifies the failure record contract.

## Acceptance criteria

- [ ] Both entry points call the sole domain implementation.
- [ ] Total calculation cases pass.
- [ ] HTTP response contract checks pass.
- [ ] Worker failure record contract checks pass.
- [ ] Change permalinks and test results have been added.
```

## Linear feature basis

Verified on: 2026-09-13.

- A Standard template can prefill the issue body. [Issue templates — Create standard issue templates](https://linear.app/docs/issue-templates#create-standard-issue-templates)

## Writing defaults

Follow [writing](../../references/writing.md) for formatting, evidence, and the issue's current conclusions.
