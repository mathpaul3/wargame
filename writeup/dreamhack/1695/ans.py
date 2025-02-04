import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
files = sorted(os.listdir(f"{BASE_PATH}/papers"))

caesar = "bcdefghimnrswy0123456789{_}"
cipher = list()
for file in files:
    with open(f"{BASE_PATH}/papers/{file}", "r") as f:
        txt = [c for c in f.read() if c in caesar]
        if len(txt):
            cipher.append(txt)

for offset in range(len(caesar)):
    if offset == 16:
        res = [
            "".join([caesar[(caesar.index(c) + offset) % len(caesar)] for c in txt])
            for txt in cipher
        ]
        print("".join([res[2], res[5], res[0], res[3], res[7], res[1], res[6], res[4]]))
