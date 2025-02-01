## 주요 개념

- socket 통신
- AES(Advanced Encryption Standard)

## 풀이

주어진 코드를 분석하며 단계별로 구현해나가는 문제였다.  
INITIALIZE 후 HANDSHAKE, SEND, ADDITIONAL 순서로 진행하면 되었다.

### INITIALIZE 과정

\_dataStorage와 \_cryptoConfig를 초기화 한다. (안 하면 나중에 ADDITIONAL 과정에서 if문에 걸릴 수도 있다)

### HANDSHAKE 과정

AES256CBC에서 사용할 key, iv를 직접 만들어 body에 담아 보낸다.  
이때, 서버측에서는 key의 마지막 바이트를 잘라내고 임의로 만들어진 1 바이트를 붙인다.  
(추후 brute forcing하는 원인이 된다)

### SEND 과정

길이 10짜리 flag를 body에 담아 보낸다. 이때 내가 보낸 flag는 서버의 \_dataStorage에 저장된다.

### ADDITIONAL 과정

앞서 SEND 과정에서 보낸 flag와 이번 과정에서 보내는 flag를 합치고 이를 if문 통과용으로 사용한다. 서버에서는 FLAG를 AES256CBC 암호화 한 값을 반환해준다.

### 복호화

AES 복호화에 필요한 key, iv를 모두 알고 있으므로 이것을 통해 복호화 하면 된다. 단, HANDSHAKE 과정에서 key의 일부가 변조되었으므로, brute forcing을 통해 FLAG의 값을 얻어낸다.
