## 주요 개념

- 무차별 대입(Brute Forcing)

## 풀이

/를 보면 session_storage에서 username을 얻어 admin인지 여부를 파악하고 있다. 또한 `if __name__ == '__main__'` 부분을 보면 random한 1byte를 생성해 key값으로 사용하여 value `admin`을 삽입했음을 알 수 있다.
따라서, cookie에 1byte를 무차별 대입하여 /로 요청을 보내면 flag를 얻어낼 수 있다. thread를 사용해 병렬처리하여 더 빠르게 flag를 얻어낼 수 있도록 하였다.
