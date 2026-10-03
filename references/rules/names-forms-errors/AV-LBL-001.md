---
id: "AV-LBL-001"
title: "Form controls have persistent programmatic labels"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.3.1", "level": "A"}, {"criterion": "3.3.2", "level": "A"}, {"criterion": "4.1.2", "level": "A"}]
users: ["blind", "low-vision"]
categories: ["names-forms-errors"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT"]}
severity_default: "serious"
---

# AV-LBL-001 — Form controls have persistent programmatic labels

## User impact

Disappearing prompts and missing associations make forms hard to understand and revisit. Affected users: blind, low-vision. Default severity is serious; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- inputs requiring user understanding need labels/instructions appropriate to purpose;
- placeholder text must not be treated as a general replacement for a persistent label;
- visible labels should be programmatically associated with controls;
- groups such as radio/checkbox sets should expose group context where needed.

## Applies to

Inputs needing labels or instructions and groups needing shared context.

## Does not apply / exceptions

Submit buttons may be named by their text/value. Hidden inputs need no visible label. An accessible name alone does not always meet visible instruction needs.

## Failure patterns

```html
<input type="email" placeholder="Email address">
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<label for="email">Email address</label><input id="email" type="email" autocomplete="email">
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Check persistent visible labels, programmatic association, instructions and group context; inspect fieldset/legend or equivalent where meaningful.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: An input has aria-label but the complete form's visible instructions and group context are unavailable.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For subjective content, inspect purpose and meaning before reporting success; syntax alone is not enough. Do not infer unavailable component output.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Associate visible labels and use native grouping; retain placeholder only as supplementary help. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Replacing every visible label with aria-label or hiding instructions needed by low-vision users. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-LBL-001.md)
- [pass case](../../../evals/fixtures/pass/AV-LBL-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-LBL-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.3.1 (A)](https://www.w3.org/TR/WCAG22/#info-and-relationships)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html)
- [WCAG 2.2 SC 3.3.2 (A)](https://www.w3.org/TR/WCAG22/#labels-or-instructions)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html)
- [WCAG 2.2 SC 4.1.2 (A)](https://www.w3.org/TR/WCAG22/#name-role-value)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [WAI-ARIA 1.2 roles and author requirements](https://www.w3.org/TR/wai-aria-1.2/#roles)
- [WAI-ARIA 1.2 states and properties](https://www.w3.org/TR/wai-aria-1.2/#states_and_properties)
- [AccName 1.1 computation](https://www.w3.org/TR/accname-1.1/#mapping_additional_nd_te)
