#!/usr/bin/env bash
set -euo pipefail

CREDENTIALS_DIR="$HOME/.claude"
CREDENTIALS_FILE="$CREDENTIALS_DIR/credentials.json"

mkdir -p "$CREDENTIALS_DIR"
chmod 700 "$CREDENTIALS_DIR"

read -rsp "Enter your Claude OAuth token: " TOKEN
echo

if [[ -z "$TOKEN" ]]; then
  echo "Error: token cannot be empty" >&2
  exit 1
fi

cat > "$CREDENTIALS_FILE" <<EOF
{
  "claudeAiOauth": {
    "accessToken": "$TOKEN"
  }
}
EOF

chmod 600 "$CREDENTIALS_FILE"
echo "Token saved to $CREDENTIALS_FILE"
