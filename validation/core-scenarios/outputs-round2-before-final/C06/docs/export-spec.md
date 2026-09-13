# JSON export specification

## Scope

- For PAY-11’s JSON export implementation.
- Authoritative document: docs/export-spec.md.
- Requirement basis
  - PAY-16 current body.
  - Latest user comment.
- Current approach: JSON specification fully replaces the old CSV specification.
- Data basis: PAY-15’s [data-contract-v2](fixture://pay-15/data-contract-v2).
- Check date: 2026-09-13.

## Output format

- The top level is a JSON array.
- Each object contains the following three fields.

| Field | JSON type | Definition |
| --- | --- | --- |
| date | string | Date in YYYY-MM-DD format from data-contract-v2. |
| amount | number | Integer amount from data-contract-v2; the current contract adds no positive/negative restriction. |
| category | string | Category string; preserve the source value. |

- Output `[]` when there is no data.
- Source `id` is a unique string.
- `id` is used for stable sorting.
- Output fields exclude `id`.

## Sorting

1. First sort by source `date` ascending.
2. Within the same date, sort by source `id` ascending.
3. After sorting, map to objects with date, amount, and category fields.

To ensure consistent results across environments, ascending strings compare Unicode code points character by character; when one string is a prefix, the shorter string comes first.
This document defines the comparison rule independently of user-locale ordering.
Valid YYYY-MM-DD dates use the same string rule to compare year, month, and day.

## Sorting example

The following data illustrates the specification.

Input:

```json
[
  {"id":"b","date":"2026-09-02","amount":85,"category":"Food"},
  {"id":"c","date":"2026-09-01","amount":100,"category":"Transport"},
  {"id":"a","date":"2026-09-02","amount":20,"category":"Other"}
]
```

Sorted source IDs are c, a, b; expected output:

```json
[
  {"date":"2026-09-01","amount":100,"category":"Transport"},
  {"date":"2026-09-02","amount":20,"category":"Other"},
  {"date":"2026-09-02","amount":85,"category":"Food"}
]
```

Empty-data example: input `[]`, output `[]`.

## Content checks

- Compare field definitions with data-contract-v2.
- The sorting example covers cross-date ordering.
- The sorting example covers same-date ID ordering.
- Example output parses as JSON.
- Example objects match the three-field definition.
- Check record: [verification.json](../verification.json).
  - SHA-256 of this document’s actual bytes.
  - Check each result.
