# 10 — Agentic DevOps

Study how tool-using AI agents can support cloud and infrastructure operations. Agents should augment deterministic engineering controls, not bypass them.

## Topics
- [Agent architecture](agent-architecture/README.md): state, planning, tools and bounded execution.
- [Tool calling](tool-calling/README.md): schemas, validation, authorization and idempotency.
- [Evaluations](evaluations/README.md): quality, safety and regression testing.
- [Safety model](safety-model.md): read-only defaults, human approval, audit and blast-radius controls.
- [AI Infrastructure curriculum](../AI-INFRASTRUCTURE.md): GPU serving, RAG, MLOps, model gateways, MCP and AIOps.

## Practical project ladder
- Read-only Kubernetes diagnostic assistant.
- CI/CD failure explanation assistant.
- Log and alert summarizer with evidence links.
- Approval-gated remediation proposal in an isolated lab.

## Supplementary learning
- [AI-Assisted DevOps](https://github.com/iam-veeramalla/ai-assisted-devops) — AI for DevOps, prompting, local LLMs, scripting, observability and agent projects.
- [DevOps AI Playbook](https://github.com/vishakhasadhwani/devops-ai-playbook) — a project architecture connecting microservices, CI, GitOps, Terraform, Kubernetes and AIOps.

Use these as learning references. Verify repository code, dependencies, cloud configuration, current model/provider behaviour and cost before implementation. Do not blindly execute generated shell commands, Terraform or Kubernetes manifests.

## Operational safety
Agents default to read-only investigation. Any operation that changes infrastructure, deploys software, modifies access, restarts workloads, deletes data, changes routing or incurs cost must be explicitly bounded, authorized, logged and protected by human approval.
