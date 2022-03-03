---
title: postgre SQL-practice28
tag: postgre SQL-practice28
date: 2022-03-03
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'5장  12강 시계열에 따른 사용자 전체의 상태 변화 찾기 - 4. 액션 수에 따른 정착률 집계하기'

페이지 263 ~ 270을 참고했다.

액션의 계급 마스터와 사용자 액션 플래그의 조합을 산출하는 쿼리문
```python
WITH
repeat_interval(index_name, interval_begin_date, interval_end_date) AS (
  -- ■PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
  -- ■Hive, Redshift, BigQuery, SparkSQL의 경우 SELECT 구문으로 대체 가능
  -- 8강 5절 참조하기
  VALUES('14 day retention', 8, 14)
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
, mst_action_bucket(action, min_count, max_count) AS (
  -- 액션 단계 마스터
  -- ■PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
  -- ■Hive, Redshift, BigQuery, SparkSQL의 경우 SELECT 구문과 UNION ALL로 대체 가능
  VALUES
	('comment', 0,   0)
  , ('comment', 1,   5)
  , ('comment', 6,  10)
  , ('comment', 11,  9999) -- 최대값으로 간단하게 9999 입력
  , ('follow', 0,    0)
  , ('follow', 1,    5)
  , ('follow', 6,   10)
  , ('follow', 11,   9999) -- 최대값으로 간단하게 9999 입력
)
, mst_user_action_bucket AS (
  -- 사용자 마스터와 액션 단계 마스터 조합하기
  SELECT
	 u.user_id
   , u.register_date
   , a.action
   , a.min_count
   , a.max_count
  FROM
	 mst_users as u
  CROSS JOIN
   mst_action_bucket AS a
)
SELECT *
FROM
 mst_user_action_bucket
ORDER BY
 user_id, action, min_count
;
```

등록 후 7일 동안의 액션 수를 집계하는 쿼리문
```python
WITH
repeat_interval(index_name, interval_begin_date, interval_end_date) AS (
  -- ■PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
  -- ■Hive, Redshift, BigQuery, SparkSQL의 경우 SELECT 구문으로 대체 가능
  -- 8강 5절 참조하기
  VALUES('14 day retention', 8, 14)
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
, mst_action_bucket(action, min_count, max_count) AS (
  -- 액션 단계 마스터
  -- ■PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
  -- ■Hive, Redshift, BigQuery, SparkSQL의 경우 SELECT 구문과 UNION ALL로 대체 가능
  VALUES
	('comment', 0,   0)
  , ('comment', 1,   5)
  , ('comment', 6,  10)
  , ('comment', 11,  9999) -- 최대값으로 간단하게 9999 입력
  , ('follow', 0,    0)
  , ('follow', 1,    5)
  , ('follow', 6,   10)
  , ('follow', 11,   9999) -- 최대값으로 간단하게 9999 입력
)
, mst_user_action_bucket AS (
  -- 사용자 마스터와 액션 단계 마스터 조합하기
  SELECT
	 u.user_id
   , u.register_date
   , a.action
   , a.min_count
   , a.max_count
  FROM
	 mst_users as u
  CROSS JOIN
   mst_action_bucket AS a
)
, register_action_flag AS (
  -- 등록일에서 7일 후까지의 액션 수를 세고,
  -- 액션 단계와 14일 정착 달성 플래그 계산하기
  SELECT
	 m.user_id
   , m.action
   , m.min_count
   , m.max_count
   , COUNT(a.action) AS action_count
   , CASE
	  WHEN COUNT(a.action) BETWEEN m.min_count AND m.max_count THEN 1
	  ELSE 0
	END AS achieve
   , index_name
   , index_date_action
  FROM
	 mst_user_action_bucket AS m
	LEFT JOIN
	  action_log AS a
	  ON m.user_id = a.user_id
	  -- 등록일 당일부터 7일 후까지의 액션 로그 결합하기
	  -- ■PostgreSQL, Redshift의 경우
	  AND CAST(a.stamp AS date)
	      BETWEEN CAST(m.register_date AS date)
	         AND CAST(m.register_date AS date) + interval '7 days'
	  -- ■BigQuery의 경우
	  -- AND date(timestamp(a.stamp))
	  --      BETWEEN CAST(m.register_date AS date)
	  --         AND date_add(CAST(m.register_date AS date), 7)
	  -- ■Hive의 경우 JOIN 구문에 BETWEEN 구문을 사용할 수 없으므로 WHERE 구문을 사용해야 함
	  AND m.action = a.action
    LEFT JOIN
	 user_action_flag AS f
	 ON m.user_id = f.user_id
 WHERE
  f.index_date_action IS NOT NULL
 GROUP BY
	m.user_id
  , m.action
  , m.min_count
  , m.max_count
  , f.index_name
  , f.index_date_action
)
SELECT *
FROM
 register_action_flag
ORDER BY
 user_id, action, min_count
;
```

