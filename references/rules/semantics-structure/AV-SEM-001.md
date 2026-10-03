---
id: "AV-SEM-001"
title: "Prefer native semantic elements over simulated controls"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.3.1", "level": "A"}, {"criterion": "2.1.1", "level": "A"}, {"criterion": "4.1.2", "level": "A"}]
users: ["blind", "low-vision"]
categories: ["semantics-structure"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT", "RENDERED_DOM", "KEYBOARD_INTERACTION"]}
severity_default: "moderate"
---

# AV-SEM-001 — Prefer native semantic elements over simulated controls

## User impact

Simulated controls may hide their role or prevent keyboard operation. Affected users: blind, low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- use native `button`, `a`, `input`, `select`, `textarea`, headings, lists, and table elements when they match the intended behavior;
- a `div`/`span` with `role="button"` is not equivalent unless role, focusability, keyboard interaction, states, and behavior are all correctly implemented;
- native semantics are the preferred remediation when practical.

## Applies to

Content and actions whose intended behavior matches a native HTML element.

## Does not apply / exceptions

Custom controls can satisfy requirements when semantics and complete behavior are equivalent; custom markup alone is not a failure.

## Failure patterns

```html
<span class="save" onclick="save()">Save</span>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<button type="button">Save</button>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Determine intended action; inspect all name, role, state and event implementations. Test Tab, Enter and Space where button behavior is intended.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A div has role="button" and tabindex="0" but its event implementation is not supplied.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Replace simulated controls with native buttons or links as appropriate; preserve handlers and styling. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Adding only a role or tabindex while leaving mouse-only operation. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-SEM-001.md)
- [pass case](../../../evals/fixtures/pass/AV-SEM-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-SEM-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.3.1 (A)](https://www.w3.org/TR/WCAG22/#info-and-relationships)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html)
- [WCAG 2.2 SC 2.1.1 (A)](https://www.w3.org/TR/WCAG22/#keyboard)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html)
- [WCAG 2.2 SC 4.1.2 (A)](https://www.w3.org/TR/WCAG22/#name-role-value)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [WAI-ARIA 1.2 roles and author requirements](https://www.w3.org/TR/wai-aria-1.2/#roles)
- [WAI-ARIA 1.2 states and properties](https://www.w3.org/TR/wai-aria-1.2/#states_and_properties)
- [AccName 1.1 computation](https://www.w3.org/TR/accname-1.1/#mapping_additional_nd_te)
