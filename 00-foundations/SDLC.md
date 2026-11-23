# Software Development Life Cycle (SDLC)

> **Interview objective:** Explain how software moves from a business need to a maintained production service, then show where DevOps, CI/CD and DevSecOps improve that lifecycle.

## 1. What is SDLC?

The Software Development Life Cycle (SDLC) is a structured framework for planning, specifying, designing, building, testing, deploying and maintaining software. It aligns engineering work with business and user needs while managing quality, cost, schedule, security and operational risk.

SDLC describes the lifecycle activities. An **SDLC model** describes how those activities are organised (sequentially, iteratively, incrementally, risk-first, or through prototyping). The seven stages are a useful teaching model, not a mandatory universal sequence. Real teams overlap activities and revisit earlier decisions.

### Why SDLC matters

- Creates shared understanding of scope, requirements, responsibilities and acceptance criteria.
- Finds defects, security weaknesses and feasibility problems earlier, when they are generally cheaper to address.
- Makes quality, delivery and operational expectations explicit.
- Provides traceability from requirements through design, implementation, tests and release.
- Establishes feedback and maintenance as part of product ownership, not an afterthought.

## 2. Seven commonly described SDLC stages

| Stage | Main work | Typical outputs | DevOps / operations perspective |
|---|---|---|---|
| 1. Planning and feasibility | Define problem, scope, stakeholders, budget, schedule, constraints and technical/operational feasibility | Project charter/plan, estimates, risk register | Estimate infrastructure, delivery complexity, cost, skills, capacity and operational ownership |
| 2. Requirements analysis | Gather, validate and prioritise functional and non-functional requirements | SRS, acceptance criteria, traceability | Clarify availability, latency, throughput, security, recovery, compliance, scalability and observability requirements |
| 3. System design | Convert requirements into architecture and implementation detail | HLD, LLD, architecture decisions, data/API designs | Design network, IAM, environments, deployment topology, secrets, backups, monitoring and failure domains |
| 4. Development | Implement features, review code, manage dependencies and run developer tests | Source code, reviewed changes, build configuration | Support Git workflows, reproducible environments, containers and developer automation |
| 5. Testing | Verify components and system behaviour against requirements | Test suites/results, defect reports, quality evidence | Automate tests and scans in CI; test integration, resilience, performance and security at appropriate levels |
| 6. Deployment / release | Package and promote a tested version into target environments | Versioned artifact, release record, deployed service | Build CI/CD, infrastructure automation, approvals, progressive rollout, smoke checks and rollback |
| 7. Maintenance / operations | Monitor, support, patch, repair, improve and eventually retire software | Incidents, patches, updates, postmortems, new releases | Operate observability, incident response, vulnerability remediation, capacity, backup/restore and cost controls |

### Functional vs non-functional requirements

- **Functional requirements:** What the system must do. Example: a customer can transfer money between eligible accounts.
- **Non-functional requirements (NFRs):** How well and under what constraints it must operate. Example: an API's latency target, availability objective, security controls, recovery objectives and expected load.

NFRs must be measurable where possible. "Fast" is vague; "p95 latency below 300 ms at the agreed load" is testable. The target itself must come from stakeholders and workload evidence, not be invented by an engineer.

### HLD vs LLD

- **High-Level Design (HLD):** System boundaries, major components, architecture, integrations, technology choices, data stores and deployment topology.
- **Low-Level Design (LLD):** Component behaviour, API contracts, schemas, algorithms, validation, error handling and detailed interactions.

Names and document formats vary by organisation. The important point is that design decisions should be sufficiently clear to implement, test and operate the system.

## 3. SDLC models

A model organises lifecycle work. No model is universally best; selection depends on requirement stability, uncertainty, risk, regulation, delivery cadence, modularity and stakeholder availability.

### Waterfall
A predominantly sequential, plan-driven approach. Teams typically complete and approve one phase before moving to the next.

- **Useful when:** Requirements and acceptance criteria are stable; formal phase gates and documentation are important.
- **Trade-off:** Late changes can trigger expensive rework; working software and user feedback may arrive late.
- **Do not claim:** Waterfall means testing is absent until the very end in every implementation. Test planning and reviews can still happen earlier.

