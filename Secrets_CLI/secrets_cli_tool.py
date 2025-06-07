import argparse
import secrets
import string
import time
import json

def generate_token(length=16, symbols=False, json_output=False):
    alphabet = string.ascii_letters + string.digits
    if symbols:
        alphabet += string.punctuation

    start = time.time()
    token = ''.join(secrets.choice(alphabet) for _ in range(length))
    elapsed = round(time.time() - start, 6)

    if json_output:
        result = {
            "token": token,
            "length": length,
            "symbols_included": symbols,
            "time_seconds": elapsed
        }
        print(json.dumps(result, indent=2))
    else:
        print(f"✅ Token: {token}")
        print(f"🔢 Length: {length}")
        print(f"🔐 Symbols included: {symbols}")
        print(f"⏱ Time: {elapsed} sec")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, default=16, help="Length of token (default 16)")
    parser.add_argument("--symbols", action="store_true", help="Include symbols")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    args = parser.parse_args()

    generate_token(length=args.length, symbols=args.symbols, json_output=args.json)
