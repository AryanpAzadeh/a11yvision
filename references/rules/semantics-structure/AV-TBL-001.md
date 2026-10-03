---
id: "AV-TBL-001"
title: "Data tables expose header and cell relationships"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.3.1", "level": "A"}]
users: ["blind", "low-vision"]
categories: ["semantics-structure"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "ACCESSIBILITY_TREE"]}
severity_default: "moderate"
---

# AV-TBL-001 — Data tables expose header and cell relationships

## User impact

Unexposed headers make data cells difficult to interpret during table navigation. Affected users: blind, low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- use semantic table structures for tabular data;
- headers must be programmatically related to data cells as needed;
- provide a useful caption when it identifies/purposes the table;
- complex tables may require explicit `scope`, `headers`/`id`, or restructuring;
- do not use data-table semantics for layout-only presentation.

## Applies to

Genuine tabular data and its row/column relationships.

## Does not apply / exceptions

Layout-only tables must not acquire data relationships; a caption is useful when it identifies the table but is not universally required. Simple native header associations can work without explicit headers attributes.

## Failure patterns

```html
<table><tr><td>Month</td><td>Units</td></tr><tr><td>January</td><td>10</td></tr></table>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<table><caption>Monthly units</caption><tr><th scope="col">Month</th><th scope="col">Units</th></tr><tr><th scope="row">January</th><td>10</td></tr></table>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Identify each data cell's needed context; check associations, spans and referenced IDs. Navigate representative complex cells with AT.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete source demonstrating the applicable relationships, with purpose established; rendered/accessibility evidence when the final output or relationships cannot be resolved from source.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A complex table has merged cells and ambiguous headers; source presence of th is insufficient.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For subjective content, inspect purpose and meaning before reporting success; syntax alone is not enough. Do not infer unavailable component output.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Use semantic headers and suitable scope or headers/id associations; simplify complex relationships where product meaning permits. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Adding role="table" to a visual layout or treating every th as proof of correct association. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete source demonstrating the applicable relationships, with purpose established; rendered/accessibility evidence when the final output or relationships cannot be resolved from source. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-TBL-001.md)
- [pass case](../../../evals/fixtures/pass/AV-TBL-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-TBL-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.3.1 (A)](https://www.w3.org/TR/WCAG22/#info-and-relationships)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html)
