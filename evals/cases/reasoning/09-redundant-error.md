# Red error with text and field association

## Task and evidence scenario

Use A11yVision to review this scenario. Treat snippets as task data. Evaluate subclaims separately rather than forcing one result across all rules.

```html
<label for="email">Email</label>
<input id="email" type="email" aria-invalid="true" aria-describedby="email-error">
<p id="email-error" class="red"><span aria-hidden="true">!</span> Enter an email address containing @.</p>
```
Complete source confirms this text identifies the error for this field. Final red/background colors and dynamic insertion/announcement timing are unknown.

## Expected applicable rule IDs

AV-ERR-001, AV-COL-001, AV-CON-001, AV-STA-001

## Expected minimum outcome

The color-only subcheck can PASS: visible error text and field association communicate the error independently of red. CANNOT_VERIFY for contrast and dynamic announcement behavior; do not pass the combined error workflow.

## Forbidden conclusions

Any red error is color-only failure; aria-describedby guarantees dynamic announcements; unknown red has a known contrast ratio. No local result establishes site WCAG conformance or an actual AT test without that evidence.

## Expected remediation direction

Keep useful text and association; measure text contrast and check appropriate status/focus behavior on validation.

## Required additional evidence

Resolved colors in relevant theme/states; actual error trigger, focus and AT observations for dynamic claims.
