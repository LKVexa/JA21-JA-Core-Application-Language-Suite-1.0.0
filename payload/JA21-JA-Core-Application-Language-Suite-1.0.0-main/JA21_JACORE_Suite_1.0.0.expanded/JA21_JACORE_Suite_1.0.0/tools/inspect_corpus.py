#!/usr/bin/env python3
"""Inspect the JA Core technical corpus using only the Python standard library."""
import argparse, collections, gzip, json

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("corpus")
    ap.add_argument("--feature")
    ap.add_argument("--level")
    ap.add_argument("--validation-class")
    ap.add_argument("--limit",type=int,default=10)
    args=ap.parse_args()
    counts=collections.Counter()
    shown=0
    with gzip.open(args.corpus,"rt",encoding="utf-8") as f:
        for line in f:
            r=json.loads(line)
            counts[(r["level"],r["validation_class"],r["feature"])]+=1
            if args.feature and r["feature"]!=args.feature: continue
            if args.level and r["level"]!=args.level: continue
            if args.validation_class and r["validation_class"]!=args.validation_class: continue
            if shown<args.limit:
                print(json.dumps({
                    "record_id":r["record_id"],"level":r["level"],
                    "validation_class":r["validation_class"],"feature":r["feature"],
                    "expected_status":r["validation_result"]["expected_status"]
                },ensure_ascii=False))
                shown+=1
    print("records:",sum(counts.values()))
    print("features:",len({k[2] for k in counts}))
if __name__=="__main__":
    main()
