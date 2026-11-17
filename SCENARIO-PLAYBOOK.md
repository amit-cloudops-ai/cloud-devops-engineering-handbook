# Production Troubleshooting & Scenario Interview Playbook

Use these scenarios to practise an evidence-led response. Do not jump directly to a restart. State the impact, ask for constraints, collect evidence, mitigate safely, verify and prevent recurrence.

## Universal incident response structure

1. **Scope:** What is broken, who is affected, when did it start, and what changed?
2. **Impact:** Availability, latency, errors, data integrity, security and business impact.
3. **Evidence:** Metrics, logs, traces, events, recent deployments, configuration and dependencies.
4. **Hypotheses:** List likely causes and rank them by evidence and blast radius.
5. **Mitigation:** Choose the smallest reversible action that restores service.
6. **Verification:** Confirm recovery from the user and system perspective.
7. **Prevention:** Tests, alerting, rollout controls, runbooks and ownership.

Never claim a specific root cause without evidence. Preserve logs and timelines during security or data-loss incidents.

## A. Linux and operating systems

1. CPU is at 100% after a deployment. Identify top processes, threads, system/user CPU, recent changes and saturation; decide whether rollback or traffic reduction is safer.
2. Load average is high but CPU utilization is low. Check uninterruptible I/O waits, storage latency, blocked processes and hypervisor contention.
3. A host reports disk full but df and du disagree. Check deleted-but-open files, mount points, inode usage and reserved blocks.
4. A service fails after reboot. Inspect systemd status, dependencies, environment files, permissions, mount readiness and journal logs.
5. Memory usage grows over hours. Separate cache from anonymous memory, inspect process RSS, OOM events and leak evidence.
6. SSH access suddenly fails. Verify network path, security controls, sshd state, keys, permissions, user shell and authentication logs.
7. A process cannot bind to its configured port. Check listener ownership, address binding, namespace and port conflicts.
8. A process is stuck in D state. Inspect storage/network filesystem and kernel I/O evidence; do not assume SIGKILL will resolve it.
9. Logs stopped appearing. Check application output, journald/syslog, disk pressure, log rotation and agent/collector health.
10. A scheduled backup did not run. Check scheduler, timezone, service account, environment, lock files, exit status and destination permissions.

## B. Networking and web

11. A website resolves to an unexpected IP. Check DNS resolver, authoritative records, TTL, split DNS, local cache and CDN.
12. A service is reachable by IP but not hostname. Inspect DNS records, search domains, resolver config, TLS SNI and application host routing.
13. Requests time out only from one subnet. Compare routes, NACLs, security groups, firewall, NAT and return path.
14. TCP connection is refused. Check listener state, bind address, port mapping, service health and local firewall.
15. TLS works in one client but fails in another. Compare certificate chain, hostname, SNI, protocol and trust store.
16. API latency spikes but server CPU remains low. Inspect dependency latency, DNS, connection pools, queueing, retries and network retransmits.
17. Intermittent 502/504 errors appear behind a load balancer. Check target health, backend timeout, connection draining, application saturation and proxy logs.
18. Only large requests fail. Investigate MTU, body-size limits, proxy buffers, timeouts and upstream limits.
19. A private host cannot reach an AWS service. Check route tables, NAT or VPC endpoint, endpoint policy, DNS and security rules.
20. A service is reachable inside a cluster but not externally. Trace ingress/gateway, service, endpoints, network policy, target health and DNS.

## C. AWS and cloud

21. An EC2 instance is running but SSH is unavailable. Check reachability, route, public IP, SG, NACL, OS firewall, sshd and key/user.
22. A private EC2 instance cannot download updates. Inspect NAT route, NAT health, egress controls, DNS and endpoint alternatives.
23. An application receives AccessDenied after deployment. Identify the principal, action, resource, session, policy layers and explicit denies before changing IAM.
24. An S3 upload fails for one workload. Check identity, bucket policy, KMS key policy, endpoint policy, encryption headers and object ownership.
25. An ALB target is unhealthy. Verify health path/port, security group references, app binding, response code and startup time.
26. AWS costs increase overnight. Use Cost Explorer/CUR by service, region, usage type and tag; check NAT, data transfer, logs, snapshots and idle compute.
27. An RDS database is slow. Check connections, CPU, memory, IOPS, locks, query plans, storage and recent changes before scaling.
28. A VPC peering connection is active but traffic fails. Check CIDR overlap, both route tables, security controls and DNS resolution options.
29. A deployment role can read but cannot update a resource. Inspect assumed role, session context, permissions boundary, SCP and resource policy.
30. A region outage is suspected. Validate provider status and multi-AZ/region dependencies; follow tested failover runbook, not an improvised migration.

