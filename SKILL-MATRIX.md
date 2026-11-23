# Role-Based Skill & Tool Matrix

This is the competency inventory for the roles targeted by this handbook. It is deliberately broad, but priority labels prevent tool collecting from replacing depth.

**Priority:** P0 = common screening/core delivery skill; P1 = important role differentiator; P2 = specialization or role-dependent.  
**Readiness:** Awareness → Explain → Implement → Troubleshoot → Design / operate independently.

## Role families and expected emphasis

| Role | Core emphasis | Differentiators |
|---|---|---|
| DevOps Engineer | Linux, networking, Git, scripting, Docker, CI/CD, cloud, IaC | Kubernetes, security automation, release engineering |
| Cloud Engineer | Cloud networking, IAM, compute, storage, DNS, monitoring, backup, cost | Landing zones, hybrid connectivity, governance |
| Platform Engineer | Kubernetes, IaC, developer experience, internal platforms, automation | Backstage, Crossplane, policy-as-code, platform APIs |
| SRE | Linux, networking, observability, SLOs, incidents, capacity, automation | Distributed systems, chaos engineering, error budgets |
| Cloud / DevOps Support | OS, networking, cloud service operations, logs, tickets, runbooks | Incident communication, ITSM, scripting |
| AI Infrastructure Engineer | Linux, GPUs, containers, Kubernetes, networking, storage, observability | Model serving, inference optimization, GPU scheduling |
| AI Platform / MLOps Engineer | Python, ML lifecycle, model registry, pipelines, feature/data systems | MLflow, Kubeflow, KServe, model monitoring |
| Agentic AI / AIOps Engineer | APIs, agents, tool contracts, workflow orchestration, evaluation | MCP, LangGraph, safety, auditability, human approval |

## 0. Software delivery lifecycle — P0

### SDLC and delivery fundamentals
- [ ] Explain the seven commonly described SDLC stages, their outputs and operational implications
- [ ] Distinguish functional and non-functional requirements; explain HLD vs LLD
- [ ] Compare Waterfall, V-Model, Agile, Iterative, Incremental, Spiral, RAD and Prototype models
- [ ] Distinguish Agile from Scrum/Kanban; iterative from incremental; verification from validation
- [ ] Map DevOps, CI/CD and DevSecOps practices across the lifecycle
- [ ] Trace a code change through build, test, artifact promotion, deployment, health checks and rollback

**Study notes:** [SDLC foundations](00-foundations/SDLC.md) · **Interview drill:** [SDLC question bank](12-interview-preparation/sdlc-interview-questions.md)

## 1. Core systems and programming — P0

### Linux and operating systems
- [ ] Filesystem hierarchy, mounts, inodes, symlinks, permissions, ownership, ACLs, umask
- [ ] Users, groups, sudo, PAM basics, SSH keys and hardening
- [ ] Processes, threads, signals, jobs, priorities, systemd, services and timers
- [ ] CPU load, memory, swap, OOM killer, disk I/O, filesystem capacity
- [ ] Logs: journald, syslog, log rotation, application logs
- [ ] Package managers, repositories, kernel basics, boot sequence
- [ ] Shell environment, pipes, redirection, grep, awk, sed, find, xargs, jq
- [ ] Troubleshooting with ps, top/htop, free, vmstat, iostat, df, du, lsof, ss, journalctl, dmesg, strace
- [ ] Linux networking: interfaces, routes, firewall, DNS resolver
- [ ] Backup, restore, cron, systemd timers, process supervision

**Study material (covered so far):** [Linux foundations chapter](00-foundations/LINUX-FOUNDATIONS.md) · [daily command drills](00-foundations/LINUX-DAILY-COMMAND-PRACTICE.md) · [interview questions and scenarios](12-interview-preparation/linux-foundations-interview-questions.md). This is a partial learning record, not a completed competency checklist.

**Tools:** Ubuntu/RHEL, WSL, SSH, tmux, systemd, journalctl, coreutils, procps, iproute2, lsof, strace.

