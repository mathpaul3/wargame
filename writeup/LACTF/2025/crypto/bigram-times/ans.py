characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}~_"
encrypted = "jlT84CKOAhxvdrPQWlWT6cEVD78z5QREBINSsU50FMhv662W"
not_the_flag = "mCtRNrPw_Ay9mytTR7ZpLJtrflqLS0BLpthi~2LgUY9cii7w"
also_not_the_flag = "PKRcu0l}D823P2R8c~H9DMc{NmxDF{hD3cB~i1Db}kpR77iU"
MOD = 67
prefix = "lactf{"


def reverse(bigram):
    assert len(bigram) == 2
    p1 = characters.find(bigram[0]) + 1
    p2 = characters.find(bigram[1]) + 1

    # Brute force search for possible integer solutions
    solutions = []
    for pos1_candidate in range(1, MOD):
        for pos2_candidate in range(1, MOD):
            for shift in range(1, MOD):
                if (
                    (pos1_candidate * pos2_candidate) % MOD == shift
                    and (pos1_candidate * shift) % MOD == p1
                    and (pos2_candidate * shift) % MOD == p2
                ):
                    solutions.append(
                        characters[pos1_candidate - 1] + characters[pos2_candidate - 1]
                    )
    return solutions


def get_chr(shift, target, mod=67):
    shift_inv = pow(shift, -1, mod)
    pos = (target * shift_inv) % mod
    return characters[pos - 1]


ans = []
for i in range(0, len(encrypted), 2):
    bigram = encrypted[i : i + 2]
    shifted_bigram = reverse(bigram)
    ans.append(shifted_bigram)
print(ans)


not_the_ans = ""
for shift in range(MOD):
    not_the_ans = ""
    for i in range(0, len(not_the_flag), 2):
        bigram = not_the_flag[i : i + 2]
        try:
            not_the_ans += get_chr(shift, characters.find(bigram[0]) + 1) + get_chr(
                shift, characters.find(bigram[1]) + 1
            )
        except ValueError:
            not_the_ans = "Error"
            break

    if not_the_ans[: len(prefix)] == prefix:
        print(f"{shift = }, {not_the_ans}")


for shift in range(MOD):
    also_not_the_ans = ""
    for i in range(0, len(also_not_the_flag), 2):
        bigram = also_not_the_flag[i : i + 2]
        try:
            also_not_the_ans += get_chr(
                shift, characters.find(bigram[0]) + 1
            ) + get_chr(shift, characters.find(bigram[1]) + 1)
        except ValueError:
            also_not_the_ans = ""
            break

    if also_not_the_ans[: len(prefix)] == prefix:
        print(f"{shift = }, {also_not_the_ans}")
