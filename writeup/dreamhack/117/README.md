## 주요 개념

- 메모리 정렬(Memory Alignment)
- Buffer Overflow

## 풀이

read에서 100bytes를 읽어오는데 center_name이 24 bytes이므로 Buffer Overflow가 발생한다.

char cmd_ip[256]; // 256 bytes  
int dummy; // 4 bytes  
char center_name[24]; // 24 bytes

주어진 executable 파일을 확인해보면 x86-64 환경에서 컴파일 되었음을 알 수 있다.  
8bytes 단위로 메모리 정렬이 일어나, 28bytes가 아니라 4bytes의 padding이 더해진  
32bytes의 더미 bytes를 보내야 cmd_ip를 덮어쓸 수 있다는 것을 알 수 있다.

조건문을 통과해야하므로 cmd_ip의 앞 8bytes는 `ifconfig`로 채우고,  
이후 shell에서 필요한 행동을 수행하는 문자열을 삽입한다.
`{'A'*32}ifconfig;sh`를 입력하면  
shell을 얻어 자유롭게 명령어를 입력할 수 있게 된다.
