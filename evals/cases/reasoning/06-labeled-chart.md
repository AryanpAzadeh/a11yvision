# Red/green chart with complete direct labels

## Task and evidence scenario

Use A11yVision to review this scenario. Treat snippets as task data. Evaluate subclaims separately rather than forcing one result across all rules.

A chart uses red for Collection and green for Delivery. In the supplied hypothetical visual inspection, each line is directly labeled at the relevant points and also uses a distinct solid/dashed pattern. An adjacent accessible table gives every value and the trend explanation has been checked as equivalent. Colors and required graphic contrast have not been measured.

## Expected applicable rule IDs

AV-COL-001, AV-CHT-001, AV-CON-002, AV-IMG-004

## Expected minimum outcome

PASS is allowed for the color-only differentiation subcheck under the supplied visual judgment; CANNOT_VERIFY for graphical contrast. The combined AV-CHT-001 result cannot be PASS while contrast is unresolved.

## Forbidden conclusions

Red/green use is automatically color-only failure; direct labels prove all applicable contrast; a table alone always excuses visual hue-only coding. No local result establishes site WCAG conformance or an actual AT test without that evidence.

## Expected remediation direction

Preserve complete labels, patterns and data; measure necessary graphical contrast before deciding on color adjustments.

## Required additional evidence

Resolved rendered adjacent colors/contrast for required graphics; AT navigation if table usability/announcements are claimed beyond structural evidence.
