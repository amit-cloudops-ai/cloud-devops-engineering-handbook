# Resume Playbook: Amit P M (DevOps / Cloud / Platform Engineering)

Give this whole file to ChatGPT at the start of a chat, then paste a job description (JD). ChatGPT should follow Sections 1-6 and return a new Overleaf script.

---

## 1. Role and hard rules for ChatGPT

You are a resume editor, not an author. The facts belong to Amit.

1. Use ONLY facts from Section 4 (Verified Facts) and from the JD. Never invent a number, tool, project, employer, date, or result.
2. If a JD needs a skill or metric that is not in Section 4, do NOT add it. List it under "Missing from your facts" and ask Amit.
3. Keep the layout and LaTeX exactly as in Section 7. Change only the text inside bullets, skills lines, and (if told) the F13 and project selection.
4. Output one complete Overleaf script that compiles with pdfLaTeX (no fontspec, no XeLaTeX).
5. After the script, list every change made and why, in under 10 lines.
6. Never include a graduation/pass-out year, CGPA, or percentage in the resume, even if present in the verified-facts source. Education should list the degree, discipline and institution only.

## 2. Format rules (the reference template)

- One page, one column, letter size, Times-style 10 pt font, margins 0.75 in left and right.
- Header: name (19 pt bold, centred), then one line: Location | LinkedIn | GitHub | Portfolio | phone | email.
- Section order: Education, Work Experience, Projects, Technical Skills. Section titles in bold caps with a full-width rule.
- Entry format: bold name left and bold location right; italic role left and italic dates right (Month YYYY -- Month YYYY, same style everywhere).
- Bullets: filled round bullets, justified text.
- No photo, icons, graphics, skill bars, tables, text boxes, or colour except blue hyperlinks.
- Education has no bullets. Every other entry has exactly 2 or 3 bullets, never 1, never 4.

## 3. Bullet rules (what we used)

1. Every bullet fills exactly two lines (about 190-215 characters). The second line must reach at least 80% of the width. Check this in the compiled PDF.
2. Each bullet starts with a different past-tense action verb (present tense only for the current job). No verb is used twice anywhere on the page.
3. Shape: what Amit did + with which tools + a number or concrete result. If no real number exists, state the concrete outcome instead.
4. Numbers must come from Section 4. Counts, sizes, percentages, durations, and time limits are the only kinds used.
5. Banned filler and buzzwords: passionate, dynamic, results-driven, spearheaded, leveraged, synergy, cutting-edge, robust, seamless, innovative, proven track record, responsible for, worked on, helped with, various, utilized, end-to-end, hands-on (as an adjective), fast-paced.
6. No repeated words inside a bullet, and avoid repeating the same non-technical word across the page. Tool names (AWS, Terraform) may repeat.
7. Write like a person: plain, specific, slightly uneven sentence length. Avoid triplets ("A, B, and C") in every bullet, avoid em dashes, avoid "by doing X, resulting in Y" in every line.
8. Mirror the JD's wording only where Amit truly has the skill. Use the JD's exact tool names (for example "Amazon EKS" vs "Kubernetes") in the skills block and the bullets they apply to.

## 4. Verified Facts (the only source for content)

**Header:** Amit P M | Karnataka, India | 7349400805 | amitpm.work@gmail.com | www.linkedin.com/in/amitops | github.com/amit-cloudops-ai | portfolio https://amitpm.dpdns.org/

**Education:** B.Tech, Metallurgical and Materials Engineering, NITK Surathkal. Do not display the graduation/pass-out year, CGPA or percentage.

**F13 Technologies, AWS Cloud Intern, Sept 2026 - Present, Bengaluru**
- Leads a team of 4; splits each project into 3 parts, assigns an owner per part, integrates the parts; shared team workspace; mentor reviews.
- Attendance system: S3, Lambda, Rekognition, DynamoDB, EventBridge; sized for 100 employees; pre-signed URL upload, S3 event trigger, daily 11:59 PM absentee job, images deleted after recognition (1-hour TTL), DynamoDB encryption at rest, S3 versioning, result target of 3 seconds.
- Resume screener: Textract, Comprehend, SQS with dead-letter queue, DynamoDB, Cognito, SES, API Gateway; scoring weights skills 50%, title 30%, experience 20%. (Status: in progress, deadline Nov 25, 2026. Confirm before claiming "deployed".)
- Onboarding service: Lambda, DynamoDB, Cognito, SES, Step Functions, API Gateway, S3, SNS; cost estimate for 50 onboarding events per month. (Confirm status.)
- Epic Games AWS case study: 14 slides plus written report; Amit owned the lobby slides, match statistics, lessons learned, and the visual theme; delivered to mentor as PDF.