### V-Model
A sequential model that pairs development specifications with corresponding verification/validation activities. Test planning begins alongside the associated development stages; execution of the corresponding test levels generally follows implementation.

Common conceptual pairing:
- User/business requirements ↔ Acceptance testing.
- System requirements ↔ System testing.
- Architecture/high-level design ↔ Integration testing.
- Detailed/module design ↔ Unit testing.
- Coding/implementation sits at the bottom of the V.

- **Useful when:** Traceability, formal verification and validation, and controlled testing are important.
- **Trade-off:** Can be rigid when requirements change frequently.

**Verification vs validation:** Verification asks, "Are we building the product correctly against the specification?" Validation asks, "Are we building the right product for the user's need?"

### Iterative
Build an initial version, evaluate it, then repeatedly refine or improve it through cycles.

- **Useful when:** The solution needs learning, refinement or technical discovery.
- **Trade-off:** Rework can grow without clear architecture, priorities and feedback.

### Incremental
Deliver the product in separately planned functional increments. Each increment adds capability to the existing product and has its own design, implementation and testing.

- **Useful when:** The product can be decomposed into valuable, testable features and early delivery matters.
- **Trade-off:** Integration, shared architecture and compatibility must be managed.

**Remember:** Iterative = improve what exists. Incremental = add another piece of capability. A project can be both.

### Agile
An adaptive family of approaches guided by the Agile values and principles. Work is prioritised, developed in small increments, reviewed frequently and adjusted using feedback.

- **Useful when:** Requirements evolve and stakeholders can collaborate regularly.
- **Trade-off:** Agile does not remove the need for architecture, documentation, testing, planning or operational discipline. Weak prioritisation can create churn.

Agile is not synonymous with Scrum:
- **Scrum** is a framework with defined accountabilities, events, artefacts and timeboxed Sprints.
- **Kanban** manages and improves flow using visualised work, explicit policies and work-in-progress limits; it does not require fixed-length iterations.
- **Extreme Programming (XP)** emphasises engineering practices such as pair programming, test-driven development, refactoring and continuous integration.

### Spiral
A risk-driven iterative model. Each cycle defines objectives, analyses risks and alternatives, engineers/evaluates a solution, and plans the next cycle.

- **Useful when:** Projects are large, complex, costly or technically uncertain, and risk analysis is essential.
- **Trade-off:** Risk assessment and management require expertise and can be expensive.

### RAD (Rapid Application Development)
Emphasises rapid prototyping, reusable components, modular development and frequent user participation.

Typical phases are requirements planning, user design, construction and cutover.
- **Useful when:** A system can be modularised and users can give frequent feedback under time constraints.
- **Trade-off:** Poor fit for highly constrained systems, unavailable users, or cases where speed undermines architecture and quality.

### Prototype model
Build a preliminary representation to discover, clarify or validate requirements before committing to the final product.

- **Throwaway prototype:** Built to learn, then discarded; the production solution is engineered separately.
- **Evolutionary prototype:** Refined progressively and may evolve into the final system, provided quality and architecture are deliberately engineered.
- **Useful when:** Requirements or user expectations are unclear.
- **Trade-off:** A demo/prototype can be mistaken for production-ready software; technical shortcuts must not silently become permanent architecture.

## 4. Quick comparison

| Model | Organising idea | Flexibility / feedback | Typical fit |
|---|---|---|---|
| Waterfall | Sequential phases | Lower; formal change control | Stable, well-defined scope |
| V-Model | Sequential with paired test levels | Lower; strong traceability | Formal verification/validation |
| Agile | Adaptive, iterative and incremental delivery | High; frequent feedback | Evolving product requirements |
| Iterative | Repeated refinement | High | Progressive learning/improvement |
| Incremental | Feature delivery in increments | Moderate to high | Modular product with staged value |
| Spiral | Repeated risk analysis and engineering | High, risk-led | Large, high-risk work |
| RAD | Fast modular construction and user design | High, user-intensive | Time-sensitive modular applications |
| Prototype | Build/evaluate/refine representation | High during discovery | Unclear requirements |

These are broad tendencies, not immutable rules. Actual projects may combine approaches.

