---
id: "AV-LMK-001"
title: "Repeated content can be bypassed and primary regions are identifiable"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "2.4.1", "level": "A"}, {"criterion": "1.3.1", "level": "A"}]
users: ["blind", "low-vision"]
categories: ["semantics-structure"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT", "RENDERED_DOM", "KEYBOARD_INTERACTION"]}
severity_default: "moderate"
---

# AV-LMK-001 — Repeated content can be bypassed and primary regions are identifiable

## User impact

Repeated navigation can force unnecessary traversal before reaching primary content. Affected users: blind, low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- repeated navigation/content must have a bypass mechanism such as a functional skip link, headings, landmarks, or another conforming mechanism;
- pages should expose primary content with suitable structure such as `<main>` where appropriate;
- multiple same-type landmarks should be distinguishable when necessary.

## Applies to

Repeated blocks across a set of pages and meaningful page regions.

## Does not apply / exceptions

A functional heading or landmark bypass can be sufficient; absence of a skip link or a main element alone is not automatically a WCAG failure.

## Failure patterns

```html
<div>Repeated site navigation: 60 unnamed controls</div><div>Primary content, with no bypass mechanism or structure in the complete scenario.</div>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<a href="#main">Skip to content</a><nav aria-label="Primary">Navigation</nav><main id="main" tabindex="-1"><h1>Account</h1></main>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Inventory repeated blocks and available bypasses; activate the selected bypass and verify destination. Distinguish duplicate same-type landmarks when needed.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A skip link exists but whether activation reaches the intended focus/reading position is unknown.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Add or repair a functional bypass and appropriate native regions without excessive landmarks. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Adding a dead skip link or demanding a skip link despite another tested conforming bypass. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-LMK-001.md)
- [pass case](../../../evals/fixtures/pass/AV-LMK-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-LMK-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 2.4.1 (A)](https://www.w3.org/TR/WCAG22/#bypass-blocks)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html)
- [WCAG 2.2 SC 1.3.1 (A)](https://www.w3.org/TR/WCAG22/#info-and-relationships)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html)
