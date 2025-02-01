## 주요 개념

- 역공학 기법(Reverse Engineering)
- 문자 인코딩

## 풀이

IDA를 통해 해당 executable 파일을 Decompile 해보면 strcmp 함수를 사용하는 부분이 있다.  
해당 부분에서 숫자를 문자로 변환하여 모두 이어붙이면 flag를 얻어낼 수 있다.
(커서를 숫자에 놓고 'r' 눌러 hex를 char로 변환 가능하다)
