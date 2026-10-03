---
id: "AV-HDG-001"
title: "Headings expose meaningful document structure"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.3.1", "level": "A"}, {"criterion": "2.4.6", "level": "AA"}]
users: ["blind", "low-vision"]
categories: ["semantics-structure"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT"]}
severity_default: "moderate"
---

# AV-HDG-001 — Headings expose meaningful document structure

## User impact

Missing structural headings make section navigation and orientation harder. Affected users: blind, low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- content that functions as a heading should be programmatically identifiable as a heading;
- heading text should describe the section;
- do not fail merely because a numeric level is skipped without understanding structure; evaluate hierarchy and relationships, not a simplistic “never skip a heading level” rule;
- avoid using headings only for visual styling.

## Applies to

Content that functions as a heading and its document hierarchy.

## Does not apply / exceptions

A skipped numeric level is not an automatic failure; assess relationships. WCAG does not impose a universal one-h1 rule.

## Failure patterns

```html
<p class="large-bold">Delivery options</p><p>Choose collection or shipping.</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<h2>Delivery options</h2><p>Choose collection or shipping.</p>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Compare visual/content section relationships with semantic headings and descriptive text. Inspect the complete hierarchy before judging a skipped level.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A page skips h2 but the supplied excerpt lacks its surrounding hierarchy.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For subjective content, inspect purpose and meaning before reporting success; syntax alone is not enough. Do not infer unavailable component output.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Use heading elements at levels representing actual relationships and keep styling independent of levels. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Renumbering headings blindly or inserting empty headings for a tidy outline. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-HDG-001.md)
- [pass case](../../../evals/fixtures/pass/AV-HDG-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-HDG-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.3.1 (A)](https://www.w3.org/TR/WCAG22/#info-and-relationships)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html)
- [WCAG 2.2 SC 2.4.6 (AA)](https://www.w3.org/TR/WCAG22/#headings-and-labels)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html)