**Kannur PU College (CBSE), Mathematics Teacher, Sept 2025 - June 2026, Ranebennur**
- Taught Class 11-12 plus competitive-exam preparation for 10 months; planned lessons, pacing, assessments independently. (No student count or results on file. Ask Amit before adding any.)

**BHEL Electronics Division, Industrial Trainee, May 2024 - July 2024, Bengaluru**
- Delivery performance up 30% using time-motion studies and line balancing; coordinated Engineering, PPC, Quality, Material Management (4 teams); wrote a department-wide report on SAP workflow integration, ISO 9001 audits, and defect tracking. (No other numbers on file.)

**Project 1: Progressive Delivery Platform on EKS (Sept 2026)** github.com/amit-cloudops-ai/pdp-eks-gitops
- Terraform-built VPC (2 AZs) and EKS 1.34; Karpenter (v1.13.0) launching nodes in about 10 seconds, limited to free-tier instance types; ArgoCD auto-syncing a Git repo; OWASP Juice Shop as the app.
- Gateway API weighted canary (90/10 confirmed with 20 test requests, about 16:2); Argo Rollouts steps 10%, 50%, 100% with pauses; a deliberately broken image tag never received traffic and the rollout turned Degraded and recovered after reverting to the good version.
- External Secrets Operator with AWS Secrets Manager (Pod Identity role limited to GetSecretValue and DescribeSecret on one path); Prometheus, Grafana, Loki, Alertmanager sending a real alert to Slack.
- NOT to claim: Prometheus-gated canary analysis, a deployed AI copilot (code written, not deployed), k6 numbers (no figures on file).

**Project 2: Three-Tier Web Application on AWS (June 2026)** github.com/Amitpm8/Devops-3-tire-project-001
- VPC with 6 subnets across 2 AZs; 2 NAT Gateways; 4 security groups (NLB, Nginx, app, database) with the database reachable only from the app tier; Nginx reverse proxy to Tomcat 10 on Java 17; Spring Boot app; RDS MySQL; registered a user and signed in through the browser to confirm the full chain.
- NOT to claim: load testing.

**Project 3: Zero-Downtime API Deployments on AWS (March 2026)** github.com/Amitpm8/aws-zero-downtime-deployment
- Blue-Green and Canary on Lambda behind API Gateway, 10% traffic steps; CloudWatch Alarms on 4XX/5XX with SNS alerts within 60 seconds; 12+ releases with zero incidents. (Taken from the earlier resume; verify against the repo.)

**Skills:** Python, Bash, YAML, SQL | EC2, S3, VPC, IAM, Lambda, CloudFront, RDS, API Gateway, CloudWatch | Docker, Kubernetes, Amazon EKS, CNI, CSI, NGINX Ingress, Gateway API, Karpenter | Git, GitHub Actions, ArgoCD, Terraform, CloudFormation, Ansible | Prometheus, Grafana, CloudWatch, OpenTelemetry, Loki | Linux (Ubuntu), DNS, TCP/IP, subnetting, Nginx

**Not on this resume by choice:** Ajji's Secret, Ventablk.co, leadership activities. Do not add unless Amit asks.

## 5. JD-tailoring workflow (do these in order)

1. Read the JD. List its must-have skills and tools, in its own words.
2. Match each against Section 4. Mark: Have / Partial / Missing.
3. Re-order the Technical Skills lines so the JD's tools come first. Rename a skills heading if the JD uses a different term for the same thing.
4. Choose which project bullets to keep (all three projects stay; adjust the bullets inside them). Put the most JD-relevant project first.
5. Rewrite only the bullets that need it, following Section 3. Keep each at two full lines.
6. Reply with: (a) the full Overleaf script, (b) a Have / Partial / Missing table, (c) up to 3 questions for facts you would need to strengthen a weak bullet.

## 6. Industry standards for 2026 (what the sources say) and 2027 (what is not yet known)

