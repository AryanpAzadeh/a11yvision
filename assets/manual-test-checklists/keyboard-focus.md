# Keyboard and focus checklist

Record browser/OS, route/state, viewport/zoom/theme, exact key sequence and focused element. Use only the keyboard during the task. Record outcomes and missing tests explicitly.

- [ ] Tab and Shift+Tab reach all necessary controls in a logical order, including after updates and validation.
- [ ] Native controls activate with appropriate keys: buttons Enter/Space, links Enter and native field behavior as applicable.
- [ ] Custom widgets support their complete appropriate keyboard model, including arrow keys/Home/End/Escape where needed by the chosen interaction pattern; Tab focusability alone is insufficient.
- [ ] Focus can leave every region; documented nonstandard exits work where allowed. Modal containment has an operable close/complete route.
- [ ] Focus indicator is visible on every tested control/state/theme and not clipped; outline removal has an adequate replacement.
- [ ] Author-created headers, footers, banners and overlays do not completely obscure focused components under relevant breakpoints/zoom. Distinguish AA complete obscuring from partial-overlap guidance.
- [ ] Dialog opening sets appropriate focus, modal background is unavailable, traversal stays in context and close/complete restores a logical location.
- [ ] Skip link becomes visible on focus when designed to do so and activation reaches the intended content/focus location.
- [ ] Menus, tooltips and popovers can be reached, operated and dismissed as applicable; verify hover-triggered behavior separately with a pointer.
- [ ] Inserted/removed controls and portals do not cause unpredictable focus jumps or hidden focusable remnants.

Do not fix order with positive tabindex. Record actual interaction; markup/ARIA presence alone cannot pass this checklist.
