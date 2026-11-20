# SDLC — Interview Question Bank

Use these questions for active recall. Attempt an answer aloud before opening the handbook note. Record the result as Correct, Incomplete, Incorrect or Unknown.

Reference: [SDLC study notes](../../00-foundations/SDLC.md)

## Level 1 — Fundamentals

1. What is the Software Development Life Cycle (SDLC)?
2. Why do engineering teams use an SDLC?
3. What are the commonly described seven stages of SDLC?
4. What is the difference between an SDLC stage and an SDLC model?
5. What is feasibility analysis?
6. What is an SRS?
7. What are functional requirements?
8. What are non-functional requirements? Give five examples.
9. What is the difference between HLD and LLD?
10. What is User Acceptance Testing (UAT)?
11. What happens during software maintenance?
12. Does SDLC always have exactly seven stages? Explain.

## Level 2 — Models and comparisons

13. Explain the Waterfall model.
14. When would Waterfall be a reasonable choice?
15. What are the limitations of Waterfall?
16. Explain the V-Model.
17. What is the relationship between development phases and testing levels in the V-Model?
18. Distinguish verification from validation.
19. Explain Agile development.
20. Is Agile the same as Scrum? Explain.
21. What is Kanban, and how does it differ from Scrum?
22. Distinguish iterative and incremental development.
23. Can a project be both iterative and incremental? Give an example.
24. Explain the Spiral model and why it is risk-driven.
25. When might RAD be appropriate?
26. What is the Prototype model?
27. Distinguish throwaway and evolutionary prototyping.
28. How would you select an SDLC model for a project?

## Level 3 — DevOps, CI/CD and security

29. Where does a DevOps engineer contribute across SDLC?
30. Is DevOps an SDLC model? Explain the distinction.
31. How does CI/CD support the SDLC?
32. What happens after a developer opens a pull request in a mature CI pipeline?
33. Distinguish Continuous Integration, Continuous Delivery and Continuous Deployment.
34. Why should the same versioned artifact be promoted between environments?
35. What is a deployment approval gate?
36. What is a smoke test, and when should it run?
37. What is the purpose of a rollback strategy?
38. What is DevSecOps?
39. Give security practices for requirements, design, development, testing and operations.
40. Why is a vulnerability scan not sufficient to prove that an application is secure?
41. How do observability and production feedback influence the next SDLC cycle?

## Level 4 — Scenario and troubleshooting

42. A customer changes a major requirement after design approval. Which model or approach might handle this well, and what trade-offs must be managed?
43. A team has unclear requirements and stakeholders cannot explain the expected workflow. How could prototyping help?
44. A safety-critical system needs traceability from requirements to tests. Which model may be suitable and why?
45. A large project has major technical and security uncertainty. How could Spiral help?
46. A release passes unit tests but fails in staging because two services cannot communicate. Which testing level failed to catch the issue?
47. A deployment succeeds technically but customers experience errors. What validation and operational checks should have detected this?
48. A team deploys manually once every three months. What would you improve first, and why?
49. A CI pipeline passes but production deployment fails. Explain a safe diagnosis and recovery process.
50. A team has automated deployment but no monitoring or rollback. Why is this incomplete DevOps practice?

## Level 5 — Applied engineering

51. Design a high-level SDLC and release process for a small REST API.
52. Map a banking money-transfer feature to functional requirements, NFRs, design, tests and operations.
53. Propose CI checks for a Dockerised application.
54. Propose a safe deployment strategy for a customer-facing API.
55. Explain how you would measure whether a release is healthy.
56. Explain how a production incident should feed back into requirements, tests and future releases.

## Scoring rubric

| Score | Meaning |
|---|---|
| 0 | Cannot answer or answer is materially incorrect |
| 1 | Can define the term but cannot explain it |
| 2 | Can explain with a reasonable example |
| 3 | Can compare alternatives and discuss trade-offs |
| 4 | Can apply it to a realistic engineering scenario and defend decisions |

**Interview-tested exit gate:** Attempt at least 15 questions unaided, including five scenario questions. Revisit every 0–2 score. Do not mark Interview ready solely because the definitions are memorised.
