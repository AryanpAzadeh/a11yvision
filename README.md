# A11yVision

**English** · [فارسی](README.fa.md)

An open-source Agent Skill that helps AI coding agents find, explain and fix web accessibility barriers for blind users, people with low vision and people with color-vision deficiencies.

**Status: v0.1 / Phase 1.** The package includes 43 accessibility rules, review workflows, reporting templates and manual test checklists. It contains static files and requires no runtime, package manager, framework adapter or paid API.

## What is A11yVision?

An Agent Skill is a reusable set of instructions and references that an AI agent can load for a task. A11yVision guides the agent through inspecting web UI, explaining user impact, proposing safe fixes and identifying missing evidence.

The entry point is [SKILL.md](SKILL.md). It directs the agent to load only the references relevant to the requested work. Rules concern web semantics and behavior, so the package applies to static HTML, component-based interfaces and server-rendered templates.

Use it when building UI, auditing existing code, fixing known findings, reviewing a patch or preparing a manual accessibility test plan.

## Why it helps

Accessibility review requires more than finding missing attributes. An image can have `alt` text that conveys no useful information; a dialog can have valid ARIA and still lose keyboard focus. A11yVision makes those distinctions part of the review.

- **Connect findings to real tasks.** Explain how a barrier affects navigation, reading, form completion or control operation.
- **Tie conclusions to evidence.** Separate source inspection, rendered appearance, interaction tests, content judgment and actual assistive-technology testing.
- **Keep fixes focused.** Prefer native HTML and preserve localization, product behavior and visual intent.
- **Make reviews easier to follow up.** Use stable rule IDs, consistent outcomes and explicit manual checks.
- **Reuse guidance across projects.** Evaluate the resulting web interface independently of a particular framework or CSS library.

These are review principles, not a guarantee that an agent will find every barrier or make every fix correctly. Review proposed changes and perform the required verification.

## Installation

### 1. Get the package

Clone the repository:

```sh
git clone https://github.com/AryanpAzadeh/a11yvision.git
```

