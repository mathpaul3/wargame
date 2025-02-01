## 주요 개념

- 역공학 기법(Reverse Engineering)

## 풀이

IDA를 통해 해당 executable 파일을 Decompile 해보면  
`byte_140003000[i] != (i ^ *(a1+i)) + 2*i`일 때 return 되어버리므로  
반대로 `byte_140003000[i] == (i ^ *(a1+i)) + 2*i`를 만족해야 Correct가 나옴을 알 수 있다.
`byte_140003000`의 데이터를 확인해 해당 조건을 만족하도록 코드를 작성하면 된다.
