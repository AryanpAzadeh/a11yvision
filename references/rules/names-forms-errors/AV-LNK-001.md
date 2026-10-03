---
id: "AV-LNK-001"
title: "Link purpose is understandable in context"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "2.4.4", "level": "A"}]
users: ["blind", "low-vision"]
categories: ["names-forms-errors"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT"]}
severity_default: "moderate"
---

# AV-LNK-001 — Link purpose is understandable in context

## User impact

Ambiguous links make choosing a destination difficult in context or link navigation. Affected users: blind, low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- link purpose should be determinable from link text or its programmatically determined context;
- repeated “Read more” links require contextual evaluation rather than blanket failure;
- do not hide essential distinguishing information only visually.

## Applies to

Links with a purpose that must be determinable from text or programmatically determined context.

## Does not apply / exceptions

Repeated Read more can be adequate in its paragraph/list/table context; ambiguity to users generally is an exception. Do not impose a universal link-text-only AA rule.

## Failure patterns

```html
<a href="/report">Click here</a><p>Complete supplied context has no description of the destination.</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<a href="/report">Read the annual report</a>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Determine purpose from link text and permitted programmatic context; check repeated destinations and distinguishable purposes.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: Several Read more links have article headings but the programmatic contextual relationship is unknown.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For subjective content, inspect purpose and meaning before reporting success; syntax alone is not enough. Do not infer unavailable component output.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Use meaningful link text or associate necessary context without hiding essential visual distinctions. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Failing every Read more link regardless of context or inventing labels that conflict with visible text. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-LNK-001.md)
- [pass case](../../../evals/fixtures/pass/AV-LNK-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-LNK-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 2.4.4 (A)](https://www.w3.org/TR/WCAG22/#link-purpose-in-context)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html)
