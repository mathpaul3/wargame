## 주요 개념

- SQL 주입(SQL Injection)

## 풀이

POST /login을 보면 클라이언트로부터 넘겨받은 인자들을 검증 없이 그대로 대입하여 SQL query를 날리고 있는 것을 확인할 수 있다.
따라서 {"userid": 'admin" OR userpassword = "', "userpassword": "--"}을 담아 날려주면 flag를 취득할 수 있다.
