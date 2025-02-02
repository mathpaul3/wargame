## 주요 개념

- 무차별 대입(Brute Forcing)

## 풀이

소스코드를 보면 locker_num은 클라이언트에서 보낸 길이만큼만 비교해서 맞으면 Good, 아니면 Wrong!을 보내고 있다. 한글자씩 총 4글자를 Brute force로 알아내고, 비밀번호는 100~200 사이의 숫자이므로 이것도 Brute force로 알아내면 flag를 얻어낼 수 있다.
