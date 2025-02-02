import requests
import re

HOST = "http://host1.dreamhack.games"
PORT = 9534

res = requests.post(f"{HOST}:{PORT}/", data={"id": "GUEST", "ps": "guest"})
flag = re.search(r"DH{.*}", res.text).group()
print(flag)