### Networking
- [ ] OSI and TCP/IP models; encapsulation and MTU
- [ ] IPv4/IPv6, CIDR, subnetting, private/public ranges, route tables
- [ ] ARP, ICMP, TCP handshake/teardown, UDP, ports, ephemeral ports
- [ ] DNS records, recursive resolution, TTL, caching, split-horizon DNS
- [ ] HTTP methods, status codes, headers, cookies, keep-alive, HTTP/2 and HTTP/3 concepts
- [ ] TLS handshake, certificates, CA chain, SNI, mTLS
- [ ] NAT, SNAT/DNAT, proxies, reverse proxies, load balancers
- [ ] Firewalls, security groups, NACLs, stateful/stateless filtering
- [ ] VPN, peering, transit routing, private endpoints, CDN
- [ ] Packet-path troubleshooting, latency, packet loss, retransmission

**Tools:** ip, ss, dig, nslookup, curl, wget, ping, traceroute, mtr, tcpdump, Wireshark, nc, openssl s_client.

### Programming and automation
- [ ] Bash: quoting, exit codes, traps, functions, arrays, strict mode, idempotence
- [ ] Python: data structures, exceptions, modules, virtual environments, typing, logging
- [ ] Files, JSON/YAML, CSV, HTTP APIs, pagination, retries, timeouts
- [ ] Process execution safely, subprocess, environment variables
- [ ] Unit tests, mocks, fixtures, linting, formatting and dependency pinning
- [ ] API design basics, REST, authentication, status codes, schema validation
- [ ] Concurrency basics, async I/O and thread/process distinctions

**Tools:** Bash, Python 3, pytest, requests/httpx, jq, yq, Make, pre-commit.

### Git and collaboration
- [ ] Working tree, index, commits, branches, tags, remotes, refs
- [ ] Merge vs rebase, cherry-pick, revert, reset, reflog
- [ ] Conflict resolution, interactive rebase, bisect
- [ ] PR reviews, branch protection, CODEOWNERS, conventional commit practices
- [ ] GitHub Actions, issues, releases, artifacts and permissions

**Tools:** Git CLI, GitHub, gh CLI.

## 2. Cloud engineering — AWS-first P0, other clouds P2

### AWS identity, governance and security
- [ ] IAM users, roles, policies, trust policies, permission boundaries, session policies
- [ ] STS, AssumeRole, temporary credentials, federation and OIDC
- [ ] Resource policies, identity policies, explicit deny and policy evaluation
- [ ] Organizations, SCPs, account boundaries, Control Tower concepts
- [ ] KMS, envelope encryption, key policies, rotation
- [ ] Secrets Manager, SSM Parameter Store, certificate management
- [ ] CloudTrail, Config, GuardDuty, Security Hub, Inspector, WAF and Shield concepts
- [ ] Least privilege, access reviews, break-glass and audit evidence

### AWS networking
- [ ] VPC, CIDR, public/private subnets, route tables
- [ ] Internet Gateway, NAT Gateway, egress-only gateway
- [ ] Security Groups vs Network ACLs
- [ ] VPC endpoints: gateway and interface; PrivateLink
- [ ] VPC peering, Transit Gateway, VPN, Direct Connect concepts
- [ ] Route 53 public/private hosted zones, health checks, routing policies
- [ ] ALB, NLB, GWLB, target groups, health checks
- [ ] CloudFront, origins, caching, TLS and WAF integration

### Compute, storage and data
- [ ] EC2 types, AMIs, user data, metadata, placement, EBS and snapshots
- [ ] Auto Scaling Groups, launch templates, scaling policies
- [ ] S3 storage classes, versioning, lifecycle, replication, encryption, bucket policies
- [ ] EFS and FSx concepts; backup and restore
- [ ] RDS, Multi-AZ, read replicas, backups, parameter groups
- [ ] DynamoDB partition keys, indexes, capacity modes, TTL, streams
- [ ] SQS, SNS, EventBridge, Kinesis concepts and delivery semantics
- [ ] Lambda, API Gateway, Step Functions and event-driven design

### Operations and governance
- [ ] CloudWatch metrics, logs, alarms, dashboards, Logs Insights
- [ ] CloudTrail event history and audit trails
- [ ] AWS Backup, restore testing, RTO/RPO
- [ ] Budgets, Cost Explorer, CUR, tagging, Savings Plans and Reserved Instances
- [ ] Well-Architected pillars and trade-offs
- [ ] Multi-account strategy, regions, availability zones and quotas

**AWS tools:** AWS CLI, Console, IAM Access Analyzer, CloudFormation, Systems Manager, CloudWatch, CloudTrail, Config, Cost Explorer, Budgets.