2026, based on current recruiter and career-centre guidance:
- Single-column, reverse-chronological layout with standard headings (Education, Work Experience, Projects, Skills) parses most reliably in applicant tracking systems.
- Upload a text-based PDF or .docx. Avoid text in images, graphics, skill bars, tables, and overlapping columns.
- Systems now use semantic matching (meaning and context), not only keyword counts. Use the JD's real terms where true, but do not stuff keywords.
- Recruiters care about measurable results and relevant tools more than job duties.
- Length: one page is normal for a fresher; one survey reports many hiring managers expect two pages, but that applies to people with longer careers.
- Authenticity: one 2026 hiring-manager survey reports about 80% say they can often tell when a resume was AI-written, and about 51% name unnatural phrasing or tone as the top giveaway. Another test of eight ATS products found they do not detect AI text; the real risk is a human reader noticing generic wording. Be ready to explain every line in an interview.
- Keep LinkedIn and GitHub consistent with the resume.

2027: no formal standard has been published. Reasonable direction, based on the current trend and not on a rule: more AI-assisted screening, more emphasis on proof (GitHub repos, live demos, portfolio links), and more disclosure expectations. The rules above (real facts, plain language, a clean single column) should remain safe.

## 7. The Overleaf script (compile with pdfLaTeX, the Overleaf default)

