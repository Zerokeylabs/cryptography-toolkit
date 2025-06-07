# RSA keygen/encrypt/decrypt CLI
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import argparse, time

def generate_keys():
    key = RSA.generate(2048)
    private = key.export_key()
    public = key.publickey().export_key()
    with open("private.pem", "wb") as f: f.write(private)
    with open("public.pem", "wb") as f: f.write(public)
    print("✅ Keys generated (private.pem, public.pem)")

def encrypt(infile, outfile):
    pub = RSA.import_key(open("public.pem").read())
    cipher = PKCS1_OAEP.new(pub)
    data = open(infile, "rb").read()
    start = time.time()
    ct = cipher.encrypt(data)
    open(outfile, "wb").write(ct)
    print("✅ Encrypted.")
    print(f"⏱ Time: {round(time.time() - start, 6)} sec")

def decrypt(infile, outfile):
    priv = RSA.import_key(open("private.pem").read())
    cipher = PKCS1_OAEP.new(priv)
    ct = open(infile, "rb").read()
    start = time.time()
    pt = cipher.decrypt(ct)
    open(outfile, "wb").write(pt)
    print("✅ Decrypted.")
    print(f"⏱ Time: {round(time.time() - start, 6)} sec")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--genkeys", action="store_true")
    p.add_argument("--encrypt", action="store_true")
    p.add_argument("--decrypt", action="store_true")
    p.add_argument("--infile")
    p.add_argument("--outfile")
    args = p.parse_args()

    if args.genkeys:
        generate_keys()
    elif args.encrypt:
        encrypt(args.infile, args.outfile)
    elif args.decrypt:
        decrypt(args.infile, args.outfile)
