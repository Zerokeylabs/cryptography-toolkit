# AES encryption/decryption CLI tool
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import argparse, os, time

BLOCK_SIZE = 16

def encrypt_file(key, infile, outfile):
    cipher = AES.new(key.encode(), AES.MODE_CBC)
    with open(infile, 'rb') as f:
        data = pad(f.read(), BLOCK_SIZE)
    start = time.time()
    ct = cipher.encrypt(data)
    with open(outfile, 'wb') as f:
        f.write(cipher.iv + ct)
    print("✅ Encrypted.")
    print(f"⏱ Time: {round(time.time() - start, 6)} sec")
    print(f"🔐 Saved to: {outfile}")

def decrypt_file(key, infile, outfile):
    with open(infile, 'rb') as f:
        iv = f.read(16)
        ct = f.read()
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    start = time.time()
    pt = unpad(cipher.decrypt(ct), BLOCK_SIZE)
    with open(outfile, 'wb') as f:
        f.write(pt)
    print("✅ Decrypted.")
    print(f"⏱ Time: {round(time.time() - start, 6)} sec")
    print(f"📄 Saved to: {outfile}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--encrypt", action="store_true")
    parser.add_argument("--decrypt", action="store_true")
    parser.add_argument("--key", required=True, help="16-byte key")
    parser.add_argument("--infile", required=True)
    parser.add_argument("--outfile", required=True)
    args = parser.parse_args()

    if args.encrypt:
        encrypt_file(args.key, args.infile, args.outfile)
    elif args.decrypt:
        decrypt_file(args.key, args.infile, args.outfile)
