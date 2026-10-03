---
id: "AV-TRG-001"
title: "Pointer targets meet WCAG 2.2 minimum target size or an allowed exception"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "2.5.8", "level": "AA"}]
users: ["low-vision"]
categories: ["visual-presentation"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "RENDERED_GEOMETRY", "VISUAL_INSPECTION"]}
severity_default: "moderate"
---

# AV-TRG-001 — Pointer targets meet WCAG 2.2 minimum target size or an allowed exception

## User impact

Dense small targets are hard to locate and acquire with magnification or larger pointers. Affected users: low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Baseline:

- target is at least **24 × 24 CSS pixels**, or satisfies a valid WCAG exception such as spacing, equivalent control, inline text, user-agent control, or essential presentation.

Requirements:

- do not fail every target under 24×24 without checking exceptions;
- do not claim the spacing exception without geometry evidence;
- include this rule because enlarged pointers, magnified interfaces, and dense UI can compound visual-access difficulty, while noting that the criterion primarily addresses target acquisition more broadly.

## Applies to

Pointer targets covered by 2.5.8, including dense icon controls.

## Does not apply / exceptions

Check spacing, same-page equivalent, inline, unmodified user-agent and essential presentation exceptions. Target acquisition benefits broader users as well as this visual-access scope.

## Failure patterns

```html
<button type="button" style="width:20px;height:20px;padding:0">A</button><button type="button" style="width:20px;height:20px;padding:0">B</button>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<button type="button" style="min-width:24px;min-height:24px">A</button><button type="button" style="min-width:24px;min-height:24px">B</button>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Measure actual hit areas in CSS pixels. Baseline is 24x24. For undersized targets, center 24px-diameter circles on bounding boxes: they must not intersect other targets or circles for other undersized targets. Review every exception before failure.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A 20x20 target may meet spacing: geometry and neighboring targets have not been measured.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Enlarge hit areas or spacing, or retain a documented valid equivalent/inline exception. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Failing every target under 24x24 or claiming spacing without geometry. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-TRG-001.md)
- [pass case](../../../evals/fixtures/pass/AV-TRG-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-TRG-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 2.5.8 (AA)](https://www.w3.org/TR/WCAG22/#target-size-minimum)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
