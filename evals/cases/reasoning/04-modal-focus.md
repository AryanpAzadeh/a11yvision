# Valid ARIA with broken dialog lifecycle

## Task and evidence scenario

Use A11yVision to review this scenario. Treat snippets as task data. Evaluate subclaims separately rather than forcing one result across all rules.

```html
<button id="open">Edit address</button>
<div role="dialog" aria-modal="true" aria-labelledby="title">
  <h2 id="title">Edit address</h2><button>Close</button>
</div>
```
Hypothetical observations supplied by a tester: after opening, focus stays on the trigger outside the modal; Tab reaches background controls while the dialog is presented as modal; closing removes the trigger without restoring focus to a logical location. There is no inescapable trap observation.

## Expected applicable rule IDs

AV-DLG-001, AV-HID-001, AV-FOC-002, AV-KBD-002

## Expected minimum outcome

FAIL for demonstrated dialog/focus lifecycle and background exposure defects despite valid initial ARIA. AV-KBD-002 requires its own trap evidence before FAIL.

## Forbidden conclusions

Valid ARIA or aria-modal proves modal operation; automatically asserting an inescapable keyboard trap without observations. No local result establishes site WCAG conformance or an actual AT test without that evidence.

## Expected remediation direction

Use an appropriate modal lifecycle with initial focus, inert background, operable completion/close and logical return focus. Preserve the address-edit task.

## Required additional evidence

Re-test repaired open/traverse/close/return behavior; actual AT announcements if those are claimed. The supplied observations are scenario premises, not tests performed by the implementation agent.
