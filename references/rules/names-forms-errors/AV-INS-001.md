---
id: "AV-INS-001"
title: "Instructions do not depend only on sensory characteristics or color"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.3.3", "level": "A"}, {"criterion": "1.4.1", "level": "A"}, {"criterion": "3.3.2", "level": "A"}]
users: ["blind", "low-vision", "color-vision-deficiency"]
categories: ["names-forms-errors"]
evaluation: {"primary": "agent-review", "evidence": ["SOURCE", "CONTENT_JUDGMENT"]}
severity_default: "moderate"
---

# AV-INS-001 — Instructions do not depend only on sensory characteristics or color

## User impact

Location, shape or hue alone can make an instruction unusable without its visual cue. Affected users: blind, low-vision, color-vision-deficiency. Default severity is moderate; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Flag instructions such as:

- “click the green button” with no textual/function cue;
- “fields in red are required”;
- “use the box on the right” when spatial location is the only identifier.

Sensory cues may supplement but should not be the sole means when the criterion applies.

## Applies to

Instructions for understanding or operating content.

## Does not apply / exceptions

Sensory cues may supplement a textual/function cue. Directional cues with a meaningful identified referent are not automatically failures.

## Failure patterns

```html
<p>Click the green button to continue.</p><button type="button">A</button><button type="button">B</button>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<p>Select Continue to proceed.</p><button type="button">Continue</button>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Read instructions with the target controls and required-field cues; test whether meaning survives removal of sensory/color information.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: The text says use the box on the right but omitted context may also name it.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For subjective content, inspect purpose and meaning before reporting success; syntax alone is not enough. Do not infer unavailable component output.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Identify controls by descriptive visible labels and express required status in text/programmatic form as appropriate. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Merely swapping green for red or hiding the only meaningful instruction from sighted users. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-INS-001.md)
- [pass case](../../../evals/fixtures/pass/AV-INS-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-INS-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.3.3 (A)](https://www.w3.org/TR/WCAG22/#sensory-characteristics)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/sensory-characteristics.html)
- [WCAG 2.2 SC 1.4.1 (A)](https://www.w3.org/TR/WCAG22/#use-of-color)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)
- [WCAG 2.2 SC 3.3.2 (A)](https://www.w3.org/TR/WCAG22/#labels-or-instructions)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html)
