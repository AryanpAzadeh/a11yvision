---
id: "AV-REF-001"
title: "Content reflows at narrow equivalent viewport without two-dimensional scrolling except allowed content"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.4.10", "level": "AA"}]
users: ["low-vision"]
categories: ["visual-presentation"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "RENDERED_GEOMETRY", "VISUAL_INSPECTION"]}
severity_default: "moderate"
---

# AV-REF-001 — Content reflows at narrow equivalent viewport without two-dimensional scrolling except allowed content

## User impact

Two-dimensional scrolling for ordinary content makes reading difficult under magnification. Affected users: low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- test at the WCAG reflow dimensions/conditions, commonly represented by content reflowing at a width equivalent to **320 CSS pixels** for vertically scrolling content;
- content should not require scrolling in two dimensions for ordinary reading/use;
- recognize allowed exceptions for content requiring two-dimensional layout for meaning or use, such as some data tables, maps, diagrams, video, games, and presentations;
- a responsive mobile breakpoint is not automatically proof of conformance;
- fixed/sticky elements must be considered at magnified layouts.

## Applies to

Vertical scrolling content at 320 CSS px width and horizontal scrolling content at 256 CSS px height under WCAG conditions.

## Does not apply / exceptions

Genuine content requiring two-dimensional layout, such as some data tables/maps/diagrams, may be excepted; surrounding headings, controls and prose still need review.

## Failure patterns

```html
<main style="width:900px"><p style="white-space:nowrap">Ordinary reading text extends beyond the narrow viewport.</p><button>Continue</button></main>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<main style="max-width:100%;overflow-wrap:anywhere"><p>Ordinary reading text can wrap in the available width.</p><button>Continue</button></main>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Test width equivalent to 320 CSS px (often 1280px viewport at 400% zoom) or 256 CSS px height for horizontal content. Check two-dimensional scrolling, loss, fixed UI and task completion; record each justified exception.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A 320px layout includes a genuine data table; table overflow is known but surrounding reading and actions are untested.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Use flexible layout and wrapping; localize necessary table/map scrolling rather than clipping or destroying relationships. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Calling every table overflow a failure or assuming a mobile breakpoint proves reflow. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-REF-001.md)
- [pass case](../../../evals/fixtures/pass/AV-REF-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-REF-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.4.10 (AA)](https://www.w3.org/TR/WCAG22/#reflow)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
