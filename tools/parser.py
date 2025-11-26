#!/usr/bin/env python3
import re, os, sys, json
BASE = os.path.join(os.path.dirname(__file__), "..")
BROWSER_PATTERNS = [
    (r'Chrome/(\d+)', 'Chrome'),
    (r'Firefox/(\d+)', 'Firefox'),
    (r'OPR/(\d+)|Opera/(\d+)', 'Opera'),
    (r'Edg/(\d+)', 'Edge'),
    (r'Version/(\d+).*Safari', 'Safari'),
    (r'Safari/537', 'Safari'),
]
BOT_PATTERNS = [
    (r'Googlebot/(\d+\.\d+)', 'Googlebot'),
    (r'Bingbot/(\d+\.\d+)', 'Bingbot'),
    (r'YandexBot/(\d+\.\d+)', 'YandexBot'),
    (r'Baiduspider/(\d+\.\d+)', 'Baiduspider'),
    (r'facebookexternalhit/(\d+\.\d+)', 'FacebookExternalHit'),
]
APP_KEYWORDS = ['Instagram', 'TikTok', 'WhatsApp', 'Telegram', 'TwitterAndroid', 'Instagram']
def classify_ua(ua):
    lower = ua.lower()
    for pat, name in BOT_PATTERNS:
        m = re.search(pat, ua)
        if m: return {'category':'bot','name':name,'version':m.group(1) if m.groups() else None}
    for kw in APP_KEYWORDS:
        if kw.lower() in lower:
            ver = None
            m = re.search(r'%s[ /]?([0-9\.]+)' % re.escape(kw), ua)
            if m: ver = m.group(1)
            return {'category':'app','name':kw,'version':ver}
    for pat, name in BROWSER_PATTERNS:
        m = re.search(pat, ua)
        if m:
            ver = next((g for g in m.groups() if g), None)
            os_match = re.search(r'\(([^)]+)\)', ua)
            os_str = os_match.group(1) if os_match else ''
            device = None
            if 'android' in os_str.lower(): device = 'Android'
            elif 'iphone' in os_str.lower() or 'ipad' in os_str.lower(): device = 'iOS'
            return {'category':'browser','name':name,'version':ver,'os':os_str,'device':device}
    os_match = re.search(r'\(([^)]+)\)', ua)
    os_str = os_match.group(1) if os_match else ''
    return {'category':'unknown','name':None,'version':None,'os':os_str}
def parse_file(path):
    out = []
    with open(path) as fh:
        for line in fh:
            ua = line.strip()
            if not ua: continue
            out.append({'ua':ua, 'parsed': classify_ua(ua)})
    return out
def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/parser.py <path-to-ua-file-or-directory>"); sys.exit(2)
    path = sys.argv[1]
    results = []
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for f in files:
                if f.endswith('.txt'):
                    results.extend(parse_file(os.path.join(root, f)))
    else:
        results = parse_file(path)
    print(json.dumps(results, indent=2))
if __name__ == '__main__': main()
