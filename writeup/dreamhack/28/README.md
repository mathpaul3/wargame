## 주요 개념

- XSS(Cross-Site Scripting)

## 풀이

주어진 코드를 보면, /flag로 접근했을 때, cookie에 flag를 담아 webdriver로 param에 접근하고 있는 것을 확인할 수 있다. 이때 param에 script를 담아 /memo?memo에 cookie의 내용물을 추가하도록 하면 /memo에서 flag를 확인할 수 있다.
