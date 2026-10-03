# Source-review tasks

For each rule in [the index](../../../references/rule-index.md), give an agent `SKILL.md` and one HTML specimen with the evidence scenario from its companion Markdown file. Ask it to identify applicability, evidence, outcome, user impact, safe remediation and missing verification. Keep expectation sections from the agent during blind evaluation.

The paired [fail](../../fixtures/fail/AV-IMG-001.md), [pass](../../fixtures/pass/AV-IMG-001.md) and [needs-review](../../fixtures/needs-review/AV-IMG-001.md) directories contain the same three bundles for every stable ID. Follow the rule's links to select its cases. Candidate runtime passes require refusal of a source-only PASS; content judgments must be supplied rather than inferred from syntax.

For an intentionally uncertain component, also use [the uninspected component case](../reasoning/01-uninspected-component.md). For unknown final CSS, use [the theme case](../reasoning/02-theme-focus.md). Expectations evaluate judgment, not the mere occurrence of a rule ID in the answer.
