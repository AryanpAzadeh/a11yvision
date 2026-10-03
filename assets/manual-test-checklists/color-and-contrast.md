# Color and contrast checklist

Record route/state/theme, rendered foreground/background, font size/weight, compositing, measured ratio and applicable exception. Never invent a ratio from unresolved tokens, gradients, images, opacity or blending.

- [ ] Text meets 4.5:1 for normal text or 3:1 for WCAG large text (18pt regular or 14pt bold under the criterion's definition); do not round below-threshold results up.
- [ ] Placeholder, help and error text receive the same applicable analysis, along with hover/focus and other relevant states.
- [ ] Keyboard focus is visibly perceivable on actual backgrounds; evaluate applicable non-text contrast separately.
- [ ] Required component boundaries, states, icons and meaningful graphics meet applicable 3:1 against adjacent colors. Check inactive/default-user-agent/essential exceptions; do not fail decorative borders automatically.
- [ ] Charts and legends distinguish series with direct labels, markers, patterns or line styles where needed, and offer equivalent nonvisual data/meaning.
- [ ] Error and required-field indications communicate information without hue alone, with useful visible text or other complete cues.
- [ ] Selected, active, success and warning states have non-color cues where color communicates information.
- [ ] Links are distinguishable under the applicable color/contrast and hover/focus conditions; underline or another suitable cue may help.
- [ ] Test light/dark and other supported themes rather than assuming one token works everywhere.
- [ ] Review forced-colors/high-contrast rendering for disappearing boundaries, focus, icons or states. Report resilience as advisory unless a separate mapped criterion violation is demonstrated.

Increasing red/green contrast alone does not fix hue-only communication. Color perception varies; a simulation does not represent all users.
