---
id: "AV-CON-001"
title: "Text meets minimum contrast"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.4.3", "level": "AA"}]
users: ["low-vision", "color-vision-deficiency"]
categories: ["visual-presentation"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "COMPUTED_STYLE", "VISUAL_INSPECTION"]}
severity_default: "moderate"
---

# AV-CON-001 — Text meets minimum contrast

## User impact

Low text contrast makes reading harder for low-vision and color-vision-deficient users. Affected users: low-vision, color-vision-deficiency. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Minimums:

- normal text: **4.5:1**;
- large-scale text: **3:1**;
- large-scale definition must follow WCAG rather than arbitrary CSS breakpoints (approximately 18pt regular or 14pt bold, with the actual WCAG definition controlling).

Requirements:

- evaluate relevant states including hover/focus/placeholder text when they are text presented to users;
- logos/logotypes and other normative exceptions must be handled correctly;
- never invent a ratio when gradients, images, transparency, blending, overlays, or unresolved CSS variables make the rendered colors uncertain;
- if final colors cannot be determined, use `CANNOT_VERIFY` or `NEEDS_REVIEW`.

## Applies to

Text and images of text in relevant normal, hover, focus, placeholder/help/error and theme states.

## Does not apply / exceptions

Inactive components, incidental text, logos/logotypes and other normative exceptions require contextual review. Large text uses the WCAG definition, not a mobile breakpoint.

## Failure patterns

```html
<p style="color:#aaa;background:#fff;font-size:16px">Important delivery instructions</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<p style="color:#111;background:#fff;font-size:16px">Important delivery instructions</p>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Resolve rendered foreground and adjacent background, opacity/compositing, font size/weight and states. Compute WCAG relative-luminance ratio: (lighter+0.05)/(darker+0.05); use sRGB linearization, do not round a subthreshold value up. Normal text requires 4.5:1; large text requires 3:1 (18pt regular or 14pt bold per WCAG).
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: Foreground uses a theme variable over a translucent gradient/image; final colors cannot be resolved.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Adjust the nearest suitable design token or background while preserving hierarchy and all themes. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Fabricating ratios from unresolved colors or exempting placeholder/help text merely because it looks secondary. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-CON-001.md)
- [pass case](../../../evals/fixtures/pass/AV-CON-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-CON-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.4.3 (AA)](https://www.w3.org/TR/WCAG22/#contrast-minimum)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
