#!/usr/bin/env python3
"""Structural validator for JA21_JACORE_Suite_1.0.0."""
from pathlib import Path
import argparse, collections, csv, gzip, hashlib, json, re, sys

def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("root",nargs="?",default=str(Path(__file__).resolve().parents[1]))
    args=ap.parse_args()
    root=Path(args.root)
    failures=[]
    corpus=root/"corpus/technical/JA21_JACORE_TECHNICAL_CORPUS_10000.jsonl.gz"
    records=[]
    with gzip.open(corpus,"rt",encoding="utf-8") as f:
        records=[json.loads(x) for x in f if x.strip()]
    if len(records)!=10000: failures.append(f"corpus count {len(records)}")
    ids=[r["record_id"] for r in records]
    if len(set(ids))!=10000: failures.append("duplicate record IDs")
    if [r["sequence"] for r in records]!=list(range(1,10001)): failures.append("sequence mismatch")
    for r in records:
        if hashlib.sha256(r["source"].encode()).hexdigest()!=r["ast"]["origin_hash"]:
            failures.append(f"source hash {r['record_id']}")
            break
    scripts=list((root/"scripts").rglob("*.ja"))
    if len(scripts)!=1000: failures.append(f"script count {len(scripts)}")
    with open(root/"catalogs/SCRIPT_CATALOG.csv",encoding="utf-8",newline="") as f:
        rows=list(csv.DictReader(f))
    if len(rows)!=1000: failures.append(f"catalog count {len(rows)}")
    level_counts=collections.Counter(r["level"] for r in rows)
    if set(level_counts.values())!={100}: failures.append(f"level distribution {dict(level_counts)}")
    expected={"positive":400,"negative":150,"boundary":100,"integration":100,"security":75,
              "performance":50,"determinism":50,"interoperability":25,"recovery":25,"certification":25}
    if collections.Counter(r["validation_class"] for r in rows)!=collections.Counter(expected):
        failures.append("validation-class distribution")
    if len(set(r["feature"] for r in rows))!=31: failures.append("feature coverage")
    record_by_id={r["record_id"]:r for r in records}
    for row in rows:
        p=root/row["path"]
        if not p.exists(): failures.append(f"missing {row['path']}"); break
        text=p.read_text(encoding="utf-8").rstrip()
        source=record_by_id[row["record_id"]]["source"].rstrip()
        if text!=source: failures.append(f"source mismatch {row['record_id']}"); break
        if hashlib.sha256(source.encode()).hexdigest()!=row["source_sha256"]:
            failures.append(f"catalog hash {row['record_id']}"); break
        if "ja source" not in text or "module " not in text or "policy no_network" not in text:
            failures.append(f"required source declarations {row['record_id']}"); break
        if text.count("{")!=text.count("}"): failures.append(f"brace balance {row['record_id']}"); break
    tb=(root/"textbook/JA21_JA_CORE_APPLICATION_LANGUAGE_TEXTBOOK.md").read_text(encoding="utf-8")
    if len(re.findall(r"^# Chapter \d+ — ",tb,flags=re.M))!=22: failures.append("textbook chapter count")
    sums=root/"manifest/SHA256SUMS.txt"
    if sums.exists():
        for line in sums.read_text(encoding="utf-8").splitlines():
            if not line.strip(): continue
            digest,rel=line.split("  ",1)
            if sha(root/rel)!=digest:
                failures.append(f"manifest mismatch {rel}"); break
    maxlen=max(len(str(p.relative_to(root))) for p in root.rglob("*"))
    if maxlen>160: failures.append(f"path length {maxlen}")
    if failures:
        print("FAIL")
        for x in failures: print("-",x)
        return 1
    print("PASS")
    print("records=10000 scripts=1000 chapters=22 features=31 max_relative_path="+str(maxlen))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
