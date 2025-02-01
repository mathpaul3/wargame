import pwn
import re

HOST = "host1.dreamhack.games"
PORT = 10691

p = pwn.remote(HOST, PORT)
p.recvline()
res = p.recvline()
p.close()

flag = re.search(r"DH{.*}", res.decode()).group()
print(flag)
