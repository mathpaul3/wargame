## 주요 개념

- 아파치(Apache) - .htaccess
- php
- Misconfig
- 파일 업로드 취약점(File Upload Vulnerability)

## 풀이

000-default.conf 파일을 보면 Apache 관련 설정들이 작성되어 있는 것을 확인할 수 있다.  
Apache의 .htaccess은 디렉토리별로 설정을 변경하고 싶을 때 사용하는 파일 형식이다.  
그리고, upload.php를 보면 `$deniedExts`에 .htaccess가 없다는 것을 확인할 수 있다.
임의의 확장자를 php 타입으로 추가하는 구문을 작성하여 서버에 업로드 한 후,  
해당 확장자로 된, php 구문이 작성된 코드를 서버에 업로드하면 php처럼 사용할 수 있다.
이를 통해 flag의 값을 알아낼 수 있다.