## 5. Security across the lifecycle: DevSecOps

Security is not a final-stage activity. DevSecOps integrates security responsibilities and controls throughout the lifecycle.

| SDLC activity | Example security practice |
|---|---|
| Planning | Identify data classification, regulatory obligations and threat assumptions |
| Requirements | Define authentication, authorisation, encryption, audit and retention requirements |
| Design | Threat modelling, secure architecture, trust boundaries and least privilege |
| Development | Secure coding, peer review, secret detection and dependency hygiene |
| Testing | SAST, DAST, dependency/container scanning, IaC checks and security tests |
| Deployment | Protected environments, signed/provenanced artifacts, restricted credentials and policy gates |
| Maintenance | Patch management, vulnerability response, logging, incident handling and access reviews |

Tool scans are evidence, not proof that a system is secure. Findings need triage, ownership, remediation and verification.

## 6. Banking application example

Suppose a bank commissions a mobile application.

1. **Planning:** Confirm business case, budget, timeline, stakeholders, risks and delivery feasibility.
2. **Requirements:** Specify account viewing and transfers (functional); define security, availability, auditability, performance and recovery requirements (non-functional).
3. **Design:** Define mobile/API architecture, identity, transaction workflow, database, network boundaries, encryption, audit trail and deployment topology.
4. **Development:** Implement APIs and application features through reviewed Git changes.
5. **Testing:** Unit, integration, system, security, performance and user acceptance testing. Verify transaction correctness and failure handling.
6. **Deployment:** Promote a tested artifact through controlled environments, run smoke checks and monitor release health.
7. **Maintenance:** Monitor service health, respond to incidents, patch dependencies, restore backups when required and improve the product.

## 7. Common failure modes

- Requirements are documented but assumptions are not validated with users.
- NFRs are vague or ignored until production.
- Testing is delayed, shallow or disconnected from acceptance criteria.
- Teams treat security as a final scan instead of a lifecycle responsibility.
- Design ignores failure domains, integration, capacity, recovery or cost.
- Handoffs create unclear ownership between development, QA, security and operations.
- Deployment is automated without safe rollout, observability or rollback.
- Teams follow a model mechanically instead of adapting it to evidence and risk.

SDLC provides structure; it does not guarantee success. Outcomes depend on clear requirements, stakeholder involvement, engineering quality, risk management, ownership and feedback.

## 8. DevOps connection: from SDLC to CI/CD

SDLC is the overall lifecycle. CI/CD automates selected integration, verification, packaging and release activities within that lifecycle. DevOps adds shared ownership, automation, feedback and operational learning across development and operations.

A representative pipeline:

1. Developer creates a branch and opens a pull request.
2. CI runs linting, unit tests, dependency checks and build validation.
3. A versioned artifact (for example, a container image) is created and stored.
4. The same artifact is promoted to a staging environment.
5. Integration, acceptance, security and smoke checks run.
6. A release decision or automated policy gate authorises production promotion.
7. Deployment uses an appropriate strategy (rolling, blue/green or canary).
8. Health checks and observability validate the release; rollback or roll-forward follows the incident/release policy.
9. Production feedback informs the next development cycle.

- **Continuous Integration:** Frequently integrate changes and automatically build/test them.
- **Continuous Delivery:** Keep changes in a deployable state; production release is available through a controlled decision.
- **Continuous Deployment:** Automatically release every change that passes the required pipeline gates to production.

Not every organisation uses every stage or fully automated production deployment. The release design should match risk and regulatory requirements.

## 9. Interview answer framework

For "Explain SDLC and the role of DevOps", structure the answer:

1. Define SDLC in one sentence.
2. Walk through the seven commonly described stages.
3. Explain that models organise the stages differently.
4. Explain DevOps as shared responsibility, automation and feedback across the lifecycle.
5. Give a concrete CI/CD example from code commit to monitored production release.
6. Mention security, reliability and rollback as lifecycle concerns.

**Sample concise answer:**

