---
id: "AV-VIS-001"
title: "Visually hidden content patterns remain robust under zoom and user styles"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.4.4", "level": "AA"}, {"criterion": "1.4.10", "level": "AA"}, {"criterion": "2.4.1", "level": "A"}, {"criterion": "4.1.2", "level": "A"}]
users: ["blind", "low-vision"]
categories: ["visual-presentation"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "RENDERED_GEOMETRY", "VISUAL_INSPECTION", "KEYBOARD_INTERACTION", "ACCESSIBILITY_TREE"]}
severity_default: "moderate"
---

# AV-VIS-001 — Visually hidden content patterns remain robust under zoom and user styles

## User impact

Hidden labels can vanish from AT or create clipped focus and fragments under zoom. Affected users: blind, low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- visually-hidden text intended for AT remains available to AT;
- skip links intended to become visible on focus actually become visible;
- hiding techniques must not create unintended tiny scroll areas, clipped focused elements, or visible fragments at zoom;
- do not use `display:none`, `hidden`, or `visibility:hidden` for text that must remain available to screen readers.

---

## Applies to

Text meant for AT, visually hidden utilities and focus-revealed skip links.

## Does not apply / exceptions

Content truly inactive should be hidden from everyone; focus-revealed content is intentionally visible on focus. Map a conformance finding to the actual violated criterion, not the utility name.

## Failure patterns

```html
<button type="button"><span style="display:none">Close</span><span aria-hidden="true">×</span></button>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<button type="button">Close</button>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Inspect exposure of required text; focus skip links and inspect actual visibility and destination. At zoom/user styles check fragments, tiny scroll areas and clipping; map observed effects to the relevant criterion.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A clipped visually-hidden class has not been tested at zoom or with focus and user styles.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Use a tested hiding utility only when visually hidden copy is needed; reveal focusable skip links on focus. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

display:none, hidden or visibility:hidden for required AT text; hiding focused controls without making them visible. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-VIS-001.md)
- [pass case](../../../evals/fixtures/pass/AV-VIS-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-VIS-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.4.4 (AA)](https://www.w3.org/TR/WCAG22/#resize-text)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)
- [WCAG 2.2 SC 1.4.10 (AA)](https://www.w3.org/TR/WCAG22/#reflow)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- [WCAG 2.2 SC 2.4.1 (A)](https://www.w3.org/TR/WCAG22/#bypass-blocks)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html)
- [WCAG 2.2 SC 4.1.2 (A)](https://www.w3.org/TR/WCAG22/#name-role-value)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [WAI-ARIA 1.2 roles and author requirements](https://www.w3.org/TR/wai-aria-1.2/#roles)
- [WAI-ARIA 1.2 states and properties](https://www.w3.org/TR/wai-aria-1.2/#states_and_properties)
- [AccName 1.1 computation](https://www.w3.org/TR/accname-1.1/#mapping_additional_nd_te)
