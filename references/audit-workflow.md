# Audit workflow

## A. Establish scope and access

Record requested files/routes/components, task mode and relevant flows: navigation, search, authentication, forms, checkout, dialogs, tables and charts. Establish whether source, a running application, browser evidence and actual AT testing are available. Follow shared primitives; do not silently reduce a requested component audit to one file when its behavior lives elsewhere.

## B. Inventory web primitives

Search source for controls and handlers; images/SVG/canvas/video; headings/landmarks/lists/tables; form labels, grouping and validation; dialogs/drawers/popovers/tooltips; tabs/menus/disclosures/carousels/composites; roles, aria-* and tabindex; hidden-text utilities; focus styles; sticky/fixed layers; theme/color tokens; breakpoints, overflow, fixed dimensions and CSS ordering/repositioning.

Use framework-specific search syntax to locate implementation, then apply independent web requirements. Load [the rule index](rule-index.md) and only applicable rules.

## C. Review source with bounded conclusions

Complete source may establish a confirmed meaningful image lacks any alternative, a button has no name source, an operable control is aria-hidden, or a fully inspected mouse-only implementation lacks keyboard support. State precisely what was established.

Do not source-pass reflow, unresolved contrast, visible focus in rendered states, focus obscuring, hover persistence, modal lifecycle, actual announcements or subjective alternative quality. Treat outline removal as a risk until context/rendering establishes whether another indicator exists. See [evidence outcomes](evidence-and-outcomes.md).

## D. Obtain rendered evidence when available

Inspect actual DOM, tree, computed styles, target bounds, keyboard order/activation, focus indicators, occluding layers, 200% text enlargement, reflow, spacing overrides, popup behavior and status changes. Record browser, viewport/zoom, theme, state and method. The package assumes no particular automation library and does not require installing one.

## E. Plan missing manual checks

Identify the target route/flow and exact controls, expected announcements/structure, transitions and status updates. Suggest relevant AT/browser combinations without treating one as universal. Use [AT guidance](assistive-technology-testing.md) and [checklists](../assets/manual-test-checklists/screen-reader.md). List NOT_TESTED and CANNOT_VERIFY with their missing evidence and next action.

## F. Prioritize and fix

Start with core-task blockers, missing semantics/names, keyboard traps and focus loss; then errors/instructions, visual perceivability and structural navigation. Address advisory resilience after confirmed barriers. Use [remediation policy](remediation-policy.md) rather than a numeric score. For a patch review, compare changed behavior and affected shared consumers; for a build, apply the same rules before and after rendering.

## G. Verify and report

Repeat the failing check after changes. Verify no new keyboard/focus issue, relevant responsive/localization behavior and both visible and accessible names. Report counts of confirmed failures, needs review, not tested/cannot verify and checks actually passed; keep detailed unresolved records. Use the [report template](../assets/accessibility-audit-report-template.md). Never declare site conformance from this focused audit.
