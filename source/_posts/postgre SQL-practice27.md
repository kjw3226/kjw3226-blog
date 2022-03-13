---
title: postgre SQL-practice27
tag: postgre SQL-practice27
date: 2022-03-02
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

페이지 257 ~ 263을 참고했다.

5장  12강 시계열에 따른 사용자 전체의 상태 변화 찾기 - 3.지속과 정착에 영향을 주는 액션 집계하기

의 쿼리문을 작성하는 실습을 진행했다.

모든 사용자와 액션의 조합을 도출하는 쿼리문
```python
WITH
repeat_interval(index_name, interval_begin_date, interval_end_date) AS (
 -- ■ Postgre SQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 -- ■ Hive, Redshift, BigQuery, SparkSQL의 경우 SELECT 구문으로 대체 가능
 -- 4강 5절 참고하기
 VALUES ('01 day repeat', 1, 1)
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
, mst_actions AS (
	        SELECT 'view'   AS action
  UNION ALL SELECT 'comment' AS action
  UNION ALL SELECT 'follow'  AS action
)
, mst_user_actions AS (
  SELECT
	 u.user_id
   , u.register_date
   , a.action
  FROM
	 mst_users AS u
   CROSS JOIN
	mst_actions AS a
)
SELECT *
FROM mst_users_actions
ORDER BY user_id, action
;
```

사용자의 액션 로그를 0, 1의 플래그로 표현하는 쿼리문
```python
WITH
repeat_interval(index_name, interval_begin_date, interval_end_date) AS (
 -- ■ Postgre SQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 -- ■ Hive, Redshift, BigQuery, SparkSQL의 경우 SELECT 구문으로 대체 가능
 -- 4강 5절 참고하기
 VALUES ('01 day repeat', 1, 1)
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
, mst_actions AS (
	        SELECT 'view'   AS action
  UNION ALL SELECT 'comment' AS action
  UNION ALL SELECT 'follow'  AS action
)
, mst_user_actions AS (
  SELECT
	 u.user_id
   , u.register_date
   , a.action
  FROM
	 mst_users AS u
   CROSS JOIN
	mst_actions AS a
)
, register_action_flag AS (
  SELECT DISTINCT
	 m.user_id
   , m.register_date
   , m.action
   , CASE
	  WHEN a.action IS NOT NULL THEN 1
	  ELSE 0
    END AS do_action
  , index_name
  , index_date_action
  FROM
	 mst_user_actions AS m
   LEFT JOIN
	action_log AS a
	ON m.user_id = a.user_id
	AND CAST(m.register_date AS date) = CAST(a.stamp AS date)
	-- ■ BigQuery의 경우 한 번 타임스탬프 자료형으로 변환한 뒤 날짜 자료형으로 변환하기
   --AND CAST(m.register_date AS date) = date(timestamp(a.stamp))
    AND m.action = a.action
   LEFT JOIN
	 user_action_flag AS f
	 ON m.user_id = f.user_id
 WHERE
   f.index_date_action IS NOT NULL
)
SELECT
  *
FROM
 register_action_flag
ORDER BY
 user_id, index_name, action
;
```
액션에 따른 지속률과 정착률을 집계하는 쿼리문
```python
WITH
repeat_interval(index_name, interval_begin_date, interval_end_date) AS (
 -- ■ Postgre SQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 -- ■ Hive, Redshift, BigQuery, SparkSQL의 경우 SELECT 구문으로 대체 가능
 -- 4강 5절 참고하기
 VALUES ('01 day repeat', 1, 1)
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
, mst_actions AS (
	        SELECT 'view'   AS action
  UNION ALL SELECT 'comment' AS action
  UNION ALL SELECT 'follow'  AS action
)
, mst_user_actions AS (
  SELECT
	 u.user_id
   , u.register_date
   , a.action
  FROM
	 mst_users AS u
   CROSS JOIN
	mst_actions AS a
)
, register_action_flag AS (
  SELECT DISTINCT
	 m.user_id
   , m.register_date
   , m.action
   , CASE
	  WHEN a.action IS NOT NULL THEN 1
	  ELSE 0
    END AS do_action
  , index_name
  , index_date_action
  FROM
	 mst_user_actions AS m
   LEFT JOIN
	action_log AS a
	ON m.user_id = a.user_id
	AND CAST(m.register_date AS date) = CAST(a.stamp AS date)
	-- ■ BigQuery의 경우 한 번 타임스탬프 자료형으로 변환한 뒤 날짜 자료형으로 변환하기
   --AND CAST(m.register_date AS date) = date(timestamp(a.stamp))
    AND m.action = a.action
   LEFT JOIN
	 user_action_flag AS f
	 ON m.user_id = f.user_id
 WHERE
   f.index_date_action IS NOT NULL
)
SELECT
   action
 , COUNT(1) users
 , AVG(100.0 * do_action) AS usage_rate
 , index_name
 , AVG(CASE do_action WHEN 1 THEN 100.0 * index_date_action END) AS idx_rate
 , AVG(CASE do_action WHEN 0 THEN 100.0 * index_date_action END) AS mo_action_idx_rate
FROM 
 register_action_flag
GROUP BY
 index_name, action
ORDER BY
 index_name, action
;
```

특정 액션의 실행이 지속률과 정착률 상승으로 이어질 석으로 보여도, 해당 액션을 실행하는 

진입 장벽이 높다면, 지속률과 정착률에 영향을 조금 주더라도 액션을 실행하는 진입 장벽이

낮은 액션을 기반으로 대책을 세우는 것이 좋습니다. (예 : 동영상 업로드보다는 이미지 업로드 촉진하기 등)

이번 절에서는 액션 여부를 기준으로 집계했지만, 액션 수에 따라서도 차이가 있을 수 있습니다.

다음 절에서는 액션 수에 주목해서 정착률을 집계하도록 합시다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 12강 페이지 263 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어
