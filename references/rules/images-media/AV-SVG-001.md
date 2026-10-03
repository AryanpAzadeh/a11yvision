---
id: "AV-SVG-001"
title: "SVG semantics match purpose"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.1.1", "level": "A"}, {"criterion": "4.1.2", "level": "A"}]
users: ["blind"]
categories: ["images-media"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT", "RENDERED_DOM", "ACCESSIBILITY_TREE"]}
severity_default: "moderate"
---

# AV-SVG-001 — SVG semantics match purpose

## User impact

Unnamed or duplicated vector content makes its purpose unclear to screen-reader users. Affected users: blind. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- decorative SVG should not create meaningless screen-reader output;
- informative SVG needs an accessible name/description appropriate to its purpose;
- interactive SVG regions need valid control semantics and keyboard support;
- avoid duplicate title/label announcements caused by competing naming mechanisms.

## Applies to

Decorative, informative and interactive inline SVG.

## Does not apply / exceptions

A decorative SVG inside an already-named control needs no independent name; an informative SVG must not be silenced.

## Failure patterns

```html
<svg role="img" viewBox="0 0 100 100"><path d="M10 90L90 10"/></svg><p>This SVG alone conveys the trend.</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<svg role="img" aria-labelledby="trend-title" viewBox="0 0 100 100"><title id="trend-title">Value rises steadily</title><path d="M10 90L90 10"/></svg>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Determine purpose; resolve title/label references and naming precedence; inspect tree exposure. Test every interactive region with keyboard and actual AT when relevant.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A titled SVG also has aria-label and interactive descendants whose keyboard behavior is unknown.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Use one coherent naming mechanism for informative SVG; hide purely decorative SVG; prefer native controls for interactive actions. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Assuming title presence proves naming or that role="img" makes interactive regions operable. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-SVG-001.md)
- [pass case](../../../evals/fixtures/pass/AV-SVG-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-SVG-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.1.1 (A)](https://www.w3.org/TR/WCAG22/#non-text-content)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)
- [WCAG 2.2 SC 4.1.2 (A)](https://www.w3.org/TR/WCAG22/#name-role-value)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [WAI-ARIA 1.2 roles and author requirements](https://www.w3.org/TR/wai-aria-1.2/#roles)
- [WAI-ARIA 1.2 states and properties](https://www.w3.org/TR/wai-aria-1.2/#states_and_properties)
- [AccName 1.1 computation](https://www.w3.org/TR/accname-1.1/#mapping_additional_nd_te)
