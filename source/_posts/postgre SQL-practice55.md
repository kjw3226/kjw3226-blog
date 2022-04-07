---
title: postgre SQL-practice55
tag: postgre SQL-practice55
date: 2022-04-07
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'7장  18강 이상값 검출하기'의

'2. 크롤러 제외하기'로 넘어갔으며

페이지 424 ~ 428을 참고하였다.


규칙을 기반으로 크롤러를 제외하는 쿼리문
```python
SELECT
 *
FROM
  action_log_with_noise
WHERE
 NOT
 --크롤러 판정 기준
 (   user_agent LIKE '%bot%'
  OR user_agent LIKE '%crawler%'
  OR user_agent LIKE '%spider%'
  OR user_agent LIKE '%archiver%'
 )
;
```

마스터 데이터를 사용해 제외하는 쿼리문
```python
WITH
mst_bot_user_agent AS (
	       SELECT '%bot%'       AS rule
 UNION ALL SELECT '%crawler%'   AS rule
 UNION ALL SELECT '%spider%'    AS rule
 UNION ALL SELECT '%archiver%'  AS rule
)
, filtered_action_log AS (
 SELECT
	l.stamp, l.session, l.action, l.products
  , l.url, l.ip, l.user_agent
 --UserAgent의 규칙에 해당하지 않는 로그만 남기기
 --■ PostgreSQL, Redshift, BigQuery의 경우
 --  WHERE 구문에 상관 서브쿼리를 사용할 수 있음
  FROM
   action_log_with_noise AS l
  WHERE 
   NOT EXISTS (
	SELECT 1
	FROM mst_bot_user_agent AS m
	WHERE
	 l.user_agent LIKE m.rule
   )
--■상관 서브쿼리를 사용할 수 없는 경우
-- CROSS JOIN으로 마스터 데이터를 결합하고,
-- HAVING 구문으로 일치하는 규칙이 0인(없는) 레코드만 남기기
-- ※ PostgreSQL, Hive, Redshift, BigQuery, SparkSQL의 경우
--FROM
--   action_log_with_noise AS l
--  CROSS JOIN
--   mst_bot_user_agent AS m
--GROUP BY
--   l.stamp, l.session, l.action, l.products
-- , l.url, l.ip, l.user_agent
--HAVING SUM(CASE WHEN l.user_agent LIKE m.rule THEN 1 ELSE 0 END) = 0
)
SELECT
 *
FROM
 filtered_action_log
;
```

<크롤러 감시하기>

접근이 많은 사용자 에이전트를 확인하는 쿼리문
```python
WITH
mst_bot_user_agent AS (
	       SELECT '%bot%'       AS rule
 UNION ALL SELECT '%crawler%'   AS rule
 UNION ALL SELECT '%spider%'    AS rule
 UNION ALL SELECT '%archiver%'  AS rule
)
, filtered_action_log AS (
SELECT
	l.stamp, l.session, l.action, l.products
  , l.url, l.ip, l.user_agent
 --UserAgent의 규칙에 해당하지 않는 로그만 남기기
 --■ PostgreSQL, Redshift, BigQuery의 경우
 --  WHERE 구문에 상관 서브쿼리를 사용할 수 있음
  FROM
   action_log_with_noise AS l
  WHERE 
   NOT EXISTS (
	SELECT 1
	FROM mst_bot_user_agent AS m
	WHERE
	 l.user_agent LIKE m.rule
   )
SELECT
   user_agent
 , COUNT(1) AS count
 , 100.0
   * SUM(COUNT(1)) OVER(ORDER BY COUNT(1) DESC
	  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
   / SUM(COUNT(1)) OVER() AS cumulative_ratio
FROM
 filtered_action_log
GROUP BY
 user_agent
ORDER BY
 count DESC
;
)
```

지금까지는 접근이 없었던 크롤러가 어느 날을 기점으로 접근이 많아지거나,

새로운 크롤러가 추가되는 등 접근 상황은 계속 변합니다.

따라서 매주 또는 적어도 매달 크롤러 접근 로그를 확인하기 바랍니다.

(데이터 분석을 위한 SQL 레시피-7장 데이터 활용의

정밀도를 높이는 분석 기술 18강 이상값 검출하기 428 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어