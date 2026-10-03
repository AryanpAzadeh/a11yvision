---
id: "AV-ERR-001"
title: "Form errors are identified, described, and associated with fields"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "3.3.1", "level": "A"}, {"criterion": "3.3.3", "level": "AA"}, {"criterion": "1.3.1", "level": "A"}, {"criterion": "4.1.3", "level": "AA"}]
users: ["blind", "low-vision", "color-vision-deficiency"]
categories: ["names-forms-errors"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT", "RENDERED_DOM"]}
severity_default: "serious"
---

# AV-ERR-001 — Form errors are identified, described, and associated with fields

## User impact

Unidentified or unassociated errors prevent users from correcting input. Affected users: blind, low-vision, color-vision-deficiency. Default severity is serious; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- errors must not be indicated by color alone;
- identify which field has an error;
- expose useful error text programmatically;
- when an error suggestion is known and safe, provide it as required by WCAG 3.3.3;
- if errors appear dynamically without focus movement, evaluate whether status messaging is needed.

## Applies to

Detected input errors, known safe suggestions and relevant dynamic validation.

## Does not apply / exceptions

Suggestions need not compromise security or purpose; not every validation update is an assertive alert. Source can verify text/association but announcement timing requires interaction.

## Failure patterns

```html
<label for="mail">Email</label><input id="mail" style="border:2px solid red" value="invalid"><p>Scenario: this color is the sole validation indication.</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<label for="mail">Email</label><input id="mail" aria-invalid="true" aria-describedby="mail-error" value="invalid"><p id="mail-error">Enter an email address containing @, such as name@example.test.</p>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Trigger errors; verify field identification, textual explanation, association and safe suggestions. Inspect dynamic status semantics and actual announcements without unnecessary focus movement.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: Error text is linked correctly but dynamic insertion and focus/announcement timing are unknown.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Add useful error text and field relationships; choose focus summary or suitable status behavior for the actual flow. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Only adding a red border, making every keystroke an assertive announcement or giving unsafe account-existence suggestions. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete relevant source and contextual judgment for static semantics; rendered evidence for generated output and actual interaction for lifecycle/bypass/state claims. A static result must explicitly exclude untested dynamic behavior. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-ERR-001.md)
- [pass case](../../../evals/fixtures/pass/AV-ERR-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-ERR-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 3.3.1 (A)](https://www.w3.org/TR/WCAG22/#error-identification)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html)
- [WCAG 2.2 SC 3.3.3 (AA)](https://www.w3.org/TR/WCAG22/#error-suggestion)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html)
- [WCAG 2.2 SC 1.3.1 (A)](https://www.w3.org/TR/WCAG22/#info-and-relationships)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html)
- [WCAG 2.2 SC 4.1.3 (AA)](https://www.w3.org/TR/WCAG22/#status-messages)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
