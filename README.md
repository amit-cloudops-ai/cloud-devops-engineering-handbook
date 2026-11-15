# Cloud & DevOps Engineering Handbook

A practical, evidence-driven handbook for **Cloud Engineering, DevOps, Platform Engineering, Site Reliability Engineering (SRE), and Agentic AI Operations**.

**Primary positioning:** AI-Agentic DevOps / Cloud Engineer  
**Primary job market:** Pune, India · **Secondary:** Bengaluru, India

This is a public learning system and engineering portfolio. It turns study into demonstrable capability through original notes, practical labs, troubleshooting records, architecture decisions, projects and interview practice.

## Handbook map

| Area | Purpose |
|---|---|
| [00 — Foundations](00-foundations/README.md) | Linux, networking, operating systems, troubleshooting |
| [01 — Programming](01-programming/README.md) | Bash, Python, APIs and automation |
| [02 — Version control](02-version-control/README.md) | Git, GitHub and collaboration |
| [03 — Cloud](03-cloud/README.md) | AWS-first cloud engineering, architecture and operations |
| [04 — Containers](04-containers/README.md) | Docker, Compose and troubleshooting |
| [05 — Orchestration](05-orchestration/README.md) | Kubernetes |
| [06 — CI/CD](06-cicd/README.md) | GitHub Actions, pipelines and deployment |
| [07 — Infrastructure as Code](07-infrastructure-as-code/README.md) | Terraform and configuration management |
| [08 — Observability & SRE](08-observability-sre/README.md) | Metrics, logs, alerting, SLOs and incidents |
| [09 — Security & FinOps](09-security-finops/README.md) | Cloud security and cost |
| [10 — Agentic DevOps](10-agentic-devops/README.md) | Tool-using agents, evaluations and guardrails |
| [11 — Projects](11-projects/README.md) | Portfolio projects and implementation evidence |
| [12 — Interview preparation](12-interview-preparation/README.md) | Role-based questions, scenarios and mock interviews |
| [13 — System design](13-system-design/README.md) | Cloud architecture and distributed systems |
| [14 — Resources](14-resources/README.md) | Official docs, articles, videos and job descriptions |
| [15 — Practical labs](15-practical-labs/README.md) | Reproducible exercises and validation evidence |
| [16 — Engineering case studies](16-engineering-case-studies/README.md) | Production incidents and architecture analysis |
| [17 — Interview intelligence](17-interview-intelligence/README.md) | Question practice, company reports and mock tracking |
| [Resource index](RESOURCE-INDEX.md) | Curated external repositories and learning platforms |
| [Lab index](15-practical-labs/README.md) | Prioritized practical backlog |
| [Interview tracker](INTERVIEW-TRACKER.md) | Topic and mock-interview tracking |
| [Templates](templates/README.md) | Consistent formats for topics, labs and interviews |

## Target role families

- DevOps Engineer
- Cloud Engineer / Cloud Operations Engineer
- Platform Engineer
- Site Reliability Engineer (SRE)
- Adjacent entry-level roles: Cloud Support, Infrastructure Support, Build & Release, Technical Operations

Agentic AI is a specialization layered on top of strong infrastructure fundamentals. The goal is not to claim broad AI expertise; it is to demonstrate safe, useful AI-assisted operations.

## How to use this handbook

1. Learn the concept and explain it in your own words.
2. Read official documentation and record useful supplementary sources.
3. Complete a reproducible practical lab.
4. Record one or more failure modes and how you diagnose them.
5. Answer interview questions without looking at notes.
6. Update [PROGRESS.md](PROGRESS.md) only when evidence supports the status.

### Topic readiness states

Not started → Learning → Lab completed → Documented → Interview tested → Interview ready.

A topic is not interview-ready because a video or article was completed. You should be able to explain, demonstrate and troubleshoot it independently.

## Engineering standards

- Prefer official documentation for technical behaviour.
- Record versions, environment assumptions and access dates where relevant.
- Distinguish verified behaviour from assumptions and untested hypotheses.
- Never publish credentials, tokens, private keys, sensitive logs, personal data or Terraform state.
- Do not run destructive commands or provision paid cloud resources without cost and safety review.
- Do not claim a feature is implemented until it is tested.
- Link external resources and write original summaries; do not copy articles or private interview material.

## Agentic operations safety

Agents default to read-only investigation. Any operation that changes infrastructure, deploys software, modifies access, restarts workloads, deletes data, changes routing or incurs cost must be explicitly bounded, authorized, logged and protected by human approval. See [the safety model](10-agentic-devops/safety-model.md).

## Current status

The handbook is an evolving scaffold with curated resource, lab, case-study and interview indexes. A listed directory or external resource does not mean its subject is complete or mastered. The roadmap and progress tracker are the source of truth.

## License

MIT. See [LICENSE](LICENSE).
