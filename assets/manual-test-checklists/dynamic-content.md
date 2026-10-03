# Dynamic-content checklist

Record initial and updated state, trigger, DOM/tree observations, keyboard/pointer steps and actual AT output when tested. Separate each evidence type; source is not a test of the lifecycle.

- [ ] Disclosure, tab, menu and composite roles/names/relationships match the intended interaction model.
- [ ] Expanded/selected/checked/pressed/current values track visible state before and after changes.
- [ ] Appropriate widget-specific keys operate every required action; focus does not jump unpredictably during updates.
- [ ] Hidden/inactive content agrees across visual presentation, tree exposure and focusability; aria-hidden does not leave reachable controls invisible to AT.
- [ ] Open/complete/cancel dialogs from each relevant trigger; check initial/contained/returned focus and background inertness.
- [ ] Trigger routine status updates such as Saved or result counts; suitable roles/properties expose them without forced focus changes.
- [ ] Actual AT announcements are useful and avoid duplicates or unjustified assertive interruption; tree evidence alone does not demonstrate output.
- [ ] Dynamic validation identifies fields and errors, preserves input and offers known safe corrections; check appropriate announcement or focus summary behavior.
- [ ] Hover/focus content is dismissible when required, hoverable when hover-triggered and persistent until trigger removal, dismissal or invalidation. Test pointer movement into it.
- [ ] Client-side navigation updates applicable document title and maintains meaningful reading/focus context.

If behavior cannot be tested, specify exact missing observations and use NOT_TESTED/CANNOT_VERIFY. Do not assume role="dialog", aria-modal, role="status" or a focus handler establishes successful behavior.
