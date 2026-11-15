# Engineering Case Studies

This section develops production reasoning from real incident reports and architecture examples. A case study is an analysis exercise, not a claim that the handbook author experienced the incident.

## Case-study sources

- [Dan Luu's post-mortem collection](https://github.com/danluu/post-mortems) — incident reports grouped around configuration errors, hardware/power, conflicts, time, databases and other categories. Follow each linked original report before making detailed claims.
- [Google Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo) — an 11-service e-commerce demo using multiple languages and gRPC. Use it to study service boundaries, dependencies, request paths and deployment behaviour.
- [DevOps AI Playbook](https://github.com/vishakhasadhwani/devops-ai-playbook) — describes a project flow spanning microservices, Docker, EKS, GitHub Actions, GitOps, Terraform, observability and an AIOps assistant. Treat its architecture as a study reference and verify the implementation before reproducing it.

## Incident analysis method

For each incident:
1. Identify the affected user-facing capability and impact window.
2. Build a timestamped event timeline from the primary report.
3. Separate trigger, root cause, contributing conditions and detection gaps.
4. Explain why existing tests, monitoring or controls did not prevent or detect it.
5. Distinguish mitigation from permanent corrective action.
6. Identify prevention, detection, response and recovery improvements.
7. Derive transferable engineering lessons without hindsight bias.

Use [the incident template](../templates/incident-template.md). Avoid blame-oriented narratives; focus on system conditions and actionable learning.

## Initial analysis backlog

| ID | Study | Questions to answer |
|---|---|---|
| CASE-01 | Cloudflare configuration and routing incidents in the post-mortem collection | How did configuration validation, rollout scope and blast-radius controls affect impact? |
| CASE-02 | CircleCI schema/deployment incident in the collection | Why did rollback not restore service cleanly? What compatibility strategy would reduce risk? |
| CASE-03 | CircleCI WAF / out-of-band change incident in the collection | How can infrastructure drift and unclear authorization mislead incident response? |
| CASE-04 | Online Boutique request flow | Which service dependencies are synchronous, where can latency propagate, and what telemetry would isolate a failing dependency? |
| CASE-05 | DevOps AI Playbook architecture | Which operations should remain deterministic, which can be assisted by AI, and where are human approval boundaries needed? |

The incident names above are pointers found in the inspected collection README. Before writing a detailed case analysis, open and cite the original incident report and record its publication date and evidence.
