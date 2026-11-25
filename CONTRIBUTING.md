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
- Keep the core skill usable as static references; optional maintenance scripts must not become required to use it.

Optional Phase 2 maintenance tools validate rule metadata against the JSON Schema and check document structure. They require Python and separate dependencies; reading and using the skill does not. From the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-maintenance.txt
python scripts/rules.py validate
python scripts/rules.py manifest > /tmp/a11yvision-rules.json
python scripts/rules.py manifest --check /tmp/a11yvision-rules.json
python -m unittest discover -s tests
```

The JSON manifest is sorted by rule ID and includes source paths and metadata. Redirect output to a location of your choice; it is not generated or modified by `validate`. A nonzero exit means validation failed or a checked manifest differs. These checks cannot judge accessibility, rule interpretation, link validity or actual user experience; review those manually. The static agent evaluation cases remain separate from the maintenance tests.

## Static HTML review candidates

Run `python3 scripts/check_html.py page.html` or supply several HTML files. It uses the Python standard library and prints JSON with paths, source line numbers, rule IDs and `NEEDS_REVIEW` candidates. It checks missing image `alt`, missing or empty document language and title when an `html` element is present, and selected potentially focusable elements marked `aria-hidden`. A return code of 0 means files were read, not that they passed accessibility checks; unreadable input returns 2. Fragments, templates, generated markup, CSS and interactions require context. No candidates does not mean the page is accessible. The checker does not execute JavaScript, compute names or styles, assess image meaning, inspect descendants of hidden ancestors, or perform browser/AT tests. Inspect each candidate under its linked rule and report unsupported conclusions as unresolved.

## Contrast calculation

The optional contrast calculator uses only the Python standard library. Quote each color so the shell does not interpret `#` as a comment:

```sh
python3 scripts/contrast.py '#777' '#ffffff'
```

Provide two final, opaque sRGB colors in `#RGB` or `#RRGGBB` form, resolved for the actual rendered state. The tool does not resolve CSS variables, transparency, gradients, images, blending or overlays; obtain final colors first or report that the contrast cannot be verified. It reports the ratio and numeric threshold comparisons using the unrounded value. It does not decide text size, applicable WCAG exceptions, user experience or conformance. See [text contrast](references/rules/visual-presentation/AV-CON-001.md) and [non-text contrast](references/rules/visual-presentation/AV-CON-002.md).
