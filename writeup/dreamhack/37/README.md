## 주요 개념

- Path Traversal

## 풀이

주어진 코드와 문제의 설명을 보고 flag.py의 파일 경로를 추측해서 얻어내야 하는 문제였다.  
/read를 보면 filename을 별도의 검증없이 바로 대입하여 파일에 접근하는 것을 확인할 수 있다.  
이 점을 이용해 /read?name=../flag.py로 접근하면 flag를 얻어낼 수 있다.
