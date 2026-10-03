---
id: "AV-DLG-001"
title: "Modal dialogs have coherent name, focus, and background behavior"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "2.1.1", "level": "A"}, {"criterion": "2.1.2", "level": "A"}, {"criterion": "2.4.3", "level": "A"}, {"criterion": "4.1.2", "level": "A"}]
users: ["blind", "low-vision"]
categories: ["keyboard-focus"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "KEYBOARD_INTERACTION", "ACCESSIBILITY_TREE", "SCREEN_READER"]}
severity_default: "serious"
---

# AV-DLG-001 — Modal dialogs have coherent name, focus, and background behavior

## User impact

Dialogs can lose focus, expose background controls or strand users on close. Affected users: blind, low-vision. Default severity is serious; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- dialog has an accessible name;
- focus moves into the dialog appropriately when it opens;
- modal background interaction is prevented when truly modal;
- keyboard focus remains in the modal interaction context while appropriate;
- close/complete controls are keyboard operable;
- focus returns to a logical location after close;
- do not assume `role="dialog"` or `aria-modal="true"` implements behavior.

---

## Applies to

Truly modal dialogs and their open/close/complete lifecycle.

## Does not apply / exceptions

Non-modal dialogs need different background/focus behavior. Escape is pattern guidance subject to task needs; an operable exit remains necessary. role="dialog" and aria-modal do not implement interaction.

## Failure patterns

```html
<div role="dialog" aria-modal="true" aria-label="Confirm"><button type="button">Confirm</button></div><button type="button">Background action</button>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<dialog aria-labelledby="confirm-title"><h2 id="confirm-title">Confirm change</h2><form method="dialog"><button value="cancel">Cancel</button><button value="confirm">Confirm</button></form></dialog>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Open from its trigger, check suitable initial focus and name, traverse content, attempt background interaction, close/complete and verify logical restored focus.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A well-named dialog has correct ARIA but opening, background inertness and focus restoration are not observed.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Use native modal dialog behavior where appropriate and manage initial/return focus for the actual workflow. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Assuming aria-modal alone traps focus or making the entire page aria-hidden while it contains the dialog. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-DLG-001.md)
- [pass case](../../../evals/fixtures/pass/AV-DLG-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-DLG-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 2.1.1 (A)](https://www.w3.org/TR/WCAG22/#keyboard)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html)
- [WCAG 2.2 SC 2.1.2 (A)](https://www.w3.org/TR/WCAG22/#no-keyboard-trap)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html)
- [WCAG 2.2 SC 2.4.3 (A)](https://www.w3.org/TR/WCAG22/#focus-order)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html)
- [WCAG 2.2 SC 4.1.2 (A)](https://www.w3.org/TR/WCAG22/#name-role-value)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [WAI-ARIA 1.2 roles and author requirements](https://www.w3.org/TR/wai-aria-1.2/#roles)
- [WAI-ARIA 1.2 states and properties](https://www.w3.org/TR/wai-aria-1.2/#states_and_properties)
- [AccName 1.1 computation](https://www.w3.org/TR/accname-1.1/#mapping_additional_nd_te)
- [APG Read Me First (informative)](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)
- [APG patterns (informative)](https://www.w3.org/WAI/ARIA/apg/patterns/)
