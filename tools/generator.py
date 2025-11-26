#!/usr/bin/env python3
"""generator.py - in tools/""" 
import argparse, random, os, sys
BASE = os.path.join(os.path.dirname(__file__), "..")
def load_uas(base_path=None, category=None):
    base_path = base_path or os.path.join(BASE, "data")
    uas = []
    search_path = os.path.join(base_path, category) if category else base_path
    for root, _, files in os.walk(search_path):
        for f in files:
            if f.endswith(".txt"):
                with open(os.path.join(root, f)) as fh:
                    uas.extend([x.strip() for x in fh if x.strip()])
    return uas
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--random", action="store_true")
    ap.add_argument("--count", type=int, default=1)
    ap.add_argument("--category", type=str)
    ap.add_argument("--sample-file", type=str)
    args = ap.parse_args()
    if args.sample_file:
        path = os.path.join(BASE, args.sample_file)
        if not os.path.exists(path): print(f"Sample file not found: {path}", file=sys.stderr); sys.exit(2)
        with open(path) as fh:
            lines = [x.strip() for x in fh if x.strip()]
        for l in lines[:args.count]:
            print(l)
        return
    uas = load_uas(category=args.category)
    if not uas:
        print("No user agents found", file=sys.stderr); sys.exit(2)
    if args.random:
        for _ in range(args.count): print(random.choice(uas))
    else:
        for ua in uas[:args.count]: print(ua)
if __name__ == '__main__': main()
