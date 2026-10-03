# Remediation policy

Fix confirmed barriers with the smallest safe change that preserves product behavior, architecture, localization and visual identity. Prioritize user impact rather than satisfying a checker.

## Preferred order

1. Correct semantic HTML.
2. Correct content, labels and alternatives based on known meaning.
3. Correct CSS/layout behavior.
4. Correct native interaction behavior.
5. Use ARIA where needed to expose otherwise unavailable semantics/state.
6. Add custom keyboard/focus logic only when the actual UI pattern needs it.

A targeted fix is preferred to rewriting a component. Replace a fundamentally inaccessible simulated native control when patching it would create fragile ARIA/keyboard behavior. Preserve the intended action and side effects.

## Copy, localization and names

Accessible text is product copy. Use existing i18n mechanisms; do not hard-code English into localized UI or translate brand/product names without reason. Hidden accessible text needs localization just like visible text.

Before adding aria-label, inspect visible text, label association, aria-labelledby references, applicable alt and native value/name sources. Follow naming precedence; do not stack mechanisms blindly. Keep visible label text in the name where 2.5.3 applies. Do not invent image content from a filename.

## Focus and hidden state

Never use positive tabindex as a general order fix. Correct DOM order, inactive focusability and modal/popover lifecycle. Use tabindex="-1" only for deliberate appropriate programmatic targets and tabindex="0" only for legitimate custom focusable elements. Do not hide an operable focus target from the accessibility tree.

Retain outlines unless a visible replacement is supplied. Recheck focus after semantic replacements, validation, insertion and dialog closure. aria-modal and aria-hidden do not implement focus management or inertness.

## Visual identity and safety

Choose a nearby suitable contrast token rather than replacing the palette. Add non-color cues while retaining useful color. Allow wrapping/growth/reflow without unnecessary redesign; preserve animation unless an applicable barrier requires a change. Respect legitimate tables/maps and target-size exceptions.

Do not install or recommend an accessibility overlay/widget as a substitute for fixing code. Do not add unnecessary ARIA/live regions/hidden copy to make automated checks green.

After a patch, repeat the failing check, verify relevant names and keyboard behavior, and check affected responsive/localized states. Report unperformed rendered/AT checks explicitly using [the finding template](../assets/finding-template.md).
