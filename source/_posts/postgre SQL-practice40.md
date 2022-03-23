---
title: postgre SQL-practice40
tag: postgre SQL-practice40
date: 2022-03-23
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

오늘 부터는 14강이 끝나서

'6장  15강 사이트 내의 사용자 행동 파악하기

1. 입구 페이지와 출구 페이지 파악하기'

로 넘어가서 쿼리문 작성 실습을 했습니다.

페이지 343 ~ 350을 참고 했습니다.

각 세션의 입구 페이지와 출구 페이지 경로를 추출하는 쿼리문
```python
WITH
activity_log_with_landing_exit AS (
 SELECT
	session
  , path
  , stamp
  , FIRST_VALUE(path)
	 OVER(
	  PARTITION BY session
	  ORDER BY stamp ASC
	   ROWS BETWEEN UNBOUNDED PRECEDING
	            AND UNBOUNDED FOLLOWING
	 ) AS landing
  , LAST_VALUE(path)
	 OVER(
	  PARTITION BY session
	  ORDER BY stamp ASC
	   ROWS BETWEEN UNBOUNDED PRECEDING
                AND UNBOUNDED FOLLOWING
	 ) AS exit
 FROM activity_log
)
SELECT *
FROM
 activity_log_with_landing_exit
;
```

각 세션의 입구 페이지와 출구 페이지를 기반으로 방문 횟수를 추출하는 쿼리문
```python
WITH
activity_log_with_landing_exit AS (
 SELECT
	session
  , path
  , stamp
  , FIRST_VALUE(path)
	 OVER(
	  PARTITION BY session
	  ORDER BY stamp ASC
	   ROWS BETWEEN UNBOUNDED PRECEDING
	            AND UNBOUNDED FOLLOWING
	 ) AS landing
  , LAST_VALUE(path)
	 OVER(
	  PARTITION BY session
	  ORDER BY stamp ASC
	   ROWS BETWEEN UNBOUNDED PRECEDING
                AND UNBOUNDED FOLLOWING
	 ) AS exit
 FROM activity_log
)
, landing_count AS (
  -- 입구 페이지의 방문 횟수 집계하기
  SELECT
	 landing AS path
   , COUNT(DISTINCT session) AS count
  FROM 
	activity_log_with_landing_exit
  GROUP BY landing
)
, exit_count AS (
  -- 출구 페이지의 방문 횟수 집계하기
  SELECT 
	 exit AS path
   , COUNT(DISTINCT session) AS count
  FROM 
	activity_log_with_landing_exit
  GROUP BY exit
)
  -- 입구 페이지와 출구 페이지 방문 횟수 결과를 한꺼번에 출력하기
  SELECT 'landing' AS type, * FROM landing_count
UNION ALL
  SELECT 'exit'    AS type, * FROM exit_count
;
```

세션별 입구 페이지와 출구 페이지의 조합을 집계하는 쿼리문
```python
WITH
activity_log_with_landing_exit AS (
 SELECT
	session
  , path
  , stamp
  , FIRST_VALUE(path)
	 OVER(
	  PARTITION BY session
	  ORDER BY stamp ASC
	   ROWS BETWEEN UNBOUNDED PRECEDING
	            AND UNBOUNDED FOLLOWING
	 ) AS landing
  , LAST_VALUE(path)
	 OVER(
	  PARTITION BY session
	  ORDER BY stamp ASC
	   ROWS BETWEEN UNBOUNDED PRECEDING
                AND UNBOUNDED FOLLOWING
	 ) AS exit
 FROM activity_log
)
SELECT
   landing
 , exit
 , COUNT(DISTINCT session) AS count
FROM
 activity_log_with_landing_exit
GROUP BY
 landing, exit
;
```

웹 사이트 담당자는 최상위 페이지부터 사이트 설계를 시작합니다.

하지만 최상위 페이지 부터 조회를 시작하는 사용자는 의외로 거의

없습니다. 

상세 페이지부터 조회를 시작하는 사용자가 많은 사이트도 존재합니다.

사용자가 어디로 유입되는지 입구 페이지를 파악하려면 사이트를 

더 매력적으로 설계할 수 있을 것입니다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 15강 페이지 350 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어