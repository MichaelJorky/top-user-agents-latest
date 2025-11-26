#!/usr/bin/env python3
from flask import Flask, request, jsonify
import os, random
BASE = os.path.join(os.path.dirname(__file__), "..")
DATA_PATH = os.path.join(BASE, "combined", "all-user-agents.txt")
app = Flask(__name__)
def load_all():
    with open(DATA_PATH) as fh:
        return [x.strip() for x in fh if x.strip()]
@app.route("/random")
def random_ua():
    count = int(request.args.get("count", "1"))
    uas = load_all()
    return jsonify(random.sample(uas, min(count, len(uas))))
@app.route("/search")
def search():
    q = request.args.get("q", "").lower()
    if not q: return jsonify([])
    uas = load_all()
    results = [u for u in uas if q in u.lower()]
    return jsonify(results[:200])
@app.route("/count")
def count():
    uas = load_all()
    return jsonify({"count": len(uas)})
@app.route("/category/<name>")
def category(name):
    uas = load_all()
    name = name.lower()
    results = []
    for u in uas:
        if name == "bots" and ("bot" in u.lower() or "spider" in u.lower()):
            results.append(u)
        if name == "mobile" and ("android" in u.lower() or "mobile" in u.lower() or "iphone" in u.lower()):
            results.append(u)
        if name == "browsers" and ("mozilla" in u.lower() and "applewebkit" in u.lower()):
            results.append(u)
        if name == "apps" and any(k in u.lower() for k in ["instagram","tiktok","whatsapp","telegram","twitter"]):
            results.append(u)
    return jsonify(results[:500])
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
