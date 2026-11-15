# Agent Architecture

Document each agent as an explicit control loop: input, context retrieval, model reasoning, tool selection, schema validation, authorization, tool execution, observation, termination and final report.

For every design, distinguish model-generated reasoning from deterministic policy enforcement. The model must not be the authorization boundary.

## Design record
- Objective and non-goals:
- Allowed inputs:
- Trusted context sources:
- Available tools:
- Tool schemas and validation:
- Permission model:
- Human approval boundary:
- Timeout / retry / idempotency strategy:
- Audit record:
- Evaluation set:
- Failure and escalation behaviour:
