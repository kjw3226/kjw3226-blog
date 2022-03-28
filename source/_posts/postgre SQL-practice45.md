---
title: postgre SQL-practice45
tag: postgre SQL-practice45
date: 2022-03-28
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'6장  15강 사이트 내의 사용자 행동 파악하기

6. 폴아웃 리포트를 사용해 사용자 회유를 가시화하기'

로 넘어갔으며, 페이지는 372 ~ 378을 참고하였다.


폴아웃 단계 순서를 접근 로그와 결합하는 쿼리문
```python
WITH
mst_fallout_step AS (
 -- 폴아웃 단계와 경로의 마스터 테이블
	      SELECT 1 AS step, '/'           AS path
UNION ALL SELECT 2 AS step, '/search_list' AS path
UNION ALL SELECT 3 AS step, '/detail'     AS path
UNION ALL SELECT 4 AS step, '/input'      AS path
UNION All SELECT 5 AS step, '/complete'    AS path
)
, activity_log_with_fallout_step AS (
  SELECT
	 l.session
   , m.step
   , m.path
	 -- 첫 접근과 마지막 접근 시간 구하기
   , MAX(l.stamp) AS max_stamp
   , MIN(l.stamp) AS min_stamp
  FROM
	 mst_fallout_step AS m
	JOIN 
	 activity_log AS l
	 ON m.path = l.path
  GROUP BY
   -- 세션별로 단계 순서와 경로를 사용해 집약하기
   l.session, m.step, m.path
)
, activity_log_with_mod_fallout_step AS (
  SELECT
	 session
   , step
   , path
   , max_stamp
	 -- 직전 단계에서의 첫 접근 시간 구하기
   , LAG(min_stamp)
	  OVER(PARTITION BY session ORDER BY step)
	 -- ■ Spark SQL의 경우 LAG 함수에 프레임 지정해야 함
	 -- OVER(PARTITION BY session ORDER BY step
     --   ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING)
	 AS lag_min_stamp
	 -- 세션에서의 단계 순서 최소값 구하기
   , MIN(step) OVER(PARTITION BY session) AS min_step
	 -- 해당 단계에 도달할 때까지 걸린 단계 수 누계
   , COUNT(1)
	   OVER(PARTITION BY session ORDER BY step
		 ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
	AS cum_count
  FROM
   activity_log_with_fallout_step
)
SELECT
 *
FROM
 activity_log_with_mod_fallout_step
ORDER BY 
 session, step
;
```


폴아웃 리포트에 필요한 로그를 압축하는 쿼리문
```python
WITH
mst_fallout_step AS (
 -- 폴아웃 단계와 경로의 마스터 테이블
	      SELECT 1 AS step, '/'           AS path
UNION ALL SELECT 2 AS step, '/search_list' AS path
UNION ALL SELECT 3 AS step, '/detail'     AS path
UNION ALL SELECT 4 AS step, '/input'      AS path
UNION All SELECT 5 AS step, '/complete'    AS path
)
, activity_log_with_fallout_step AS (
  SELECT
	 l.session
   , m.step
   , m.path
	 -- 첫 접근과 마지막 접근 시간 구하기
   , MAX(l.stamp) AS max_stamp
   , MIN(l.stamp) AS min_stamp
  FROM
	 mst_fallout_step AS m
	JOIN 
	 activity_log AS l
	 ON m.path = l.path
  GROUP BY
   -- 세션별로 단계 순서와 경로를 사용해 집약하기
   l.session, m.step, m.path
)
, activity_log_with_mod_fallout_step AS (
  SELECT
	 session
   , step
   , path
   , max_stamp
	 -- 직전 단계에서의 첫 접근 시간 구하기
   , LAG(min_stamp)
	  OVER(PARTITION BY session ORDER BY step)
	 -- ■ Spark SQL의 경우 LAG 함수에 프레임 지정해야 함
	 -- OVER(PARTITION BY session ORDER BY step
     --   ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING)
	 AS lag_min_stamp
	 -- 세션에서의 단계 순서 최소값 구하기
   , MIN(step) OVER(PARTITION BY session) AS min_step
	 -- 해당 단계에 도달할 때까지 걸린 단계 수 누계
   , COUNT(1)
	   OVER(PARTITION BY session ORDER BY step
		 ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
	AS cum_count
  FROM
   activity_log_with_fallout_step
)
, fallout_log AS (
  -- 폴아웃 리포트에 사용할 로그만 추출하기
  SELECT
	 session
   , step
   , path
  FROM
   activity_log_with_mod_fallout_step
  WHERE
  -- 세션에서 단계 순서가 1인지 확인하기
  min_step = 1
  -- 현재 단계 순서가 해당 단계의 도달할 때까지의 누계 단계 수와 같은지 확인하기
AND step = cum_count
  -- 직전 단계의 첫 접근 시간이 
  -- NULL 또는 현재 시간의 최종 접근 시간보다 이전인지 확인하기
AND (lag_min_stamp IS NULL
	OR max_stamp >= lag_min_stamp)
)
SELECT
 *
FROM
 fallout_log
ORDER BY
 session, step
;
```


