# AI Infrastructure, MLOps & Agentic Systems Engineering

This track extends Cloud & DevOps fundamentals into the infrastructure required to train, serve, observe and safely operate AI systems. It is not a shortcut around Linux, networking, containers, Kubernetes, Python or security.

## 1. Role map

| Role | Main responsibility | Required engineering depth |
|---|---|---|
| AI Infrastructure Engineer | GPU, compute, network, storage and model-serving platform | Linux, containers, Kubernetes, GPU operations, observability |
| MLOps Engineer | Reproducible ML lifecycle from data to model deployment | Python, data pipelines, CI/CD, registry, monitoring |
| LLM Platform Engineer | Shared inference, model access, routing, quotas and evaluation platform | APIs, serving, gateways, GPU capacity, security and FinOps |
| Agentic AI Engineer | Tool-using agents and workflow systems | Python, stateful orchestration, tool contracts, evaluations and guardrails |
| AIOps / AI for Operations Engineer | AI-assisted incident, log, alert and remediation workflows | SRE, observability, retrieval, agent safety and auditability |

## 2. AI and ML foundations

- ML lifecycle: data collection, cleaning, training, validation, evaluation, deployment and monitoring.
- Supervised, unsupervised and reinforcement learning at a conceptual level.
- Training vs inference; batch vs online inference.
- Model parameters, weights, checkpoints, tokenizer, tokens and context window.
- Transformer/attention concepts; embeddings and vector similarity.
- Precision formats: FP32, FP16, BF16, INT8 and 4-bit quantization.
- Model size and memory estimation; weights, activations and KV cache.
- Fine-tuning vs prompt engineering vs RAG; when each is appropriate.
- Dataset lineage, model lineage, reproducibility and data/model versioning.

**Expected interview depth:** explain the lifecycle, estimate memory needs at a high level, identify model quality risks and connect model behaviour to infrastructure.

## 3. GPU and compute infrastructure

### GPU fundamentals
- GPU vs CPU workloads; parallelism and memory bandwidth.
- VRAM capacity, utilization, fragmentation and allocation.
- CUDA concepts, drivers, runtime and compatibility.
- Multi-GPU concepts: data parallelism, tensor parallelism and pipeline parallelism.
- GPU scheduling, device plugins, node labels, taints and topology awareness.
- MIG and GPU sharing concepts where supported.
- PCIe/NVLink concepts and data transfer bottlenecks.
- Thermal, power and hardware health signals.

### Operations
- Driver/runtime compatibility and container GPU access.
- GPU telemetry and utilization dashboards.
- Node pool isolation, quotas and workload priority.
- Capacity planning based on model size, context, concurrency and throughput.
- Failure handling for unhealthy GPUs and unavailable capacity.

**Tools to recognize:** NVIDIA drivers, CUDA, NVIDIA Container Toolkit, NVIDIA GPU Operator, DCGM Exporter, Kubernetes device plugins. Validate version compatibility against official vendor matrices before implementation.

## 4. Model serving and inference systems

Understand the serving lifecycle:
1. Model artifact is retrieved and verified.
2. Runtime loads weights into host/GPU memory.
3. Requests enter an API or inference gateway.
4. Tokenization and preprocessing occur.
5. Scheduler batches and dispatches work.
6. Prefill processes input tokens; decode generates output tokens.
7. Streaming or complete responses return to clients.
8. Telemetry captures latency, tokens, errors, saturation and cost.

### Core concepts
- Time to first token (TTFT), time per output token (TPOT), tokens/second and end-to-end latency.
- Continuous batching, static batching and dynamic batching.
- KV cache and context length.
- Concurrency, queue depth, backpressure, rate limiting and admission control.
- Quantization and quality/performance trade-offs.
- Model warm-up, cold starts, autoscaling and graceful shutdown.
- Model routing, fallback, provider outages and circuit breaking.
- Streaming responses, cancellation and client disconnects.

