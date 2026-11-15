# Practical Lab Library

A curated backlog of reproducible exercises. A lab is complete only when its result is validated and its evidence is documented.

## Lab contract

Every lab record must state:
- Objective, target skill and difficulty.
- Prerequisites, tools, versions and access requirements.
- Environment: local, emulator, hosted sandbox or real cloud.
- Estimated duration and potential cost.
- Steps and expected observations.
- Validation commands and success criteria.
- At least one controlled failure or troubleshooting question.
- Cleanup and rollback steps.
- Evidence link, limitations and date completed.

Never run intentionally vulnerable infrastructure in a shared or production account. Use hosted labs or isolated disposable environments where possible. No real AWS resource creation is authorized by inclusion in this index.

## Prioritized backlog

| ID | Topic | Exercise | Source | Priority |
|---|---|---|---|---|
| LAB-LNX-01 | Linux | Diagnose CPU, memory, disk, process and service symptoms | [SadServers](https://sadservers.com), [sysadmin skills](https://github.com/trimstray/test-your-sysadmin-skills) | P0 |
| LAB-NET-01 | Networking | Trace DNS resolution and diagnose a failed HTTP/TLS path | [SRE prep](https://github.com/mxssl/sre-interview-prep-guide) | P0 |
| LAB-AWS-01 | AWS | Inspect IAM identity and policy evaluation using a safe sandbox or static policy examples | [CloudSec Labs](https://github.com/iknowjason/Awesome-CloudSec-Labs) | P0 |
| LAB-DOCKER-01 | Docker | Build and troubleshoot a multi-container Compose application | [DevOps Exercises](https://github.com/bregman-arie/devops-exercises) | P0 |
| LAB-K8S-01 | Kubernetes | Diagnose Pending, CrashLoopBackOff, ImagePullBackOff and Service-with-no-endpoints cases | [Killercoda](https://killercoda.com), [iximiuz Labs](https://labs.iximiuz.com) | P0 |
| LAB-CICD-01 | CI/CD | Build a pipeline with tests, artifact handling and explicit deployment approval | [DevOps Projects](https://github.com/NotHarshhaa/DevOps-Projects) | P1 |
| LAB-IAC-01 | Terraform | Review plan, state, drift and least-privilege provider configuration | [Cloud Projects](https://github.com/mzazon/cloud-projects) | P1 |
| LAB-SRE-01 | SRE | Convert an incident report into timeline, impact, contributing factors and corrective actions | [Post-mortems](https://github.com/danluu/post-mortems) | P1 |
| LAB-SEC-01 | Cloud security | Complete an authorized IAM or cloud attack-path challenge in an isolated lab | [Awesome CloudSec Labs](https://github.com/iknowjason/Awesome-CloudSec-Labs) | P2 |
| LAB-MSA-01 | Microservices | Deploy and inspect Online Boutique locally; trace one request across services | [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo) | P1 |
| LAB-AI-01 | Agentic DevOps | Build a read-only log summarizer with structured output and evaluation cases | [AI-Assisted DevOps](https://github.com/iam-veeramalla/ai-assisted-devops) | P2 |

## Lab status

Use Not started → Learning → Lab completed → Documented → Interview tested → Interview ready. Do not mark a lab complete from a video or a successful copy-paste alone.

## Lab record template

Use [the lab template](../templates/lab-template.md). Keep raw logs sanitized; never commit credentials, tokens, private keys, personal data, Terraform state or unredacted account identifiers.
