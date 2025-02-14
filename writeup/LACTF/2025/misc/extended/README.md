# Main Concept

- Text Encoding

## Explanation

By analyzing `gen.py`, you can determine that the given `chall.txt` file is encoded in `iso8859-1`. Therefore, the first step is to decode it to restore the original string.

Next, `gen.py` modifies each character by converting it to its 8-bit binary representation and replacing the first occurrence of `0` with `1`. This means that a binary string like `10100000` could be transformed into `11100000`, making it difficult to determine which `0` was changed to `1` when attempting to reverse the process.

To solve this, you can convert the modified string back into its binary form and iterates through each bit, changing each `1` back to `0` one by one. If the resulting character belongs to the set of valid flag characters (`[A-Za-z0-9_{}]`), it is added to the flag string.

Additionally, to verify that all characters have been correctly restored without any missing ones, we can compare the length of the recovered string with the original string. This allows us to check for any missing characters in the final result.
