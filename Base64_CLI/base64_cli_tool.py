import base64, argparse, time

def encode(infile, outfile):
    with open(infile, "rb") as f: data = f.read()
    start = time.time()
    encoded = base64.b64encode(data)
    with open(outfile, "wb") as f: f.write(encoded)
    print("✅ Encoded.")
    print(f"⏱ Time: {round(time.time() - start, 6)} sec")

def decode(infile, outfile):
    with open(infile, "rb") as f: data = f.read()
    start = time.time()
    decoded = base64.b64decode(data)
    with open(outfile, "wb") as f: f.write(decoded)
    print("✅ Decoded.")
    print(f"⏱ Time: {round(time.time() - start, 6)} sec")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--encode", action="store_true")
    p.add_argument("--decode", action="store_true")
    p.add_argument("--infile", required=True)
    p.add_argument("--outfile", required=True)
    args = p.parse_args()

    if args.encode:
        encode(args.infile, args.outfile)
    elif args.decode:
        decode(args.infile, args.outfile)
