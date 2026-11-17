# Cloud & DevOps Engineering Handbook

A practical, evidence-driven handbook for **Cloud Engineering, DevOps, Platform Engineering, Site Reliability Engineering (SRE), AI Infrastructure, MLOps and Agentic AI Operations**.

**Primary positioning:** Cloud / DevOps Engineer with an AI infrastructure and agentic operations specialization.  
**Primary job market:** Pune, India · **Secondary:** Bengaluru, India.

This is a public learning system and engineering portfolio. It turns preparation into demonstrable capability through original notes, practical labs, troubleshooting records, architecture decisions, projects and interview practice.

## Start here

<details>
<summary><strong>Preparation dashboard</strong> — track competency progress</summary>

Open the [interactive progress dashboard](dashboard/index.html). It tracks skill readiness by evidence, supports browser-local edits and exports a JSON snapshot. Browser edits do not automatically sync to GitHub; update dashboard/progress.json to persist a new baseline.
</details>

| Start point | What it contains |
|---|---|
| [Skill & Tool Matrix](SKILL-MATRIX.md) | Full role-based inventory across Cloud, DevOps, SRE, Platform, AI infrastructure and agentic engineering |
| [Interview Question Bank](INTERVIEW-QUESTION-BANK.md) | 210 original practice questions across 13 engineering domains |
| [Scenario Playbook](SCENARIO-PLAYBOOK.md) | 100 production troubleshooting, design and incident scenarios |
| [AI Infrastructure Curriculum](AI-INFRASTRUCTURE.md) | GPU, inference, RAG, MLOps, LLM platforms, MCP, agents and AIOps |
| [Roadmap](ROADMAP.md) | Accelerated, competency-based progression—not a one-week-per-topic schedule |
| [Progress Tracker](PROGRESS.md) | Evidence-backed written progress log |
| [Interview Tracker](INTERVIEW-TRACKER.md) | Company, topic and mock-interview tracking |
| [Resource Index](RESOURCE-INDEX.md) | External interview repositories, labs and engineering references |

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
| [Templates](templates/README.md) | Consistent formats for topics, labs and interviews |

## Target role families

- DevOps Engineer
- Cloud Engineer / Cloud Operations Engineer
- Platform Engineer
- Site Reliability Engineer (SRE)
- Cloud Support / Infrastructure Support / Build & Release
- AI Infrastructure Engineer / LLM Platform Engineer
- MLOps Engineer
- Agentic AI / AIOps Engineer

Agentic AI is a specialization layered on top of sound infrastructure fundamentals. The goal is to demonstrate safe, useful AI-assisted operations—not to claim expertise in every framework.

## How to use this handbook

1. Pick one P0 skill from the skill matrix.
2. Learn the mechanism from official documentation and explain it in your own words.
3. Complete a reproducible practical lab.
4. Break a safe test environment and diagnose the failure.
5. Answer related questions without looking at notes.
6. Update progress only when evidence supports the status.

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

The handbook now includes a role-based skill inventory, original question and scenario banks, an AI infrastructure curriculum and an interactive progress dashboard. The learning material is a curriculum, not proof of mastery. Use the progress tracker and project evidence as the source of truth.

## License

MIT. See [LICENSE](LICENSE).
