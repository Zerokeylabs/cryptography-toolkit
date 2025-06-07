import hashlib, argparse, time

def hash_file(file, algo):
    with open(file, "rb") as f: data = f.read()
    start = time.time()
    h = hashlib.new(algo)
    h.update(data)
    print("✅ Hash:")
    print(h.hexdigest())
    print(f"⏱ Time: {round(time.time() - start, 6)} sec")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--file", required=True)
    p.add_argument("--algo", default="sha256", help="sha256, sha1, md5, etc.")
    args = p.parse_args()
    hash_file(args.file, args.algo)