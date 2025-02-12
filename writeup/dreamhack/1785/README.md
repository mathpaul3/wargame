## 주요 개념

- Base64 Encoding/Decoding

## 풀이

폴더 구조를 보면 ../flag 파일에 flag가 있고, ./flag.php에서 해당 파일을 읽어오는 걸 알 수 있다.  
직접 /flag.php로 접근하면 막히므로, index.php에 'file' 파라미터를 넘겨서 얻어야 함을 알 수 있다.  
./flag.php를 base64 encoding한 /?file=Li9mbGFnLnBocA==로 요청하면 flag를 얻어낼 수 있다.

참고로 if문에서 필터링 되는 문자열을 base64 decode해서 살펴보면 다음과 같다. `['../', 'fla', 'hp']`
ASCII는 8bit를 사용하고, base64는 6bit를 사용하기 때문에 이들의 최소공배수인  
24bit(ASCII로 3문자, base64로 4문자) 단위로 글자가 처리된다.
따라서 `['./f', 'lag', '.ph']`로 끊기면 해당 필터에 걸리지 않게 된다.
