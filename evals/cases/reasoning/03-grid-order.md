# Meaningful CSS Grid order

## Task and evidence scenario

Use A11yVision to review this scenario. Treat snippets as task data. Evaluate subclaims separately rather than forcing one result across all rules.

```html
<div style="display:grid">
  <button style="order:2">Step 2: confirm delivery</button>
  <button style="order:1">Step 1: choose delivery</button>
</div>
```
Step 2 depends on the choice in step 1. Only source is available; rendered order and interaction have not been tested.

## Expected applicable rule IDs

AV-SEQ-001, AV-FOC-002

## Expected minimum outcome

NEEDS_REVIEW for the identified order risk, with CANNOT_VERIFY for the unobserved rendered/focus behavior. Do not claim source-only PASS.

## Forbidden conclusions

Every CSS order property is a WCAG failure; every visually different order is acceptable; positive tabindex is the proper repair. No local result establishes site WCAG conformance or an actual AT test without that evidence.

## Expected remediation direction

Inspect the complete task, align DOM order with meaningful step order and use layout that preserves it.

## Required additional evidence

Rendered layout at relevant breakpoints, DOM reading order and actual forward/backward keyboard sequence.
