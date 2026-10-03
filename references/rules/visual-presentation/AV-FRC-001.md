---
id: "AV-FRC-001"
title: "Author styling remains usable in forced-colors/high-contrast environments"
version: "0.1.0"
status: "active"
scope: "advisory"
wcag: []
users: ["low-vision"]
categories: ["visual-presentation"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "COMPUTED_STYLE", "VISUAL_INSPECTION"]}
severity_default: "advisory"
---

# AV-FRC-001 — Author styling remains usable in forced-colors/high-contrast environments

## User impact

Disappearing affordances under forced colors can make controls and states harder to perceive. Affected users: low-vision. Default severity is advisory; adjust for actual task impact rather than WCAG level.

## Requirement

This is an advisory resilience check. A FAIL denotes a demonstrated advisory concern, not an independent WCAG A/AA violation.

Requirements:

- do not erase native focus/control affordances in forced-colors mode;
- do not encode critical information only in background images/colors that disappear;
- use system-color/forced-color-aware techniques when custom styling otherwise removes meaning;
- this rule MUST NOT be reported as an independent WCAG A/AA failure unless another mapped Success Criterion is also demonstrated.

## Applies to

Authored styles tested in forced-colors/high-contrast environments.

## Does not apply / exceptions

This is advisory. A specific independently demonstrated mapped criterion failure must be reported under that other rule; do not invent a forced-colors A/AA criterion.

## Failure patterns

```html
<button type="button" style="border:0;outline:0;box-shadow:0 0 0 2px red">Continue</button>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<button type="button" style="border:2px solid currentColor">Continue</button>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Activate an actual forced-colors environment; inspect control boundaries, focus, state cues and meaningful graphics. Record the environment and distinguish advisory concerns from separate criterion evidence.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: Styles use system colors but focus, icons and selected states have not been rendered in forced colors.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Preserve native affordances, use system-aware borders/colors, and avoid unnecessary forced-color-adjust:none. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Calling this an independent WCAG failure or disabling forced colors globally. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-FRC-001.md)
- [pass case](../../../evals/fixtures/pass/AV-FRC-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-FRC-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [CSS Color Adjustment: forced colors](https://www.w3.org/TR/css-color-adjust-1/#forced-colors-mode) (platform guidance; advisory scope)
- [WCAG 2.2 Focus Visible, only if separately demonstrated](https://www.w3.org/TR/WCAG22/#focus-visible)
