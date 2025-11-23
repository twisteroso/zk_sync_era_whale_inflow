import requests, time

def zksync_whale_inflow():
    print("zkSync Era — whale bridge inflow tracker (>$500k in one tx)")
    seen = set()
    while True:
        r = requests.get("https://block-explorer-api.zksync.io/transactions?limit=30&direction=desc")
        for tx in r.json().get("items", []):
            txid = tx["hash"]
            if txid in seen or not tx.get("receivedAt"): continue
            seen.add(txid)
            if tx.get("type") == "deposit" and tx.get("valueUsd", 0) > 500000:
                print(f"WHALE JUST BRIDGED IN ${tx['valueUsd']:,.0f}!\n"
                      f"Token: {tx.get('token', {}).get('symbol', 'ETH')}\n"
                      f"Wallet: {tx['to']}\n"
                      f"Age: {(time.time() - time.mktime(time.strptime(tx['receivedAt'][:19], '%Y-%m-%dT%H:%M:%S'))):.0f}s ago\n"
                      f"https://explorer.zksync.io/tx/{txid}\n"
                      f"→ Fresh money hitting zkSync Era RIGHT NOW\n"
                      f"{'🦍💰'*20}")
        time.sleep(4)

if __name__ == "__main__":
    zksync_whale_inflow()
