---
name: a11yvision
description: Framework-agnostic web accessibility review and remediation for blind, low-vision, and color-vision-deficient users. Use when an AI coding agent is asked to audit, build, refactor, review, or fix websites or web UI for WCAG 2.2 A/AA visual accessibility, including screen-reader semantics, accessible names, keyboard/focus behavior, alt text, forms, color use, contrast, zoom, reflow, and dynamic content.
---

# A11yVision

Review web barriers within the requested scope. Phase 1 supplies instructions and static references; it requires no runtime, scanner, framework adapter or paid service. WCAG 2.2 A/AA is the conformance baseline for this visual-access rule set, not a claim of complete WCAG coverage.

## Choose the task and evidence

1. Determine whether the request is to build UI, audit code, fix known findings, review a patch/PR, or prepare manual tests. Follow the user's scope and existing project conventions.
2. Discover markup, templates, components, styles and scripts. Follow shared primitives to their implementation. Map framework syntax to final web semantics using [the framework model](references/framework-agnostic-model.md).
3. Inventory affected pages/routes, shared layouts, navigation, forms, images/media, widgets, dialogs/popovers/tooltips, charts and responsive behavior. Use [the audit workflow](references/audit-workflow.md) for a full audit.
4. Load [the rule index](references/rule-index.md), then only relevant rule files. For standards questions use [the standards policy](references/standards.md); for user impact use [user needs](references/user-needs.md).
5. Classify available evidence before the outcome using [evidence and outcomes](references/evidence-and-outcomes.md). Inspect source first. Use rendered/browser tools when available; do not install a runtime or pretend tools exist.
6. Apply confirmed fixes through native semantics first, following [remediation policy](references/remediation-policy.md). Preserve architecture, localization, product behavior and visual identity.
7. Repeat the appropriate verification after changes. Record unresolved manual checks using [AT guidance](references/assistive-technology-testing.md) and the [manual checklists](assets/manual-test-checklists/screen-reader.md).
8. Report with the [finding template](assets/finding-template.md) and [audit report](assets/accessibility-audit-report-template.md). Include every unresolved NOT_TESTED and CANNOT_VERIFY result; never replace these with a score.

For building UI, use relevant requirements during implementation, then verify them with the same evidence limits. For known fixes, reproduce or inspect the supplied evidence before changing code. For patch review, follow affected shared components and check regressions, not just changed lines. For manual plans, identify exact flows, controls, expected transitions and observations rather than implying tests occurred.

## Non-negotiable guardrails

- ARIA presence is not accessibility. Prefer native HTML; do not add unnecessary roles to native elements.
- Do not use positive tabindex to repair focus order.
- Do not use aria-label as a blanket replacement for visible labels; inspect name precedence and preserve visible label text and localization.
- Do not invent image meaning from filenames or pass alt quality from attribute presence alone.
- Do not remove focus outlines without an equally or more visible replacement.
- Do not set aria-hidden="true" on focusable controls or ancestors containing focusable descendants.
- Do not use color as the sole cue for state, errors, required fields or chart differentiation.
- Do not report a contrast ratio without resolving the rendered foreground/background for the relevant state.
- Do not pass reflow, focus visibility/obscuring, hover persistence or modal focus lifecycle from source alone.
- Accessibility-tree inspection is not a screen-reader test. Claim AT testing only when it actually occurred.
- A local PASS is not site-level WCAG conformance. Never claim certification, complete accessibility or an accessibility score from this review.
- When meaning or exceptions are uncertain use NEEDS_REVIEW. If testing was skipped use NOT_TESTED; if evidence/access is unavailable use CANNOT_VERIFY. Use NOT_APPLICABLE only with established absence of applicability.

This review identifies issues within available evidence and tested scope. It does not replace manual assistive-technology testing or testing by disabled users.
