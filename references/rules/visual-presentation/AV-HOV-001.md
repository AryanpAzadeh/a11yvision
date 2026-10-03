---
id: "AV-HOV-001"
title: "Additional content shown on hover or focus is dismissible, hoverable, and persistent"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.4.13", "level": "AA"}]
users: ["low-vision"]
categories: ["visual-presentation"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "KEYBOARD_INTERACTION", "POINTER_INTERACTION", "VISUAL_INSPECTION"]}
severity_default: "moderate"
---

# AV-HOV-001 — Additional content shown on hover or focus is dismissible, hoverable, and persistent

## User impact

Disappearing or unreachable additional content can be difficult to read under magnification. Affected users: low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Applies to examples such as:

- custom tooltips;
- non-modal popovers;
- hover/focus submenus.

Requirements when the criterion applies:

- **dismissible** without moving hover/focus when required;
- **hoverable** when pointer hover triggers the additional content;
- **persistent** until trigger is removed, user dismisses it, or information becomes invalid.

Source-only inspection cannot generally prove all three.

## Applies to

Author-controlled additional content triggered by hover or focus, such as tooltips and submenus.

## Does not apply / exceptions

User-agent-controlled content is excepted; dismissibility has an exception when content does not obscure or replace other content. Hoverability applies when hover triggers content.

## Failure patterns

```html
<button title="Native title is not this failing custom popup">Help</button><div role="tooltip">Custom help</div><p>Scenario: the custom help obscures text, disappears on pointer entry and cannot be dismissed without moving focus.</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<button type="button" aria-describedby="help">Help</button><span id="help">Delivery takes two days.</span>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Trigger with pointer and focus; attempt dismissal without moving either when required; move pointer into the popup; keep trigger active and verify persistence until dismissal, trigger removal or invalidation.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: Popup code has an Escape handler but pointer reachability and persistence have not been observed.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Repair dismissal, pointer reachability and persistence; use static associated help when it preserves intent. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Auto-hiding on a timer or calling an Escape handler proof of all three conditions. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-HOV-001.md)
- [pass case](../../../evals/fixtures/pass/AV-HOV-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-HOV-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.4.13 (AA)](https://www.w3.org/TR/WCAG22/#content-on-hover-or-focus)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html)
