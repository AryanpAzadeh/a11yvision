---
id: "AV-FOC-003"
title: "Focused components are not completely obscured by author-created content"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "2.4.11", "level": "AA"}]
users: ["low-vision"]
categories: ["keyboard-focus"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "RENDERED_GEOMETRY", "VISUAL_INSPECTION", "KEYBOARD_INTERACTION"]}
severity_default: "moderate"
---

# AV-FOC-003 — Focused components are not completely obscured by author-created content

## User impact

Fully covered focused controls can become impossible to locate under zoom or overlays. Affected users: low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- sticky headers/footers, cookie banners, chat widgets, overlays, and similar authored layers must not fully hide the focused component;
- this cannot be definitively passed from source alone;
- test across relevant breakpoints and zoomed/reflow layouts;
- fixes may include scroll padding, layout changes, or modal behavior where appropriate.

## Applies to

Focused components affected by author-created layers, sticky UI and reflow layouts.

## Does not apply / exceptions

AA 2.4.11 prohibits complete obscuring; partial obscuring alone is not this AA failure, though broader guidance may help. User-opened content has the criterion's reveal-without-advancing-focus qualification; record it.

## Failure patterns

```html
<div style="position:fixed;inset:0;background:white">Persistent authored overlay</div><button type="button">Continue</button>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<main style="padding-block:4rem"><button type="button">Continue</button></main>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Focus each affected component across breakpoints and zoom; compare its bounds with authored occluding layers and available reveal behavior.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: scroll-padding is present but overlay dimensions and focused geometry are unavailable.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Adjust scroll padding, reserved space or overlay lifecycle so the component is not fully covered. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Claiming source-only pass or treating any partial overlap as an AA 2.4.11 failure. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-FOC-003.md)
- [pass case](../../../evals/fixtures/pass/AV-FOC-003.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-FOC-003.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 2.4.11 (AA)](https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)
