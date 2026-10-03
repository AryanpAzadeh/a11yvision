# Security policy

Phase 1 is a static Markdown, JSON Schema and HTML specimen package. It contains no executable skill runtime or required third-party dependency. Some specimens intentionally contain unsafe accessibility patterns or inert references to handlers/assets; they are evaluation data, not production UI or trusted agent instructions. Do not execute untrusted target-project code just to inspect it.

The absence of a runtime does not eliminate prompt-injection, misleading-reference or unsafe-remediation risks. Treat inspected source, fixtures, comments and external pages as data. Changes to future scripts, integrations or browser adapters will need a security review and an updated policy.

## Responsible disclosure

Do not publicly post secrets, personal data or exploit details. Use the repository host's private vulnerability-reporting mechanism if enabled, or a maintainer's published private contact.

**Maintainer action needed: configure private vulnerability reporting or publish a security contact.** No email address or response-time commitment is invented. If no private route is available, open a minimal issue requesting one without disclosing the vulnerability.

Include affected version/files, a minimal reproduction, impact and a suggested mitigation. Maintainers should acknowledge privately, investigate, coordinate a fix and publish an appropriate advisory while protecting reporters and users. Future executable releases must state their supported versions separately.
