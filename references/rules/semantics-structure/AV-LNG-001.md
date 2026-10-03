---
id: "AV-LNG-001"
title: "Page and language changes are programmatically identified"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "3.1.1", "level": "A"}, {"criterion": "3.1.2", "level": "AA"}]
users: ["blind"]
categories: ["semantics-structure"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT"]}
severity_default: "moderate"
---

# AV-LNG-001 — Page and language changes are programmatically identified

## User impact

Incorrect language metadata may cause inappropriate pronunciation and reading behavior. Affected users: blind. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- primary document language should be exposed correctly;
- passages in another human language should be marked when required and when language change is programmatically determinable/applicable;
- do not mark proper names, technical terms, or common borrowed words indiscriminately.

---

## Applies to

Primary document language and meaningful passages in another language.

## Does not apply / exceptions

Proper names, technical terms, indeterminate language and common borrowed words have criterion exceptions; do not tag them indiscriminately.

## Failure patterns

```html
<html><head><title>Welcome</title></head><body><p>This document is in English.</p></body></html>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<html lang="en"><head><title>Welcome</title></head><body><p>Welcome. <span lang="fr">Bienvenue chez nous.</span></p></body></html>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Establish actual human language; inspect valid language tags on the root and passages, respecting exceptions and localization.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A localized template sets lang from an unknown value and a product name resembles another language.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For subjective content, inspect purpose and meaning before reporting success; syntax alone is not enough. Do not infer unavailable component output.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Supply accurate document and passage lang values via the project's locale system. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Treating dir="rtl" as a language declaration or tagging every borrowed term. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-LNG-001.md)
- [pass case](../../../evals/fixtures/pass/AV-LNG-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-LNG-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 3.1.1 (A)](https://www.w3.org/TR/WCAG22/#language-of-page)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html)
- [WCAG 2.2 SC 3.1.2 (AA)](https://www.w3.org/TR/WCAG22/#language-of-parts)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts.html)
