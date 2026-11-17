# Cloud, DevOps, SRE & AI Infrastructure Interview Question Bank

A curated original practice bank organized by role and depth. It is not a promise that these exact questions will appear in an interview. Pair each answer with a command, diagram, lab or project where possible.

**Practice rule:** answer aloud first. For every answer, prepare a definition, mechanism, practical example, failure mode and trade-off. Use the linked external repositories for further question volume; do not copy their answer banks into this repository.

## A. Linux and operating systems

1. Explain the Linux boot process from firmware to userspace.
2. What happens when a process is created with fork and exec?
3. What is the difference between a process and a thread?
4. How do Linux permissions, ownership, ACLs and umask interact?
5. What are hard links and symbolic links? When can each fail?
6. How do you identify which process is consuming CPU, memory or disk I/O?
7. What does load average represent, and why can it be high when CPU utilization is low?
8. Explain virtual memory, page cache, swap and the OOM killer.
9. How would you investigate a server with 100% disk usage?
10. How do systemd units, dependencies, targets and timers work?
11. How do you inspect logs for a service that failed during startup?
12. What is the difference between SIGTERM and SIGKILL?
13. How would you identify which process is listening on a port?
14. Explain file descriptors and how descriptor exhaustion affects a service.
15. How would you debug a process that is stuck in uninterruptible sleep?
16. What is inode exhaustion and how is it different from disk-space exhaustion?
17. How do SSH keys work, and how would you troubleshoot public-key authentication?
18. How do cron and systemd timers differ?
19. What is the purpose of /proc and /sys?
20. Describe a safe approach to patching and rebooting a Linux production host.

## B. Networking and web fundamentals

21. Walk through what happens after entering a URL in a browser.
22. Explain DNS recursive resolution and the role of authoritative nameservers.
23. Compare A, AAAA, CNAME, MX, TXT and NS records.
24. Explain TCP's three-way handshake and connection teardown.
25. When would you choose UDP over TCP?
26. What is a subnet mask, and how do you calculate usable addresses?
27. What happens when a host has an incorrect default gateway?
28. Explain ARP and how it differs from DNS.
29. Compare NAT, reverse proxy and load balancer.
30. What is the difference between HTTP 401, 403, 404, 429 and 5xx responses?
31. Explain TLS certificate validation and the certificate chain.
32. How do SNI and mTLS work?
33. What causes connection timeout, connection refused and DNS failure?
34. How do MTU and fragmentation affect connectivity?
35. How would you debug intermittent packet loss between two subnets?
36. Explain stateful vs stateless firewall rules.
37. What is the difference between an ALB and an NLB?
38. How do CDN caching, cache-control and invalidation work?
39. How would you use curl, dig, ss, traceroute and tcpdump in an incident?
40. Explain HTTP keep-alive, connection pooling and ephemeral port exhaustion.

## C. Git, Bash, Python and automation

41. Explain the Git working tree, staging area and commit history.
42. Compare merge, rebase, cherry-pick, revert and reset.
43. How do you recover a commit that appears to have been deleted?
44. How do you resolve a merge conflict safely?
45. What is the difference between a GitHub Actions artifact and cache?
46. How should a Bash script handle errors, signals and cleanup?
47. What are quoting and word-splitting hazards in shell scripts?
48. Explain exit codes, pipes and pipefail.
49. How would you write an idempotent backup or health-check script?
50. How do you manage Python dependencies and virtual environments?
51. How would you build a Python script that calls an API with pagination, retries and timeouts?
52. Explain exception handling, structured logging and unit testing in Python.
53. How do you avoid shell injection when executing subprocesses?
54. When would you use async I/O, threads or processes?
55. How would you test an automation script without touching production?

## D. AWS and cloud engineering

56. Explain IAM identity policies, resource policies and trust policies.
57. How does AWS evaluate an explicit deny, permission boundary and SCP?
58. Why are IAM roles and temporary credentials preferred over long-lived access keys?
59. Walk through a request from a private EC2 instance to the public internet.
60. Compare Internet Gateway, NAT Gateway and VPC endpoints.
61. Compare Security Groups and Network ACLs.
62. How do VPC peering and Transit Gateway differ?
63. What happens when two VPCs have overlapping CIDR ranges?
64. Explain EC2 user data, instance metadata and IMDSv2.
65. How do EBS volumes and snapshots work? What are their recovery limits?
66. Explain S3 versioning, lifecycle rules, replication and bucket policies.
67. Compare RDS Multi-AZ and read replicas.
68. How would you design a highly available web application on AWS?
69. Explain ALB health checks, target groups and deregistration delay.
70. How would you troubleshoot an EC2 instance that is reachable by SSH but not through its application port?
71. How do Route 53 routing policies and health checks work?
72. Explain CloudWatch metrics, logs, alarms and CloudTrail.
73. How would you investigate an unexpected AWS bill?
74. How do SQS visibility timeout, dead-letter queues and retries work?
75. When would you choose Lambda, ECS, EKS or EC2?
76. How would you design backup, restore and disaster recovery for an AWS workload?
77. What is the shared responsibility model?
78. How do KMS key policies differ from IAM policies?
79. How would you organize multiple AWS accounts and environments?
80. What are the main cost drivers for NAT Gateway, data transfer, EKS and CloudWatch?

