## 주요 개념

- Path Traversal

## 풀이

/get_info API를 보면, 검증되지 않은 userid를 그대로 넘겨받고 있어 path traversal 취약점이 존재한다. userid에 "../flag"를 담아보내면 flag를 얻어낼 수 있다.
