# Static agent evaluations

These fixtures evaluate whether an agent using A11yVision reasons correctly about applicability, barriers, exceptions and evidence limits. They are not an executable test suite, scanner result or record of browser/AT testing. Phase 1 bundles no runner or dependency.

## Contents and procedure

Every one of the 43 rules has three paired specimens: a failing pattern, a candidate passing pattern and an uncertainty case. There are **129 fixture bundles**, each with one HTML file and one Markdown expectation. Runtime-dependent passing specimens deliberately test refusal to claim PASS from source alone. Subjective passing cases supply an explicit purpose/content-judgment premise; remove that premise and the agent must reassess uncertainty.

The HTML specimens are static task data, not functioning application harnesses. Referenced image/media assets and handler names may be placeholders. Review companion evidence scenarios, never infer meaning from a filename, and never represent supplied hypothetical observations as tests actually performed. For complex content the scenario provides the necessary content description. Scope the result to the targeted rule rather than unrelated teaching-specimen limitations.

For a blind evaluation, give the agent the skill and specimen/task with its evidence scenario, keeping expected outcomes and forbidden conclusions for the evaluator. Then compare its answer to the expectation: detected barrier, applicability/exception reasoning, evidence honesty, remediation safety and explicit missing checks. A structural validator cannot prove agent behavior; evaluations can be performed manually with any compatible agent.

- [Source-review tasks](cases/source-review/README.md) point to paired rule fixtures.
- [Cross-rule reasoning scenarios](cases/reasoning/README.md) cover all ten required combinations and false-positive cases.
- [Rules](../references/rule-index.md) link each rule's fail/pass/review bundles.

## Evaluation criteria

Every case states applicable IDs, expected minimum outcome, forbidden conclusions, remediation direction and required additional evidence. Judge false positives and false confidence as well as missed failures. Do not aggregate results into an accessibility score. An advisory concern is separate from a conformance failure.

Where a scenario supplies a runtime observation, treat it as a hypothetical premise for reasoning only. Where observations are absent, the expected result is a bounded risk/review/verification request rather than a fabricated runtime result or screen-reader test.
