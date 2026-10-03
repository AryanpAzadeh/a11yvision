---
id: "AV-CHT-001"
title: "Data visualizations do not depend on color alone and expose equivalent data/meaning"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.4.1", "level": "A"}, {"criterion": "1.1.1", "level": "A"}, {"criterion": "1.4.11", "level": "AA"}]
users: ["blind", "low-vision", "color-vision-deficiency"]
categories: ["visual-presentation"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT", "RENDERED_DOM", "COMPUTED_STYLE", "VISUAL_INSPECTION"]}
severity_default: "moderate"
---

# AV-CHT-001 — Data visualizations do not depend on color alone and expose equivalent data/meaning

## User impact

Color-only series and missing data equivalents conceal a chart's conclusions. Affected users: blind, low-vision, color-vision-deficiency. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- chart series must be differentiable without hue alone when color conveys information;
- use labels, patterns, marker shapes, line styles, direct annotation, or equivalent cues;
- meaningful graphical elements should satisfy applicable non-text contrast;
- provide a nonvisual route to the important data/conclusion;
- avoid massive inaccessible `aria-label` strings as a substitute for structured data.

## Applies to

Meaningful chart series, legends, graphical details and nonvisual equivalents.

## Does not apply / exceptions

Direct labels or patterns may fully differentiate red/green series; decorative graphics need no fabricated data. Contrast applies to required visual information, not every pixel.

## Failure patterns

```html
<img src="chart.svg" alt="Chart"><p>Scenario: unlabeled red/green lines alone distinguish two series; no figures or explanation exists.</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<h2>Monthly units</h2><p>Collection: January 10, February 15. Delivery: January 8, February 12. Both rise.</p><p>Scenario: the chart also directly labels Collection and Delivery with distinct solid/dashed lines and sufficient required graphical contrast.</p>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Check series differentiation without hue, structured data/meaning equivalence, and rendered contrast of necessary lines/regions against adjacent colors.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: Direct labels are present but it is unclear whether all series and relationships are explained or contrast is sufficient.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Add direct labels, distinct markers/line styles and an adjacent structured data/explanation route. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Giant inaccessible aria-label datasets or blanket failure merely because red and green are used. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-CHT-001.md)
- [pass case](../../../evals/fixtures/pass/AV-CHT-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-CHT-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.4.1 (A)](https://www.w3.org/TR/WCAG22/#use-of-color)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)
- [WCAG 2.2 SC 1.1.1 (A)](https://www.w3.org/TR/WCAG22/#non-text-content)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)
- [WCAG 2.2 SC 1.4.11 (AA)](https://www.w3.org/TR/WCAG22/#non-text-contrast)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
