---

# 5. Secrets_CLI/README.md

markdown
# Secrets_CLI - Secure Token Generator

This CLI tool generates cryptographically secure random tokens using Python's `secrets` module.

## Features
- Generate random tokens of customizable length.
- Include digits, letters, and symbols.
- Output tokens in plain text or JSON format.

## Usage

Generate a token (default 32 characters):

bash
python secrets_tool.py 


# Generate a 16 character token including symbols
python secrets_tool.py --length 16 --symbols


# Generate token output in JSON format
python secrets_tool.py --json


## ✅ Tool Tested Successfully
- Platform: Windows 11
- Python Version: 3.11
- Last Run: June 6, 2025
- Command Used: python secrets_tool.py --length 16 --symbols --json
- Status: ✅ Ran successfully with valid token output