**Azure mapping (P2):** Entra ID, subscriptions, VNets, NSGs, VMs, Blob Storage, AKS, Azure Monitor, Key Vault, Bicep.  
**GCP mapping (P2):** IAM, projects, VPC, Compute Engine, Cloud Storage, GKE, Cloud Logging/Monitoring, Secret Manager, Cloud Build.

## 3. Containers, orchestration and delivery — P0/P1

### Docker
- [ ] Images, layers, registries, tags, digests and content trust concepts
- [ ] Dockerfile, build context, cache, multi-stage builds, non-root user
- [ ] Volumes, bind mounts, networks, DNS, port publishing
- [ ] Compose services, health checks, depends_on semantics and profiles
- [ ] Resource limits, logs, inspect, exec, events and pruning
- [ ] Image scanning, SBOM, signing, minimal base images and secrets at build time

**Tools:** Docker Engine, Docker CLI, Compose, BuildKit, ECR, GHCR, Trivy, Syft, Cosign.

### Kubernetes
- [ ] Control plane, API server, etcd, scheduler, controller manager, kubelet, kube-proxy
- [ ] Pods, Deployments, ReplicaSets, StatefulSets, DaemonSets, Jobs, CronJobs
- [ ] Services, EndpointSlices, Ingress, Gateway API, DNS and network policies
- [ ] ConfigMaps, Secrets, service accounts, RBAC and admission controls
- [ ] Requests, limits, QoS, HPA, VPA concepts, PDB and scheduling constraints
- [ ] Liveness, readiness, startup probes; rollout, rollback and disruption
- [ ] PersistentVolumes, PVCs, StorageClasses, CSI
- [ ] Namespaces, quotas, LimitRanges, affinity, taints and tolerations
- [ ] CNI, CoreDNS, kube-proxy/eBPF concepts, cluster networking
- [ ] Troubleshooting Pending, CrashLoopBackOff, OOMKilled, ImagePullBackOff, DNS and service routing

**Tools:** kubectl, kind, minikube, k3d, Helm, Kustomize, k9s, stern, kubectx/kubens, Cilium concepts.

### CI/CD and GitOps
- [ ] Pipeline stages, runners, artifacts, caches, environments and approvals
- [ ] Build/test/package/scan/sign/publish/deploy/verify/rollback
- [ ] Secrets, OIDC federation, scoped tokens, runner isolation
- [ ] Reproducible builds, immutable artifacts, provenance and SBOM
- [ ] Deployment strategies: rolling, blue-green, canary, feature flags
- [ ] GitOps reconciliation, drift, promotion and rollback
- [ ] Pipeline security, dependency pinning and supply-chain controls

**Tools:** GitHub Actions, Jenkins, GitLab CI, Argo CD, Flux, ECR/GHCR, Renovate, Dependabot.

### Infrastructure as Code
- [ ] Terraform providers, resources, data sources, variables, outputs, locals
- [ ] State, remote backends, locking, import, moved blocks, state recovery
- [ ] Modules, version constraints, provider locks and environment separation
- [ ] Plan/apply/destroy lifecycle, drift, dependency graph and lifecycle meta-arguments
- [ ] Secrets and sensitive values; state encryption and access controls
- [ ] Policy-as-code, validation and CI plan review
- [ ] Configuration management and immutable infrastructure concepts

**Tools:** Terraform, OpenTofu, tflint, tfsec/Trivy, Checkov, Terratest, Ansible, Packer.

## 4. Reliability, observability, security and FinOps — P1

### Observability and SRE
- [ ] Metrics, logs, traces, events and correlation IDs
- [ ] RED and USE methods; cardinality and sampling
- [ ] Prometheus, PromQL, exporters, Alertmanager
- [ ] Grafana dashboards, alert routing and runbooks
- [ ] OpenTelemetry SDK, Collector, OTLP and context propagation
- [ ] SLIs, SLOs, error budgets, burn-rate alerts and availability math
- [ ] Incident command, severity, communication, timeline and postmortem
- [ ] Capacity planning, load testing, saturation and graceful degradation
- [ ] Backups, restore drills, RTO, RPO, HA and disaster recovery
- [ ] Chaos engineering and resilience testing

**Tools:** Prometheus, Grafana, Loki, Tempo, Jaeger, OpenTelemetry, ELK/OpenSearch, Datadog/New Relic concepts, k6, Locust.