Alternatively, download and extract the ZIP from the [repository](https://github.com/AryanpAzadeh/a11yvision). Git is needed only for cloning; it is not a dependency of the skill.

### 2. Add it to your agent

If your agent supports the Agent Skills format, copy the repository directory into its supported project-level or user-level skills directory and name the folder `a11yvision`. The location depends on the agent; follow its skill-discovery documentation.

Keep the package together. Copying only `SKILL.md` loses the linked rules, templates and checklists. The resulting structure should look like this:

```text
<your-agent-skills-directory>/
└── a11yvision/
    ├── SKILL.md
    ├── references/
    ├── assets/
    ├── schemas/
    └── evals/
```

The path above is illustrative; use your agent's actual skills directory. No build or dependency-installation command is required. Reload or restart the agent if its discovery mechanism requires it.

### 3. Use the skill

Ask the agent to use A11yVision and identify the component, route or task to review. If it provides an explicit skill selector, select `a11yvision` there.

If your agent has no skill-discovery support but can read files, point it directly to `a11yvision/SKILL.md` and ask it to follow the linked references. This is a file-based workflow rather than an automatic installation.

## Example prompts

> Use A11yVision to audit this component for blind and low-vision users. Report confirmed barriers, uncertain findings and checks requiring a browser or screen reader.

> Fix confirmed A11yVision findings in this form. Preserve its behavior, localization and visual design, then report verification and remaining manual checks.

> Review this patch using A11yVision. Inspect affected shared components and flag accessibility regressions with supporting evidence.

> Use A11yVision to prepare a manual test plan for this dialog and its validation flow. Include keyboard steps, focus transitions and expected screen-reader behavior.

The agent can review source without a running application. Rendered appearance, geometry and interaction checks need relevant browser evidence; claims about screen-reader output need actual AT testing. The skill does not supply those tools.

## Coverage

| Area | Examples |
|---|---|
| Images and media | Meaningful alternatives, decorative images, functional icons, SVG, complex visuals and prerecorded visual information |
| Semantics and structure | Native controls, headings, bypass mechanisms, reading order, tables, lists, titles and language |
| Names, forms and errors | Control names, labels, instructions, error relationships, link purpose and visible-label consistency |
| ARIA and dynamic content | Truthful roles/states, hidden content, status messages and custom widgets |
| Keyboard and focus | Keyboard operation, traps, visible focus, focus order, obscuring and dialog lifecycle |
| Visual presentation | Color-independent cues, contrast, enlargement, reflow, text spacing, hover content, targets and charts |

See the [43-rule index](references/rule-index.md) for exact applicability and exceptions. Forced-colors resilience is explicitly advisory; other mappings depend on the requirement actually demonstrated.

## Outcomes and limitations

| Outcome | Meaning |
|---|---|
| `PASS` | Enough evidence supports this rule within the declared tested scope |
| `FAIL` | Evidence demonstrates a violation with established applicability |
| `NEEDS_REVIEW` | Meaning, interpretation or an exception needs further judgment |
| `NOT_APPLICABLE` | The rule's applicability is definitively absent |
| `NOT_TESTED` | Required testing was not performed |
| `CANNOT_VERIFY` | Necessary evidence or access is unavailable |

Reports use [the evidence model](references/evidence-and-outcomes.md) and [report template](assets/accessibility-audit-report-template.md) to keep unresolved checks visible. A11yVision does not produce an accessibility score.

A11yVision is not an automated scanner, accessibility overlay, browser extension, hosted service or certification product. Phase 1 focuses on visual access and does not cover every WCAG A/AA success criterion. Source alone cannot prove reflow, focus behavior, contrast with unresolved colors or screen-reader usability.

**A review identifies issues within the tested scope and available evidence. It does not certify WCAG conformance or replace manual assistive-technology testing and testing by disabled users.** A passing check is local to its rule and tested surface; one passing AT/browser combination is not universal proof.

## Standards

The conformance baseline is [WCAG 2.2 Levels A and AA](https://www.w3.org/TR/WCAG22/). [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/) supplies ARIA author requirements, [AccName 1.1](https://www.w3.org/TR/accname-1.1/) is the stable naming reference, and [ACT Rules Format 1.1](https://www.w3.org/TR/act-rules-format/) informs rule structure.

WCAG Understanding documents and ARIA Authoring Practices are informative guidance, distinct from normative requirements. See [standards and source policy](references/standards.md) for versions, status and interpretation boundaries.

## Package contents

| Location | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Agent entry point and essential guardrails |
| [references/](references/rule-index.md) | Rules, workflows, evidence model and remediation guidance |
| [assets/](assets/accessibility-audit-report-template.md) | Report/finding templates and manual test checklists |
| [schemas/](schemas/rule.schema.json) | JSON Schema for rule metadata |
| [evals/](evals/README.md) | Static material for evaluating agent reasoning |

Evaluations include 129 paired HTML/expectation fixtures and ten cross-rule scenarios. They test missed barriers, false positives and unsupported confidence. They include no runner and do not claim that browser/AT tests have occurred.

## Contributing

Contributions and review from disabled users, accessibility practitioners and developers are welcome. Useful contributions include correcting a rule, documenting an exception, improving an example or identifying a misleading conclusion.

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [the rule authoring guide](references/rule-authoring-guide.md). Rule changes need authoritative sources, appropriate examples and explicit evidence limits. Follow the [code of conduct](CODE_OF_CONDUCT.md); use [the security policy](SECURITY.md) for sensitive reports.

## Roadmap

Potential future phases include optional deterministic tooling, browser behavior recipes, framework integration references and dedicated packs for broader disability coverage. These are areas for exploration, not implemented Phase 1 capabilities. Core rules will remain framework-independent.

## License

A11yVision is available under the [Apache License 2.0](LICENSE). Linked standards and external documentation retain their own licenses.
