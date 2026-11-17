#!/usr/bin/env python3
"""Regenerate the README progress summary and composite section/topic ring map."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
DATA=json.loads((ROOT/"progress.json").read_text(encoding="utf-8"))
README=ROOT/"README.md"; SVG=ROOT/"assets"/"handbook-progress.svg"
STAGES=DATA["statuses"]; skills=DATA["skills"]; items=DATA["detailed_competencies"]
if any(x["status"] not in STAGES+["Not assessed"] for x in items): raise SystemExit("Invalid granular status")
legacy_points=sum(STAGES.index(x["status"]) for x in skills); legacy_max=len(skills)*5
legacy_pct=round(legacy_points/legacy_max*100) if legacy_max else 0
def stats(rows):
    assessed=[x for x in rows if x["status"]!="Not assessed"]; maximum=len(assessed)*5
    return (round(sum(STAGES.index(x["status"]) for x in assessed)/maximum*100) if maximum else None,len(assessed),len(rows))
def ring(cx,cy,pct,label):
    r=23; c=2*math.pi*r; dash=c*(pct or 0)/100; shown="—" if pct is None else str(pct)+"%"
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#111b24" stroke="#344653" stroke-width="6"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#45d6ad" stroke-width="6" stroke-linecap="round" stroke-dasharray="{dash:.2f} {c:.2f}" transform="rotate(-90 {cx} {cy})"/><text x="{cx}" y="{cy+4}" text-anchor="middle" font-family="Arial" font-size="11" fill="#f2f7f9">{shown}</text>'
def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
entries=[]
for sec in DATA["structure"]:
    sr=[x for x in items if x["section_id"]==sec["id"]]
    entries.append(("SECTION",sec["name"],stats(sr)))
    for top in sec["topics"]:
        tr=[x for x in sr if x["topic_id"]==top["id"]]
        entries.append(("TOPIC","  "+top["name"],stats(tr)))
width=1000; row_h=58; height=70+len(entries)*row_h
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="'+str(height)+'" viewBox="0 0 1000 '+str(height)+'">','<rect width="100%" height="100%" rx="18" fill="#0d1720"/>','<text x="28" y="38" fill="#f2f7f9" font-family="Arial" font-size="20" font-weight="700">Handbook progress by section and topic</text>']
for idx,(kind,name,(pct,assessed,total)) in enumerate(entries):
    y=70+idx*row_h
    svg.append(ring(52,y+18,pct,name))
    svg.append(f'<text x="100" y="{y+16}" fill="#f2f7f9" font-family="Arial" font-size="{14 if kind=="SECTION" else 13}" font-weight="{700 if kind=="SECTION" else 400}">{esc(name)}</text>')
    svg.append(f'<text x="100" y="{y+36}" fill="#9fb3c0" font-family="Arial" font-size="11">{assessed} assessed / {total} checklist items</text>')
    svg.append(f'<line x1="28" y1="{y+49}" x2="972" y2="{y+49}" stroke="#263642"/>')
svg.append("</svg>"); SVG.parent.mkdir(parents=True,exist_ok=True); SVG.write_text("\n".join(svg),encoding="utf-8")
counts={s:sum(x["status"]==s for x in skills) for s in STAGES}
projects=DATA.get("projects",[]); pd=sum(bool(c.get("done")) for p in projects for c in p.get("checklist",[])); pt=sum(len(p.get("checklist",[])) for p in projects)
L=["<!-- PREP-PROGRESS:START -->",'<p align="center">','<img src="assets/preparation-progress.svg" width="145" alt="Overall baseline progress">','</p>',f'<p align="center"><strong>{legacy_pct}% overall baseline</strong> · {legacy_points}/{legacy_max} weighted points · {len(skills)} original broad competencies</p>',
"","### Preserved baseline","","| Readiness stage | Broad competencies |","|---|---:|"]+[f"| {s} | {counts[s]} |" for s in STAGES]
L += ["",f"**Project evidence:** {pd}/{pt} checks complete across {len(projects)} projects.","","### Detailed handbook map","","Every handbook section and topic has its own circular progress ring in the map below. Each individual checklist item has a separate readiness status. All newly split items begin as **Not assessed**; this is different from Not started. The original 9% baseline is preserved.",
L += ["", '<img src="assets/handbook-progress.svg" alt="Circular progress rings for each handbook section and topic" width="100%">', "", "<details>", "<summary>Expand topic breakdowns and every individual competency</summary>", ""]
for sec in DATA["structure"]:
    sr=[x for x in items if x["section_id"]==sec["id"]]
    L += ["#### "+sec["name"],"","| Topic | Progress | Assessed / total |","|---|---:|---:|"]
    for top in sec["topics"]:
        tr=[x for x in sr if x["topic_id"]==top["id"]]; pct,assessed,total=stats(tr); label="Not assessed" if pct is None else str(pct)+"%"
        L.append("| **{}** | {} | {}/{} |".format(top["name"], label, assessed, total))
        for item in tr: L.append("| ↳ {} | {} | — |".format(item["name"], item["status"]))
    L.append("")
L += ["</details>","","**Scoring:** Each assessed item receives 0–5 points across the six readiness stages. Topic and section percentages are weighted averages of assessed child items. Unassessed items are excluded until evaluated and never counted as completed.",
"","Edit progress.json to update any individual status or project evidence check. GitHub Actions regenerates the README map and SVG on push.","<!-- PREP-PROGRESS:END -->"]
text=README.read_text(encoding="utf-8"); start="<!-- PREP-PROGRESS:START -->"; end="<!-- PREP-PROGRESS:END -->"
before,rest=text.split(start,1); _,after=rest.split(end,1); README.write_text(before+"\n".join(L)+after,encoding="utf-8")
print("Granular handbook progress regenerated.")
