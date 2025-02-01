from Crypto.Util.number import long_to_bytes
from pwn import remote

# Remote host
HOST = "host1.dreamhack.games"
PORT = 12345

p = remote(HOST, PORT)
p.sendlineafter("info".encode(), "3".encode())
_, _, N, e, FLAG = map(
    lambda _: ([None] if _ == 0 else p.recvline().decode().strip().split(" "))[-1],
    range(5),
)
N, e, FLAG = map(int, (N, e, FLAG))
# print(f"{N = }, {e = }, {FLAG = }")
p.sendlineafter("info".encode(), "2".encode())
p.sendlineafter(":".encode(), hex((FLAG * 2) % N)[2:].encode())
c_doubled = int(p.recvline().decode().strip())
# print(f"{c_doubled = }")

p.sendlineafter("info".encode(), "2".encode())
p.sendlineafter(":".encode(), (f"{2:02x}".encode()))
c_mul = int(p.recvline().decode().strip())
# print(f"{c_mul = }")
modinv_c_mul = pow(c_mul, -1, N)

p.close()

print(long_to_bytes(c_doubled * modinv_c_mul % N).decode())
