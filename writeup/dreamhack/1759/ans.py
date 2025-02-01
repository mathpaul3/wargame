import socket
from enum import IntEnum
import bson
from functools import reduce
from Crypto.Cipher import AES


##################
# AES decryption #
##################
def decrypt(key: bytes, iv: bytes, enc: bytes):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    dec = cipher.decrypt(enc)
    return dec.decode()


##############
# For socket #
##############
class KnownRequestMethod(IntEnum):
    HANDSHAKE = 0x01
    SEND = 0x02
    ADDITIONAL = 0x03


class Header:
    method: KnownRequestMethod
    name: str
    length: int

    def __init__(self, method: KnownRequestMethod, name: str, length: int):
        self.method = method  # 1 byte
        self.name = name  # 13 bytes
        self.length = length  # 4 bytes

    def getBytes(self):
        return (
            self.method.to_bytes(1)
            + self.name.rjust(13, chr(0x00)).encode()
            + self.length.to_bytes(4, "big")
        )


class Data:
    header: Header
    body: bytes

    def __init__(self, method: KnownRequestMethod, name: str, body: dict):
        self.body = bson.dumps(body)
        self.header = Header(method=method, name=name, length=len(self.body))

    def getBytes(self):
        return self.header.getBytes() + self.body


#########
# Solve #
#########

# Remote host
HOST = "host1.dreamhack.games"
PORT = 12345

# Localhost
# HOST = "0.0.0.0"
# PORT = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IP/TCP로 소켓을 생성
server_address = (HOST, PORT)  # 접속할 주소와 포트넘버
sock.connect(server_address)  # 생성한 소켓으로 해당 주소에 접속

# INITIALIZE 과정
sock.send("INITIALIZE".encode())
res = sock.recv(1024)
print(res)

# HANDSHAKE 과정
data = Data(
    KnownRequestMethod.HANDSHAKE,
    "test",
    {
        "iv": hex(ord("a"))[2:] * 16,
        "key": hex(ord("a"))[2:] * 32,
    },
)
sock.send(data.getBytes())
res = sock.recv(1024)
print(res)

# SEND 과정
data = Data(KnownRequestMethod.SEND, "test", {"flag": "pleasegive"})
sock.send(data.getBytes())
res = sock.recv(1024)
print(res)

# ADDITIONAL 과정
data = Data(
    KnownRequestMethod.ADDITIONAL,
    "test",
    {"flag": "meaflag"},
)
sock.send(data.getBytes())
res = sock.recv(2048)
print(res)

# AES 복호화 과정
res = res.decode()
final = reduce(
    lambda acc, cur: acc + int(cur, 16).to_bytes(),
    [res[idx * 2] + res[idx * 2 + 1] for idx in range(len(res[::2]))],
    bytes(),
)

# brute forcing
for h in range(0x00, 0xFF):
    try:
        flag = decrypt(("a" * 31).encode() + h.to_bytes(), ("a" * 16).encode(), final)
        prefix = "null{"
        if flag[: len(prefix)] == prefix:
            print(flag)
            break
    except Exception as e:
        pass

sock.close()
