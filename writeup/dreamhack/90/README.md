## 주요 개념

- URL parsing
- NOSQL Injection
- 무차별 대입(Brute forcing)
- 정규표현식(Regular Expression)

## 풀이

URL에 객체를 담아 보낼 수 있다는 점과 MongoDB에서 $regex를 통해 record를 조회할 수 있다는 점을 알아야 풀 수 있는 문제였다.  
`{'uid': 'admin', 'upw': 'DH{32alphanumeric}'}`라고 주어져 있으므로, $regex를 활용하여 upw에 alphanumeric을 무차별 대입하면 풀 수 있는 문제였다.
단일 스레드로 실행할 경우 너무 오래 걸려서 스레드를 통해 병렬처리하였다.
