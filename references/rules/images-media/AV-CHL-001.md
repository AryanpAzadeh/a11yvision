---
id: "AV-CHL-001"
title: "Visual-only challenges provide accessible alternatives"
version: "0.1.0"
status: "active"
scope: "conformance"
wcag: [{"criterion": "1.1.1", "level": "A"}]
users: ["blind", "low-vision", "color-vision-deficiency"]
categories: ["images-media"]
evaluation: {"primary": "manual-human", "evidence": ["SOURCE", "CONTENT_JUDGMENT"]}
severity_default: "serious"
---

# AV-CHL-001 — Visual-only challenges provide accessible alternatives

## User impact

A visual verification task can block access to an essential service. Affected users: blind, low-vision, color-vision-deficiency. Default severity is serious; adjust for actual task impact rather than WCAG level.

## Requirement

These are A11yVision interpretations of the linked authority. Apply only the criterion demonstrated by the evidence; related mappings are not automatic additional failures.

Scope includes:

- image CAPTCHAs;
- color-identification challenges;
- “click the object in the picture” tasks;
- visual verification steps.

Requirements:

- users must not be blocked because a verification mechanism depends only on vision/color perception;
- do not assume an audio CAPTCHA is always sufficient or usable; review the complete task and available alternatives;
- classify uncertain challenge systems as `NEEDS_REVIEW`.

---

## Applies to

Image CAPTCHAs, color-identification tasks and visual verification in relevant user flows.

## Does not apply / exceptions

For CAPTCHA, identify and describe its purpose and provide alternatives using different sensory modes as required by 1.1.1; the answer itself need not be exposed as alt. Authentication context may require separate 3.3.8 evaluation, outside a claim of complete coverage here.

## Failure patterns

```html
<p>To continue, choose the green shapes in the image. There is no other verification route.</p><img src="challenge.svg" alt="Verification challenge">
```

This specimen illustrates a barrier under the stated scenario, not an assertion that this repository ran a browser/AT test. For runtime rules use the case's explicit observation scenario before deciding FAIL.

## Passing patterns

```html
<p>Confirm access using a sign-in link sent to your email.</p><label for="email">Email address</label><input id="email" type="email"><button type="button">Send sign-in link</button>
```

This is a candidate pattern. PASS depends on the evidence and scope below, not its placement in this section.

## Evaluation procedure

1. Establish purpose, applicability and exceptions for the actual element and task.
2. Inspect every offered route and test task completion; consider more than one sensory need. Check whether any route still requires vision or color identification.
3. Separate observed facts from inferred risks. Minimum definitive evidence: Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS.
4. Record scope, evidence types and outstanding tests in the finding template.

## Outcome rules

- **PASS:** all applicable requirements within the declared scope are demonstrated by the minimum evidence above. Do not extend static or single-state evidence to untested states.
- **FAIL:** the failing condition is demonstrated with known applicability and no valid exception. For behavior/appearance claims, require relevant observations; source may demonstrate an explicit static defect only when the complete implementation resolves it.
- **NEEDS_REVIEW:** purpose, content equivalence, exception applicability or interpretation remains uncertain. Example: An audio challenge exists but its usability, expiry and end-to-end completion have not been checked.
- **NOT_APPLICABLE:** applicability is definitively absent; record why.
- **NOT_TESTED:** applicable or potentially applicable testing was not performed, although the environment could support it.
- **CANNOT_VERIFY:** required evidence or access is unavailable; identify exactly what is missing.

For subjective content, inspect purpose and meaning before reporting success; syntax alone is not enough. Do not infer unavailable component output.

Confidence is **high** only for a directly demonstrated result in complete relevant context. Use **medium** for well-supported limited evidence and **low** for unresolved assumptions; confidence cannot replace missing evidence. PASS is local to this check, never site-level conformance.

## Remediation guidance

Provide an equivalent usable nonvisual route; prefer a verification approach that avoids sensory puzzles where feasible. Keep the smallest safe change, preserve task behavior, localization and visual identity, and recheck related semantics/focus after changing it.

## Unsafe or misleading fixes

Assuming audio CAPTCHA is sufficient for every user or weakening security without preserving the intended verification behavior. Do not use an overlay or blanket ARIA to conceal the underlying barrier.

## Verification

Repeat the evaluation procedure on the changed surface and relevant states. Record actual observations, environment and remaining manual checks. Complete source plus a documented judgment of purpose, meaning and applicable exceptions. Inspect actual visual/media content where that determines equivalence; attribute presence alone cannot justify PASS. Accessibility-tree inspection does not demonstrate screen-reader output; actual AT testing must be recorded separately when needed.

## Framework notes

Evaluate final web semantics and behavior independently of the template/component syntax. Follow component composition to its implementation; preserve the project's localization and architecture. CSS utility names and component prop names alone are insufficient evidence of their rendered effects.

## Test fixtures

- [fail case](../../../evals/fixtures/fail/AV-CHL-001.md)
- [pass case](../../../evals/fixtures/pass/AV-CHL-001.md)
- [needs-review case](../../../evals/fixtures/needs-review/AV-CHL-001.md)

Read the specimen and evidence scenario separately. Supplied hypothetical observations are for evaluating reasoning, not a claim of tests actually performed.

## References

- [WCAG 2.2 SC 1.1.1 (A)](https://www.w3.org/TR/WCAG22/#non-text-content)
  [Informative Understanding](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)
- [WCAG 2.2 Accessible Authentication (Minimum), contextual review](https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum)
