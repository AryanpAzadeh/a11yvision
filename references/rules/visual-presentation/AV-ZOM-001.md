---
id: "AV-ZOM-001"
title: "Text can be resized to 200% without loss of content or functionality"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.4.4", "level": "AA"}]
users: ["low-vision"]
categories: ["visual-presentation"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "RENDERED_GEOMETRY", "VISUAL_INSPECTION"]}
severity_default: "moderate"
---

# AV-ZOM-001 — Text can be resized to 200% without loss of content or functionality

## User impact

Clipped enlarged text can remove instructions or controls needed to complete a task. Affected users: low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- test enlargement without assistive technology as intended by the criterion;
- detect clipped labels, overlapping text, disappearing controls, truncated form values, or inaccessible functionality;
- fixed pixel font sizes are not automatically a WCAG failure if browser zoom still works; evaluate behavior rather than applying a simplistic unit ban.

## Applies to

Text resizing without assistive technology up to 200%.

## Does not apply / exceptions

Captions and images of text have criterion exceptions; pixel units alone are not a failure when browser enlargement works.

## Failure patterns

```html
<div style="height:20px;overflow:hidden"><label>Delivery address <input></label></div>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<div style="min-height:20px"><label>Delivery address <input></label></div>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Enlarge to 200% using supported browser resizing; complete representative flows and check clipping, overlap, form values and missing actions. Record starting size and method.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: CSS uses fixed pixel fonts but no 200% resize test is available.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Allow containers and text to grow and wrap; keep labels, values and actions available. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Banning px mechanically or declaring responsive CSS sufficient evidence. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-ZOM-001.md)
- [pass case](../../../evals/fixtures/pass/AV-ZOM-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-ZOM-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.4.4 (AA)](https://www.w3.org/TR/WCAG22/#resize-text)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)
