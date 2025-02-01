from numpy import byte, int64, uint64, uint8

arr = [
    0x24,
    0x27,
    0x13,
    0x0C6,
    0x0C6,
    0x13,
    0x16,
    0x0E6,
    0x47,
    0x0F5,
    0x26,
    0x96,
    0x47,
    0x0F5,
    0x46,
    0x27,
    0x13,
    0x26,
    0x26,
    0x0C6,
    0x56,
    0x0F5,
    0x0C3,
    0x0C3,
    0x0F5,
    0x0E3,
    0x0E3,
    0x0,
]

flag = "DH{"
for i in range(len(arr)):
    i = uint64(i)
    for ans in range(256):
        ans = int64(ans)
        if (uint8(16 * byte(ans)) | int(uint8(ans)) >> 4) == arr[i]:
            flag += chr(int(ans))
flag = flag + "}"
print(flag)
