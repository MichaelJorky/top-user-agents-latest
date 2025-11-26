#!/usr/bin/env python3
import os, sys, re, argparse
def load_lines(path):
    lines = []
    with open(path) as fh:
        for l in fh:
            s = l.strip()
            if s: lines.append(s)
    return lines
def validate_list(lines):
    problems = []
    seen = {}
    for i, l in enumerate(lines, 1):
        if l in seen: problems.append(('duplicate', i, l))
        else: seen[l] = i
        if len(l) < 20: problems.append(('too_short', i, l))
        if len(l) > 1000: problems.append(('too_long', i, l))
        if re.search(r'[\\x00-\\x08\\x0B\\x0C\\x0E-\\x1F]', l): problems.append(('control_chars', i, l))
    return problems
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", help="Path to .txt file containing UAs")
    ap.add_argument("--fix-duplicates", action="store_true", help="Write a cleaned file without duplicates")
    args = ap.parse_args()
    if not os.path.exists(args.file): print("File not found", file=sys.stderr); sys.exit(2)
    lines = load_lines(args.file)
    probs = validate_list(lines)
    if not probs: print("No problems found. Total UAs: %d" % len(lines))
    else:
        print("Problems found:")
        for typ, line_no, ua in probs:
            print(f"{typ} on line {line_no}: {ua[:80]}...")
    if args.fix_duplicates:
        out = []
        seen = set()
        for l in lines:
            if l not in seen:
                out.append(l); seen.add(l)
        out_path = args.file + ".nodup"
        with open(out_path, "w") as fh:
            fh.write("\\n".join(out))
        print("Wrote cleaned file to", out_path)
if __name__ == '__main__': main()
