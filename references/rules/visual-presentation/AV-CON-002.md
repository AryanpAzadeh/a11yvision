---
id: "AV-CON-002"
title: "UI components and meaningful graphics meet non-text contrast requirements"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.4.11", "level": "AA"}]
users: ["low-vision", "color-vision-deficiency"]
categories: ["visual-presentation"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "COMPUTED_STYLE", "VISUAL_INSPECTION"]}
severity_default: "moderate"
---

# AV-CON-002 — UI components and meaningful graphics meet non-text contrast requirements

## User impact

Weak control boundaries and graphic details can make interaction or data perception difficult. Affected users: low-vision, color-vision-deficiency. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Core threshold:

- required visual information for active UI components and graphical objects generally needs at least **3:1** contrast against adjacent colors as required by WCAG.

Requirements:

- evaluate boundaries, states, icons, chart lines/regions, and focus indicators where 1.4.11 applies;
- handle user-agent/default appearance and inactive-component exceptions correctly;
- do not treat every decorative border as required visual information.

## Applies to

Visual information necessary to identify active controls/states and understand graphical objects.

## Does not apply / exceptions

Inactive controls, unmodified user-agent appearance and essential graphics exceptions apply as defined. Decorative borders need not meet this rule.

## Failure patterns

```html
<button type="button" style="background:white;border:1px solid #ddd">Choose</button><p>Scenario: the border is the only visual information identifying the control.</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<button type="button" style="background:white;border:2px solid #111">Choose</button>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Identify required visual information before measuring; resolve adjacent rendered colors for boundaries, states, icons and meaningful chart regions. Apply 3:1 where required and check exceptions.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A pale border may be decorative because text, placement or another cue identifies the control; adjacent colors are unknown.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Strengthen the required boundary/state or supply an equivalent perceivable cue; keep decorative styling as desired. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Failing every border or treating component contrast as a substitute for text contrast. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-CON-002.md)
- [pass case](../../../evals/fixtures/pass/AV-CON-002.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-CON-002.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.4.11 (AA)](https://www.w3.org/TR/WCAG22/#non-text-contrast)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
