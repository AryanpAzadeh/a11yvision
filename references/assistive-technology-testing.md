# Assistive-technology testing

Actual screen-reader behavior depends on AT, browser, OS, versions, settings, language and navigation mode. One passing combination is evidence, not universal proof. AI agents must not claim to have used NVDA, JAWS, VoiceOver, Narrator, TalkBack, Braille or magnification software unless they actually did. Tree inspection is useful but is not actual screen-reader output.

## Record a reproducible test

For each flow record route/state, AT/browser/OS versions, verbosity and relevant settings, navigation mode, input method, steps, observed output and expected task result. Record discrepancies, workarounds and remaining tests. Do not prescribe one exact announcement string when equivalent output meets the need.

Possible combinations to select for the target audience include NVDA with Firefox/Chrome on Windows, JAWS with a supported Windows browser, VoiceOver with Safari on macOS/iOS, Narrator with Edge and TalkBack with Chrome on Android. These are examples for planning, not a tested compatibility matrix or universal recommendations. Where relevant include refreshable Braille, magnification, custom colors and users' preferred configurations.

## Tasks to verify

Use the [screen-reader checklist](../assets/manual-test-checklists/screen-reader.md) for title/language, landmarks/headings, links, controls, forms/errors, state, dialogs, status, tables, alternatives, reading order and charts. Pair it with [keyboard](../assets/manual-test-checklists/keyboard-focus.md), [zoom/reflow](../assets/manual-test-checklists/zoom-reflow.md), [color/contrast](../assets/manual-test-checklists/color-and-contrast.md) and [dynamic content](../assets/manual-test-checklists/dynamic-content.md).

For a dialog, record opening trigger, initial focused item and announcement, traversal, background reachability, operable close/complete action and return location. For validation, record invalid input, detected error, field association, announcement timing, correction and successful submission. For a chart, navigate to summary and structured data, then verify that conclusions and relationships are available without the visual.

## When AT is unavailable

Report CANNOT_VERIFY for unavailable AT evidence; use NOT_TESTED when access is possible but testing was omitted. A DOM/tree result may support a limited semantic claim but cannot become an announcement-quality PASS. Provide a concrete manual plan with exact flows and expected behavior. Technical checks do not replace disabled-user task testing; obtain consent and respect participants' access preferences.
