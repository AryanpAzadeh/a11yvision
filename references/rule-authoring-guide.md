# Rule authoring guide

Phase 1 has exactly 43 stable IDs in [the index](rule-index.md). Rules are framework-agnostic web requirements; framework syntax appears only as implementation examples. Follow [standards policy](standards.md) and [evidence outcomes](evidence-and-outcomes.md).

## Metadata contract

Each rule has YAML front matter validated as an object by [rule.schema.json](../schemas/rule.schema.json). JSON-style quoted scalars and flow collections are valid YAML and used for unambiguous values in this package.

```yaml
---
id: AV-IMG-001
title: Meaningful images have equivalent text alternatives
version: 0.1.0
status: active
scope: conformance
wcag:
  - criterion: "1.1.1"
    level: A
users: [blind, low-vision]
categories: [images-media]
evaluation:
  primary: agent-review
  evidence: [SOURCE, CONTENT_JUDGMENT]
severity_default: serious
---
```

Required fields are id, title, version, status, scope, wcag, users, categories, evaluation and severity_default. Status: draft/active/deprecated. Scope: conformance/advisory. Users: blind/low-vision/color-vision-deficiency. Evaluation primary: automatic/agent-review/rendered-review/manual-at/manual-human; it describes a typical path, not a bundled runtime capability. Evidence types and severity are defined in the outcome reference. Conformance rules need criterion/level mappings; FRC has an empty mapping and advisory scope/severity. VIS has conditional related mappings that need demonstrated effects.

## Ordered sections

Every active rule uses these 15 headings, in order:

1. `# <Rule ID> — <Title>`
2. `## User impact`
3. `## Requirement`
4. `## Applies to`
5. `## Does not apply / exceptions`
6. `## Failure patterns`
7. `## Passing patterns`
8. `## Evaluation procedure`
9. `## Outcome rules`
10. `## Remediation guidance`
11. `## Unsafe or misleading fixes`
12. `## Verification`
13. `## Framework notes`
14. `## Test fixtures`
15. `## References`

## Quality requirements

Explain user impact before markup. Cite precise WCAG/ARIA authority, or explicitly mark advisory guidance. Define applicability, relevant exceptions, failure evidence, permissible PASS and mandatory review conditions. Include fail/pass and false-positive examples. Syntax cannot prove meaning; runtime-dependent passes require actual rendered/interaction evidence. Explicitly identify unresolved access/testing.

Remediation must be minimal, native-first and localization-safe. Name common unsafe fixes, especially decorative alt invention, blanket ARIA, positive tabindex, outline removal, color-only cues and fabricated contrast. Keep the 15 sections substantive; metadata validation cannot assess judgment quality.

## Evaluation material

Each rule links fail/pass/review specimen bundles. Expectations state applicable IDs, minimum outcome, forbidden conclusions, remediation and missing evidence. For runtime rules the source-only pass fixture deliberately expects refusal of PASS. Test hypothetical observations separately from actual performed tests. Cross-rule cases test false positives and false confidence; see [evals](../evals/README.md).

Use original paraphrases, short necessary quotes and direct W3C links. Do not treat anecdotes about one AT combination as universal behavior, APG deviations as automatic failures or personal preference as a conformance requirement.
