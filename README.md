# Claude OAuth Token Setup

This repository contains a script to configure your Claude OAuth token for use with Claude Code.

## Usage

```bash
bash setup_token.sh
```

Or with Python:

```bash
python3 setup_token.py
```

## What it does

- Prompts for your Claude OAuth token
- Stores it in `~/.claude/credentials.json`
- Verifies the token is valid
