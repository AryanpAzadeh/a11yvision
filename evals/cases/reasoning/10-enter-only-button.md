# Incomplete button keyboard emulation

## Task and evidence scenario

Use A11yVision to review this scenario. Treat snippets as task data. Evaluate subclaims separately rather than forcing one result across all rules.

```html
<div role="button" tabindex="0">Save</div>
```
The complete supplied implementation handles click and Enter only; there is no Space handler. Hypothetical keyboard observations confirm Space scrolls instead of activating Save. This is intended to behave as a button, with no alternative keyboard route for that activation.

## Expected applicable rule IDs

AV-SEM-001, AV-KBD-001, AV-ARIA-001

## Expected minimum outcome

FAIL for incomplete button keyboard behavior under the supplied implementation and observations. The exposed button role alone is insufficient; do not treat a valid role token as proof of complete interaction.

## Forbidden conclusions

Enter support and tabindex prove full button emulation; adding more ARIA fixes activation; custom controls always fail regardless of complete behavior. No local result establishes site WCAG conformance or an actual AT test without that evidence.

## Expected remediation direction

Prefer a native button and preserve the Save handler/state/localization; if custom architecture is genuinely needed, implement complete button interaction safely.

## Required additional evidence

Re-test Enter, Space, focus visibility and Save completion after remediation, and role/name/state exposure. Supplied observations remain hypothetical evaluation data.
