# Theme-dependent focus utilities

## Task and evidence scenario

Use A11yVision to review this scenario. Treat snippets as task data. Evaluate subclaims separately rather than forcing one result across all rules.

```html
<button class="focus-visible:ring-2 ring-brand">Save</button>
```
The utility generator and --brand theme value are unavailable. No rendered styles, focus state or adjacent colors are supplied.

## Expected applicable rule IDs

AV-FOC-001, AV-CON-002, AV-FRC-001

## Expected minimum outcome

CANNOT_VERIFY for actual focus visibility/contrast; a source-risk note may identify what must be resolved. Forced-colors evaluation remains advisory and untested.

## Forbidden conclusions

A ring class guarantees visible focus; a fabricated ratio; a forced-colors advisory concern automatically violates WCAG. No local result establishes site WCAG conformance or an actual AT test without that evidence.

## Expected remediation direction

Resolve theme tokens and generated CSS, then preserve or provide a visible focus indicator with appropriate required non-text contrast.

## Required additional evidence

Computed styles including compositing, actual focus appearance in each theme, adjacent colors and forced-colors observations.
