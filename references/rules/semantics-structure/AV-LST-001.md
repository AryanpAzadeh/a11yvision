---
id: "AV-LST-001"
title: "List relationships are programmatically represented"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.3.1", "level": "A"}]
users: ["blind"]
categories: ["semantics-structure"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT"]}
severity_default: "moderate"
---

# AV-LST-001 — List relationships are programmatically represented

## User impact

Missing list relationships can hide grouping and item count during navigation. Affected users: blind. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- content that is meaningfully a list should expose list/list-item relationships when that structure matters;
- styling a series of `div`s with bullets does not necessarily expose list semantics;
- conversely, do not convert every visually repeated group into a list unless list semantics are meaningful.

## Applies to

Groups whose ordered, unordered or description-list relationships carry meaning.

## Does not apply / exceptions

Repeated cards do not necessarily form a meaningful list; avoid automatic conversion of every repeated container.

## Failure patterns

```html
<div>1. Choose delivery</div><div>2. Confirm address</div><p>These are ordered task steps.</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<ol><li>Choose delivery</li><li>Confirm address</li></ol>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Establish the grouping's meaning; compare visual grouping with exposed list/item relationships, including CSS effects on exposure.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: Repeated product cards may or may not express a list relationship in the actual interface.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For subjective content, inspect purpose and meaning before reporting success; syntax alone is not enough. Do not infer unavailable component output.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Use ol, ul or dl as appropriate while preserving visual design. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Inserting list roles everywhere simply because a loop produces repeated markup. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-LST-001.md)
- [pass case](../../../evals/fixtures/pass/AV-LST-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-LST-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.3.1 (A)](https://www.w3.org/TR/WCAG22/#info-and-relationships)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html)
