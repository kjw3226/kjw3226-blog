---
title: postgre SQL-practice29
tag: postgre SQL-practice29
date: 2022-03-04
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'5장  12강 시계열에 따른 사용자 전체의 상태 변화 찾기 - 5. 사용 일수에 따른 정착률 집계하기'

페이지 270 ~ 275를 참고하였다.

등록일 다음날부터 7일 동안의 사용 일수와 28일 정착 플래그를 생성하는 쿼리문
```python
WITH
repeat_interval(index_name, interval_begin_date, interval_end_date) AS (
 -- ■Postgre SQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 -- ■Hive, Reshift, BigQuery, SparkSQL의 경우 SELECT 구문으로 대체 가능
 -- 8강 5절 참고하기
 VALUES('28 day retention', 22, 28)
)
, action_log_with_index_date AS (
  SELECT
	 u.user_id
   , u.register_date
   -- 액션의 날짜와 로그 전체의 최신 날짜를 날짜 자료형으로 변환하기
   , CAST(a.stamp AS date) AS action_date
   , MAX(CAST(a.stamp AS date)) OVER() AS latest_date
   -- ■ BigQuery의 경우 한 번 타임스탬프 자료형으로 변환하고 날짜 자료형으로 변환하기
   --, date(timestamp(a.stamp)) AS action_date
   --, MAX(date(timestamp(a.stamp))) OVER() AS latest_date
   , r.index_name
	
   -- ■ PostgreSQL의 경우는 다음과 같이 사용하기
   , CAST(u.register_date::date + '1day'::interval * r.interval_begin_date AS date)
	 AS index_begin__date
   , CAST(u.register_date::date + '1day'::interval * r.interval_end_date AS date)
	 AS index_end_date
	
   -- ■ Redshift의 겨우는 다음과 같이 사용하기
   --, dateadd(day, r.interval_begin_date, u.register_date::date) AS index_begin_date
   --, dateadd(day, r.interval_end_date, u.register_date::date) AS index_end_date
	
   -- ■ BigQuery의 경우는 다음과 같이 사용하기
   --, date_add(CAST(u.register_date AS date), interval r.interval_begin_date day)
   --, AS index_begin_date
   --, date_add(CAST(u.register_date AS date), interval r.interval_end_date day)
   --, AS index_end_date

   -- ■ Hive, SparkSQL의 경우는 다음과 같이 사용하기
   --, date_add(CAST(u.register_date AS date), r.interval_begin_date)
   --, AS index_begin_date
   --, date_add(CAST(u.register_date AS date), r.interval_end_date)
   --, AS index_end_date
 FROM
	mst_users AS u
  LEFT OUTER JOIN
	action_log AS a
  ON u.user_id = a.user_id
  CROSS JOIN
	repeat_interval AS r
)
, user_action_flag AS (
  SELECT
	 user_id
   , register_date
   , index_name
    -- 4. 지표의 대상 기간에 액션을 했는지 플래그로 나타내기
   , SIGN(
	  -- 3. 사용자 별로 대상 기간에 한 액션의 합계 구하기
	   SUM(
		 -- 1. 대상 기간의 종료일이 로그의 최신 날짜 이전인지 확인하기
		 CASE WHEN index_end_date <= latest_date THEN
		   -- 2. 지표의 대상 기간에 액션을 했다면 1, 안 했으면 0 지정하기
		   CASE WHEN action_date BETWEEN index_begin_date AND index_and_date
		       THEN 1 ELSE 0
		   END
		 END
	   )
   )AS index_date_action
 FROM
  action_log_with_index_date
 GROUP BY
  user_id, register_date, index_name, index_begin_date, idex_end_date
)
, register_action_flag AS (
  SELECT
	m.user_id
  , COUNT(DISTINCT CAST(a.stamp AS date)) AS dt_count
  -- ■ BigQuery의 경우 다음과 같이 사용하기
  -- , COUNT(DISTINCT date(timestamp(a.stamp))) AS dt_count
  , index_name
  , index_date_action
  FROM 
	 mst_users AS m
   LEFT JOIN
	action_log AS a
	ON m.user_id = a.user_id
	-- 등록 다음날부터 7일 이내의 액션 로그 결합하기
	-- ■ PostgreSQL, Redshift의 경우 다음과 같이 사용하기
	AND CAST(a.stmap AS date)
	     BETWEEN CAST(m.register_date AS date) + interval '1 day'
	        AND CAST(m.register_date AS date) + interval '8 days'
	-- ■ BigQuery의 경우 다음과 같이 사용하기
	-- AND date(timestamp(a.stamp))
	--      BETWEEN date_add(CAST(m.register_date AS date), interval 1 day)
	--         AND date_add(CAST(m.register_date AS date), interval 8 day)
	--■ SparkSQL의 경우 다음과 같이 사용하기
	--AND CAST(a.stamp AS date)
	--     BETWEEN date_add(CAST(m.register_date AS date), 1)
	--        AND date_add(CAST(m.register_date AS date), 8)
	--■ Hive의 경우 JOIN 구문에 BETWEEN 구문을 사용 할 수 없으므로
	--   WHERE 구문을 사용해야 함
  LEFT JOIN
	user_action_flag AS f
	ON m.user_id = f.user_id
WHERE
  f.index_date_action IS NOT NULL
GROUP BY
   m.user_id
 , f.index_name
 , f.index_date_action
)
SELECT *
FROM
 register_action_flag;
```

