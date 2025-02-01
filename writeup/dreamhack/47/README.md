## 주요 개념

- Race Condition Vulnerability
- 무차별 대입(Brute Forcing)

## 풀이

/user/{userid}로 접근하면 유저의 정보가 출력된다. 여기에서 UserLevel=1(Admin)인 계정을 적당히 고른다.
forgot_password를 통해 비밀번호를 변경할건데, 이때 코드를 보면 user[\'resetCount\']에
남은 횟수가 몇 번인지 저장하고 그것을 기반으로 변경 가능 여부를 판단하고 있다는 것을 알 수 있다.
한꺼번에 여러개의 forgot_password 요청을 보내면 race condition이 발생하고,
이로 인해 user[\'resetCount\']가 MAXRESETCOUNT를 넘어서면 `if user['resetCount'] == MAXRESETCOUNT:`가 아무 역할을 하지 못하게 된다.
그러면 backupCode를 무차별 대입하여 비밀번호를 변경할 수 있고,
변경한 비밀번호로 로그인 한 뒤 /admin으로 접근하면 flag를 얻어낼 수 있다.
