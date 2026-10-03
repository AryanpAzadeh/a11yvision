---
id: "AV-FOC-001"
title: "Keyboard focus is visible"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "2.4.7", "level": "AA"}]
users: ["low-vision"]
categories: ["keyboard-focus"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "COMPUTED_STYLE", "VISUAL_INSPECTION", "KEYBOARD_INTERACTION"]}
severity_default: "moderate"
---

# AV-FOC-001 — Keyboard focus is visible

## User impact

Invisible keyboard focus makes locating the current control difficult under magnification. Affected users: low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- keyboard focus must have a visible indicator;
- removing outlines is a failure risk unless an adequate replacement exists;
- source-only presence of `:focus` CSS is not proof that the indicator is visible in all relevant states/themes/backgrounds;
- custom focus styling should remain perceivable in high-contrast/forced-colors environments where practical.

## Applies to

Keyboard-operable components in all relevant rendered states.

## Does not apply / exceptions

The AA visible-focus requirement is not the AAA Focus Appearance metric. Native focus styles can satisfy it; custom styling is not mandatory.

## Failure patterns

```html
<style>button:focus {outline:none;box-shadow:none}</style><button type="button">Continue</button>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<style>button:focus-visible {outline:3px solid currentColor;outline-offset:3px}</style><button type="button">Continue</button>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Tab through each control, inspect the visible indicator across themes/backgrounds and zoom; check clipping and forced-colors resilience where practical.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: Focus utilities exist but clipping, background and theme colors are unresolved.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Retain native outline or supply an equally or more visible replacement in the design system. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Removing outlines without replacement or treating a focus class as rendered proof. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-FOC-001.md)
- [pass case](../../../evals/fixtures/pass/AV-FOC-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-FOC-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 2.4.7 (AA)](https://www.w3.org/TR/WCAG22/#focus-visible)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)
