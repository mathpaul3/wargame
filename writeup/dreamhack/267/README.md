## 주요 개념

## 풀이

크롬의 개발자 도구를 활용하여 푸는 문제...이지만 사실 주어진 소스코드(`main.example.map`)에서 `DH{`를 검색하면 flag가 나온다!
그래도 개발자 도구를 사용해보라고 했으니 이를 활용해 찾는다면  
Sources > Page > webpack:// > styles > main.scss에 `DH{`를 검색하면 flag를 얻어낼 수 있다.