사용 일수에 따른 정착률을 집계하는 쿼리문
```python
WITH
repeat_interval(index_name, interval_begin_date, interval_end_date) AS (
 -- ■Postgre SQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 -- ■Hive, Reshift, BigQuery, SparkSQL의 경우 SELECT 구문으로 대체 가능
 -- 8강 5절 참고하기
 VALUES('28 day retention', 22, 28)
)
, action_log_with_index_date AS (
  SELECT
	 u.user_id
   , u.register_date
   -- 액션의 날짜와 로그 전체의 최신 날짜를 날짜 자료형으로 변환하기
   , CAST(a.stamp AS date) AS action_date
   , MAX(CAST(a.stamp AS date)) OVER() AS latest_date
   -- ■ BigQuery의 경우 한 번 타임스탬프 자료형으로 변환하고 날짜 자료형으로 변환하기
   --, date(timestamp(a.stamp)) AS action_date
   --, MAX(date(timestamp(a.stamp))) OVER() AS latest_date
   , r.index_name
	
   -- ■ PostgreSQL의 경우는 다음과 같이 사용하기
   , CAST(u.register_date::date + '1day'::interval * r.interval_begin_date AS date)
	 AS index_begin__date
   , CAST(u.register_date::date + '1day'::interval * r.interval_end_date AS date)
	 AS index_end_date
	
   -- ■ Redshift의 겨우는 다음과 같이 사용하기
   --, dateadd(day, r.interval_begin_date, u.register_date::date) AS index_begin_date
   --, dateadd(day, r.interval_end_date, u.register_date::date) AS index_end_date
	
   -- ■ BigQuery의 경우는 다음과 같이 사용하기
   --, date_add(CAST(u.register_date AS date), interval r.interval_begin_date day)
   --, AS index_begin_date
   --, date_add(CAST(u.register_date AS date), interval r.interval_end_date day)
   --, AS index_end_date

   -- ■ Hive, SparkSQL의 경우는 다음과 같이 사용하기
   --, date_add(CAST(u.register_date AS date), r.interval_begin_date)
   --, AS index_begin_date
   --, date_add(CAST(u.register_date AS date), r.interval_end_date)
   --, AS index_end_date
 FROM
	mst_users AS u
  LEFT OUTER JOIN
	action_log AS a
  ON u.user_id = a.user_id
  CROSS JOIN
	repeat_interval AS r
)
, user_action_flag AS (
  SELECT
	 user_id
   , register_date
   , index_name
    -- 4. 지표의 대상 기간에 액션을 했는지 플래그로 나타내기
   , SIGN(
	  -- 3. 사용자 별로 대상 기간에 한 액션의 합계 구하기
	   SUM(
		 -- 1. 대상 기간의 종료일이 로그의 최신 날짜 이전인지 확인하기
		 CASE WHEN index_end_date <= latest_date THEN
		   -- 2. 지표의 대상 기간에 액션을 했다면 1, 안 했으면 0 지정하기
		   CASE WHEN action_date BETWEEN index_begin_date AND index_and_date
		       THEN 1 ELSE 0
		   END
		 END
	   )
   )AS index_date_action
 FROM
  action_log_with_index_date
 GROUP BY
  user_id, register_date, index_name, index_begin_date, idex_end_date
)
, register_action_flag AS (
  SELECT
	m.user_id
  , COUNT(DISTINCT CAST(a.stamp AS date)) AS dt_count
  -- ■ BigQuery의 경우 다음과 같이 사용하기
  -- , COUNT(DISTINCT date(timestamp(a.stamp))) AS dt_count
  , index_name
  , index_date_action
  FROM 
	 mst_users AS m
   LEFT JOIN
	action_log AS a
	ON m.user_id = a.user_id
	-- 등록 다음날부터 7일 이내의 액션 로그 결합하기
	-- ■ PostgreSQL, Redshift의 경우 다음과 같이 사용하기
	AND CAST(a.stmap AS date)
	     BETWEEN CAST(m.register_date AS date) + interval '1 day'
	        AND CAST(m.register_date AS date) + interval '8 days'
	-- ■ BigQuery의 경우 다음과 같이 사용하기
	-- AND date(timestamp(a.stamp))
	--      BETWEEN date_add(CAST(m.register_date AS date), interval 1 day)
	--         AND date_add(CAST(m.register_date AS date), interval 8 day)
	--■ SparkSQL의 경우 다음과 같이 사용하기
	--AND CAST(a.stamp AS date)
	--     BETWEEN date_add(CAST(m.register_date AS date), 1)
	--        AND date_add(CAST(m.register_date AS date), 8)
	--■ Hive의 경우 JOIN 구문에 BETWEEN 구문을 사용 할 수 없으므로
	--   WHERE 구문을 사용해야 함
  LEFT JOIN
	user_action_flag AS f
	ON m.user_id = f.user_id
WHERE
  f.index_date_action IS NOT NULL
GROUP BY
   m.user_id
 , f.index_name
 , f.index_date_action
)
SELECT
    dt_count AS dates
  , COUNT(user_id) As users
  , 100.0 * COUNT(user_id) / SUM(COUNT(user_id)) OVER () AS user_ratio
  , 100.0
    * SUM(COUNT(user_id))
	   OVER(ORDER BY index_name, dt_count
		ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
	/ SUM(COUNT(user_id)) OVER() AS cum_ratio
  , SUM(index_date_action) AS achieve_users
  , AVG(100.0 * index_date_action) AS achieve_ratio
FROM
 register_action_flag
GROUP BY
 index_name, dt_count
ORDER BY
 index_name, dt_count;
```

이번 절에서는 등록일 다음날부터 7일 동안의 사용 일수를 사용해 집계했지만, 사용 일수 대신 SNS 서비스에

올린 글의 개수 또는 소셜 게임의 레벨 등으로 대상을 변경해서 사용하는 경우도 많으므로 참고하기 바랍니다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 12강 페이지 275 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어
