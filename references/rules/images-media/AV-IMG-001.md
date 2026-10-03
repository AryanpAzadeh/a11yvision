---
id: "AV-IMG-001"
title: "Meaningful images have equivalent text alternatives"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.1.1", "level": "A"}]
users: ["blind", "low-vision"]
categories: ["images-media"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT"]}
severity_default: "serious"
---

# AV-IMG-001 — Meaningful images have equivalent text alternatives

## User impact

Missing meaning prevents understanding an illustration or choosing an item without sight. Affected users: blind, low-vision. Default severity is serious; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Core requirements:

- Meaningful images need a text alternative that serves the image’s purpose in context.
- Attribute presence is not sufficient evidence of quality.
- `alt="image"`, filename-derived alternatives, or redundant “image of…” wording should generally trigger review unless context makes it appropriate.
- The agent must distinguish descriptive, functional, textual, and complex image purposes.
- If meaning cannot be determined from source/context, use `NEEDS_REVIEW`, not invented alt text.

Unsafe fix:

- never generate a confident description from a filename alone;
- never copy nearby caption text blindly if it changes meaning or creates redundancy.

## Applies to

Images that communicate information rather than decoration or an action.

## Does not apply / exceptions

An equivalent already exposed through another mechanism can satisfy the requirement; assess redundancy in context.

## Failure patterns

```html
<img src="route.svg"><p>The image is the only source of the route: Library to Station via Park.</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<img src="route.svg" alt="Walk from Library through Park to Station.">
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Inspect the image, surrounding text and alternative together; distinguish informative, textual, functional and complex purpose. Judge whether essential information is equivalent.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: Only alt="route-42.svg" and an unavailable image are provided; its actual purpose is unknown.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For subjective content, inspect purpose and meaning before reporting success; syntax alone is not enough. Do not infer unavailable component output.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Write a concise alternative based on known purpose and actual content; use structured equivalents for complex material. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Inventing image meaning from filenames or copying a caption without checking equivalence. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-IMG-001.md)
- [pass case](../../../evals/fixtures/pass/AV-IMG-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-IMG-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.1.1 (A)](https://www.w3.org/TR/WCAG22/#non-text-content)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)
