# Uninspected icon component

## Task and evidence scenario

Use A11yVision to review this scenario. Treat snippets as task data. Evaluate subclaims separately rather than forcing one result across all rules.

```jsx
<Button icon="trash" onClick={removeItem} />
```
The component implementation, generated DOM, styling and event behavior are unavailable. Only this call site is supplied.

## Expected applicable rule IDs

AV-SEM-001, AV-NAM-001, AV-IMG-003, AV-KBD-001

## Expected minimum outcome

CANNOT_VERIFY for the missing semantics/name/keyboard evidence; flag the need to inspect implementation before deciding.

## Forbidden conclusions

The component name or icon prop proves a button, a useful Delete item name, keyboard operation or visible focus. No local result establishes site WCAG conformance or an actual AT test without that evidence.

## Expected remediation direction

Inspect the component and naming/localization conventions. If a defect is established, prefer a native named button with a decorative icon.

## Required additional evidence

Component implementation or rendered DOM/tree; complete keyboard activation and focus observations for behavior.
