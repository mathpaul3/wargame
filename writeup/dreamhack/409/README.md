## 주요 개념

- Cookies
- Session

## 풀이

`session_storage`에 유저들의 `session_id: username`쌍이 저장된다.
소스코드를 보면 admin의 session_id를 알아내고 그것을 쿠키에 담아 /로 요청을 날리면 flag를 얻을 수 있음을 알 수 있다.
