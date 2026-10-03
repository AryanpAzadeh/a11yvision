---
id: "AV-SPC-001"
title: "User text-spacing overrides do not cause loss of content or functionality"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.4.12", "level": "AA"}]
users: ["low-vision"]
categories: ["visual-presentation"]
evaluation: {"primary": "rendered-review", "evidence": ["SOURCE", "RENDERED_DOM", "RENDERED_GEOMETRY", "VISUAL_INSPECTION"]}
severity_default: "moderate"
---

# AV-SPC-001 — User text-spacing overrides do not cause loss of content or functionality

## User impact

Fixed containers can cut off content when users increase spacing to read comfortably. Affected users: low-vision. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Test with all of the following together where applicable:

- line height at least **1.5 ×** font size;
- paragraph spacing at least **2 ×** font size;
- letter spacing at least **0.12 ×** font size;
- word spacing at least **0.16 ×** font size.

Requirements:

- no clipped text;
- no overlapped controls;
- no disappearing labels;
- no lost functionality;
- respect language/script exceptions from WCAG.

## Applies to

Content in markup supporting user text-spacing changes.

## Does not apply / exceptions

Languages/scripts not using one or more specified properties need only the properties they use. This is override tolerance, not a demand for those default author styles.

## Failure patterns

```html
<p style="height:1.2em;overflow:hidden">Choose collection or delivery before confirming your address.</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<p>Choose collection or delivery before confirming your address.</p>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Apply together line height 1.5x, paragraph spacing 2x, letter spacing 0.12x and word spacing 0.16x font size where applicable. Inspect content and controls and complete tasks; do not force letter spacing on scripts where it is inapplicable.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: There are flexible styles but no combined override test; script-specific applicability is unknown.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For runtime-dependent behavior, source-only evidence must result in NOT_TESTED if a test is available but not performed, or CANNOT_VERIFY if the environment cannot supply it. A concrete source defect may still establish a narrower static failure; do not infer an unobserved runtime failure.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Remove clipping and rigid heights; accommodate overrides without changing default typography unnecessarily. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Applying overrides individually and assuming combined success or enforcing letter spacing that breaks script joining. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Actual observations of the rendered state and the relevant interaction/geometry/style tests described below; record the tested route, state, viewport, browser and method. Source and a plausible CSS/ARIA pattern alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-SPC-001.md)
- [pass case](../../../evals/fixtures/pass/AV-SPC-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-SPC-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.4.12 (AA)](https://www.w3.org/TR/WCAG22/#text-spacing)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)
