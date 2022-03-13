---
title: postgre SQL-practice20
tag: postgre SQL-practice20
date: 2022-02-23
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'데이터 분석을 위한 SQL 레시피' 페이지 202(제11강 5장 - 4.사용자의 방문 빈도 집계하기) 에서

페이지 205까지를 보고 실습을 진행하였다.

'한 주'에 '며칠' 사용되었는지를 집계하는 쿼리문
```python
WITH
action_log_with_dt AS(
 SELECT *
  -- 타임스탬프에서 날짜 추출하기
  -- ■ Postgre SQL, Hive, Redshift, SparkSQL의 경우 substring으로 날짜 부분 추출하기
  , substring(stamp, 1, 10)AS dt
  -- ■ Postgre SQL, Hive, BigQuery, SparkSQL의 경우 substr 사용하기
  -- , substr(stamp, 1, 10)AS dt
 FROM action_log
)
, action_day_count_per_user AS (
 SELECT
	user_id
  , COUNT(DISTINCT dt) AS action_day_count
 FROM
  action_log_with_dt
 WHERE
  -- 2016년 11월 1일부터 11월 7일까지의 한 주 동안을 대상으로 지정
  dt BETWEEN '2016-11-01' AND '2016-11-07'
 GROUP BY
  user_id
)
SELECT
   action_day_count
 , COUNT(DISTINCT user_id) AS user_count
FROM
 action_day_count_per_user
GROUP BY
 action_day_count
ORDER BY
 action_day_count
;
```


'구성비'와 '구성비누계'를 계산하는 쿼리문
```python
WITH
action_log_with_dt AS(
 SELECT *
  -- 타임스탬프에서 날짜 추출하기
  -- ■ Postgre SQL, Hive, Redshift, SparkSQL의 경우 substring으로 날짜 부분 추출하기
  , substring(stamp, 1, 10)AS dt
  -- ■ Postgre SQL, Hive, BigQuery, SparkSQL의 경우 substr 사용하기
  -- , substr(stamp, 1, 10)AS dt
 FROM action_log
)
, action_day_count_per_user AS (
 SELECT
	user_id
  , COUNT(DISTINCT dt) AS action_day_count
 FROM
  action_log_with_dt
 WHERE
  -- 2016년 11월 1일부터 11월 7일까지의 한 주 동안을 대상으로 지정
  dt BETWEEN '2016-11-01' AND '2016-11-07'
 GROUP BY
  user_id
)
SELECT
   action_day_count
 , COUNT(DISTINCT user_id) AS user_count
 
 -- 구성비
 , 100.0
  * COUNT(DISTINCT user_id)
  / SUM(COUNT(DISTINCT user_id)) OVER()
  AS composition_ratio
  
  
 -- 구성비누계
 , 100.0
  * SUM(COUNT(DISTINCT user_id))
      OVER(ORDER BY action_day_count
	   ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) 
  / SUM(COUNT(DISTINCT user_id)) OVER()
  AS cumulative_ratio
FROM
  action_day_count_per_user
 GROUP BY
  action_day_count
ORDER BY
 action_day_count
;
```

이번 항목의 응용으로 12강 5절에서는 사용 일수에 따라 어떤 차이가 있는지를 

집계하는 방법을 소개하겠다. 

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 11강 4.사용자의 방문 빈도 구하기 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어

