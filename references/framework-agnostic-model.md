# Framework-agnostic model

Framework syntax is an implementation detail. Evaluate rendered semantics, accessible names/descriptions, states, relationships, source/reading order, focus, keyboard behavior, visual presentation and content meaning.

## Map source to the web platform

Raw HTML, React/JSX and Vue templates can all produce this same native control:

```html
<button type="button">Save</button>
```

A server template may localize the same name:

```blade
<button type="button">{{ __('Save') }}</button>
```

Preserve localization and inspect the final name; the template language does not change the requirement.

```html
<button class="rounded px-4 py-2 focus-visible:ring-2">Save</button>
```

Tailwind classes are styling mechanisms. Their names do not prove focus visibility, final colors or contrast. Inspect the generated CSS, theme and rendered state before concluding.

## Follow custom components

```jsx
<Button icon="trash" onClick={removeItem} />
```

Inspect the component implementation and its composition or rendered output before deciding whether it produces a button, an actionable name, keyboard activation, required disabled/pressed/expanded state and visible focus. A prop named label may never become an accessible name. A component named Button may render a div.

If abstractions obscure the result, inspect implementation or rendered DOM/accessibility tree where available. Otherwise record CANNOT_VERIFY when implementation/output is unavailable, or NEEDS_REVIEW for an unresolved contextual interpretation. Do not guess semantics from framework/component names.

## Evidence boundaries

Source can establish an explicit missing relationship in complete markup. Generated DOM can resolve template output; an accessibility tree can show exposed role/name/state. Neither proves actual keyboard or screen-reader behavior. Use [evidence and outcomes](evidence-and-outcomes.md), then the selected rule's specific procedure.
