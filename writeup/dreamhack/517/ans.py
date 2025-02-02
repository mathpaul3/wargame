import string

cipher = "EDVLF FUBSWR GUHDPKDFN"

for idx in range(len(string.ascii_uppercase)):
    print(
        f'DH{{{"".join(
            [
                (
                    chr(
                        (ord(c) - ord("A") + idx) % len(string.ascii_uppercase)
                        + ord("A")
                    )
                    if c != " "
                    else "_"
                )
                for c in cipher
            ]
        )}}}'
    )
