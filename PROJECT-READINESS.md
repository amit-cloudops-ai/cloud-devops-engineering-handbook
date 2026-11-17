# Portfolio Project Readiness

This tracker distinguishes a project idea from an implemented, tested and interview-ready project. Current status is based on the repository's project records and known prior local work; it is not a fresh code audit of each external project repository.

## Current portfolio queue

| Project | Current evidence status | Next action |
|---|---|---|
| [AWS Infrastructure Auditor](11-projects/aws-infrastructure-auditor/README.md) | Initial project record; implementation details and tests need verification | Audit scope, IAM permissions, pagination, tests and sanitized output |
| [Ops Sentinel](11-projects/ops-sentinel/README.md) | Concept / brief; validate against actual implementation | Build read-only evidence collection and evaluation before remediation |
| [AWS Emulator Lab](11-projects/aws-emulator-lab/README.md) | Prior local S3, DynamoDB and SQS exercises; refresh version and test evidence | Reproduce smoke tests and document emulator differences |
| [Kubernetes Agents](11-projects/kubernetes-agents/README.md) | Future project area | Start with namespace-scoped read-only diagnostics |

## Definition of project-ready

A project is ready for a technical interview only when the following evidence is available:

- [ ] Problem statement, target user and scope.
- [ ] Architecture diagram and request/data flow.
- [ ] Reproducible setup with versions and prerequisites.
- [ ] Tests with visible results and meaningful failure cases.
- [ ] Security review: identity, permissions, secrets, data handling and threat model.
- [ ] Operational story: logs, metrics, errors, recovery and limitations.
- [ ] Cost assumptions and cleanup instructions.
- [ ] Professional README with screenshots or sanitized demo.
- [ ] A 2–4 minute walkthrough and answers to likely follow-up questions.

## Priority order

1. **AWS Infrastructure Auditor:** strong alignment to Cloud/DevOps/security interviews; verify the implementation and evidence first.
2. **AWS Emulator Lab:** fast hands-on refresh using local infrastructure; use it to reinforce AWS service operations without provisioning real AWS resources.
3. **Ops Sentinel:** differentiating AI + SRE project; keep the first milestone read-only and testable.
4. **Kubernetes Agents:** begin after Kubernetes troubleshooting and RBAC foundations are demonstrable.

The dashboard's project checklist is browser-local. Export its JSON and update `dashboard/progress.json` to persist completed checks in Git.
