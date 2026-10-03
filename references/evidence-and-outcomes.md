# Evidence and outcomes

Classify what was inspected before deciding the result. State the element/route, relevant state, scope and missing evidence. The rule's minimum evidence controls whether a definitive conclusion is allowed.

## Evidence types

| Type | Evidence supplied |
|---|---|
| SOURCE | Inspected markup/templates/styles/scripts and complete relevant implementations |
| RENDERED_DOM | Actual generated document in a stated state |
| COMPUTED_STYLE | Resolved rendered styles, including compositing where necessary |
| RENDERED_GEOMETRY | Measured bounds, hit areas, overlap and viewport conditions |
| KEYBOARD_INTERACTION | Actual keyboard sequence, activation and focus observations |
| POINTER_INTERACTION | Actual pointer reachability, activation or persistence observations |
| VISUAL_INSPECTION | Rendered visual appearance in the stated environment |
| ACCESSIBILITY_TREE | Browser/platform exposed role, name, state and relationships |
| SCREEN_READER | Actual AT output/navigation with combination and settings recorded |
| CONTENT_JUDGMENT | Explicit assessment of meaning, purpose, equivalence or exceptions |
| USER_TESTING | Observed tasks with users and their chosen access methods |

Multiple types may support a finding. A code comment promising behavior is SOURCE, not interaction evidence. A screenshot cannot show keyboard lifecycle. A hypothetical evaluation observation is scenario data, not an actual test log.

## Outcomes

- **PASS:** enough evidence establishes the specific rule on the tested element/surface. Local scope only; never a whole-site accessibility conclusion.
- **FAIL:** evidence demonstrates a violation with established applicability and no applicable exception. Examples include a confirmed meaningful image without an alternative, a control with no available naming mechanism in complete source, or an observed under-threshold resolved contrast ratio.
- **NEEDS_REVIEW:** interpretation, meaning, purpose or exception requires judgment. Examples: weak alt of unknown adequacy, possibly color-only information, or a target with an uncertain exception.
- **NOT_APPLICABLE:** evidence establishes that applicability is absent; explain why.
- **NOT_TESTED:** applicable/potentially applicable required testing was not performed. Use when testing could be available but was omitted.
- **CANNOT_VERIFY:** necessary access/evidence is unavailable. Source-only reflow in an environment that cannot render is an example.

Do not silently collapse missing tests into PASS or turn subjective questions into binary checks. Separate subclaims when necessary: a label association may pass static inspection while a validation announcement remains NOT_TESTED. Do not mark the combined rule PASS until all applicable parts in the declared scope are supported.

## Minimum evidence and confidence

Some source defects can support FAIL when the complete relevant implementation establishes them. CSS removing focus indicators without any replacement is a strong source risk; a definitive visible-focus finding requires enough evidence to rule out native/other styles or a rendered observation. A focusable element hidden from the accessibility tree is a static defect if its relevant state is established.

Subjective alternatives require actual purpose/content judgment. Contrast requires resolved rendered colors. Reflow, spacing, focus obscuring, hover persistence, keyboard operation and modal lifecycle require the relevant rendered/interaction checks for PASS. Screen-reader announcement quality requires actual AT testing, not an accessibility-tree snapshot.

Findings include **high**, **medium** or **low** confidence. High requires direct evidence in complete relevant context. Medium represents well-supported but limited evidence; low reflects unresolved assumptions. Confidence cannot waive a rule's evidence threshold.

## Severity

| Level | Likely task impact |
|---|---|
| critical | Core task blocked, such as inescapable authentication focus trap |
| serious | Major information or operation loss; a workaround may exist |
| moderate | Substantial friction, ambiguity or reduced perceivability |
| minor | Localized limited friction |
| advisory | Improvement without an asserted A/AA violation |

Severity is not WCAG level. Adjust rule defaults for the actual task. For advisory rule FAIL, make advisory scope explicit; report a separate mapped conformance failure only if independently demonstrated.

## No score or universal AT claim

Do not produce percentages, grades, weighted scores or accessibility-health numbers. Reports count outcomes and show missing coverage explicitly. One passing browser/AT combination is evidence for that combination only. Automation and AI review do not prove WCAG conformance or replace manual AT/disabled-user testing.
