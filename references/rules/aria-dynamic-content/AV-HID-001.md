---
id: "AV-HID-001"
title: "Hidden and inert content is exposed consistently"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "4.1.2", "level": "A"}, {"criterion": "2.4.3", "level": "A"}, {"criterion": "2.1.1", "level": "A"}]
users: ["blind"]
categories: ["aria-dynamic-content"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT", "RENDERED_DOM", "KEYBOARD_INTERACTION", "ACCESSIBILITY_TREE"]}
severity_default: "serious"
---

# AV-HID-001 — Hidden and inert content is exposed consistently

## User impact

Focus on content absent from the accessibility tree creates disorientation or inoperable controls. Affected users: blind. Default severity is serious; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- `aria-hidden="true"` must not hide focusable/interactable content from the accessibility tree while leaving it operable;
- inactive modal background content should not remain unexpectedly reachable when the modal is truly modal;
- visually hidden accessible text must not be clipped in a way that becomes visible/broken under user settings unless designed to do so;
- hidden UI state should be consistent across visual presentation, focusability, and accessibility exposure.

## Applies to

Hidden, inert, inactive and visually hidden content with semantic/focus exposure.

## Does not apply / exceptions

aria-hidden on noninteractive decoration can be appropriate. Content genuinely hidden and unfocusable is different from visually hidden text intended for AT.

## Failure patterns

```html
<button type="button" aria-hidden="true">Continue</button>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<div hidden><button type="button">Inactive action</button></div><button type="button">Continue</button>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Compare visibility, tree exposure and sequential/programmatic focus across transitions. Check ancestors as well as controls and modal background reachability.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: An inactive drawer has aria-hidden but descendants and focus state depend on uninspected code.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Align hidden/inert state with actual interaction; keep required AT text exposed. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Using aria-hidden as a focus blocker or putting aria-hidden on a focusable ancestor. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-HID-001.md)
- [pass case](../../../evals/fixtures/pass/AV-HID-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-HID-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 4.1.2 (A)](https://www.w3.org/TR/WCAG22/#name-role-value)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [WCAG 2.2 SC 2.4.3 (A)](https://www.w3.org/TR/WCAG22/#focus-order)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html)
- [WCAG 2.2 SC 2.1.1 (A)](https://www.w3.org/TR/WCAG22/#keyboard)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html)
- [WAI-ARIA 1.2 roles and author requirements](https://www.w3.org/TR/wai-aria-1.2/#roles)
- [WAI-ARIA 1.2 states and properties](https://www.w3.org/TR/wai-aria-1.2/#states_and_properties)
- [AccName 1.1 computation](https://www.w3.org/TR/accname-1.1/#mapping_additional_nd_te)
