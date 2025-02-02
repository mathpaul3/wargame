## 주요 개념

- 필터 우회(Filter Bypassing)
- SQL(Structured Query Language)

## 풀이

소스 파일을 확인해보면 주석에 block 당한 계정과 비밀번호가 적혀있다.  
또한, 자세히 보면 input을 검사하는 부분에서 소문자만 필터링하고 있다.  
그런데, SQL은 대소문자를 구분하지 않는다.  
따라서 대문자를 적당히 섞어 로그인하면 성공적으로 flag를 얻어낼 수 있다.