### Serving tools
| Tool | What to understand |
|---|---|
| [vLLM](https://docs.vllm.ai/) | High-throughput LLM serving, batching and KV-cache management |
| [Hugging Face TGI](https://huggingface.co/docs/text-generation-inference) | Text-generation serving and deployment concepts |
| [NVIDIA Triton](https://docs.nvidia.com/deeplearning/triton-inference-server/) | General inference serving across supported model backends |
| [Ollama](https://ollama.com) | Local model management and developer workflows; not a substitute for every production serving platform |
| [KServe](https://kserve.github.io/website/) | Kubernetes-native model serving abstractions |
| [Ray Serve](https://docs.ray.io/en/latest/serve/index.html) | Distributed serving and application composition |

Do not learn all runtimes at once. Understand the serving lifecycle, then implement one local runtime and compare alternatives.

## 5. RAG and retrieval infrastructure

### Request and ingestion path
- Document ingestion, parsing, normalization and access-control metadata.
- Chunking strategy, overlap, metadata and source identifiers.
- Embedding model selection and versioning.
- Vector storage, indexing and similarity search.
- Hybrid retrieval, filters and reranking.
- Context assembly, prompt construction and generation.
- Source attribution, citation mapping and response validation.

### Evaluation and operations
- Retrieval recall/precision and ranking quality.
- Answer relevance, faithfulness and groundedness.
- Freshness, re-indexing, deletion propagation and access revocation.
- Tenant isolation and row/document-level authorization.
- Cache invalidation and embedding model migration.
- Latency, storage, token and retrieval cost.

### Tools
- [pgvector](https://github.com/pgvector/pgvector) — vector search inside PostgreSQL.
- [Qdrant](https://qdrant.tech/documentation/) — vector search engine.
- [Milvus](https://milvus.io/docs) — vector database.
- [Weaviate](https://weaviate.io/developers/weaviate) — vector database.
- [LlamaIndex](https://docs.llamaindex.ai/) — data and retrieval application framework.

## 6. MLOps lifecycle and model operations

- Dataset versioning, validation, lineage and access.
- Reproducible training pipelines and experiment tracking.
- Model registry, approval and promotion.
- Model artifact storage and immutable version references.
- CI for code, data and model validation.
- CD for model serving and canary promotion.
- Feature store concepts and training/serving skew.
- Model monitoring: quality, drift, bias, latency and cost.
- Rollback, shadow deployments and A/B testing.
- Scheduled retraining and human review gates.

**Tools:** [MLflow](https://mlflow.org/docs/latest/index.html), [Kubeflow](https://www.kubeflow.org/docs/), [KServe](https://kserve.github.io/website/), [DVC](https://dvc.org/doc), [Feast](https://docs.feast.dev/).

## 7. LLM gateway and platform engineering

A shared LLM platform typically provides:
- Provider/model abstraction and routing.
- Authentication, tenant identity and authorization.
- Per-team quotas, rate limits and budget enforcement.
- Retry, timeout, circuit-breaker and provider fallback.
- Prompt/model version metadata and request correlation.
- Usage metering: input/output tokens, model, tenant and cost.
- Caching with data classification and tenant-aware keys.
- Policy checks, PII handling and retention controls.
- Centralized telemetry, audit and incident response.

**Tools to investigate:** [LiteLLM](https://docs.litellm.ai/), OpenAI-compatible APIs, API gateways, Redis, PostgreSQL, OpenTelemetry and Grafana. Verify current features and deployment requirements from official documentation.

## 8. Agentic AI systems engineering

### Architecture
- User or event trigger → orchestrator → model → tool selection → tool execution → result validation → state update → final response.
- Deterministic workflow for known steps; agent reasoning only where ambiguity adds value.
- Typed state, structured outputs, checkpoints and explicit termination conditions.
- Tool schemas, validation, authorization, idempotency and bounded retries.
- Human approval interrupts for high-impact actions.
- Memory and retrieval separated from trusted policy and system instructions.

### Frameworks and protocols
- [Model Context Protocol](https://modelcontextprotocol.io/) — interoperability for exposing tools and context; understand hosts, clients, servers, tools, resources and prompts.
- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) — stateful graph orchestration, persistence and human-in-the-loop workflows.
- [LangChain](https://docs.langchain.com/oss/python/langchain/overview) — application components and agent abstractions.
- [LlamaIndex](https://docs.llamaindex.ai/) — data ingestion and retrieval-oriented applications.
- [OpenAI API documentation](https://platform.openai.com/docs/) — model/API concepts; confirm current API features in official docs.

### Production concerns
- Tool permission boundaries and workload identity.
- Prompt injection from logs, tickets, documents and command output.
- Data exfiltration and cross-tenant leakage.
- Tool output treated as untrusted data, never as policy.
- Run budgets, token limits, deadlines, cancellation and kill switch.
- Trace IDs, tool input/output audit, versioned prompts and replay.
- Evaluation datasets, deterministic mocks and regression tests.
- Human approval, change plans, dry-runs and post-action verification.

## 9. AIOps use cases

Good initial use cases:
- Summarize alerts and correlate related events.
- Explain a CI failure using logs and pipeline metadata.
- Search runbooks and suggest diagnostic commands.
- Summarize Kubernetes events and workload status using read-only access.
- Draft an incident timeline from approved telemetry.
- Recommend a Terraform plan review checklist without applying it.

Higher-risk use cases:
- Restarting workloads, changing autoscaling, modifying IAM, applying Terraform, deleting resources, rotating secrets or changing routes. These require explicit authorization, bounded scope, a reviewed plan and human approval. A model's confidence is not authorization.

## 10. Security and threat model

| Threat | Required control |
|---|---|
| Prompt injection in retrieved content | Treat content as untrusted data; isolate instructions and validate tool calls |
| Excessive agent permissions | Read-only default, least privilege, scoped identities |
| Secret leakage | Secret manager, redaction, no credentials in prompts or logs |
| Destructive tool use | Allowlist, dry-run, approval, blast-radius estimate and rollback |
| Duplicate execution | Idempotency keys, state checkpoints and operation ledger |
| Cross-tenant data access | Tenant-aware authorization at retrieval and tool layers |
| Model/provider compromise | Provider review, model artifact provenance and network egress controls |
| Untraceable actions | Immutable audit events, actor identity, tool arguments and outcome |
| Runaway cost | Token, time, tool-call and concurrency budgets |
| Evaluation blind spots | Golden tests, adversarial cases, live monitoring and regression gates |

## 11. AI observability and evaluation

Track:
- Request count, success/error rate and timeout rate.
- TTFT, TPOT, end-to-end latency and queue duration.
- Input/output tokens and estimated cost by model/tenant.
- GPU utilization, VRAM, temperature and scheduler queue.
- Retrieval latency, top-k results and source IDs.
- Tool-call success, validation failures, retries and approval wait.
- Agent task success, policy violations, hallucination/grounding measures and human override rate.

Evaluation should cover correctness, groundedness, retrieval quality, tool selection, argument validity, policy compliance, latency and cost. Use fixed datasets and compare releases; never rely only on a subjective sample of answers.

**Tools:** OpenTelemetry, Prometheus, Grafana, Langfuse, Arize Phoenix and provider-specific telemetry. Confirm product capabilities and privacy implications before adoption.

## 12. AI infrastructure project ladder

| Project | Demonstration | Priority |
|---|---|---|
| AI-01: Local inference lab | Run one local model; measure latency, tokens/sec, RAM/VRAM and resource use | P0 |
| AI-02: Model-serving API | Containerize one model-serving endpoint with health checks and metrics | P1 |
| AI-03: RAG service | Build document ingestion, vector retrieval, source citations and evaluation cases | P1 |
| AI-04: LLM gateway | Add model routing, quotas, rate limits, usage metering and fallback | P1 |
| AI-05: Kubernetes inference | Deploy a model server with resource requests, autoscaling strategy and dashboards | P2 |
| AI-06: Read-only Ops Agent | Summarize approved logs/events and cite evidence; no write tools | P0 |
| AI-07: Approval-gated remediation | Generate a plan, estimate impact, request approval, execute in sandbox and verify | P2 |

## 13. Interview readiness gate

You should be able to:
1. Explain training vs inference and estimate a model's memory requirements at a basic level.
2. Describe GPU scheduling, serving, batching and latency bottlenecks.
3. Deploy and observe one model-serving workload locally or in an isolated environment.
4. Explain a RAG request path and evaluate retrieval quality.
5. Design a secure LLM gateway with quotas, identity, logging and cost controls.
6. Explain an agent's tool boundary, prompt-injection risk and approval workflow.
7. Diagnose at least one model-serving or agent workflow failure using evidence.

## 14. Safe implementation rule

This curriculum does not authorize cloud provisioning. Start with local Docker, the existing AWS emulator, hosted labs or static design exercises. Any real AWS/GCP/Azure resources require an explicit cost estimate, IAM review, deployment plan and user approval.
