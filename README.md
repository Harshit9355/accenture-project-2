# Project 2 - Prompt Injection Defense

## Overview

Project 2 extends the AI security lab with a Flask `/ask` endpoint protected against common prompt-injection and unsafe-output scenarios.

The project demonstrates a layered defense approach:

1. Input length validation
2. Prompt-injection and encoded-payload detection
3. Model-output scanning for sensitive or unsafe content

The application also tests legitimate security-related queries to verify that the defenses do not unnecessarily block normal use.

## Objectives

- Detect common prompt-injection attempts.
- Demonstrate application behavior before and after defense.
- Validate incoming user input before processing.
- Detect encoded/Base64 payloads.
- Limit excessive input length.
- Scan generated output for sensitive content.
- Verify legitimate security-related queries remain accepted.
- Test HTTP behavior using Burp Suite.
- Maintain reproducible evidence and test results.

## Project Structure

```text
Project_2/
├── app.py
├── validate.py
├── requirements.txt
├── README.md
├── evidence/
│   ├── P2_01_Undefended_Baseline.png
│   ├── P2_02_Five_Payloads_Without_Defense.png
│   ├── P2_03_Validate_Py_Rules.png
│   ├── P2_04_Five_Payloads_With_Defense.png
│   ├── P2_05_Burp_Malicious_400.png
│   └── P2_06_Legitimate_Query_Response.png
├── reports/
│   ├── project_2_design_document.md
│   └── project_2_setup_guide.md
├── results/
│   ├── before_after_results.csv
│   └── legitimate_queries.csv
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## Technologies

- Python
- Flask
- Requests
- Ollama
- llama3:latest
- Burp Suite
- HTML/CSS

## Application

The Flask application exposes the following endpoint:

```text
POST /ask
```

The application runs on:

```text
http://127.0.0.1:5001
```

The endpoint accepts JSON input containing a user message.

## Defense Architecture

### Layer 1 - Input Length Validation

The application limits input to 500 characters.

Inputs exceeding the configured limit are rejected before they reach the model.

### Layer 2 - Input Validation

The application checks incoming messages for common prompt-injection patterns, including:

- Ignore previous instructions
- You are now
- Pretend you are
- Act as if you have no

The application also detects Base64-encoded payloads.

Blocked requests return HTTP 400.

### Layer 3 - Output Scanning

Generated output is checked for:

- System-prompt disclosure
- System-instruction disclosure
- Internal configuration disclosure
- Credential-like patterns
- Unsolicited external URLs

Unsafe output is rejected instead of being returned to the user.

## Test Results

Five attack categories were tested:

1. Direct injection
2. Role-play bypass
3. Indirect injection
4. Multi-turn escalation
5. Encoded payload

The completed results are stored in:

```text
results/before_after_results.csv
```

All five tested attack categories were recorded as blocked with the defense enabled.

Legitimate security-related queries were tested separately and recorded in:

```text
results/legitimate_queries.csv
```

The legitimate query tests returned HTTP 200 and were not blocked.

## Evidence

The `evidence/` directory contains screenshots demonstrating:

- Undefended baseline behavior
- Five payload tests without defense
- Validation rules
- Five payload tests with defense
- Burp Suite malicious request returning HTTP 400
- Burp Suite legitimate query response

The before/after test results and legitimate-query results are maintained in the `results/` directory.

## Documentation

Additional project documentation is available in:

```text
reports/project_2_design_document.md
reports/project_2_setup_guide.md
```

## Conclusion

Project 2 demonstrates a layered prompt-injection defense for a Flask-based AI application.

The implementation validates user input before model processing, detects direct and encoded attack patterns, scans generated output for sensitive content, and verifies that legitimate security-related questions continue to be accepted.