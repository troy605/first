#!/usr/bin/env python3
import getpass
import json
import os
import stat

CREDENTIALS_DIR = os.path.expanduser("~/.claude")
CREDENTIALS_FILE = os.path.join(CREDENTIALS_DIR, "credentials.json")

os.makedirs(CREDENTIALS_DIR, mode=0o700, exist_ok=True)

token = getpass.getpass("Enter your Claude OAuth token: ").strip()
if not token:
    raise SystemExit("Error: token cannot be empty")

credentials = {"claudeAiOauth": {"accessToken": token}}

with open(CREDENTIALS_FILE, "w") as f:
    json.dump(credentials, f, indent=2)

os.chmod(CREDENTIALS_FILE, stat.S_IRUSR | stat.S_IWUSR)
print(f"Token saved to {CREDENTIALS_FILE}")
