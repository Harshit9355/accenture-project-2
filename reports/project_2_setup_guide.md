# Project 2 Setup Guide

Project 2 uses the Accenture Kali Linux VM and the local Ollama llama3:latest model.

```bash
cd ~/Project_2
source ~/Project_1/ai-lab/bin/activate
pip install -r requirements.txt
ollama list
```

Baseline:

```bash
export DEFENSE_ENABLED=0
python app.py
```

Defended service:

```bash
export DEFENSE_ENABLED=1
python app.py
```

The application runs at `http://localhost:5001` and accepts JSON POST requests at `/ask`.
