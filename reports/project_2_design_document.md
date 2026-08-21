# Project 2 Defense Design

## Layer 1 - Input length

`validate.py` rejects input over 500 characters with HTTP 400. This reduces resource-exhaustion risk.

## Layer 2 - Injection blocklist

`validate_input` detects direct injection phrases, role-play bypass language, and valid base64 payloads of 40 or more characters.

## Layer 3 - Output scanner

`scan_output` blocks system-prompt markers, credential patterns such as `password=`, `api_key=`, and `token=`, and unsolicited external URLs.

The defended endpoint is enabled with `DEFENSE_ENABLED=1`. Legitimate queries are tested separately to measure false positives.
