# Main Concept

- Bigram-based Cipher
- Brute-force Search

## Explanation

The given code applies a transformation to the original string by splitting it into bigrams (pairs of two characters), modifying each pair, and concatenating the results.

This transformation follows a bigram-based multiplicative shift, which adheres to the following equations:

```python
(pos1 * pos2) % 67 == shift
(pos1 * shift) % 67 == characters.find(bigram[0]) + 1
(pos2 * shift) % 67 == characters.find(bigram[1]) + 1
```

To retrieve the original flag, a brute-force search is used to identify all integer solutions that satisfy these equations.
This process helps determine all possible original bigrams that could have resulted in the given encrypted output.

By applying this method to each bigram in the encrypted string, it is possible to gradually reconstruct the full flag.
However, since each bigram has multiple valid solutions, the most plausible combination must be selected to recover the correct flag.

Additionally, the values of `not_the_flag` and `also_not_the_flag` provided in `chall.py` serve as hints to guide the selection of the most likely flag.

```
shift = 29, lactf{mUD81pl1cAtiV3_6c{uPz_4rE_3cB~7y_5}kpR~~iU
shift = 37, lactf{mU_A1pl1cAtiV3_6truPz_4rE_pthi7y_5UY9c~~7w
```
