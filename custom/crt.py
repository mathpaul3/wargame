from functools import reduce


# Chinese Remainder Theorem
class CRT:

    # 중국인의 나머지 정리의 해
    x: int
    a: int
    m: int

    # 합동식, x ≡ a (mod m)일 때, [(a1, m1), (a2, m2), ...]의 형태로 입력
    congruents: list[tuple[int, int]]

    def __init__(self, *congruents: list[tuple[int, int]]):
        self.congruents = congruents
        self.solve()

    def solve(self):
        m: int = reduce(lambda acc, cur: acc * cur[1], *self.congruents, 1)
        a = reduce(
            lambda acc, cur: (
                acc + m // cur[1] * pow(m // cur[1], -1, cur[1]) * cur[0]
            ),
            *self.congruents,
            0,
        )
        self.x = a
        self.a = a % m
        self.m = m

    def __str__(self):
        return f"{self.x} ≡ {self.a} (mod {self.m})"


if __name__ == "__main__":
    # x ≡ 3 (mod 5)
    # x ≡ 4 (mod 7)
    crt = CRT([(3, 5), (4, 7)])
    print(crt)

    # x ≡ 1 (mod 3)
    # x ≡ 2 (mod 5)
    # x ≡ 3 (mod 7)
    crt = CRT([(1, 3), (2, 5), (3, 7)])
    print(crt)

    # x ≡ 2 (mod 3)
    # x ≡ 3 (mod 5)
    # x ≡ 2 (mod 7)
    crt = CRT([(2, 3), (3, 5), (2, 7)])
    print(crt)
