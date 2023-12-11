import requests
import json
import urllib.parse

# https://layerzeroscan.com/api/trpc/messages.list?input={"filters":{"address":"","stage":"mainnet","created":{}}}
wallet_addr = "0x786eb3e5e19b6cf638d7a3c9dd7898a14e4911d7"
l0scan_url = "https://layerzeroscan.com/api/trpc/messages.list?input=%7B%22filters%22%3A%7B%22address%22%3A%220x786eb3e5e19b6cf638d7a3c9dd7898a14e4911d7%22%2C%22stage%22%3A%22mainnet%22%2C%22created%22%3A%7B%7D%7D%7D"
res = requests.get(url=l0scan_url)
if res.status_code == 200:
    src_chains = []
    dst_chains = []
    cross_chains = []

    for item in res.json().get('result').get("data").get("messages"):
        src_chain = item.get("srcChainKey")
        dst_chain = item.get("dstChainKey")

        if not src_chain in src_chains:
            src_chains.append(src_chain)
        if not dst_chain in dst_chains:
            dst_chains.append(dst_chain)
        isExist = False
        for cross_chain in cross_chains:
            if src_chain == cross_chain["src_chain"] and dst_chain == cross_chain["dst_chain"]:
                isExist = True
                break
        if not isExist:
            cross_chains.append({
                    "src_chain": src_chain,
                    "dst_chain": dst_chain
                })        
    print("--- total cross chain number ---")
    print(len(res.json().get("result").get("data").get("messages")))

    print("--- unique src chain number ---")
    print(len(src_chains), src_chains)

    print("--- unique dst chain number ---")
    print(len(dst_chains), dst_chains)

    print("--- unique cross chain number ---")
    print(len(cross_chains), cross_chains)
else:
    print(res.json())