등록 후 7일 동안의 액션 횟수별로 14일 정착률을 집계하는 쿼리문
```python
WITH
repeat_interval(index_name, interval_begin_date, interval_end_date) AS (
  -- ■PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
  -- ■Hive, Redshift, BigQuery, SparkSQL의 경우 SELECT 구문으로 대체 가능
  -- 8강 5절 참조하기
  VALUES('14 day retention', 8, 14)
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
, mst_action_bucket(action, min_count, max_count) AS (
  -- 액션 단계 마스터
  -- ■PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
  -- ■Hive, Redshift, BigQuery, SparkSQL의 경우 SELECT 구문과 UNION ALL로 대체 가능
  VALUES
	('comment', 0,   0)
  , ('comment', 1,   5)
  , ('comment', 6,  10)
  , ('comment', 11,  9999) -- 최대값으로 간단하게 9999 입력
  , ('follow', 0,    0)
  , ('follow', 1,    5)
  , ('follow', 6,   10)
  , ('follow', 11,   9999) -- 최대값으로 간단하게 9999 입력
)
, mst_user_action_bucket AS (
  -- 사용자 마스터와 액션 단계 마스터 조합하기
  SELECT
	 u.user_id
   , u.register_date
   , a.action
   , a.min_count
   , a.max_count
  FROM
	 mst_users as u
  CROSS JOIN
   mst_action_bucket AS a
)
, register_action_flag AS (
  -- 등록일에서 7일 후까지의 액션 수를 세고,
  -- 액션 단계와 14일 정착 달성 플래그 계산하기
  SELECT
	 m.user_id
   , m.action
   , m.min_count
   , m.max_count
   , COUNT(a.action) AS action_count
   , CASE
	  WHEN COUNT(a.action) BETWEEN m.min_count AND m.max_count THEN 1
	  ELSE 0
	END AS achieve
   , index_name
   , index_date_action
  FROM
	 mst_user_action_bucket AS m
	LEFT JOIN
	  action_log AS a
	  ON m.user_id = a.user_id
	  -- 등록일 당일부터 7일 후까지의 액션 로그 결합하기
	  -- ■PostgreSQL, Redshift의 경우
	  AND CAST(a.stamp AS date)
	      BETWEEN CAST(m.register_date AS date)
	         AND CAST(m.register_date AS date) + interval '7 days'
	  -- ■BigQuery의 경우
	  -- AND date(timestamp(a.stamp))
	  --      BETWEEN CAST(m.register_date AS date)
	  --         AND date_add(CAST(m.register_date AS date), 7)
	  -- ■Hive의 경우 JOIN 구문에 BETWEEN 구문을 사용할 수 없으므로 WHERE 구문을 사용해야 함
	  AND m.action = a.action
    LEFT JOIN
	 user_action_flag AS f
	 ON m.user_id = f.user_id
 WHERE
  f.index_date_action IS NOT NULL
 GROUP BY
	m.user_id
  , m.action
  , m.min_count
  , m.max_count
  , f.index_name
  , f.index_date_action
)
SELECT
   action
 --■ PostgreSQL, Redshift의 경우는 다음과 같이 문자열 연결하기
 , min_count || '~' || max_count AS count_range
 --■ BigQuery의 경우는 다음과 같이 문자열 연결하기
 --, CONCAT(CAST(min_count AS string), '~', CAST(max_count AS string))
 --  AS count_range
 , SUM(CASE achieve WHEN 1 THEN 1 ELSE 0 END)AS achieve
 , index_name
 , AVG(CASE achieve WHEN 1 THEN 100.0 * index_date_action END) AS achieve_index_rate
FROM
   register_action_flag
GROUP BY
   index_name, action, min_count, max_count
ORDER BY
   index_name, action, min_count;
```
이처럼 액션별로 사용자를 집계하면, 사용자가 어떤 기능을 더 많이 사용하도록 유도해야 하는지 알 수 있다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 12강 페이지 270 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어