"SDLC is the structured lifecycle used to plan, specify, design, develop, test, deploy and maintain software. A common representation has seven stages, although teams can organise them using models such as Waterfall, V-Model, Agile, Iterative, Incremental or Spiral. DevOps improves the lifecycle by bringing development and operations together, automating build, test and release workflows through CI/CD, managing infrastructure as code, and feeding production telemetry back into engineering. For example, a pull request can trigger automated tests and security checks, produce a versioned container image, deploy that same artifact to staging, and promote it to production with health checks and rollback controls."

## 10. Self-check checklist

- [ ] Define SDLC and explain why it is used.
- [ ] Explain all seven stages with one practical output each.
- [ ] Distinguish functional and non-functional requirements.
- [ ] Explain HLD vs LLD.
- [ ] Compare Waterfall, V-Model, Agile, Iterative, Incremental, Spiral, RAD and Prototype.
- [ ] Distinguish iterative from incremental.
- [ ] Distinguish Agile from Scrum and Kanban.
- [ ] Explain verification vs validation.
- [ ] Explain how DevSecOps integrates security throughout SDLC.
- [ ] Trace a code change through CI/CD to monitored production.
- [ ] Explain Continuous Integration vs Continuous Delivery vs Continuous Deployment.
- [ ] Explain what happens when a production deployment fails.

## 11. Revision in 60 seconds

- **SDLC:** lifecycle activities; a model organises them.
- **Stages:** Plan → Requirements → Design → Develop → Test → Deploy → Maintain.
- **Waterfall:** sequential.
- **V-Model:** development specifications paired with testing levels.
- **Agile:** adaptive delivery and feedback.
- **Iterative:** refine existing solution.
- **Incremental:** add functional pieces.
- **Spiral:** risk-driven cycles.
- **RAD:** rapid modular development with user participation.
- **Prototype:** learn/validate requirements using a preliminary representation.
- **DevOps:** shared ownership, automation and feedback across delivery and operations.
- **DevSecOps:** security integrated throughout the lifecycle.
- **CI/CD:** automated integration, verification and release pipeline.

## 12. Sources and terminology note

This note consolidates the SDLC and SDLC-model material supplied during the learning session. It uses common industry terminology; exact stage names, model taxonomies and document names can vary by organisation. Treat model suitability as a decision based on project context, not a rigid rule.

---

**Study status:** Learning. Do not mark this topic documented or interview-ready until the explanation, comparison and interview drills have been completed and reviewed.


---

## 11. Beginner-first mental model and visual lifecycle

### Explain it like you're five

Imagine a team is asked to build a school library. They do not start hammering wood randomly. First they understand what the school needs, plan the work, draw the design, build it, check that it is safe and useful, open it, and then repair and improve it. Software follows the same kind of journey.

```text
IDEA / BUSINESS NEED
        |
        v
1. PLAN       Is it useful, possible and affordable?
        |
        v
2. REQUIRE    What must it do? What quality is required?
        |
        v
3. DESIGN     What components and interfaces will make it work?
        |
        v
4. DEVELOP    Build the software and review changes.
        |
        v
5. TEST       Does it behave correctly against requirements?
        |
        v
6. DEPLOY     Release a known version safely to users.
        |
        v
7. MAINTAIN   Monitor, fix, secure and improve it.
        |
        +---------------------> feedback informs the next cycle
```

This is a teaching sequence, not a mandatory one-way path. Real teams overlap stages and revisit earlier decisions.

## 12. SDLC technical vocabulary

