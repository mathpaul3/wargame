with open("P:\wargame\dreamhack\\517\encode.txt", "r") as f:
    line = f.readline().split()
    for i in range(26):
        temp_line = []
        for word in line:
            temp_word = ""
            for c in word:
                order = (ord(c) - 64 + i) % 26 + 65
                temp_word += chr(order)
            temp_line.append(temp_word)
        print("_".join(temp_line))
    
    print("\n")
    ans_mv = 22
    ans_line = []
    for word in line:
        ans_word = ""
        for c in word:
            order = (ord(c) - 64 + ans_mv) % 26 + 65
            ans_word += chr(order)
        ans_line.append(ans_word)
    print("DH{" + "_".join(ans_line) + "}")