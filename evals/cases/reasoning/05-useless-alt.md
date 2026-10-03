# Attribute presence without useful meaning

## Task and evidence scenario

Use A11yVision to review this scenario. Treat snippets as task data. Evaluate subclaims separately rather than forcing one result across all rules.

```html
<img src="quarterly.svg" alt="image">
```
The surrounding product context says quarterly results, but the actual image and any equivalent data are unavailable.

## Expected applicable rule IDs

AV-IMG-001, AV-IMG-004

## Expected minimum outcome

NEEDS_REVIEW for adequacy/purpose and the possible complex visual; no syntax-only PASS. If later inspection establishes important chart data with no equivalent, FAIL becomes justified.

## Forbidden conclusions

alt presence proves equivalence; the filename proves chart figures; automatically treating an unknown image as decorative. No local result establishes site WCAG conformance or an actual AT test without that evidence.

## Expected remediation direction

Inspect the actual visual and nearby equivalent, then write a purpose-based summary and structured data explanation if needed.

## Required additional evidence

Actual image content, intended purpose, nearby text/data and content-equivalence judgment.
