## 주요 개념

- 역공학 기법(Reverse Engineering)

## 풀이

IDA를 통해 해당 executable 파일을 Decompile 해보면 strcmp 함수를 사용해 입력을 문자열과 비교하는 부분이 있다.  
해당 부분에서 문자열이 저장된 위치로 이동하면 flag를 얻어낼 수 있다.