## E. Docker and container engineering

81. Explain Docker image layers and copy-on-write.
82. What is the difference between an image, container, volume and bind mount?
83. How does Docker bridge networking and service-name DNS work?
84. Explain multi-stage builds and why they reduce image size.
85. Why should containers run as non-root?
86. How do ENTRYPOINT and CMD differ?
87. How do you troubleshoot a container that exits immediately?
88. How do you diagnose a container that is healthy locally but unreachable from another container?
89. How do resource limits and OOM kills work?
90. How do you handle secrets during image build and runtime?
91. What is the difference between a mutable image tag and immutable digest?
92. How would you scan, sign and promote an image through environments?

## F. Kubernetes and orchestration

93. Explain the Kubernetes control plane components and their responsibilities.
94. What happens after kubectl apply is executed?
95. Compare Pod, Deployment, StatefulSet, DaemonSet, Job and CronJob.
96. How do ClusterIP, NodePort and LoadBalancer Services work?
97. Explain Ingress and Gateway API at a high level.
98. What is the difference between readiness, liveness and startup probes?
99. How do requests, limits and QoS classes affect scheduling and eviction?
100. What causes CrashLoopBackOff and how do you investigate it?
101. What causes ImagePullBackOff and how do you fix it?
102. Why does a Pod remain Pending?
103. How do ConfigMaps, Secrets and service accounts differ?
104. Explain Kubernetes RBAC and least privilege.
105. How does CoreDNS resolve a service name?
106. How do you debug a Service with no endpoints?
107. Explain PV, PVC, StorageClass and CSI.
108. How do HPA, PDB, taints, tolerations and affinity work?
109. What is a rolling update and how do you roll back?
110. How would you secure a Kubernetes cluster and its workloads?
111. How would you troubleshoot a node in NotReady state?
112. What are CNI and CSI plugins responsible for?

## G. CI/CD, GitOps and release engineering

113. Design a CI/CD pipeline from pull request to production.
114. How should tests, linting, SAST, dependency scans and image scans be ordered?
115. How do you store and expose secrets to a pipeline securely?
116. Explain OIDC federation from GitHub Actions to AWS.
117. How do you promote the same immutable artifact across environments?
118. Compare rolling, blue-green and canary deployments.
119. How would you implement rollback when a deployment passes CI but fails health checks?
120. What is GitOps reconciliation, and how does Argo CD detect drift?
121. How do you secure self-hosted runners?
122. How do you diagnose a pipeline that passes locally but fails in CI?
123. How do you prevent dependency and action supply-chain compromise?
124. What is the difference between a pipeline cache and a release artifact?

## H. Terraform and infrastructure as code

125. Explain Terraform's init, validate, plan, apply and destroy lifecycle.
126. What is Terraform state and why must it be protected?
127. How do remote state and state locking work?
128. What happens when state is lost or corrupted?
129. How do you structure reusable Terraform modules?
130. How do provider and module version constraints work?
131. What is drift and how do you detect it?
132. Compare count and for_each.
133. How do depends_on and implicit dependencies differ?
134. How do you import an existing resource into Terraform management?
135. How do you handle secrets and sensitive values in Terraform?
136. How would you review a plan that proposes replacing a critical resource?
137. How do you test Terraform modules and enforce policy?
138. What is the purpose of a provider lock file?

## I. Observability, SRE and incident response

139. Explain metrics, logs, traces and events and when each is useful.
140. What are the RED and USE methods?
141. Explain SLI, SLO, SLA and error budget.
142. How do you choose alert thresholds and reduce alert fatigue?
143. What is Prometheus scraping and how does PromQL work?
144. How do you design a useful Grafana dashboard for an API?
145. Explain OpenTelemetry instrumentation and context propagation.
146. How do you investigate high latency when CPU and memory look normal?
147. What is a blameless postmortem and what should it contain?
148. How do retries amplify an outage?
149. Explain circuit breakers, bulkheads, backoff and jitter.
150. How do you plan capacity and load testing?
151. Explain RTO, RPO, HA and disaster recovery.
152. How do you prioritize incidents and communicate during an outage?

