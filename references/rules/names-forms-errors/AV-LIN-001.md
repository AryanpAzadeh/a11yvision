---
id: "AV-LIN-001"
title: "Visible labels and accessible names do not conflict"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "2.5.3", "level": "A"}]
users: ["low-vision"]
categories: ["names-forms-errors"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT"]}
severity_default: "moderate"
---

# AV-LIN-001 — Visible labels and accessible names do not conflict

## User impact

Conflicting visual and accessible labels confuse people using magnification and mixed input methods. Affected users: low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- when a control has visible text, its accessible name should contain that visible label text as required;
- do not “improve” a visible button named “Search” by setting an unrelated accessible name such as `aria-label="Find products in catalog"` if that removes the visible label token from the accessible name.

Although this criterion also benefits speech-input users outside the primary scope, it prevents confusing accessible naming for low-vision and mixed-AT workflows and is included in Phase 1.

---

## Applies to

Controls with visible labels containing text or images of text.

## Does not apply / exceptions

A symbolic icon without a textual label is not treated as literal label text. Additional name text is allowed if it includes the visible label; beginning with the label is useful guidance.

## Failure patterns

```html
<button type="button" aria-label="Find products in catalog">Search</button>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<button type="button" aria-label="Search products in catalog">Search</button>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Compare visible label text with the computed accessible name, including translation and naming precedence.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: The visible label is localized at runtime but aria-label may remain in a different language.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For subjective content, inspect purpose and meaning before reporting success; syntax alone is not enough. Do not infer unavailable component output.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Prefer the visible text as the name; retain its text when extra context is necessary. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Replacing Search with an unrelated supposedly descriptive name. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-LIN-001.md)
- [pass case](../../../evals/fixtures/pass/AV-LIN-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-LIN-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 2.5.3 (A)](https://www.w3.org/TR/WCAG22/#label-in-name)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html)
- [WAI-ARIA 1.2 roles and author requirements](https://www.w3.org/TR/wai-aria-1.2/#roles)
- [WAI-ARIA 1.2 states and properties](https://www.w3.org/TR/wai-aria-1.2/#states_and_properties)
- [AccName 1.1 computation](https://www.w3.org/TR/accname-1.1/#mapping_additional_nd_te)
