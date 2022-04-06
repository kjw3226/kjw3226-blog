---
title: postgre SQL-practice54
tag: postgre SQL-practice54
date: 2022-04-06
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'7장  18강 이상값 검출하기'의

'1. 데이터 분산 계산하기'로 넘어갔으며

페이지 420 ~ 423을 참고하였다.

세션별로 페이지 열람 수 랭킹 비율을 구하는 쿼리문
```python
WITH
session_count AS (
  SELECT
	 session
   , COUNT(1) AS count
  FROM
   action_log_with_noise
  GROUP BY
	session
)
SELECT
   session
 , count
 , RANK() OVER(ORDER BY count DESC) AS rank
 , PERCENT_RANK() OVER(ORDER BY count DESC) AS percent_rank
FROM
  session_count
;
```

URL 접근 수 워스트(worst) 랭킹 비율을 출력하는 쿼리문
```python
WITH
url_count AS (
  SELECT
	 url
   , COUNT(*) AS count
  FROM
	action_log_with_noise
  GROUP BY
	 url
)
SELECT
   url
 , count
 , RANK() OVER(ORDER BY count ASC) AS rank
 , PERCENT_RANK() OVER(ORDER BY count ASC)
FROM
 url_count
;
```