폴아웃 리포트를 출력하는 쿼리문
```python
WITH
mst_fallout_step AS (
 -- 폴아웃 단계와 경로의 마스터 테이블
	      SELECT 1 AS step, '/'           AS path
UNION ALL SELECT 2 AS step, '/search_list' AS path
UNION ALL SELECT 3 AS step, '/detail'     AS path
UNION ALL SELECT 4 AS step, '/input'      AS path
UNION All SELECT 5 AS step, '/complete'    AS path
)
, activity_log_with_fallout_step AS (
  SELECT
	 l.session
   , m.step
   , m.path
	 -- 첫 접근과 마지막 접근 시간 구하기
   , MAX(l.stamp) AS max_stamp
   , MIN(l.stamp) AS min_stamp
  FROM
	 mst_fallout_step AS m
	JOIN 
	 activity_log AS l
	 ON m.path = l.path
  GROUP BY
   -- 세션별로 단계 순서와 경로를 사용해 집약하기
   l.session, m.step, m.path
)
, fallout_log AS (
  -- 폴아웃 리포트에 사용할 로그만 추출하기
  SELECT
	 session
   , step
   , path
  FROM
   activity_log_with_mod_fallout_step
  WHERE
  -- 세션에서 단계 순서가 1인지 확인하기
  min_step = 1
  -- 현재 단계 순서가 해당 단계의 도달할 때까지의 누계 단계 수와 같은지 확인하기
AND step = cum_count
  -- 직전 단계의 첫 접근 시간이 
  -- NULL 또는 현재 시간의 최종 접근 시간보다 이전인지 확인하기
AND (lag_min_stamp IS NULL
	OR max_stamp >= lag_min_stamp)
)
SELECT
   step
 , path
 , COUNT(1) AS count
   --<단계 순서> = 1인 URL부터의 이동률
 , 100.0 * COUNT(1)
   / FIRST_VALUE(COUNT(1))
      OVER(ORDER BY step ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
   AS first_trans_rate
   -- 직전 단계까지의 이동률
 , 100.0 * COUNT(1)
   / LAG(COUNT(1)) OVER(ORDER BY step ASC)
   -- ■ SparkSQL의 경우 LAG 함수에 프레임 지정해야 함
   -- / LAG(COUNT(1)) OVER(ORDER BY step ASC ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING)
   AS step_trans_rate
FROM
  fallout_log
GROUP BY
  step, path
ORDER BY
  step
;
```


폴아웃 리포트는 웹사이트가 사용자를 어떻게 유도하는지를 대략적으로 

파악하고 싶을 때 굉장히 유용한 리포트입니다. 

성과로 이어진 사용자와 이어지지 못한 사용자를 따로 구분해보면

유용한 정보를 더 얻을 수 있을 것입니다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 15강 페이지 378 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어