### Security / DevSecOps
- [ ] Threat modeling, attack surface and trust boundaries
- [ ] IAM least privilege, RBAC, network segmentation and workload identity
- [ ] Secret management, rotation and secret scanning
- [ ] SAST, DAST, SCA, container/IaC scanning
- [ ] SBOM, signing, provenance and dependency pinning
- [ ] Kubernetes security contexts, Pod Security Standards and admission policy
- [ ] Encryption in transit/at rest, key management, audit logging
- [ ] Vulnerability triage, patching, incident response and evidence retention

**Tools:** Trivy, Semgrep, Gitleaks, Checkov, OPA/Conftest, Kyverno, Falco, Cosign, Syft, Vault.

### FinOps
- [ ] Cost allocation, tags/labels, budgets, forecasts and anomaly detection
- [ ] Compute, storage, network egress, logs and idle resource cost drivers
- [ ] Rightsizing, autoscaling, spot/preemptible trade-offs
- [ ] Unit economics, cost per request, cost per workload and showback
- [ ] GPU utilization, model token cost and inference cost per request

## 5. AI, MLOps and AI infrastructure — P1 specialization

See [AI Infrastructure Engineering](AI-INFRASTRUCTURE.md) for the detailed curriculum.

- [ ] Python for services, data pipelines, async APIs and packaging
- [ ] ML lifecycle: datasets, training, validation, model registry and deployment
- [ ] LLM basics: tokens, context windows, embeddings, attention, quantization
- [ ] Inference: batching, streaming, KV cache, concurrency, latency and throughput
- [ ] GPU fundamentals: VRAM, CUDA concepts, drivers, utilization and scheduling
- [ ] Model serving: vLLM, Hugging Face TGI, Triton, Ollama (compare use cases)
- [ ] RAG: ingestion, chunking, embeddings, retrieval, reranking and citations
- [ ] Vector databases: pgvector, Qdrant, Milvus, Weaviate concepts
- [ ] AI gateways, model routing, rate limits, caching, quotas and provider failover
- [ ] MLOps: MLflow, Kubeflow, KServe, feature/data versioning and model monitoring
- [ ] LLM evaluation, prompt/version tests, quality, latency and cost metrics
- [ ] AI security: prompt injection, data leakage, model supply chain and tool abuse

## 6. Agentic AI and autonomous operations — P1 specialization

- [ ] Agent loop, state, planning, tool selection and termination
- [ ] Tool contracts, JSON schema, validation, timeouts, retries and idempotency
- [ ] MCP architecture: host, client, server, tools, resources and prompts
- [ ] Workflow orchestration vs autonomous agents; deterministic boundaries
- [ ] LangGraph concepts: state graph, nodes, edges, checkpoints and human interrupts
- [ ] Multi-agent patterns, delegation, shared state and coordination failure
- [ ] Memory, retrieval, context management and data retention
- [ ] Agent tracing, evaluations, regression sets and adversarial tests
- [ ] Guardrails: read-only defaults, allowlists, approvals, budgets and kill switches
- [ ] Audit logs, provenance, identity, tenant isolation and secret boundaries
- [ ] AIOps: alert triage, log summarization, incident correlation and remediation proposals
- [ ] Safe remediation: dry run, blast-radius estimate, approval, execution and verification

**Tools to understand:** MCP, LangGraph, LangChain, LlamaIndex, OpenAI-compatible APIs, Ollama, LiteLLM, MLflow, Langfuse, Arize Phoenix, OpenTelemetry. Learn concepts before collecting frameworks.

## 7. System design and engineering breadth — P1/P2

- [ ] Load balancing, caching, CDN, database scaling and queue-based decoupling
- [ ] Consistency, replication, partitioning, CAP trade-offs and failure domains
- [ ] Retries, timeouts, backoff, jitter, circuit breakers and bulkheads
- [ ] Idempotency, deduplication, ordering and at-least-once delivery
- [ ] API gateways, service discovery, authentication and authorization
- [ ] Relational vs NoSQL data modeling, indexes, transactions and connection pools
- [ ] High availability, multi-AZ/region, backup, restore and disaster recovery
- [ ] Secure-by-default architecture, observability and cost estimation

## 8. Evidence standard

For every P0/P1 skill, keep one of each:
1. A concise explanation in your own words.
2. A reproducible lab or project link.
3. One failure mode with diagnosis and fix.
4. At least five interview questions answered unaided.
5. A readiness state backed by evidence in [PROGRESS.md](PROGRESS.md).

A tool is not a skill. Do not mark Kubernetes ready because kubectl is installed, or AI infrastructure ready because an LLM API returned text.