## D. Docker and containers

31. A container exits immediately. Inspect exit code, logs, entrypoint, command, config and dependencies.
32. A container works locally but not in Compose. Check service DNS, exposed vs published ports, network membership, env vars and health dependencies.
33. Container memory grows until it is killed. Inspect cgroup limits, process memory, OOM events, leak and workload pattern.
34. A Docker build is unexpectedly slow. Inspect context size, layer ordering, cache invalidation, package downloads and multi-stage build.
35. A container cannot write to a mounted volume. Check UID/GID, mount mode, ownership, SELinux/AppArmor and filesystem permissions.
36. An image works on a developer laptop but fails in production. Compare architecture, base image, libc, runtime, environment and immutable digest.
37. A secret is found in an image layer. Stop distribution, revoke/rotate the secret, rebuild cleanly, inspect registry consumers and add scanning.
38. A registry pull fails. Check authentication, image name/tag/digest, network, rate limits, certificate trust and architecture.

## E. Kubernetes

39. A Pod is Pending. Inspect describe/events, scheduler constraints, resource requests, taints, PVCs, quotas and node capacity.
40. A Pod is CrashLoopBackOff. Inspect previous logs, exit code, probes, config, secrets, dependencies and OOM status.
41. A Pod is ImagePullBackOff. Verify image reference, tag/digest, registry credentials, pull secret, network and architecture.
42. A Service has no endpoints. Compare selectors and labels, Pod readiness, namespace and EndpointSlices.
43. Pods cannot resolve service names. Check CoreDNS Pods, logs, DNS config, network policies and cluster domain.
44. A rollout is stuck. Inspect rollout status, ReplicaSets, events, readiness, image and deployment strategy; decide rollback criteria.
45. A node is NotReady. Inspect node conditions, kubelet, container runtime, disk/memory pressure, CNI and control-plane reachability.
46. HPA does not scale. Check metrics API, resource requests, target metric, workload behavior and max replicas.
47. A workload is OOMKilled. Compare memory limit, working set, peak usage, request and application leak; avoid blind limit increases.
48. A persistent volume is stuck Pending. Inspect StorageClass, CSI controller, topology, access mode, capacity and events.
49. A network policy blocks traffic. Map source/destination namespace, labels, ports, policy selectors and CNI enforcement.
50. A cluster upgrade is planned. Check version skew, deprecated APIs, add-on compatibility, PDBs, backups, node pools and rollback limitations.

## F. CI/CD, GitOps and Terraform

51. CI passes but deployment fails. Separate artifact correctness from runtime configuration, identity, networking and environment drift.
52. A pipeline is suddenly failing after a dependency update. Pinpoint changed dependency/action, inspect lock files and reproduce in a controlled branch.
53. GitHub Actions cannot assume an AWS role. Inspect OIDC provider, audience, subject condition, role trust policy and permissions.
54. A deployment partially updates production. Stop further rollout, assess mixed versions, choose rollback or forward-fix and validate data compatibility.
55. Argo CD reports OutOfSync continuously. Inspect desired vs live diff, mutating admission, ignored fields, manual edits and reconciliation loops.
56. Terraform plan wants to replace a critical resource. Read replacement reason, immutable attributes, state and provider changes; do not apply until reviewed.
57. Terraform apply fails halfway. Refresh state, inspect actual cloud resources and state lock, then produce a new plan; never delete state as a shortcut.
58. Terraform state is exposed. Restrict access, rotate any exposed credentials, assess state contents, migrate/secure backend and audit access.
59. Infrastructure drift is detected. Identify who/what changed it, compare intended state and decide import, revert or codify after review.
60. A module upgrade changes many resources. Pin versions, inspect changelog and plan, test in non-production and promote through review.

## G. Observability, SRE and incidents

