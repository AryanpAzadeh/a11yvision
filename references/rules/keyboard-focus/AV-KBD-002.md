---
id: "AV-KBD-002"
title: "Keyboard focus cannot become trapped"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "2.1.2", "level": "A"}]
users: ["blind", "low-vision"]
categories: ["keyboard-focus"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "KEYBOARD_INTERACTION"]}
severity_default: "serious"
---

# AV-KBD-002 — Keyboard focus cannot become trapped

## User impact

Inescapable focus traps prevent users from continuing or leaving a task. Affected users: blind, low-vision. Default severity is serious; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- users can move focus away using standard navigation, or are clearly informed of a non-standard exit mechanism where allowed;
- modal dialogs may intentionally contain focus while open but must provide an operable way to close/complete and return focus appropriately;
- embedded editors and rich widgets require careful review.

## Applies to

Focusable regions, editors, embedded content and modal contexts.

## Does not apply / exceptions

A modal can contain focus while open if completion/close is operable and exit is coherent; an allowed nonstandard exit must be explained.

## Failure patterns

```html
<div role="dialog" aria-modal="true" aria-label="Notice"><input aria-label="Response"><p>Scenario: Tab cycles here forever and no close, completion or documented exit works.</p></div>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<dialog open aria-labelledby="notice"><h2 id="notice">Notice</h2><form method="dialog"><button>Close</button></form></dialog>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Enter each region, attempt Tab/Shift+Tab and documented exits, and complete or cancel modal flows. Record whether users can leave and resume the task.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A modal cycles Tab internally; operable close/return behavior has not been tested.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Provide a reachable operable exit or completion and sensible return focus. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Removing legitimate modal containment or adding an undocumented obscure exit shortcut. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-KBD-002.md)
- [pass case](../../../evals/fixtures/pass/AV-KBD-002.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-KBD-002.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 2.1.2 (A)](https://www.w3.org/TR/WCAG22/#no-keyboard-trap)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html)
