# Project 2 - Prompt Injection Defense

This project extends the Project 1 lab with a separate `/ask` endpoint and a three-layer defense module.

## VM setup

```bash
cd ~/Project_2
source ~/Project_1/ai-lab/bin/activate
pip install -r requirements.txt
```

## Baseline without defense

```bash
export DEFENSE_ENABLED=0
python app.py
```

The service runs on `http://localhost:5001`.

## Defended service

Stop the service with Ctrl+C, then run:

```bash
export DEFENSE_ENABLED=1
python app.py
```

The five attack payloads should return HTTP 400. Ten normal queries should return HTTP 200 when Ollama responds.

## Evidence

Project 2 requires seven evidence screenshots: undefended startup, five undefended payload responses, `validate.py`, five defended 400 responses, Burp blocked request, Burp legitimate request, and the completed before/after table. Keep screenshots in `evidence/` and place them in one Word document before exporting `Project_2.pdf`.
