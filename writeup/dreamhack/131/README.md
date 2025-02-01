## 주요 개념

- RSA(Rivest–Shamir–Adleman)
- CCA(Chosen Ciphertext Attack)

## 풀이

모듈로 연산의 특징을 활용하여 CCA를 할 수 있다.

1. Get $(2c)^d mod N = (2m^e)^{d} mod N$

```python
c_doubled = decrypt((c * 2) % N)
```

2. Get $2^d mod^{-1} N$

```python
modinv_c_mul = pow(decrypt(2), -1, N)
```

3. Get $m = c^d mod N = (\frac {2c} {2})^d mod N = ((2c)^d mod N \times 2^d mod^{-1} N) mod N $

```python
m = (c_doubled * modinv_c_mul) % N
```
