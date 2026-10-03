---
id: "AV-KBD-001"
title: "All required functionality is keyboard operable"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "2.1.1", "level": "A"}]
users: ["blind", "low-vision"]
categories: ["keyboard-focus"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "KEYBOARD_INTERACTION"]}
severity_default: "serious"
---

# AV-KBD-001 — All required functionality is keyboard operable

## User impact

Mouse-only functionality can block core tasks for keyboard users. Affected users: blind, low-vision. Default severity is serious; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- functionality must be usable through a keyboard interface when the criterion applies;
- a click handler on a focusable element does not automatically prove correct keyboard activation behavior;
- test native and custom controls in the actual interaction flow;
- do not count mouse-emulated activation by assistive software as source evidence.

## Applies to

All functionality subject to the keyboard-interface requirement.

## Does not apply / exceptions

Functions inherently dependent on the path of movement have a criterion exception; a freehand drawing tool differs from choosing its color or submitting it.

## Failure patterns

```html
<div tabindex="0" onclick="save()">Save</div>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<button type="button">Save</button>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Use keyboard alone through the complete task; test native activation keys, widget-specific keys and completion, including disabled and error states.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A focusable custom control has a click handler but the keyboard event implementation is not known.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Use native controls and preserve actions; implement genuinely necessary custom keyboard behavior completely. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Assuming focusability or mouse-emulated AT activation proves keyboard functionality. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-KBD-001.md)
- [pass case](../../../evals/fixtures/pass/AV-KBD-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-KBD-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 2.1.1 (A)](https://www.w3.org/TR/WCAG22/#keyboard)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html)
