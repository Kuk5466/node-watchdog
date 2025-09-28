import argparse, time, requests, pandas as pd
from datetime import datetime

def probe(rpc, tries=3):
    results = []
    payload = {"jsonrpc":"2.0","id":1,"method":"eth_blockNumber","params":[]}
    for _ in range(tries):
        t0 = time.time()
        try:
            r = requests.post(rpc, json=payload, timeout=5)
            latency = round((time.time()-t0)*1000, 2)
            status = "ok" if r.ok else f"err:{r.status_code}"
        except Exception as e:
            latency, status = None, f"fail:{type(e).__name__}"
        results.append({"time":datetime.utcnow().isoformat(), "latency_ms":latency, "status":status})
    return results

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--rpc", required=True, help="RPC endpoint")
    p.add_argument("--tries", type=int, default=3)
    p.add_argument("--out", default="out.csv")
    args = p.parse_args()

    df = pd.DataFrame(probe(args.rpc, args.tries))
    df.to_csv(args.out, index=False)
    print(df)

if __name__ == "__main__":
    main()
