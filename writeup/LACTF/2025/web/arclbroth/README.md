# Main Concept

- Null Byte Injection

## Explanation

SQLite stores **`\x00` (NULL byte)** within strings and treats it as part of the value.
However, when performing a **SELECT** query, it only retrieves characters before `\x00`.
([Reference: SQLite Official Documentation](https://www.sqlite.org/nulinstr.html))

By exploiting this behavior, it is possible to **bypass admin authentication** and obtain the flag.

### Attack Flow Analysis

1. Conditions for obtaining the flag from `/brew`

   - If `arcs >= 50`, the response will return `{ broth: flag }`.
   - To reach `arcs >= 50`, `/replenish` must be used to set `arcs = 100`.
   - However, `/replenish` only sets `arcs = 100` if `username === 'admin'`.

2. `username` is retrieved from `res.locals.user`.

   - `res.locals.user` is set in middleware defined by `app.use`.
   - This middleware uses a SELECT query to retrieve the username based on the session ID (`session`).
   - Using SQLite’s **NULL byte handling behavior**, an account named `admin\00` can be interpreted as `admin`.

3. Attack Steps
   1. Send a `/register` request to create an account with `username="admin\00"`.
   2. Send a `/login` request using `username="admin\00"` to generate a session.
   3. Send a `/replenish` request to set `arcs = 100`.
   4. Send a `/brew` request to obtain the flag.

By following these steps in order, the flag can be successfully retrieved.
