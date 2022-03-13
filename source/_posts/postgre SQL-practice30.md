---
title: postgre SQL-practice30
tag: postgre SQL-practice30
date: 2022-03-12
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

페이지 275~279를 참고했다.

'5장  12강 시계열에 따른 사용자 전체의 상태 변화 찾기 - 6. 사용자의 잔존율 집계하기'

를 보고 쿼리문 작성 실습을 하였다.

12개월 후 까지의 월을 도출하기 위한 보조 테이블을 만드는 쿼리문
```python
WITH
mst_intervals(interval_month) AS (
 --12개월 동안의 순번 만들기(generate_series 등으로 대체 가능)
 --■ PostgreSQL의 경우 VALUES 구문으로 일시 테이블 만들기
 --■ Hive, Redashift, BigQuery, SparkSQL의 경우 SELECT 구문과 UNION ALL로 대체 가능
 -- 8강 5절 참고하기
 VALUES (1), (2), (3), (4), (5), (6)
	  , (7), (8), (9), (10), (11), (12)
)
SELECT *
FROM mst_intervals
;
```

등록 월에서 12개월 후까지의 잔존율을 집계하는 쿼리문
```python
WITH
mst_intervals(interval_month) AS (
 --12개월 동안의 순번 만들기(generate_series 등으로 대체 가능)
 --■ PostgreSQL의 경우 VALUES 구문으로 일시 테이블 만들기
 --■ Hive, Redashift, BigQuery, SparkSQL의 경우 SELECT 구문과 UNION ALL로 대체 가능
 -- 8강 5절 참고하기
 VALUES (1), (2), (3), (4), (5), (6)
	  , (7), (8), (9), (10), (11), (12)
)
, mst_users_with_index_month AS (
  -- 사용자 마스터에 등록 월부터 12개월 후까지의 월을 추가하기
  SELECT
	 u.user_id
   , u.register_date
   -- n개월 후의 날짜, 등록일, 등록 월 n개월 후의 월 계산하기
   --■ PostgreSQL의 경우 다음과 같이 사용하기
	, CAST(u.register_date::date + i.interval_month * '1 month'::interval AS date)
	  AS index_date
	, substring(u.register_date, 1, 7) AS register_month
	, substring(CAST(
	   u.register_date::date + i.interval_month * '1 month'::interval
	  AS text), 1, 7) AS index_month
   --■ Redshift의 경우 다음과 같이 사용하기
   -- , dateadd(month, i.interval_month, u.register_date::date) AS index_date
   -- , substring(u.register_date, 1, 7) AS register_month
   -- , substring(
   --    CAST(dateadd(month, i.interval_month, u.register_date::date) AS text), 1, 7)
   -- AS index_month
   --■ BigQuery의 경우 다음과 같이 사용하기
   -- , date_add(date(timestamp(u.register_date)), interval i.interval_month month)
   -- AS index_date
   -- , substr(u.register_date, 1, 7) AS register_month
   -- , substr(CAST(
   -- 	 date_add(date(timestamp(u.register_date)), interval i.interval_month)
   --  AS string), 1, 7) AS index_month
   --■ Hive, SparkSQL의 경우 다음과 같이 사용하기
   --, add_months(u.register_date, i.interval_month) As index_date
   --, substing(u.register_date, 1, 7) AS register_month
   --, substring(
   --   CAST(add_months(u.register_date, i.interval_month) AS string), 1, 7)
   --  AS index_month
 FROM
	mst_users AS u
  CROSS JOIN
   mst_intervals AS i
)
, action_log_in_month AS (
  -- 액션 로그의 날짜에서 월 부분만 추출하기
  SELECT DISTINCT
	 user_id
   , substring(stamp, 1, 7) AS action_month
   -- ■ BigQuery의 경우는 substr 사용하기
   -- , substr(stamp, 1, 7) AS action_month
 FROM
  action_log
)
SELECT
 --사용자 마스터와 액션 로그를 결합한 뒤, 월별로 잔존율 집계하기
  u.register_month
, u.index_month
-- action_month이 NULL이 아니라면(액션을 했다면) 사용자 수 집계
, SUM(CASE WHEN a.action_month IS NOT NULL THEN 1 ELSE 0 END) AS users
, AVG(CASE WHEN a.action_month IS NOT NULL THEN 100.0 ELSE 0.0 END)
  AS retension_rate
FROM
   mst_users_with_index_month AS u
 LEFT JOIN
  action_log_in_month AS a
  ON u.user_id = a.user_id
  AND u.index_month = a.action_month
 GROUP BY
  u.register_month, u.index_month
 ORDER BY
  u.register_month, u.index_month
;
```

매일 확인해야 할 리포트는 아니지만, 장기적인 관점에서 사용자 등록과 

지속 사용을 파악할 때는 굉장히 유요할 수 있습니다. 

참고로 이러한 리포트를 작성할 때는 해당 월에 실시한 대책 또는 캠페인 등의

이벤트를 함께 기록하면, 수치 변화의 원인 등도 쉽게 파악할 수 있어서

더 효율적으로 활용할 수 있습니다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 12강 페이지 279 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어