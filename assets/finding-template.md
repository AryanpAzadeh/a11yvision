# Accessibility finding

ID: AV-...
Outcome: PASS | FAIL | NEEDS_REVIEW | NOT_APPLICABLE | NOT_TESTED | CANNOT_VERIFY
Severity: critical | serious | moderate | minor | advisory
Confidence: high | medium | low
Scope: conformance | advisory
WCAG / ARIA: exact criterion, level and authority; advisory when applicable
Affected users: blind | low-vision | color-vision-deficiency
Location: file/component/route/selector/line, where known
Evidence type: SOURCE, RENDERED_DOM, COMPUTED_STYLE, RENDERED_GEOMETRY,
KEYBOARD_INTERACTION, POINTER_INTERACTION, VISUAL_INSPECTION,
ACCESSIBILITY_TREE, SCREEN_READER, CONTENT_JUDGMENT, USER_TESTING
Tested state/environment: browser/OS/AT/version, viewport, zoom, theme and method

## Problem

State the demonstrated barrier or unresolved question. Distinguish observations from risks and assumptions.

## User impact

Explain the affected task and why severity is appropriate. Do not infer severity solely from WCAG level.

## Evidence

Record relevant source excerpts, observations, steps, colors/geometry where actually resolved, and content judgment. Name missing evidence and any exception evaluated. Do not imply a runtime or AT test happened if it did not.

## Recommended fix

Describe the smallest safe native-first change, preserving product behavior, localization and visual intent. For unresolved cases, obtain evidence before making speculative changes.

## Example patch or code

Insert an applicable localized example or patch. Explain any architecture-dependent behavior that must be preserved.

## Verification

Record the repeated check and actual result; identify the exact scope of a local PASS. Keep unresolved portions visible.

## Manual follow-up

List route/flow, control, required test, expected behavior, missing evidence and responsible next action. Use NOT_TESTED or CANNOT_VERIFY honestly. Tree inspection is not screen-reader testing.