| Term | Beginner-friendly meaning | Why it matters |
|---|---|---|
| Stakeholder | Person/group affected by or able to influence the product | Requirements must reflect real needs |
| Feasibility | Whether the idea can realistically be delivered | Prevents impossible or unaffordable work |
| Scope | What is included and excluded | Controls expectations and change |
| Requirement | A needed capability or constraint | Defines what success means |
| Functional requirement | What the system must do | Describes features and behaviour |
| Non-functional requirement (NFR) | How well or under what constraints it must work | Drives reliability, security and performance |
| SRS | Software Requirements Specification | Shared reference for implementation and testing |
| Acceptance criteria | Conditions that must be met for a requirement/story to be accepted | Makes completion testable |
| Traceability | Link from requirement to design, code, tests and release evidence | Helps prove important requirements were addressed |
| HLD | High-Level Design; big-picture architecture | Shows major components and relationships |
| LLD | Low-Level Design; detailed component behaviour | Guides implementation and testing |
| API | Application Programming Interface; defined way for components to communicate | Enables integration |
| QA | Quality Assurance; practices that prevent/detect quality problems | Quality is a process, not only a final test |
| Unit test | Test of a small unit such as a function | Finds local logic defects |
| Integration test | Test that connected components work together | Finds interface/dependency defects |
| System test | Test of the whole system | Checks end-to-end behaviour |
| UAT | User Acceptance Testing by business/users | Checks whether it solves the intended need |
| Defect/bug | Behaviour that fails an expected requirement | Needs triage, correction and retest |
| Artifact | Built, versioned output such as a package or container image | Enables repeatable promotion |
| Environment | Place where software runs, such as dev, staging or production | Separates test and live workloads |
| Smoke test | Short check that key service functions after release | Detects obvious release failures |
| Rollback | Return to a previously known-good version/state | Limits release impact |
| Verification | Are we building the product according to the specification? | Checks conformance |
| Validation | Are we building the right product for the user's need? | Checks fitness for purpose |
| DevOps | Shared ownership, automation and feedback across development and operations | Connects building and running software |
| CI | Continuous Integration; frequent integration with automated build/test | Finds integration problems early |
| Continuous Delivery | Keep changes deployable, with a controlled production-release decision | Makes releases repeatable |
| Continuous Deployment | Automatically release every qualifying change to production after required gates | Removes the manual production-release step |
| DevSecOps | Security practices and shared responsibility across delivery and operations | Avoids treating security as a final-stage activity |
| SAST | Static Application Security Testing; examines code without running the app | Finds certain code weaknesses early |
| DAST | Dynamic Application Security Testing; tests a running application | Finds certain runtime-visible weaknesses |

## 13. Apply SDLC to an e-portfolio website

Your older Foundation notes suggest using an e-portfolio website as an SDLC example. This is a generic worked example; it is not a claim that any particular portfolio project has completed these stages.

| Stage | Example |
|---|---|
| Planning | Identify audience (recruiters/clients), purpose, timeline, budget and success measures |
| Requirements | Define pages, projects, contact method, accessibility, mobile behaviour, SEO and performance needs |
| Design | Create sitemap, layouts, content model, responsive behaviour, hosting and deployment architecture |
| Development | Build pages, project details, navigation, contact flow and metadata in version control |
| Testing | Check links, forms, mobile layouts, keyboard access, browser compatibility, metadata and performance |
| Deployment | Publish a version, verify DNS/HTTPS and run smoke checks |
| Maintenance | Update projects, patch dependencies, monitor availability, fix defects and refresh content |

A requirement such as "the website must be fast" is vague. Define a measurable target and test method based on the actual project requirements; do not invent an arbitrary performance promise.

## 14. Interview answer and revision method

For "Explain SDLC", answer in this order:

1. Define SDLC.
2. Explain the seven commonly described stages.
3. Explain that models organise the stages differently.
4. Connect DevOps, CI/CD and DevSecOps to the lifecycle.
5. Give a concrete example and mention feedback/maintenance.

**Sample answer:**

"SDLC is the structured lifecycle used to turn a business need into software that can be maintained. A common representation includes planning, requirements, design, development, testing, deployment and maintenance. Models such as Waterfall, V-Model and Agile organise this work differently depending on uncertainty, risk and feedback needs. DevOps improves the lifecycle through shared development/operations ownership, automation and production feedback. CI/CD automates integration, verification and release steps, while DevSecOps integrates security throughout the lifecycle. For example, an e-portfolio project begins with audience and content requirements, moves through design and implementation, is tested on mobile and desktop, deployed to hosting, and maintained as projects and dependencies change."

Use the [SDLC interview question bank](../12-interview-preparation/sdlc-interview-questions.md). First explain SDLC from memory in 60–90 seconds, draw the seven stages, compare two models, answer 5–10 questions aloud, and complete one scenario. Mark each answer correct, incomplete, incorrect or unknown; revisit weak answers after 24–72 hours. Do not mark SDLC interview-ready until you can map a real project to all seven stages and handle follow-up questions without notes.
