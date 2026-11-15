# Learning Roadmap

This is a prioritized sequence, not a claim that every subject can be mastered in 30 days. Build shared infrastructure competence first; then deepen the Agentic DevOps specialization.

## Priority levels

- **P0:** common interview foundation.
- **P1:** role differentiators.
- **P2:** specialization and follow-on breadth.

| Order | Area | Priority | Evidence required |
|---:|---|---|---|
| 1 | Linux and operating systems | P0 | Diagnose process, disk, memory, permission, service and log issues |
| 2 | Networking | P0 | Explain DNS and HTTP request path; diagnose connectivity and TLS |
| 3 | Git and GitHub | P0 | Branch, merge, resolve conflicts, review PRs and recover safely |
| 4 | Bash and Python | P0 | Tested scripts with validation, logging and failure handling |
| 5 | AWS fundamentals | P0 | Explain IAM, VPC, EC2, S3, routing, security and monitoring |
| 6 | Docker and Compose | P0 | Build, inspect and troubleshoot a multi-container app |
| 7 | CI/CD | P0 | Pipeline with tests, artifacts, security checks and approval gates |
| 8 | Kubernetes | P1 | Deploy and diagnose common Pod and Service failures |
| 9 | Terraform / IaC | P1 | Explain plan, state, modules, drift and safe changes |
| 10 | Observability and SRE | P1 | Investigate an incident using metrics, logs and runbooks |
| 11 | Security and FinOps | P1 | Review least privilege, secrets, image risks and cost |
| 12 | Agentic AI engineering | P1 | Bounded tool-using operations agent with evaluations |
| 13 | System design | P2 | Defend resilient, secure, observable and cost-aware architectures |
| 14 | Azure and GCP | P2 | Understand service mappings after the AWS foundation |

## Resource-backed study path

Use [RESOURCE-INDEX.md](RESOURCE-INDEX.md) to choose a source, [15-practical-labs](15-practical-labs/README.md) to select an exercise, [16-engineering-case-studies](16-engineering-case-studies/README.md) to develop production reasoning and [17-interview-intelligence](17-interview-intelligence/README.md) to test recall and explanation.

Do not complete every external repository. Select one resource per gap, build evidence, then move on.

## 30-day execution framework

### Days 1–3 — Baseline and repair
- Diagnose current Linux, networking, Git, Docker and AWS knowledge.
- Record gaps in [PROGRESS.md](PROGRESS.md).
- Validate portfolio project READMEs, demos and links.
- Start applying immediately; preparation must not delay applications.

### Days 4–9 — Core infrastructure
Linux troubleshooting, DNS, TCP, HTTP/S, TLS, SSH, routing, Git workflows, Bash and Python automation. Use LAB-LNX-01 and LAB-NET-01 as practical anchors.

### Days 10–15 — Cloud and containers
IAM, EC2, VPC, subnets, routing, gateways, security groups, S3, CloudWatch, Dockerfiles, networking, volumes, Compose and debugging. Prefer local/emulated work or hosted sandboxes until cloud cost and permissions are reviewed.

### Days 16–20 — Delivery and orchestration
GitHub Actions, pipeline stages, secrets, artifacts, approvals, rollback, Kubernetes objects, probes, services, configuration, storage and Terraform fundamentals. Use Online Boutique as an optional multi-service study application.

### Days 21–24 — Reliability and security
Metrics, logs, alerting, dashboards, SLIs/SLOs, incident response, least privilege, secret handling, vulnerability scanning and cost controls. Analyse at least one original post-mortem report.

### Days 25–27 — Agentic operations
Agent architecture, tool calling, bounded execution, structured outputs, safety controls and evaluation. Demonstrate read-only diagnosis and approval gates.

### Days 28–30 — Interview execution
Role-specific mock interviews, project walkthroughs, behavioural examples, weak-area revision, applications and follow-ups.

## Daily learning loop

Understand → Implement → Break safely → Diagnose → Document → Retrieve from memory → Apply to job requirements.

## Interview readiness gate

You are ready on a topic when you can:
- Define it and explain why it exists.
- Describe its architecture or execution flow.
- Use relevant commands or tooling.
- Diagnose at least one common failure.
- Explain security, reliability and cost implications where relevant.
- Answer foundational, practical and scenario-based questions in your own words.

## Weekly review

- What can I explain without notes?
- What have I implemented and verified?
- What failed, and how did I diagnose it?
- Which interview questions are still weak?
- Which job descriptions reveal a meaningful skill gap?
- What low-priority study should I stop doing?
