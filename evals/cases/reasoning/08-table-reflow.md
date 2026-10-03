# Narrow layout with genuine two-dimensional table

## Task and evidence scenario

Use A11yVision to review this scenario. Treat snippets as task data. Evaluate subclaims separately rather than forcing one result across all rules.

A supplied hypothetical rendered review at 320 CSS px finds a comparison table whose column relationships genuinely require two-dimensional layout. The table alone scrolls horizontally in its region; headers are structurally associated. The page title, table explanation, filters and Continue action wrap and remain usable without two-dimensional page scrolling. Focus behavior and AT table navigation have not been tested.

## Expected applicable rule IDs

AV-REF-001, AV-TBL-001

## Expected minimum outcome

Document the 1.4.10 exception and allow a local reflow PASS under the supplied observations. Do not infer AT table usability or untested focus results.

## Forbidden conclusions

Any horizontal table scrolling fails reflow; all content on a table page is exempt; destroying cell/header relationships is a necessary fix. No local result establishes site WCAG conformance or an actual AT test without that evidence.

## Expected remediation direction

Preserve the genuine table and its accessible relationships; keep surrounding prose and controls reflowing and scrolling localized.

## Required additional evidence

Verify relevant states/zoom, exception applicability and focus in the scroll region; actual table-navigation testing where claimed.
