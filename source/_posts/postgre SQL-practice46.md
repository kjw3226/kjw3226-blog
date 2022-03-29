---
title: postgre SQL-practice46
tag: postgre SQL-practice46
date: 2022-03-29
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'6장  15강 사이트 내의 사용자 행동 파악하기

7. 사이트 내부에서 사용자 흐름 파악하기'

로 넘어갔으며, 페이지는 378 ~ 387을 참고하였다.


/detail 페이지 이후의 사용자 흐름을 집계하는 쿼리문
```python
WITH
activuty_log_with_lead_path AS (
 SELECT
   session
 , stamp
 , path AS path0
   -- 곧바로 접근한 경로 추출하기
 , LEAD(path, 1) OVER(PARTITION BY session ORDER BY stamp ASC) AS path1
   -- 이어서 접근한 경로 추출하기
 , LEAD(path, 2) OVER(PARTITION BY session ORDER BY stamp ASC) AS path2
 FROM
  activity_log
)
, raw_user_flow AS (
  SELECT
	 path0
	 -- 시작 지점 경로로의 접근 수
   , SUM(COUNT(1)) OVER() AS count0
	 -- 곧바로 접근한 경로 (존재하지 않는 경우 문자열 NULL)
   , COALESCE(path1, 'NULL') AS path1
	 -- 곧바로 접근한 경로로의 접근 수
   , SUM(COUNT(1)) OVER(PARTITION BY path0, path1) AS count1
	 -- 이어서 접근한 경로 (존재하지 않는 경우 문자열 'NULL' 지정)
   , COALESCE(path2, 'NULL') AS path2
     -- 이어서 접근한 경로로의 접근 수
   , COUNT(1) AS count2
  FROM
   activity_log_with_lead_path
  WHERE 
   -- 상세 페이지를 시작 지점으로 두기
   path0 = '/detail'
  GROUP BY
   path0, path1, path2
)
SELECT
   path0
 , count0
 , path1
 , count1
 , 100.0 * count1 / count0 AS rate1
 , path2
 , count2
 , 100.0 * count2 / count1 AS rate2
FROM
 raw_user_flow
ORDER BY
   count1 DESC    , count2 DESC
;
```


