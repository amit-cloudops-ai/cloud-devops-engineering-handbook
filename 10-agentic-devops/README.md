# Agentic DevOps

Study how tool-using AI agents support cloud and infrastructure operations. Agents complement deterministic automation; they do not replace engineering review.

## Curriculum
1. LLM fundamentals and structured outputs.
2. Agent loops, planning, tool calling and execution boundaries.
3. Tool schemas, validation, idempotency, timeouts and retries.
4. State, memory, context and provenance.
5. Retrieval grounded in trusted runbooks.
6. Guardrails, authorization, approval gates and audit logs.
7. Prompt injection and untrusted infrastructure output.
8. Evaluation datasets, success criteria and regression tests.
9. Human oversight, rollback, escalation and handoff.

## Candidate workflows
- Cloud configuration auditor: read-only inventory and evidence-backed findings.
- Incident investigation assistant: summarize approved alerts, logs and events.
- Kubernetes diagnostic assistant: inspect workload status and propose next steps.
- CI/CD failure assistant: explain failed stages and suggest reproducible fixes.

## Supplementary learning
- [AI-Assisted DevOps](https://github.com/iam-veeramalla/ai-assisted-devops) — syllabus-style material covering AI for DevOps, prompting, local LLMs, scripting, observability and agent projects.
- [DevOps AI Playbook](https://github.com/vishakhasadhwani/devops-ai-playbook) — an end-to-end project description connecting microservices, CI, GitOps, Terraform, Kubernetes and AIOps.

Use these as learning references. Verify repository code, dependencies, cloud configuration, current model/provider behaviour and cost before implementation. Do not blindly execute generated shell commands, Terraform or Kubernetes manifests.

Read the [safety model](safety-model.md) before designing agents with operational access.
