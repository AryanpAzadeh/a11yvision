---
id: "AV-SEQ-001"
title: "DOM/source sequence preserves meaning and operation"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.3.2", "level": "A"}, {"criterion": "2.4.3", "level": "A"}]
users: ["blind", "low-vision"]
categories: ["semantics-structure"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "RENDERED_GEOMETRY", "VISUAL_INSPECTION", "KEYBOARD_INTERACTION"]}
severity_default: "moderate"
---

# AV-SEQ-001 — DOM/source sequence preserves meaning and operation

## User impact

Reading and focus sequences that change meaning can confuse task completion. Affected users: blind, low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- meaningful reading order should be preserved independent of visual layout;
- CSS Grid/Flex `order`, absolute positioning, and responsive rearrangements must not create a visual order that materially conflicts with DOM reading/focus order;
- source-only inspection may find risks but often cannot prove the rendered relationship.

## Applies to

Layouts where order matters to information or operation, including CSS rearrangement.

## Does not apply / exceptions

Multiple orders may preserve meaning; decorative rearrangement or independent cards are not automatically failures.

## Failure patterns

```html
<div style="display:flex"><p style="order:2">Step 2: confirm address</p><p style="order:1">Step 1: choose delivery</p></div>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<div><p>Step 1: choose delivery</p><p>Step 2: confirm address</p></div>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Compare DOM reading order, rendered sequence and keyboard sequence at affected breakpoints. Determine whether the difference changes meaning or operation.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: CSS Grid order differs from DOM order but no rendered layout or dependency between items is known.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Correct source order to preserve meaningful sequence; use layout without creating contradictory task order. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Using positive tabindex to imitate visual order or declaring every CSS order use a failure. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-SEQ-001.md)
- [pass case](../../../evals/fixtures/pass/AV-SEQ-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-SEQ-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.3.2 (A)](https://www.w3.org/TR/WCAG22/#meaningful-sequence)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence.html)
- [WCAG 2.2 SC 2.4.3 (A)](https://www.w3.org/TR/WCAG22/#focus-order)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html)
