## 주요 개념

- 설정 오류(Misconfig)

## 풀이

주어진 default.ini 파일을 살펴보면 `admin_user = admin`, `admin_password = admin`으로 설정되어 있는 것을 확인할 수 있다.
해당 아이디와 비밀번호로 로그인 한 후 /admin/settings에 접근하여 org_name을 찾아보면 flag를 얻어낼 수 있다.