61. Error rate rises but no alert fires. Inspect metric coverage, labels, thresholds, alert evaluation and telemetry pipeline.
62. Latency increases while error rate remains low. Inspect percentile latency, saturation, queues and dependencies; average latency can hide tail issues.
63. Alert volume overwhelms responders. Group symptoms, tune thresholds, add burn-rate alerts, ownership and actionable runbooks.
64. A metrics dashboard suddenly shows gaps. Check scrape targets, exporter, service discovery, cardinality, retention and storage.
65. A service violates its SLO. Calculate error budget burn, assess user impact and decide whether to slow releases or prioritize reliability.
66. A retry storm overloads a dependency. Inspect retry policy, concurrency, timeouts, queue depth and circuit breaker; reduce amplification.
67. A database connection pool is exhausted. Inspect pool limits, leaks, query duration, traffic and database capacity.
68. A region or AZ failure is declared. Follow tested failover, verify data consistency, capacity, DNS and dependencies.
69. A security incident is suspected. Preserve evidence, contain identity/network access, follow incident command and legal/security escalation.
70. An incident is resolved but repeats. Write a timeline, causal analysis, contributing conditions, detection gaps and owned corrective actions.

## H. AI infrastructure and MLOps

71. Model inference latency increases sharply. Split queueing, prefill, decode, token count, batch size, GPU utilization and downstream latency.
72. GPU utilization is low but requests are slow. Inspect CPU preprocessing, tokenization, network, batching, memory bandwidth and queueing.
73. Model server runs out of VRAM. Check model size, precision, KV cache, context length, batch/concurrency and GPU sharing.
74. Model deployment works on one node but fails on another. Compare driver, CUDA/runtime compatibility, architecture, image digest and model artifact.
75. Token cost increases unexpectedly. Attribute by model, tenant, prompt, output tokens, retries, context size and routing.
76. RAG answers are irrelevant. Inspect source quality, chunking, embeddings, metadata filters, retrieval recall, reranking and prompt construction.
77. RAG answer cites wrong sources. Check retrieval IDs, chunk provenance, citation mapping, stale indexes and evaluation set.
78. Model quality regresses after a release. Compare model/version, prompt, data, retrieval, quantization and golden-set results; roll back if thresholds fail.
79. Inference queue grows under burst traffic. Inspect concurrency, batching, autoscaling signals, cold starts, queue limits and admission control.
80. A model endpoint leaks sensitive data. Contain exposure, review logs/prompts, access policy, retention and model/provider configuration; rotate exposed credentials.

## I. Agentic AI and AIOps

81. An agent proposes a destructive command. Tool policy should reject it; explain allowlists, dry-run, approval and audit boundaries.
82. An agent repeats the same action. Check idempotency keys, workflow state, retry semantics and external side effects.
83. Agent output contains instructions from a log file. Treat logs as untrusted data; isolate data from system instructions and validate tool arguments.
84. An MCP server exposes too many tools. Minimize tool surface, scope permissions and expose read-only capabilities by default.
85. Agent recommendations are plausible but wrong. Inspect retrieval, tool evidence, model version, prompt, confidence and evaluation failures.
86. A multi-agent workflow deadlocks. Inspect shared state, ownership, dependency graph, timeouts, termination and coordination protocol.
87. An agent cannot access Kubernetes. Verify workload identity, RBAC, namespace scope, token audience and audit logs; never grant cluster-admin by default.
88. Agent evaluation passes but production failures increase. Check distribution shift, live tool errors, new cluster states, evaluation coverage and feedback loops.
89. An agent wants to run Terraform apply. Require plan inspection, impact estimate, authorized scope, explicit human approval and post-apply verification.
90. A provider API is rate-limiting agent requests. Add bounded concurrency, exponential backoff with jitter, caching, quotas and graceful degradation.

## J. Design and leadership scenarios

91. Design a multi-account AWS landing zone for several teams.
92. Design a secure CI/CD platform deploying to Kubernetes across dev, staging and production.
93. Design centralized observability for 50 microservices.
94. Design a resilient event-driven service using SQS and a relational database.
95. Design a platform that safely hosts internal AI agents with tenant isolation and approvals.
96. Design GPU inference serving for bursty workloads with latency and cost objectives.
97. Explain how you would migrate a VM-based application to containers without a risky big-bang cutover.
98. A team wants admin access to move faster. How do you deliver a safe least-privilege alternative?
99. You disagree with an engineer's proposed production fix. How do you use evidence and communicate risk?
100. A release deadline conflicts with unresolved security findings. How do you communicate and decide?

## Answer scoring rubric

Score each scenario 0–4:

- **0:** guesses or jumps to destructive action.
- **1:** identifies a plausible cause but lacks a diagnostic plan.
- **2:** structured evidence gathering and reasonable mitigation.
- **3:** includes verification, rollback, security and communication.
- **4:** anticipates failure modes, blast radius, prevention and trade-offs.

Record scenario scores and weak areas in [INTERVIEW-TRACKER.md](INTERVIEW-TRACKER.md).