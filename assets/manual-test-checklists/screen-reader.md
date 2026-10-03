# Screen-reader manual checklist

Record route/state, OS/browser/AT versions, settings, language, input and navigation mode. For each item record PASS/FAIL/NEEDS_REVIEW/NOT_APPLICABLE/NOT_TESTED/CANNOT_VERIFY, steps and observed output. Use these checks in addition to relevant rule procedures; one tested combination is limited evidence.

- [ ] Page title describes purpose; primary language and applicable passage changes are exposed appropriately.
- [ ] Landmarks identify regions and allow primary-content navigation; repeated content can be bypassed.
- [ ] Heading navigation represents meaningful sections and hierarchy.
- [ ] Links have understandable purposes in permitted context; the link list is useful where possible.
- [ ] Form labels, groups and instructions are available when navigating and entering values.
- [ ] Trigger invalid input; identify the erroneous field, explanation and known safe correction; confirm association and appropriate dynamic announcement/focus.
- [ ] Buttons/controls expose usable names, roles and values.
- [ ] Expanded, selected, checked, pressed, disabled and current states match the actual interface through changes.
- [ ] Open a modal from its trigger; verify name, initial focus, traversal, background behavior, completion/close and logical return focus.
- [ ] Trigger Save, cart/search result changes or completion; applicable statuses are available without unnecessary focus movement or duplicate announcements.
- [ ] Navigate representative table cells; required row/column headers and caption/context are exposed.
- [ ] Image alternatives communicate actual purpose; decorative images avoid noise; functional icons communicate actions.
- [ ] Reading sequence preserves meaning, including reordered/responsive content.
- [ ] Reach chart summaries, data and relationships without relying on visual interpretation.
- [ ] Review prerecorded media for important visual information conveyed by the applicable alternative/audio description; controls alone are insufficient.

Accessibility-tree inspection is not this test. If AT is unavailable record CANNOT_VERIFY and provide exact steps for a tester. Include relevant Braille or disabled-user task evaluation when available and appropriate.
