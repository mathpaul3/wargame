## 주요 개념

- strncmp 함수

## 풀이

executable 파일을 열어보면 /dev/urandom에서 생성한 password값과 사용자의 입력값을 strncmp로 비교하여 조건을 통과할 경우 flag를 출력한다는 것을 알 수 있다.  
strncmp 함수는 null 문자를 만나면 거기서 비교가 끝난다는 점을 이용해, 첫 byte에 \x00을 보내고, urandom으로 생성된 password의 첫 byte가 \x00일 때까지 반복적으로 시도하면 어느 순간 뚫리게 된다. 아래는 공식 문서의 설명이다.

### Compare characters of two strings [링크](https://cplusplus.com/reference/cstring/strncmp/)

Compares up to num characters of the C string str1 to those of the C string str2.
This function starts comparing the first character of each string. If they are equal to each other, it continues with the following pairs until the characters differ, `until a terminating null-character is reached`, or until num characters match in both strings, whichever happens first.