```latex
\documentclass[10pt,letterpaper]{article}
\usepackage[left=0.75in,right=0.75in,top=0.2in,bottom=0.3in]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{mathptmx}
\usepackage{enumitem}
\usepackage[hidelinks,pdftitle={Amit P M - Resume},pdfauthor={Amit P M},pdfcreator={},pdfproducer={},pdfsubject={},pdfkeywords={}]{hyperref}
\usepackage{xcolor}
\usepackage{microtype}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\linespread{1.0}\hyphenpenalty=10000\exhyphenpenalty=10000\tolerance=2000

\newcommand{\sect}[1]{\noindent{\bfseries #1}\par\nointerlineskip\vspace{2pt}\hrule height 0.6pt\vspace{2pt}}
\newcommand{\entry}[4]{%
  \noindent{\bfseries #1}\hfill{\bfseries #2}\par
  \noindent{\itshape #3}\hfill{\itshape #4}\par}
\newenvironment{bul}{\begin{itemize}[leftmargin=18pt,labelsep=0pt,labelwidth=18pt,itemsep=0pt,parsep=0pt,topsep=0pt,partopsep=0pt,align=left,label={\raisebox{0.3pt}{\large$\bullet$}}]}{\end{itemize}}
\newcommand{\gap}{\vspace{10pt}}

\begin{document}
\begin{center}\vspace{0pt}
{\bfseries\fontsize{19}{21}\selectfont Amit P M}\\[1pt]
{\fontsize{11}{12}\selectfont Karnataka, India | \href{https://www.linkedin.com/in/amitops}{\textcolor{blue}{\underline{LinkedIn}}} | \href{https://github.com/amit-cloudops-ai}{\textcolor{blue}{\underline{GitHub}}} | \href{https://amitpm.dpdns.org/}{\textcolor{blue}{\underline{Portfolio}}} | 7349400805 | amitpm.work@gmail.com}
\end{center}
\vspace{-4pt}

\sect{EDUCATION}
\entry{National Institute of Technology Karnataka (NITK), Surathkal}{Surathkal, Karnataka}{Bachelor of Technology in Metallurgical and Materials Engineering}{}

\gap
\sect{WORK EXPERIENCE}
\entry{F13 Technologies}{Bengaluru, India}{AWS Cloud Intern}{September 2026 -- Present}
\begin{bul}
\item Lead a 4-member team on cloud builds, splitting each project into 3 parts, assigning an owner to every part, and merging them into one working system, with progress tracked in a shared team workspace and reviewed by the mentor.
\item Built a serverless attendance system on S3, Lambda, Rekognition, DynamoDB, and EventBridge sized for 100 employees, plus a Textract and Comprehend resume screener ranking candidates by skills 50\%, title 30\%, experience 20\%.
\item Authored a 14-slide case study on how Epic Games scales its AWS infrastructure for live matches, owning the lobby slides, match statistics, lessons learned, and the visual theme, then delivered it to the mentor as a PDF report.
\end{bul}

\gap
\entry{Kannur PU College (CBSE)}{Ranebennur, India}{Mathematics Teacher --- Competitive Exams \& Class XI--XII}{September 2025 -- June 2026}
\begin{bul}
\item Taught Mathematics for 10 months to Class 11--12 CBSE students, covering the full syllabus alongside a separate preparation track for competitive exams, with every lesson planned and delivered independently all year.
\item Managed pacing, assessments, and exam readiness over the academic year, balancing board syllabus coverage with competitive-exam preparation and keeping both on a single teaching schedule.
\item Rewrote hard topics as step-by-step worked solutions, so students could follow the reasoning behind each step, retrace it during revision, and attempt unfamiliar exam problems on their own.
\end{bul}

\gap
\entry{Bharat Heavy Electricals Limited (BHEL), Electronics Division}{Bengaluru, India}{Industrial Trainee --- Manufacturing Operations}{May 2024 -- July 2024}
\begin{bul}
\item Raised on-floor delivery performance by 30\% during a 3-month trainee stint by timing each work step in time-motion studies, then rebalancing workload across stations on the manufacturing line.
\item Coordinated Engineering, PPC, Quality, and Material Management teams to keep production, inspection, and material flow aligned on the shop floor and streamline the hand-offs between them as work moved from planning to inspection.
\item Wrote a department-wide report covering SAP workflow integration, ISO 9001 audits, and defect-tracking systems, drawn from observations made while working with all four teams and shared across the department.
\end{bul}

\gap
\sect{PROJECTS}
\entry{Progressive Delivery Platform on EKS}{\href{https://github.com/amit-cloudops-ai/pdp-eks-gitops}{GitHub}}{Terraform, Karpenter, ArgoCD, Argo Rollouts}{September 2026}
\begin{bul}
\item Provisioned an EKS cluster with Terraform and used Karpenter to launch nodes in about 10 seconds, with ArgoCD syncing every Juice Shop manifest from Git and External Secrets pulling credentials from Secrets Manager.
\item Shipped releases as Argo Rollouts canary steps of 10\%, 50\%, and 100\% over Gateway API, then showed a deliberately broken image never received traffic and reverted on its own, with Grafana, Loki, and Slack alerts watching.
\end{bul}

\gap
\entry{Three-Tier Web Application on AWS}{\href{https://github.com/Amitpm8/Devops-3-tire-project-001}{GitHub}}{AWS VPC, EC2, RDS, Tomcat, Spring Boot}{June 2026}
\begin{bul}
\item Architected a VPC with 6 subnets across 2 Availability Zones, separating public, application, and database tiers, with 2 NAT Gateways for outbound traffic and 4 Security Groups limiting each tier to its upstream neighbor.
\item Deployed a Spring Boot login app behind Nginx and Tomcat with an RDS MySQL backend, then verified the full chain by registering a user, signing in, and confirming the session against the database.
\end{bul}

\gap
\entry{Zero-Downtime API Deployments on AWS}{\href{https://github.com/Amitpm8/aws-zero-downtime-deployment}{GitHub}}{AWS Lambda, API Gateway, CloudWatch}{March 2026}
\begin{bul}
\item Implemented Blue-Green and Canary strategies for a serverless API, shifting traffic through API Gateway in 10\% increments, and staged 12+ releases with zero incidents, keeping the old version live until the new one proved healthy.
\item Automated 4XX and 5XX error-rate detection with CloudWatch Alarms and SNS, sending alerts within 60 seconds of a threshold breach so a faulty release could be caught before it reached every user.
\end{bul}

\gap
\sect{TECHNICAL SKILLS}
\noindent{\bfseries Languages \& Scripting:} Python | Bash/Shell Scripting | YAML | SQL\par\vspace{2pt}
\noindent{\bfseries Cloud (AWS):} EC2 | S3 | VPC | IAM | Lambda | CloudFront | RDS | API Gateway | CloudWatch\par\vspace{2pt}
\noindent{\bfseries Containers \& Orchestration:} Docker | Kubernetes | Amazon EKS | CNI | CSI | NGINX Ingress | Gateway API | Karpenter\par\vspace{2pt}
\noindent{\bfseries CI/CD, GitOps \& IaC:} Git | GitHub Actions | ArgoCD | Terraform | AWS CloudFormation | Ansible\par\vspace{2pt}
\noindent{\bfseries Monitoring \& Observability:} Prometheus | Grafana | CloudWatch | OpenTelemetry | Loki\par\vspace{2pt}
\noindent{\bfseries OS \& Networking:} Linux (Ubuntu) | DNS | TCP/IP | Subnetting | Nginx
\end{document}
```