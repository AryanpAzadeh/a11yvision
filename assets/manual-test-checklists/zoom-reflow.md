# Zoom, reflow and text-spacing checklist

Record browser, original viewport and text size, resizing method, zoom, resulting CSS viewport and affected routes/states. Use relevant WCAG exceptions rather than assuming every overflow is a failure.

- [ ] Resize text to 200% without assistive technology; inspect and complete tasks without lost content/functionality. Pixel units alone do not fail this test.
- [ ] For vertically scrolling content test a width equivalent to 320 CSS px, often 400% browser zoom from a 1280px viewport. For horizontally scrolling content test the 256 CSS px height condition.
- [ ] Ordinary reading/use does not require two-dimensional scrolling; controls and prose remain available.
- [ ] No clipped labels, form values or help/error text.
- [ ] No overlapping controls and no hidden primary actions; navigation and form completion remain usable.
- [ ] Fixed/sticky headers, footers, banners and chat UI do not remove meaningful content or completely obscure focus.
- [ ] Document genuine two-dimensional content exceptions, such as applicable data tables/maps/diagrams. Inspect surrounding prose/actions independently; do not destroy table relationships to eliminate legitimate scrolling.
- [ ] Apply all applicable text-spacing overrides together: line height at least 1.5×, paragraph spacing at least 2×, letter spacing at least 0.12× and word spacing at least 0.16× font size.
- [ ] Under those combined overrides there is no clipping, overlap, disappearing label or lost function; handle language/script properties that do not apply without breaking shaping.
- [ ] Focus-revealed links and visually hidden utilities do not create clipped focus, visible fragments or tiny scroll regions.

A responsive breakpoint or flexible CSS is a candidate implementation, not evidence of PASS. Record NOT_TESTED/CANNOT_VERIFY if these rendered checks did not occur.
