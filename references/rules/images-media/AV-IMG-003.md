---
id: "AV-IMG-003"
title: "Functional images and icon controls expose their function"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.1.1", "level": "A"}, {"criterion": "4.1.2", "level": "A"}]
users: ["blind"]
categories: ["images-media"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT"]}
severity_default: "serious"
---

# AV-IMG-003 — Functional images and icon controls expose their function

## User impact

An icon description can leave the action unidentified, risking accidental operations. Affected users: blind. Default severity is serious; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Core requirements:

- An image/icon used as a control must expose the control’s function, not a visual description of the icon.
- Icon-only buttons need a usable accessible name.
- Decorative icon descendants inside an already-named control should not create duplicated announcements.

Example intent:

- “Delete item” is useful; “trash can icon” usually is not the functional name.

## Applies to

Images used as links, controls and icon-only buttons.

## Does not apply / exceptions

A control already named by visible text should normally hide its decorative icon descendants.

## Failure patterns

```html
<button type="button"><img src="trash.svg" alt="trash can icon"></button>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<button type="button">Delete item <img src="trash.svg" alt=""></button>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Compute the control name using naming precedence; compare it with the intended action, and check for duplicated icon announcements.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A library icon component has an inaccessible implementation; the computed control name cannot be determined.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For subjective content, inspect purpose and meaning before reporting success; syntax alone is not enough. Do not infer unavailable component output.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Name the action through visible text when practical; use a localized control label when an icon-only design is necessary. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Describing the icon shape instead of the action or layering redundant naming mechanisms. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-IMG-003.md)
- [pass case](../../../evals/fixtures/pass/AV-IMG-003.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-IMG-003.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.1.1 (A)](https://www.w3.org/TR/WCAG22/#non-text-content)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)
- [WCAG 2.2 SC 4.1.2 (A)](https://www.w3.org/TR/WCAG22/#name-role-value)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
