---
id: "AV-STA-001"
title: "Dynamic status messages are programmatically available without unnecessary focus movement"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "4.1.3", "level": "AA"}]
users: ["blind"]
categories: ["aria-dynamic-content"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "ACCESSIBILITY_TREE", "SCREEN_READER"]}
severity_default: "serious"
---

# AV-STA-001 — Dynamic status messages are programmatically available without unnecessary focus movement

## User impact

Unannounced completion or result counts can leave users unaware that their action succeeded. Affected users: blind. Default severity is serious; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Examples:

- “Saved” confirmation;
- cart count update;
- search results count;
- validation status;
- loading completion state.

Requirements:

- status messages meeting WCAG’s definition should be exposed using a suitable role/property so assistive technologies can announce them without moving focus;
- do not make everything `aria-live="assertive"`;
- avoid duplicate announcements caused by overlapping live regions.

## Applies to

Changes meeting WCAG's status-message definition without a change of context.

## Does not apply / exceptions

A focused dialog or navigation is not automatically a status message; not all changing content needs a live region.

## Failure patterns

```html
<p id="result">Saved</p><p>Scenario: this unfocused message replaces blank text after Save, with no status semantics.</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<p role="status" aria-atomic="true">Saved</p>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Identify the status message; inspect role/property and update timing; trigger it while keeping focus on the initiating control. Test actual AT output separately from tree inspection.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: role="status" exists but creation timing, duplicate regions and AT announcement behavior are unknown.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Use an appropriately established polite status region for routine completion; reserve alerts for justified urgency. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Making every update assertive, moving focus merely to announce status or nesting overlapping live regions. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-STA-001.md)
- [pass case](../../../evals/fixtures/pass/AV-STA-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-STA-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 4.1.3 (AA)](https://www.w3.org/TR/WCAG22/#status-messages)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
- [WAI-ARIA 1.2 roles and author requirements](https://www.w3.org/TR/wai-aria-1.2/#roles)
- [WAI-ARIA 1.2 states and properties](https://www.w3.org/TR/wai-aria-1.2/#states_and_properties)
- [AccName 1.1 computation](https://www.w3.org/TR/accname-1.1/#mapping_additional_nd_te)
