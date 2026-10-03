---
id: "AV-TIT-001"
title: "Pages have descriptive titles"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "2.4.2", "level": "A"}]
users: ["blind", "low-vision"]
categories: ["semantics-structure"]
evaluation: {"primary": "automatic", "evidence": ["SOURCE", "CONTENT_JUDGMENT", "RENDERED_DOM"]}
severity_default: "moderate"
---

# AV-TIT-001 — Pages have descriptive titles

## User impact

Generic or stale titles make pages difficult to identify in tabs and navigation history. Affected users: blind, low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- document/page title describes topic or purpose;
- generic titles such as “Home” may require contextual judgment;
- SPAs must update titles appropriately when navigation changes page/topic semantics.

## Applies to

Documents and route transitions that change page topic or purpose.

## Does not apply / exceptions

A short title such as Home may be adequate in context; length alone is not a failure.

## Failure patterns

```html
<title>Untitled</title><h1>Shipping address for order 42</h1>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<title>Shipping address - Example store</title><h1>Shipping address</h1>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Compare document title with purpose; repeat after each relevant route transition. Source can establish a static title but cannot prove dynamic updates.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: The initial title is descriptive but client-side navigation may leave it stale.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Set concise descriptive titles through the existing document or route title mechanism. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Reusing a branded generic title for every distinct route or relying only on an h1. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-TIT-001.md)
- [pass case](../../../evals/fixtures/pass/AV-TIT-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-TIT-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 2.4.2 (A)](https://www.w3.org/TR/WCAG22/#page-titled)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html)
