#!/usr/bin/env python3
"""Generate the README progress summary and circular SVG from progress.json."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
DATA=json.loads((ROOT/"progress.json").read_text(encoding="utf-8"))
README=ROOT/"README.md"; SVG=ROOT/"assets"/"preparation-progress.svg"
STAGES=["Not started","Learning","Lab completed","Documented","Interview tested","Interview ready"]
skills=DATA["skills"]
if not skills: raise SystemExit("progress.json must contain at least one skill")
invalid=[s for s in skills if s.get("status") not in STAGES]
if invalid: raise SystemExit("Unknown readiness status: "+", ".join(s.get("name",s.get("id","?")) for s in invalid))
points=sum(STAGES.index(s["status"]) for s in skills); maximum=len(skills)*5
percent=round(points/maximum*100) if maximum else 0
counts={stage:sum(1 for skill in skills if skill["status"]==stage) for stage in STAGES}
projects=DATA.get("projects",[])
done=sum(1 for project in projects for check in project.get("checklist",[]) if check.get("done"))
total=sum(len(project.get("checklist",[])) for project in projects)
r=99; circumference=2*math.pi*r; dash=circumference*percent/100
SVG.parent.mkdir(parents=True,exist_ok=True)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="260" height="260" viewBox="0 0 260 260" role="img" aria-labelledby="title desc">
<title id="title">Preparation readiness {percent}%</title><desc id="desc">{points} of {maximum} weighted competency points across {len(skills)} skills.</desc>
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#45d6ad"/><stop offset="1" stop-color="#91e6c8"/></linearGradient></defs>
<circle cx="130" cy="130" r="{r}" fill="#111b24" stroke="#263642" stroke-width="16"/>
<circle cx="130" cy="130" r="{r}" fill="none" stroke="url(#g)" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.1f} {circumference:.1f}" transform="rotate(-90 130 130)"/>
<text x="130" y="119" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="43" font-weight="750" fill="#f2f7f9">{percent}%</text>
<text x="130" y="148" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="13" letter-spacing="1.3" fill="#a8bbc6">READINESS</text>
<text x="130" y="174" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="11" fill="#8299a7">{points} / {maximum} points</text></svg>'''
SVG.write_text(svg,encoding="utf-8")
rows="\n".join(f"| {stage} | {counts[stage]} |" for stage in STAGES)
block=f'''<!-- PREP-PROGRESS:START -->
<p align="center">
  <img src="assets/preparation-progress.svg" alt="Cloud and DevOps preparation readiness: {percent}%" width="190">
</p>

<p align="center">
  <strong>{percent}% readiness progress</strong> · {points} of {maximum} weighted competency points · {len(skills)} tracked skills
</p>

| Readiness stage | Skills |
|---|---:|
{rows}

**Portfolio evidence:** {done} / {total} project evidence checks complete across {len(projects)} tracked projects.

Progress is calculated from the six readiness stages (0–5 points per skill). A skill only earns credit for its current evidence-backed stage. Update the root `progress.json`; GitHub Actions regenerates this README section and the circular graphic automatically.
<!-- PREP-PROGRESS:END -->'''
text=README.read_text(encoding="utf-8"); start="<!-- PREP-PROGRESS:START -->"; end="<!-- PREP-PROGRESS:END -->"
if start not in text or end not in text: raise SystemExit("README progress markers are missing")
before,rest=text.split(start,1); _,after=rest.split(end,1)
README.write_text(before+block+after,encoding="utf-8")
print(f"Updated README progress: {percent}% ({points}/{maximum})")
