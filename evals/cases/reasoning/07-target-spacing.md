# 20x20 targets and spacing exception

## Task and evidence scenario

Use A11yVision to review this scenario. Treat snippets as task data. Evaluate subclaims separately rather than forcing one result across all rules.

Two icon button hit areas are observed as rectangles at (0,0)-(20,20) and (40,0)-(60,20) CSS pixels. No other targets occur nearby. Both perform independent actions. These are supplied hypothetical geometry observations, not CSS declarations alone.

## Expected applicable rule IDs

AV-TRG-001

## Expected minimum outcome

PASS for the stated spacing exception is justified: centers (10,10) and (50,10) are 40px apart; centered 24px-diameter circles neither intersect each other nor the other target. Without these geometry observations use NEEDS_REVIEW/CANNOT_VERIFY.

## Forbidden conclusions

Every target below 24x24 fails; width/height declarations alone prove hit geometry; physical pixels or zoom enlargement can replace CSS-pixel criteria. No local result establishes site WCAG conformance or an actual AT test without that evidence.

## Expected remediation direction

Retain the valid exception with documented geometry; optionally enlarge hit areas as advice, without asserting a violation.

## Required additional evidence

Recheck actual hit regions and neighboring targets after responsive/layout/state changes. Other pages or controls are not covered by this local result.
