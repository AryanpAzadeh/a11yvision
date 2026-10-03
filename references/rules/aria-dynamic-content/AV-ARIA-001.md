---
id: "AV-ARIA-001"
title: "ARIA roles, states, and properties are valid and truthful"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "4.1.2", "level": "A"}]
users: ["blind"]
categories: ["aria-dynamic-content"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT", "RENDERED_DOM", "ACCESSIBILITY_TREE"]}
severity_default: "serious"
---

# AV-ARIA-001 — ARIA roles, states, and properties are valid and truthful

## User impact

Incorrect role or state makes assistive technology report misleading controls. Affected users: blind. Default severity is serious; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- role/state/property must match actual behavior;
- required ARIA attributes for a role must be present when applicable;
- unsupported attributes should not be used;
- state values such as `aria-expanded`, `aria-selected`, `aria-checked`, `aria-pressed`, and `aria-current` must track real UI state;
- do not override useful native semantics unnecessarily.

The rule must prominently repeat the APG principle: **No ARIA is better than bad ARIA.**

## Applies to

Authored ARIA roles, states, properties and their behavioral contracts.

## Does not apply / exceptions

Useful native semantics need no redundant role. APG keyboard patterns are informative, while WAI-ARIA author requirements are normative.

## Failure patterns

```html
<button type="button" aria-expanded="true" aria-controls="panel">Details</button><div id="panel" hidden>Details</div>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<button type="button" aria-expanded="false" aria-controls="panel">Details</button><div id="panel" hidden>Details</div>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Check role-supported and required properties, valid values, referenced IDs and native conflicts; operate state changes and compare visual and exposed state.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: Correct initial aria-expanded is supplied but state synchronization after activation is unknown.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Remove unnecessary ARIA and synchronize needed states with actual behavior. No ARIA is better than bad ARIA. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Treating ARIA presence as accessibility or applying unsupported properties just to satisfy a checker. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-ARIA-001.md)
- [pass case](../../../evals/fixtures/pass/AV-ARIA-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-ARIA-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 4.1.2 (A)](https://www.w3.org/TR/WCAG22/#name-role-value)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [WAI-ARIA 1.2 roles and author requirements](https://www.w3.org/TR/wai-aria-1.2/#roles)
- [WAI-ARIA 1.2 states and properties](https://www.w3.org/TR/wai-aria-1.2/#states_and_properties)
- [AccName 1.1 computation](https://www.w3.org/TR/accname-1.1/#mapping_additional_nd_te)
- [APG Read Me First (informative)](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)
- [APG patterns (informative)](https://www.w3.org/WAI/ARIA/apg/patterns/)
