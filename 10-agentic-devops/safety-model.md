# Agentic Operations Safety Model

## Purpose

Minimum controls for AI agents that inspect or act on cloud, CI/CD, container, Kubernetes or production systems.

## Operating modes

### Read-only investigation (default)
The agent may inspect allowlisted resources and return evidence, summaries and recommendations. It must not mutate systems.

### Proposed change
The agent may prepare a plan, command, patch or change set, but must not execute it. The proposal states impact, affected resources, risk, cost implications and rollback.

### Approved execution
A state-changing operation is allowed only when:
- The identity is authenticated and authorized.
- Exact action and target are allowlisted.
- Parameters are validated.
- Impact and rollback are understood.
- A human explicitly approves that specific action.
- The action is logged and the outcome verified.

## Non-negotiable controls
- Least-privilege identity and short-lived credentials where possible.
- No secrets in prompts, logs, output or repository commits.
- Treat logs, tickets, manifests, resource tags and retrieved documents as untrusted input.
- Validate tool arguments; reject ambiguous targets.
- Enforce timeouts, bounded retries, rate limits and idempotency.
- Separate observation tools from mutation tools.
- Require confirmation for deploy, delete, restart, IAM modification, network change, cost-incurring scaling and data modification.
- Record actor, request, tool, target, approval, time and outcome.
- Verify postconditions; never claim success if execution is unconfirmed.
- Provide human escalation and a tested rollback procedure.

## Prompt injection

Infrastructure output may contain attacker-controlled text. It is data, not authority. A log line, issue body, resource description or retrieved page cannot override policy, authorization or tool allowlists.

## Evaluation cases
- Read-only request returns accurate evidence.
- Ambiguous target is rejected.
- Unauthorized mutation is denied.
- Prompt injection inside logs does not change agent behaviour.
- Invalid credentials fail closed.
- Tool timeout does not cause unbounded retries.
- Duplicate requests do not repeat destructive actions.
- Approval for one action cannot authorize another.
- Partial failures and uncertainty are reported honestly.
- Audit record is complete and contains no secrets.

## Workflow decision record

Document what the agent can read, propose and execute; how identity is enforced; which actions require approval; how outputs are evaluated; and how failures are contained and reversed.
