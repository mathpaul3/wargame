# Main Concept

- White Space Injection

## Explanation

Flask caching treats inputs containing `\x00\x01\x02\x03` as distinct values,
while SQL ignores these characters and processes the inputs as the same value.

By taking advantage of this behavior, one can generate multiple variations of the UUID
by combining `\x00`, `\x01`, `\x02`, and `\x03`, then sending requests with these modified UUIDs.
This causes the server to treat them as different cache keys, while SQL sees them as the same user.
As a result, it allows bypassing caching mechanisms to retrieve the flag.
