"""Check English artifact integrity, separately from historical evaluation verdicts."""
from pathlib import Path
import hashlib
import json
import re
import sys
import zipfile

root = Path(__file__).resolve().parent
out = root / (sys.argv[1] if len(sys.argv) > 1 else "outputs")
manifest = json.loads((root / "skill-manifest.json").read_text(encoding="utf-8-sig"))
snapshot = zipfile.ZipFile(root / "tested-skill.zip")
skill = zipfile.Path(snapshot, "linear-handbook/")
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
checks = []

checks.append({"name": "localized_fixed_input_unchanged", "passed": sha(root / "inputs/requests.md") == "c2501c7dee17a04274ad5a9e6322d377542336cdc93af613acf2b8b3cfd9d16f"})
checks.append({"name": "localized_expected_unchanged", "passed": sha(root / "expected.md") == "265df982e86d327b5cf3d75f2e88c7759707bd55ced225131777d295b38308af"})
checks.append({"name": "skill_matches_tested_manifest", "passed": all(sha(skill / x["path"].removeprefix("linear-handbook/")) == x["sha256"] for x in manifest)})
for case in (f"C{i:02}" for i in range(1, 7)):
    route = json.loads((out / case / "route.json").read_text(encoding="utf-8"))
    ops = json.loads((out / case / "operations.json").read_text(encoding="utf-8"))
    checks.append({"name": f"{case}_routes_resolve", "passed": all((skill / item["path"]).is_file() for item in route["paths"])})
    checks.append({"name": f"{case}_operations_preserved", "passed": bool(ops["operations"]) and ops["simulationOnly"]})

c01 = json.loads((out / "C01/workspace.json").read_text(encoding="utf-8"))
checks.append({"name": "C01_existing_team_and_human_assignee", "passed": all(x["teamId"] == "team-pocket" and x["assigneeId"] == "user-owner" for x in c01["issues"])})
c05 = json.loads((out / "C05/workspace.json").read_text(encoding="utf-8"))
checks.append({"name": "C05_reopened_for_repair", "passed": c05["issue"]["statusId"] == "exp-implement"})
c06dir = out / "C06"
document = (c06dir / "docs/export-spec.md").read_text(encoding="utf-8")
examples = [json.loads(x) for x in re.findall(r"```json\s*([\s\S]*?)```", document)]
calculated = [{k: x[k] for k in ("date", "amount", "category")} for x in sorted(examples[0], key=lambda x: (x["date"], x["id"]))]
checks.append({"name": "C06_example_sort_and_projection", "passed": calculated == examples[1]})
verification = json.loads((c06dir / "verification.json").read_text(encoding="utf-8"))
checks.append({"name": "C06_localized_document_hash", "passed": sha(c06dir / "docs/export-spec.md") == verification["localization"]["sha256"]})
state = json.loads((c06dir / "workspace.json").read_text(encoding="utf-8"))
body = (c06dir / "PAY-16.md").read_text(encoding="utf-8")
checks.append({"name": "C06_body_model_and_file_version", "passed": state["issue"]["body"] == body and sha(c06dir / "docs/export-spec.md") in body})
json_files = list(out.rglob("*.json"))
for path in json_files:
    json.loads(path.read_text(encoding="utf-8"))
for path in out.rglob("readback.json"):
    readback = json.loads(path.read_text(encoding="utf-8"))
    checks.append({"name": f"{path.parent.name}_localized_readback_hashes", "passed": all(sha(path.parent / item["file"]) == item["localizedSha256"] for item in readback["files"])})
print(json.dumps({"scope": "English artifact integrity; historical verdicts remain in artifact-check*.json and the Chinese archive.", "checks": checks, "json_files_parsed": len(json_files), "passed": all(x["passed"] for x in checks)}, ensure_ascii=False, indent=2))
raise SystemExit(0 if all(x["passed"] for x in checks) else 1)
