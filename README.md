
# Top User Agents — Comprehensive Repository

**Top User Agents** is a curated, well-structured, and developer-friendly repository containing a large collection of user-agent strings across browsers, mobile devices, bots/crawlers, and popular applications.

This repository is designed for:
- Web developers and QA engineers (testing user-agent parsing and feature detection)
- Security and analytics teams (filtering bots, traffic classification)
- Researchers and data scientists (sampling traffic patterns)
- DevOps/Infrastructure (server and CDN rules)

---

## Repository Highlights

- **~1,200+ synthetic sample user-agents** (split into categories) — suitable for testing and CI.
- **tools/** — utilities for generating, parsing, and validating lists.
- **api/** — a lightweight Flask API for quick access (local usage).
- **combined/** — aggregated files like `all-user-agents.txt` and `top-100.txt`.
- **Modular structure** so you can add categories, scripts and CI checks easily.

---

## Quickstart

### 1) Browse files
Open `combined/all-user-agents.txt` — it contains the aggregated set.

### 2) Generate random user-agent(s)
```
python tools/generator.py --random --count 5
python tools/generator.py --count 10 --category mobile
python tools/generator.py --sample-file combined/top-100.txt --count 10
```

### 3) Parse a file (JSON output)
```
python tools/parser.py combined/top-100.txt > parsed.json
```

### 4) Validate a file
```
python tools/validator.py combined/top-100.txt
python tools/validator.py combined/all-user-agents.txt --fix-duplicates
```

### 5) Run the API (optional)
```
pip install flask
python api/api.py
# then visit http://127.0.0.1:5000/random?count=3
```

---

## How to add your own list
1. Add a plain `.txt` file to the appropriate `data/<category>/` folder.
2. Ensure one UA per line.
3. Optional: run `python tools/validator.py` to clean duplicates and errors.

---

## Contributing
Contributions are welcome. Please:
- Keep files plain text.
- Add new categories as folders under `data/`.
- Send pull requests for additions — include source or evidence for unusual UA strings.

---

## License
MIT License — see `LICENSE` (add if needed).

