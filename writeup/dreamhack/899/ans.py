import requests
import re
from bs4 import BeautifulSoup

# # org = 19자리 수
# org = int("9" * 19)
# max_bit = org.bit_length()
# org = int("1" + "0" * 18)
# min_bit = org.bit_length()
# print(f"{min_bit} <= org.bit_length() <= {max_bit}")
# for i in range(0, 16):
#     res = (org >> (4 * i)) & 0xF

HOST = "http://host1.dreamhack.games"
PORT = 10211


# Get menu string
res = requests.get("http://host1.dreamhack.games:10211/")
soup = BeautifulSoup(res.text, "html.parser")
menu_str = soup.select("code")[0].text
print(menu_str)


# Calculate input string
menu_str = menu_str[::-1]
input_str = 0
for idx, char in enumerate(menu_str):
    num = 0
    if char.isnumeric():
        num = int(char)
    elif char in ["a", "b", "c", "d", "e", "f"]:
        num = ord(char) - ord("a") + 10
    elif char == "_":
        num = 0xF & ~0x4
    # print(num, end=' ')
    input_str += num << (4 * idx)
input_str = str(input_str)
# print(len(input_str))


# Get flag
res = requests.post(f"{HOST}:{PORT}/", data={"menu_input": input_str})
flag = re.search(r"DH{.*}", res.text).group()
print(flag)
