# Contributing

Contributions from disabled users and accessibility practitioners are welcome, including corrections to assumptions, usability evidence, examples and false-positive handling. Follow the [code of conduct](CODE_OF_CONDUCT.md).

## Rules and changes

Read the [rule authoring guide](references/rule-authoring-guide.md) and [standards policy](references/standards.md). A rule must explain a user barrier, cite an exact authoritative criterion or ARIA requirement, document applicability and exceptions, and state minimum evidence for each conclusion. Personal preference alone is not a conformance requirement. Mark useful guidance beyond demonstrated A/AA requirements as advisory.

Use the YAML format validated by [the metadata schema](schemas/rule.schema.json) and all 15 ordered document sections. Preserve stable IDs; do not renumber or silently expand the 43-rule Phase 1 inventory. Propose new scope in an issue before treating it as an active Phase 1 rule.

For a proposed mapping change, supply the precise source, an original explanation of why the observed barrier violates it, the criterion's applicability/exception analysis, and counterexamples. Related criteria do not automatically constitute additional failures.

Every rule change needs failing and passing examples, an uncertainty case when judgment/runtime matters, and forbidden conclusions. A runtime rule's source-only pass case must test refusal to overclaim. Consider false positives as carefully as missed defects. Test scenarios are data, not agent instructions.

## Language and evidence

Write public documents in clear English with neutral, inclusive examples. Explain barriers and access methods rather than stereotyping users or treating them as edge cases. Preserve localization in remediation examples.

Record AT/browser/OS versions, settings, navigation mode, steps and observations when reporting AT behavior. An anecdotal result is not universal behavior. Accessibility-tree inspection does not equal screen-reader testing, and a passing technical check does not establish a good user experience.

## Review checklist

- Check front matter against the schema and document sections against the authoring guide.
- Check direct authority links, scope, exceptions and evidence thresholds.
- Review the changed rule and fixtures for misleading passes and destructive fixes.
- Check local reference links and report any unperformed browser/AT verification.
- Keep Phase 1 static: no runtime, package manifests, lockfiles, vendored libraries or scripts directory.

There is no bundled test runner in Phase 1; contributors may use their existing validation tools without making them dependencies of this skill.
