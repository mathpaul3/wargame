## 주요 개념

- 역공학 기법(Reverse Engineering)
- 무차별 대입(Brute forcing)

## 풀이

IDA를 통해 해당 executable 파일을 Decompile 해보면  
`(uint8(16 * byte(a1[i])) | (int(uint8(a1[i])) >> 4)) != byte_140003000[i]`일 때 return 되어버리므로  
반대로 `(uint8(16 * byte(a1[i])) | (int(uint8(a1[i])) >> 4)) == byte_140003000[i]`를 만족해야 Correct가 나옴을 알 수 있다.
`byte_140003000`의 데이터를 확인해 해당 조건을 만족하도록 코드를 작성하면 된다.
