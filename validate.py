import base64
import re

MAX_LENGTH = 500
INJECTION_PATTERNS = [
    re.compile(r"ignore\s+(all\s+)?previous\s+instructions", re.I),
    re.compile(r"you\s+are\s+now", re.I),
    re.compile(r"pretend\s+you\s+are", re.I),
    re.compile(r"act\s+as\s+if\s+you\s+have\s+no", re.I),
]
CREDENTIAL_PATTERNS = [
    re.compile(r"password\s*=", re.I),
    re.compile(r"api[_-]?key\s*=", re.I),
    re.compile(r"token\s*=", re.I),
]
URL_PATTERN = re.compile(r"https?://\S+", re.I)
SYSTEM_PROMPT_MARKERS = ("system prompt", "system instructions", "internal configuration")


def validate_input(value):
    if len(value) > MAX_LENGTH:
        return False, f"Input exceeds the {MAX_LENGTH}-character limit."
    for pattern in INJECTION_PATTERNS:
        if pattern.search(value):
            return False, "Prompt-injection phrase detected."
    compact = re.sub(r"\s+", "", value)
    if len(compact) >= 40:
        try:
            decoded = base64.b64decode(compact, validate=True).decode("utf-8", errors="ignore")
        except (ValueError, UnicodeDecodeError):
            decoded = ""
        if decoded:
            return False, "Encoded payload detected."
    return True, "Input accepted."


def scan_output(value):
    lowered = value.lower()
    if any(marker in lowered for marker in SYSTEM_PROMPT_MARKERS):
        return False, "System-prompt content detected."
    for pattern in CREDENTIAL_PATTERNS:
        if pattern.search(value):
            return False, "Credential-pattern content detected."
    if URL_PATTERN.search(value):
        return False, "Unsolicited external URL detected."
    return True, "Output accepted."
