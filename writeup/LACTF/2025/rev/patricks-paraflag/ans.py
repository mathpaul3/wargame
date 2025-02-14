s = "l_alcotsft{_tihne__ifnlfaign_igtoyt}"
arr = [None for _ in range(len(s))]
v3 = len(s)
v4 = v3 >> 1

for i in range(len(s) >> 1):
    arr[i], arr[i + v4] = s[i * 2], s[i * 2 + 1]
print("".join(arr))
