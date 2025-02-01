from math import pow
from typing import Literal, Union


class RSA:
    p: int | None = None  # prime number
    q: int | None = None  # prime number
    N: int | None = None  # p * q
    phi: int | None = None  # (p - 1) * (q - 1)
    e: int | None = None  # usually 0x10001 or 65537
    d: int | None = None  # d = e^-1 mod phi (e * d = 1 mod phi)
    c: int | None = None  # cipher_text or encrypted_message
    m: int | None = None  # plain_text or decrypted_message

    # from Crypto.Util.number import bytes_to_long, long_to_bytes
    # bytes_to_long equals to int.from_bytes(b, "big")
    # long_to_bytes equals to n.to_bytes((n.bit_length() + 7) // 8, "big")

    def __init__(
        self,
        p: int = None,
        q: int = None,
        N: int = None,
        phi: int = None,
        e: int = None,
        d: int = None,
        m: int | bytes | str = None,
        c: int | bytes | str = None,
    ):
        self.set_p(p)
        self.set_q(q)
        if isinstance(self.p, int) and isinstance(self.q, int):
            self.set_N(p * q)
            self.set_phi((p - 1) * (q - 1))
        else:
            self.set_N(N)
            self.set_phi(phi)

        # public key: N, e
        self.set_e(e)
        if isinstance(self.e, int) and isinstance(self.phi, int):
            # private key: N, d
            self.set_d(pow(e, -1, self.phi))
        else:
            self.set_d(d)

        self.set_m(m)
        self.set_c(c)

    def set_p(self, p: int):
        if not isinstance(p, int) or isinstance(self.p, int):
            return
        self.p = p

        if not isinstance(self.q, int):
            return
        self.set_N(p * self.q)
        self.set_phi((p - 1) * (self.q - 1))

    def set_q(self, q: int):
        if not isinstance(q, int) or isinstance(self.q, int):
            return
        self.q = q
        if not isinstance(self.p, int):
            return
        self.set_N(self.p * q)
        self.set_phi((self.p - 1) * (q - 1))

    def set_N(self, N: int):
        if not isinstance(N, int) or isinstance(self.N, int):
            return
        self.N = N

        self.set_c(self.encrypt(self.m))
        self.set_m(self.decrypt(self.c))

        # if possible, get p and q from N
        if isinstance(self.p, int) and not isinstance(self.q, int):
            self.set_q(N // self.p)
        if not isinstance(self.p, int) and isinstance(self.q, int):
            self.set_p(N // self.q)

    def set_phi(self, phi: int):
        if not isinstance(phi, int) or isinstance(self.phi, int):
            return
        self.phi = phi
        if isinstance(self.e, int):
            self.set_d(pow(self.e, -1, phi))

        # if possible, get p and q from phi
        if isinstance(self.p, int) and not isinstance(self.q, int):
            self.set_q(phi // (self.p - 1) + 1)
        if not isinstance(self.p, int) and isinstance(self.q, int):
            self.set_p(phi // (self.q - 1) + 1)

    def set_e(self, e: int):
        if not isinstance(e, int) or isinstance(self.e, int):
            return
        self.e = e
        if isinstance(self.phi, int):
            self.set_d(pow(e, -1, self.phi))
        self.set_c(self.encrypt(self.m))

    def set_d(self, d: int):
        if not isinstance(d, int) or isinstance(self.d, int):
            return
        self.d = d
        self.set_m(self.decrypt(self.c))

    def set_m(self, m: int | bytes | str):
        if (
            not isinstance(m, int)
            and not isinstance(m, bytes)
            and not isinstance(m, str)
        ):
            return
        if isinstance(self.m, int):
            return
        if isinstance(m, bytes) or isinstance(m, str):
            m = self._message_to_number(m)
        self.m = m
        self.set_c(self.encrypt(m))

    def set_c(self, c: int | bytes | str):
        if (
            not isinstance(c, int)
            and not isinstance(c, bytes)
            and not isinstance(c, str)
        ):
            return
        if isinstance(self.c, int):
            return
        if isinstance(c, bytes) or isinstance(c, str):
            c = self._message_to_number(c)
        self.c = c
        self.set_m(self.decrypt(c))

    def get_public_key(self):
        return self.N, self.e

    def get_private_key(self):
        return self.N, self.d

    def encrypt(self, m: int) -> int:
        if not isinstance(m, int):
            return
        if not isinstance(self.N, int) or not isinstance(self.e, int):
            return
        return pow(m, self.e, self.N)

    def decrypt(self, c: int) -> int:
        if not isinstance(c, int):
            return
        if not isinstance(self.N, int) or not isinstance(self.d, int):
            return
        return pow(c, self.d, self.N)

    def CCA(
        self,
        decrypted_multiplied_c: int = None,
        decrypted_multiplication: int = None,
    ):
        # CCA(Chosen Ciphertext Attack)
        ## use this method when knowing c, N and you can decrypt specific c
        if not isinstance(self.N, int):
            return

        # 1. get 2m = 2c^d mod N = 2m^ed mod N
        if not isinstance(decrypted_multiplied_c, int):
            # decrypted_multiplied_c = self.decrypt((self.c * multiple) % self.N)
            return

        # 2. get modular inverse of 2^d mod N
        if not isinstance(decrypted_multiplication, int):
            # decrypted_multiplication = self.decrypt(multiple)
            return

        modinv_decrypted_multiplication = pow(decrypted_multiplication, -1, self.N)

        # 3. (2c / 2)^d mod N = (2c^d mod N * mod^-1(2) mod N) mod N = c^d mod N
        self.set_m((decrypted_multiplied_c * modinv_decrypted_multiplication) % self.N)

    @staticmethod
    def _message_to_number(m: bytes | str) -> int:
        if not isinstance(m, bytes) and not isinstance(m, str):
            return
        return int.from_bytes(m.encode() if isinstance(m, str) else m, "big")

    @staticmethod
    def _number_to_message(
        m_int: int, to: Literal["bytes", "str"] = "bytes"
    ) -> Union[bytes, str]:
        if to == "bytes":
            return m_int.to_bytes((m_int.bit_length() + 7) // 8, "big")
        if to == "str":
            return m_int.to_bytes((m_int.bit_length() + 7) // 8, "big").decode()

    def __str__(self):
        return f"""RSA(
    p={self.p}
    q={self.q}
    N={self.N}
    phi={self.phi}
    e={self.e}
    d={self.d}
    m={self.m}
    hex(m)={hex(self.m)[2:] if isinstance(self.m, int) else None}
    plain(m)={self._number_to_message(self.m) if isinstance(self.m, int) else None}
    c={self.c}
    hex(c)={hex(self.c)[2:] if isinstance(self.c, int) else None}
    plain(c)={self._number_to_message(self.c) if isinstance(self.c, int) else None}
)"""


if __name__ == "__main__":

    from Crypto.Util.number import getPrime

    p = getPrime(1024)
    q = getPrime(1024)
    e = 0x10001
    rsa = RSA(p=p, q=q, e=e, m="TEST{Th1s_i5_f1a9}")
    print(rsa)
    print(rsa._number_to_message(rsa.decrypt(rsa.c)))