바로 위의 레코드와 같은 값을 가졌을 때 출력하지 않게 데이터 가공하기
```python
WITH
activuty_log_with_lead_path AS (
 SELECT
   session
 , stamp
 , path AS path0
   -- 곧바로 접근한 경로 추출하기
 , LEAD(path, 1) OVER(PARTITION BY session ORDER BY stamp ASC) AS path1
   -- 이어서 접근한 경로 추출하기
 , LEAD(path, 2) OVER(PARTITION BY session ORDER BY stamp ASC) AS path2
 FROM
  activity_log
)
, raw_user_flow AS (
  SELECT
	 path0
	 -- 시작 지점 경로로의 접근 수
   , SUM(COUNT(1)) OVER() AS count0
	 -- 곧바로 접근한 경로 (존재하지 않는 경우 문자열 NULL)
   , COALESCE(path1, 'NULL') AS path1
	 -- 곧바로 접근한 경로로의 접근 수
   , SUM(COUNT(1)) OVER(PARTITION BY path0, path1) AS count1
	 -- 이어서 접근한 경로 (존재하지 않는 경우 문자열 'NULL' 지정)
   , COALESCE(path2, 'NULL') AS path2
     -- 이어서 접근한 경로로의 접근 수
   , COUNT(1) AS count2
  FROM
   activity_log_with_lead_path
  WHERE 
   -- 상세 페이지를 시작 지점으로 두기
   path0 = '/detail'
  GROUP BY
   path0, path1, path2
)
SELECT
    CASE
     WHEN
	  COALESCE(
	  -- 바로 위의 레코드가 가진 path0 추출하기(존재하지 않는 경우 NOT FOUND로 지정)
	   LAG(path0)
	    OVER(ORDER BY count1 DESC, count2 DESC)
      , 'NOT FOUND') <> path0
     THEN path0
    END AS path0
  , CASE
    WHEN 
	  COALESCE(
	   LAG(path0)
	    OVER(ORDER BY count1 DESC, count2 DESC)
      , 'NOT FOUND') <> path0
     THEN count0
   END AS count0
  , CASE
    WHEN
	 COALESCE(
	 -- 바로 위의 레코드가 가진 여러 값을 추출할 수 있게 문자열 결합 후 추출하기
	 -- ■ PostgreSQL, Redshift의 경우 || 연산자 사용하기
	 -- ■ Hive, BigQuery, SparkSQL의 경우 concat 함수 사용하기
	   LAG(path0 || path1)
		OVER(ORDER BY count1 DESC, count2 DESC)
	  , 'NOT FOUND') <> (path0 || path1)
    THEN path1
   END AS page1
  , CASE
    WHEN
	 COALESCE(
	  LAG(path0 || path1)
		OVER(ORDER BY count1 DESC, count2 DESC)
	 , 'NOT FOUND') <> (path0 || path1)
	THEN count1
   END AS count1
  , CASE
    WHEN 
	 COALESCE(
	  LAG(path0 || path1)
		OVER(ORDER BY count1 DESC, count2 DESC)
	 , 'NOT FOUND') <> (path0 || path1)
	THEN 100.0 * count1 / count0
   END AS rate1
  , CASE
     WHEN 
	  COALESCE(
	   LAG(path0 || path1 || path2)
		OVER(ORDER BY count1 DESC, count2 DESC)
	  , 'NOT FOUND') <> (path0 || path1 || path2)
	 THEN path2
   END AS page2
  , CASE
     WHEN 
	  COALESCE(
	   LAG(path0 || path1 || path2)
		OVER(ORDER BY count1 DESC, count2 DESC)
	  , 'NOT FOUND') <> (path0 || path1 || path2)
	 THEN count2
   END AS count2
  , CASE
     WHEN
	  COALESCE(
	   LAG(path0 || path1 || path2)
		OVER(ORDER BY count1 DESC, count2 DESC)
	  , 'NOT FOUND') <> (path0 || path1 || path2)
	 THEN 100.0 * count2 / count1
	END AS rate2
FROM
 raw_user_flow
ORDER BY
   count1 DESC
 , count2 DESC
;
```


/detail 페이지 이전의 사용자 흐름을 집계하는 쿼리문
```python
WITH
activity_log_with_lag_path AS (
  SELECT
	session
  , stamp
  , path AS path0
	-- 바로 전에 접근한 경로 추출하기(존재하지 않는 경우 문자열 'NULL'로 지정하기)
  , COALESCE(LAG(path, 1) OVER(PARTITION BY session ORDER BY stamp ASC), 'NULL') AS path1
	-- 그 전에 접근한 경로 추출하기(존재하지 않는 경우 문자열 'NULL'로 지정하기)
  , COALESCE(LAG(path, 2) OVER(PARTITION BY session ORDER BY stamp ASC), 'NULL') AS path2
 FROM
  activity_log
)
, raw_user_flow AS (
  SELECT
	 path0
	 -- 시작 지점 경로로의 접근 수
   , SUM(COUNT(1)) OVER() AS count0
   , path1
	 -- 바로 전의 경로로의 접근 수
   , SUM(COUNT(1)) OVER(PARTITION BY path0, path1) AS count1
   , path2
	 -- 그 전에 접근한 경로로의 접근 수
   , COUNT(1) AS count2
 FROM
  activity_log_with_lag_path
 WHERE
  -- 상세 페이지를 시작 지점으로 두기
  path0 = '/detail'
 GROUP BY
  path0, path1, path2
)
SELECT
   path2
 , count2
 , 100.0 * count2 / count1 AS rate2
 , path1
 , count1
 , 100.0 * count1 / count0 AS rate1
 , path0
 , count0
FROM
 raw_user_flow
ORDER BY
   count1 DESC
 , count2 DESC
;
```

이번 절에서 소개한 SQL과 함께 사용해서 컴퓨터 사용자, 스마트폰 사용자,

광고 유입자에 따라 어떤 흐름이 발생하는지 확인해보세요.

새로운 문제를 찾고 해결할 수  있을 것입니다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 15강 페이지 387 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어