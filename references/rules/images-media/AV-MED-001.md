---
id: "AV-MED-001"
title: "Important prerecorded visual video content has an accessible alternative"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.2.3", "level": "A"}, {"criterion": "1.2.5", "level": "AA"}]
users: ["blind", "low-vision"]
categories: ["images-media"]
evaluation: {"primary": "manual-human", "evidence": ["SOURCE", "CONTENT_JUDGMENT"]}
severity_default: "serious"
---

# AV-MED-001 — Important prerecorded visual video content has an accessible alternative

## User impact

Important visual events in video may be unavailable to viewers who cannot see them. Affected users: blind, low-vision. Default severity is serious; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Requirements:

- important information shown visually in prerecorded video must be available to users who cannot see it, through audio description and/or the applicable media alternative mechanism;
- agent must not assert a pass merely because the `<video>` element has controls;
- content review is required.

## Applies to

Prerecorded synchronized video with important visual information; assess the applicability of each media criterion separately.

## Does not apply / exceptions

Live media is outside these prerecorded criteria. SC 1.2.3 has a clearly labeled media-alternative-for-text exception; do not transfer that exception or a transcript-only solution to 1.2.5. No extra description is needed if the existing audio already conveys all important visuals.

## Failure patterns

```html
<video controls><source src="demo.mp4" type="video/mp4"></video><p>Scenario: the silent visual instruction says turn the valve clockwise; the audio omits it and no alternative is offered.</p>
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<video controls aria-label="Valve demonstration with audio description"><source src="described-demo.mp4" type="video/mp4"></video><p>Scenario: narration includes the clockwise instruction and all other essential visual actions.</p>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Review the entire media and its audio; document each important visual and its equivalent. At A, evaluate audio description OR an applicable complete media alternative; at AA, 1.2.5 requires audio description for applicable synchronized video.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: A transcript is linked but the video cannot be reviewed; controls and a transcript do not prove AA audio-description coverage.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For subjective content, inspect purpose and meaning before reporting success; syntax alone is not enough. Do not infer unavailable component output.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Supply integrated narration or an audio-described version for AA; keep a complete media alternative where useful or needed for A. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Treating captions, playback controls or a transcript alone as proof of 1.2.5. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-MED-001.md)
- [pass case](../../../evals/fixtures/pass/AV-MED-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-MED-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.2.3 (A)](https://www.w3.org/TR/WCAG22/#audio-description-or-media-alternative-prerecorded)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded.html)
- [WCAG 2.2 SC 1.2.5 (AA)](https://www.w3.org/TR/WCAG22/#audio-description-prerecorded)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded.html)