## J. Databases, distributed systems and system design

153. Compare relational databases and NoSQL databases.
154. Explain indexes, query plans, connection pools and slow-query analysis.
155. What is replication lag and how does it affect reads?
156. Explain partitioning, sharding and consistent hashing.
157. What is eventual consistency?
158. Compare at-most-once, at-least-once and exactly-once processing claims.
159. How do idempotency keys and deduplication work?
160. What are the trade-offs of synchronous and asynchronous communication?
161. Design a highly available URL-shortener service.
162. Design a log ingestion and alerting platform.
163. Design a multi-tenant SaaS platform on AWS.
164. Design a secure CI/CD platform for multiple teams.
165. How would you design a resilient queue-based order-processing service?

## K. Security and FinOps

166. Explain least privilege and how you continuously validate it.
167. What is the difference between SAST, DAST, SCA and container scanning?
168. What is an SBOM and why should an image be signed?
169. How do you detect secrets committed to Git?
170. How do you prioritize vulnerabilities based on exploitability and exposure?
171. Explain threat modeling and trust boundaries.
172. How would you investigate suspicious API activity in CloudTrail?
173. How do you reduce cloud costs without harming reliability?
174. What is cost allocation and why do tags matter?
175. How do you calculate cost per request or cost per customer?

## L. AI, MLOps and AI infrastructure

176. Explain the difference between model training and inference.
177. What are tokens, context windows, embeddings and vector similarity?
178. What is quantization and what trade-offs does it introduce?
179. Explain GPU VRAM, utilization and memory bottlenecks during inference.
180. Compare vLLM, Triton, Hugging Face TGI and Ollama use cases.
181. What are prefill and decode phases in LLM inference?
182. How do batching, streaming and KV cache affect latency and throughput?
183. How would you deploy a model-serving endpoint on Kubernetes?
184. How do you autoscale a model server when requests are bursty?
185. Explain RAG ingestion, chunking, embedding, retrieval and reranking.
186. How do you evaluate retrieval quality and answer faithfulness?
187. Compare pgvector, Qdrant, Milvus and Weaviate at a conceptual level.
188. What is a model registry and how does MLflow help?
189. How do you monitor data drift, model quality and inference latency?
190. How would you control token cost and provider rate limits?
191. What is an AI gateway and why would an organization use one?
192. How do you secure model endpoints and prevent sensitive prompt leakage?

## M. Agentic AI, MCP and AIOps

193. What distinguishes an agent from a deterministic workflow?
194. Explain the agent loop: observe, reason, select tool, execute and verify.
195. What makes a tool contract safe and reliable?
196. What are MCP hosts, clients, servers, tools, resources and prompts?
197. How do you authenticate and authorize an MCP tool call?
198. Compare LangGraph stateful workflows with a free-form agent loop.
199. How do you prevent an agent from executing destructive shell commands?
200. How would you implement human approval for an infrastructure change?
201. How do you evaluate an agent beyond checking whether its final answer sounds correct?
202. What is prompt injection and how can retrieved content attack an agent?
203. How do you prevent tool output from being treated as trusted instructions?
204. How would you build an agent that summarizes Kubernetes events without changing the cluster?
205. How do you trace, audit and replay an agent run?
206. How do you handle retries, duplicate tool calls and partial workflow failures?
207. How would you design a multi-agent incident response system?
208. What should happen when an agent's confidence is low or tools disagree?
209. How do you isolate tenants and protect credentials in an agent platform?
210. Which operational actions should remain deterministic even when an AI agent is available?

## How to use this bank

- **First pass:** 10–15 questions per session from one section.
- **Second pass:** answer weak questions and add one follow-up per answer.
- **Practical pass:** implement or troubleshoot a related lab.
- **Mock pass:** mix Linux, networking, cloud, containers, IaC and incident scenarios.
- **AI pass:** explain safety boundaries, evaluation and infrastructure trade-offs—not only framework APIs.

Related external practice: [DevOps Interview Questions](https://github.com/NotHarshhaa/DevOps-Interview-Questions), [SRE Interview Prep](https://github.com/mxssl/sre-interview-prep-guide), [DevOps Exercises](https://github.com/bregman-arie/devops-exercises), [Sysadmin Skills](https://github.com/trimstray/test-your-sysadmin-skills).
