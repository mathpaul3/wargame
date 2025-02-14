import os
import string

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

flag = ""
with open(f"{BASE_PATH}/chall.txt", "rb") as f:
    data = f.read()
    decoded = data.decode("iso8859-1")
    for s in decoded:
        res = bin(ord(s))[2:].zfill(8)
        for i in range(8):
            if res[i] == "1":
                res = res[:i] + "0" + res[i + 1 :]
            if (
                chr(int(res, 2))
                in string.ascii_uppercase + string.ascii_lowercase + "_{}"
            ):
                flag += chr(int(res, 2))
                break
print(flag)
print(f"{len(data) = } {len(flag) = }")
