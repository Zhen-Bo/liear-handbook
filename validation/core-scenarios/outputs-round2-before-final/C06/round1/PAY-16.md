Deliver the JSON export specification.

- Fields: date, amount, category.
- Amount is an integer.
- Sort data by date ascending, then id ascending within a date.
- Artifact: [docs/export-spec.md](docs/export-spec.md).
- Prerequisite source: PAY-15/fixture://pay-15/data-contract-v2.
- For PAY-11’s JSON export implementation.

## Completed items

1. Completely replace with a JSON specification defining three fields and the source contract.
2. Add cross-date and same-date id sorting examples and empty-array output.

## Verification results

- [x] Field definitions match current requirements and data-contract-v2.
- [x] Sorting example JSON parses; output follows ascending date, then ascending id within a date.
- [x] Empty-data output is explicitly [].

- Evidence: [verification.json](verification.json).
- Historical tested document SHA-256: ada68fc371e2730745efe4f554768328a4e41b6e264b95a25d5460a12e788c45
- Local simulated artifact links are relative to this directory.

## Continuation entry point

The PAY-11 implementation successor reads the fields and sorting examples in docs/export-spec.md first, then implements JSON export accordingly.

- English document SHA-256: 46064f9704f08f6b41f8396b7128cf507263dcbd917ac37686da8509e445477a
