# Ops Sentinel — AI Incident Commander

**Documentation status:** Project concept / brief to validate against implementation. Do not describe planned capabilities as implemented.

## Intended outcome
Assist operators during incidents by collecting approved evidence, summarizing timelines, proposing diagnostic steps and generating a human-reviewed incident record.

## Constraints
- Read-only evidence gathering by default.
- Source attribution for findings.
- Confidence and uncertainty shown.
- Human approval before remediation.
- No unrestricted production shell or cloud-admin credentials.
- Repeatable evaluation scenarios.

## Milestones
1. Define incident scenarios and fixtures.
2. Define read-only tools and schemas.
3. Build evidence collection and timeline generation.
4. Add evaluation and unsafe-action tests.
5. Add proposed remediation only after the read-only path is reliable.
