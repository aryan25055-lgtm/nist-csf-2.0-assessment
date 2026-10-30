"""
NIST Cybersecurity Framework 2.0 Assessment Tool
Educational project: interactive organizational assessment and ransomware scenario.
Uses only the Python standard library.
"""
from datetime import datetime
from pathlib import Path
import json
import csv

FUNCTIONS = {
    "GV": {"name": "Govern", "purpose": "Establish cybersecurity strategy, policies, roles, and oversight.", "controls": [
        ("GV-01", "Written cybersecurity policy is approved and reviewed."),
        ("GV-02", "Cybersecurity roles and responsibilities are assigned."),
        ("GV-03", "Cybersecurity risks are included in enterprise risk management."),
        ("GV-04", "Third-party and supplier cybersecurity risks are assessed."]},
    "ID": {"name": "Identify", "purpose": "Understand assets, data, business context, and cybersecurity risks.", "controls": [
        ("ID-01", "Hardware, software, and cloud assets are inventoried."),
        ("ID-02", "Sensitive data and critical business services are identified."),
        ("ID-03", "Threats and vulnerabilities are assessed periodically."),
        ("ID-04", "Security risks are prioritized by business impact."]},
    "PR": {"name": "Protect", "purpose": "Implement safeguards to reduce cybersecurity risk.", "controls": [
        ("PR-01", "Multi-factor authentication is enabled for important accounts."),
        ("PR-02", "Access follows least-privilege principles."),
        ("PR-03", "Sensitive information is encrypted where appropriate."),
        ("PR-04", "Employees receive phishing and security awareness training."),
        ("PR-05", "Backups are maintained and tested."),
        ("PR-06", "Endpoints and systems are securely configured and patched."]},
    "DE": {"name": "Detect", "purpose": "Find and analyze possible cybersecurity attacks and anomalies.", "controls": [
        ("DE-01", "Important systems generate and retain security logs."),
        ("DE-02", "Endpoints and networks are monitored for suspicious activity."),
        ("DE-03", "Alerts are reviewed and escalated promptly."),
        ("DE-04", "Detection processes are tested and improved."]},
    "RS": {"name": "Respond", "purpose": "Take action after a cybersecurity incident is detected.", "controls": [
        ("RS-01", "A documented incident response plan exists."),
        ("RS-02", "The organization can isolate affected devices and accounts."),
        ("RS-03", "Incidents are analyzed and evidence is preserved."),
        ("RS-04", "Relevant stakeholders are notified through defined procedures."]},
    "RC": {"name": "Recover", "purpose": "Restore affected services and improve resilience after incidents.", "controls": [
        ("RC-01", "Recovery priorities and responsibilities are defined."),
        ("RC-02", "Backups can be restored and checked for integrity."),
        ("RC-03", "Recovery progress is communicated to stakeholders."),
        ("RC-04", "Lessons learned are used to improve security controls."]},
}
LEVELS = {0:"Not Implemented", 1:"Initial", 2:"Developing", 3:"Established", 4:"Optimized"}
RECOMMENDATIONS = {
    "GV":"Approve security policies, assign owners, and review supplier risks.",
    "ID":"Create an asset inventory, classify data, and perform risk assessments.",
    "PR":"Enable MFA, least privilege, patching, employee training, and tested backups.",
    "DE":"Centralize logs, monitor endpoints, and establish alert escalation procedures.",
    "RS":"Document an incident response plan and practice containment exercises.",
    "RC":"Test restoration, define recovery priorities, and record lessons learned.",
}

def pause():
    input("\nPress Enter to continue...")

def score_function(data, code):
    ids = [cid for cid, _ in FUNCTIONS[code]["controls"]]
    vals = [data.get("ratings", {}).get(cid, 0) for cid in ids]
    return sum(vals) / len(vals)

def overall_score(data):
    vals = list(data.get("ratings", {}).values())
    return sum(vals) / len(vals) if vals else 0

def status(score):
    if score < 1: return "Critical gap"
    if score < 2: return "High improvement need"
    if score < 3: return "Moderate improvement need"
    if score < 4: return "Good"
    return "Optimized"

def framework_map():
    print("\nNIST CSF 2.0 FRAMEWORK MAP")
    print("=" * 66)
    print("                    GOVERN (GV)")
    print("                       |")
    print("       +---------------+---------------+")
    print("       |               |               |")
    print("   IDENTIFY (ID)  PROTECT (PR)    DETECT (DE)")
    print("       |               |               |")
    print("       +---------------+---------------+")
    print("                       |")
    print("                 RESPOND (RS)")
    print("                       |")
    print("                 RECOVER (RC)")
    print("\nAll six functions work together continuously; the map is a simplified")
    print("learning view, not a mandatory linear sequence.")
    for code, f in FUNCTIONS.items():
        print(f"\n{code} - {f['name']}: {f['purpose']}")

def create_assessment():
    print("\nCREATE ORGANIZATIONAL ASSESSMENT")
    org = input("Organization name [SecureMart Technologies]: ").strip() or "SecureMart Technologies"
    data = {"organization": org, "created_at": datetime.now().isoformat(timespec="seconds"),
            "framework":"NIST Cybersecurity Framework 2.0", "ratings":{}, "notes":{}}
    for code, f in FUNCTIONS.items():
        print(f"\n{f['name'].upper()} ({code}) — {f['purpose']}")
        for cid, desc in f["controls"]:
            while True:
                raw = input(f"{cid}: {desc}\nRating 0-4 (0=Not implemented, 4=Optimized): ").strip()
                if raw in {"0","1","2","3","4"}:
                    data["ratings"][cid] = int(raw)
                    break
                print("Enter a number from 0 to 4.")
        data["notes"][code] = input(f"Notes for {f['name']} (optional): ").strip()
    return data

def dashboard(data):
    print("\nASSESSMENT DASHBOARD")
    print("=" * 66)
    print("Organization:", data["organization"])
    print("Assessment date:", data.get("created_at", "Unknown"))
    s = overall_score(data)
    print(f"Overall score: {s:.2f}/4.00 — {status(s)}")
    for code, f in FUNCTIONS.items():
        v = score_function(data, code)
        print(f"{f['name']:<10} {v:.2f}/4 — {status(v)}")

def recommendations(data):
    print("\nPRIORITIZED IMPROVEMENT PLAN")
    print("=" * 66)
    ranked = sorted((score_function(data,c),c) for c in FUNCTIONS)
    for i,(v,c) in enumerate(ranked,1):
        print(f"{i}. {FUNCTIONS[c]['name']} ({v:.2f}/4)")
        print("   Recommendation:", RECOMMENDATIONS[c])
        weak = [(cid,desc,data.get("ratings",{}).get(cid,0))
                for cid,desc in FUNCTIONS[c]["controls"]
                if data.get("ratings",{}).get(cid,0) < 3]
        for cid,desc,rating in weak:
            print(f"   - {cid} [{rating}/4]: {desc}")

def ransomware_scenario():
    print("\nTABLETOP SCENARIO: RANSOMWARE AT SECUREMART")
    print("=" * 66)
    print("A fictional e-commerce employee opens a malicious attachment. Ransomware")
    print("runs on the workstation and attempts to encrypt shared files.")
    actions = [
        ("GOVERN","Activate assigned incident roles and follow approved policy."),
        ("IDENTIFY","Determine affected devices, accounts, data, and business services."),
        ("PROTECT","Apply MFA, least privilege, endpoint safeguards, and tested backups."),
        ("DETECT","Review endpoint alerts, authentication logs, and unusual file activity."),
        ("RESPOND","Isolate affected devices, disable compromised accounts, preserve evidence, and notify stakeholders."),
        ("RECOVER","Restore clean systems and data from verified backups; validate before reconnecting."),
    ]
    for name,action in actions: print(f"\n{name}: {action}")
    print("\nSafe response checklist:")
    for item in [
        "Disconnect affected systems using approved procedures.",
        "Preserve logs and evidence; do not destroy relevant artifacts.",
        "Contact the incident response and IT teams.",
        "Determine the scope of affected devices, accounts, and information.",
        "Restore only from verified clean backups after containment.",
        "Review lessons learned and improve controls.",
    ]: print("[ ]",item)
    print("\nThis is a tabletop learning scenario, not instructions to deploy malware.")

def export_report(data, path):
    out = ["NIST CYBERSECURITY FRAMEWORK 2.0 ASSESSMENT REPORT","="*60,
           f"Organization: {data['organization']}",f"Assessment date: {data.get('created_at')}",
           f"Overall score: {overall_score(data):.2f}/4.00",f"Overall status: {status(overall_score(data))}","",
           "FUNCTION SUMMARY","-"*60]
    for code,f in FUNCTIONS.items():
        v = score_function(data,code)
        out += [f"{f['name']} ({code}): {v:.2f}/4 — {status(v)}",f"Purpose: {f['purpose']}",
                f"Notes: {data.get('notes',{}).get(code,'')}","Controls:"]
        for cid,desc in f["controls"]:
            rating=data.get("ratings",{}).get(cid,0)
            out.append(f"  {cid}: {desc} | {rating}/4 — {LEVELS[rating]}")
        out.append("")
    out += ["PRIORITIZED RECOMMENDATIONS","-"*60]
    for v,c in sorted((score_function(data,c),c) for c in FUNCTIONS):
        out.append(f"{FUNCTIONS[c]['name']} ({v:.2f}/4): {RECOMMENDATIONS[c]}")
    out += ["","LIMITATIONS","This educational self-assessment is not a formal NIST assessment, audit,",
            "certification, or guarantee of security.","","REFERENCE",
            "NIST, The NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 (2024).",
            "https://doi.org/10.6028/NIST.CSWP.29"]
    path.write_text("\n".join(out),encoding="utf-8")
    print("Report exported:",path)

def export_csv(data,path):
    with path.open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f)
        w.writerow(["Function","Code","Control ID","Control Description","Rating","Rating Meaning"])
        for code,func in FUNCTIONS.items():
            for cid,desc in func["controls"]:
                rating=data.get("ratings",{}).get(cid,0)
                w.writerow([func["name"],code,cid,desc,rating,LEVELS[rating]])
    print("CSV exported:",path)

def main():
    base=Path(__file__).resolve().parent
    json_path=base/"assessment_data.json"
    data=None
    if json_path.exists():
        try: data=json.loads(json_path.read_text(encoding="utf-8"))
        except (OSError,json.JSONDecodeError): print("Saved assessment could not be loaded.")
    while True:
        print("\n"+"="*66)
        print(" NIST CYBERSECURITY FRAMEWORK 2.0 ASSESSMENT TOOL")
        print("="*66)
        print("1. View framework map\n2. Create new assessment\n3. View dashboard")
        print("4. View prioritized recommendations\n5. Explore ransomware scenario")
        print("6. Export report (.txt)\n7. Export control ratings (.csv)\n8. Save assessment\n0. Exit")
        choice=input("\nChoose an option: ").strip()
        if choice=="1": framework_map(); pause()
        elif choice=="2":
            data=create_assessment()
            json_path.write_text(json.dumps(data,indent=2),encoding="utf-8")
            print("Assessment saved:",json_path); pause()
        elif choice=="3":
            if data: dashboard(data)
            else: print("Create an assessment first.")
            pause()
        elif choice=="4":
            if data: recommendations(data)
            else: print("Create an assessment first.")
            pause()
        elif choice=="5": ransomware_scenario(); pause()
        elif choice=="6":
            if data: export_report(data,base/"NIST_CSF_Assessment_Report.txt")
            else: print("Create an assessment first.")
            pause()
        elif choice=="7":
            if data: export_csv(data,base/"NIST_CSF_Control_Ratings.csv")
            else: print("Create an assessment first.")
            pause()
        elif choice=="8":
            if data:
                json_path.write_text(json.dumps(data,indent=2),encoding="utf-8")
                print("Assessment saved:",json_path)
            else: print("No assessment to save.")
            pause()
        elif choice=="0":
            if data: json_path.write_text(json.dumps(data,indent=2),encoding="utf-8")
            print("Thank you for using the NIST CSF 2.0 Assessment Tool."); break
        else: print("Invalid choice. Select 0–8.")

if __name__=="__main__": main()
