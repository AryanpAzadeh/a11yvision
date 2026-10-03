---
id: "AV-IOT-001"
title: "Images of text are avoided when real text can achieve the presentation"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.4.5", "level": "AA"}]
users: ["low-vision"]
categories: ["visual-presentation"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT"]}
severity_default: "moderate"
---

# AV-IOT-001 — Images of text are avoided when real text can achieve the presentation

## User impact

Rasterized text prevents users from adapting typography and color for readability. Affected users: low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- prefer real text that can resize, reflow, recolor, and adapt;
- correctly handle logos and essential/customizable exceptions;
- screenshots containing incidental text are context-sensitive and must not be simplistically flagged as all “images of text”.

## Applies to

Images whose principal purpose is presenting text that real text can achieve.

## Does not apply / exceptions

Logos and essential presentation or user-customizable images of text are excepted. Incidental text in a meaningful screenshot is context-sensitive.

## Failure patterns

```html
<img src="delivery-text.svg" alt="Delivery takes two days"><p>Scenario: the image only renders this ordinary announcement as styled text.</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<p>Delivery takes two days.</p>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Determine whether the image principally communicates text; inspect essential/customizable exceptions and whether equivalent real text can achieve the presentation.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A screenshot contains text but its purpose is demonstrating a visual interface rather than replacing ordinary prose.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For subjective content, inspect purpose and meaning before reporting success; syntax alone is not enough. Do not infer unavailable component output.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Replace ordinary images of text with styled real text and retain meaningful visual examples when justified. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Treating alt text as a complete 1.4.5 remedy or replacing essential logo artwork. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-IOT-001.md)
- [pass case](../../../evals/fixtures/pass/AV-IOT-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-IOT-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.4.5 (AA)](https://www.w3.org/TR/WCAG22/#images-of-text)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html)
