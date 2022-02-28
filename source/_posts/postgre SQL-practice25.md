---
title: postgre SQL-practice25
tag: postgre SQL-practice25
date: 2022-02-28
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

어제에 이어서 이번엔 

페이지 239에서 바로 '5장 12강 2. 지속률과 정착률 산출하기'로 넘어가서

250 페이지까지 참고해서 쿼리문을 작성했다.

'로그 최근 일자'와 '사용자별 등록일의 다음날'을 계산하는 쿼리문
```python
WITH
action_log_with_mst_users AS(
 SELECT 
	u.user_id
  , u.register_date
  -- 액션 날짜와 로그 전체의 최신 날짜를 날짜 자료형으로 변환하기
  , CAST(a.stamp AS date) AS action_date
  , MAX(CAST(a.stamp AS date)) OVER() AS latest_date
  -- ■ BigQuery의 경우 한번 타임 스탬프 자료형으로 변환하고 날짜 자료형으로 변환하기
  -- , date(timestamp(a.stamp)) AS action_date
  -- , MAX(date(timestamp(a.stamp))) OVER() AS latest_date
	
  -- 등록일 다음날의 날짜 계산하기
  -- ■ PostgreSQL의 경우는 다음과 같이 사용하기
  , CAST(u.register_date::date + '1 day'::interval AS date)
  -- ■ Redshift의 경우는 다음과 같이 사용하기
  -- , date_add(day, 1, u.register_date::date)
  -- ■ BigQuery의 경우는 다음과 같이 사용하기
  -- , date_add(CAST(u.register_date AS date), interval 1 day)
  -- ■ Hive, SparkSQL의 경우는 다음과 같이 사용하기
  -- , date_add(CAST(u.register_date AS date), 1)
    AS next_day_1
  FROM 
	 mst_users AS u
    LEFT OUTER JOIN
	 action_log AS a
	ON u.user_id = a.user_id
)
SELECT *
FROM 
 action_log_with_mst_users
ORDER BY
 register_date
;
```

'사용자'의 '액션 플래그'를 계산하는 쿼리문
```python
WITH
action_log_with_mst_users AS(
 SELECT 
	u.user_id
  , u.register_date
  -- 액션 날짜와 로그 전체의 최신 날짜를 날짜 자료형으로 변환하기
  , CAST(a.stamp AS date) AS action_date
  , MAX(CAST(a.stamp AS date)) OVER() AS latest_date
  -- ■ BigQuery의 경우 한번 타임 스탬프 자료형으로 변환하고 날짜 자료형으로 변환하기
  -- , date(timestamp(a.stamp)) AS action_date
  -- , MAX(date(timestamp(a.stamp))) OVER() AS latest_date
	
  -- 등록일 다음날의 날짜 계산하기
  -- ■ PostgreSQL의 경우는 다음과 같이 사용하기
  , CAST(u.register_date::date + '1 day'::interval AS date)
  -- ■ Redshift의 경우는 다음과 같이 사용하기
  -- , date_add(day, 1, u.register_date::date)
  -- ■ BigQuery의 경우는 다음과 같이 사용하기
  -- , date_add(CAST(u.register_date AS date), interval 1 day)
  -- ■ Hive, SparkSQL의 경우는 다음과 같이 사용하기
  -- , date_add(CAST(u.register_date AS date), 1)
    AS next_day_1
  FROM 
	 mst_users AS u
    LEFT OUTER JOIN
	 action_log AS a
	ON u.user_id = a.user_id
)
, user_action_flag AS(
  SELECT
     user_id
   , register_date
	-- 4. 등록일 다음날엔 액션을 했는지 안 했는지를 플래그로 나타내기
   , SIGN(
	  -- 3. 사용자별로 등록일 다음날에 한 액션의 합계 구하기
	  SUM(
	   -- 1. 등록일 다음날이 로그이 최신 날짜 이전인지 확인하기
	   CASE WHEN next_day_1 <= latest_date THEN
		 -- 2. 등록일 다음날의 날짜에 액션을 했다면 1, 안 했다면 0 지정하기
		 CASE WHEN next_day_1 = action_date THEN 1 ELSE 0 END
	   END
	  )
   )AS next_1_day_action
  FROM
	action_log_with_mst_users
  GROUP BY
	user_id, register_date
)
SELECT *
FROM
  user_action_flag
ORDER BY
 register_date, user_id;
```

다음날 지속률을 계산하는 쿼리문
```python
WITH
action_log_with_mst_users AS(
 SELECT 
	u.user_id
  , u.register_date
  -- 액션 날짜와 로그 전체의 최신 날짜를 날짜 자료형으로 변환하기
  , CAST(a.stamp AS date) AS action_date
  , MAX(CAST(a.stamp AS date)) OVER() AS latest_date
  -- ■ BigQuery의 경우 한번 타임 스탬프 자료형으로 변환하고 날짜 자료형으로 변환하기
  -- , date(timestamp(a.stamp)) AS action_date
  -- , MAX(date(timestamp(a.stamp))) OVER() AS latest_date
	
  -- 등록일 다음날의 날짜 계산하기
  -- ■ PostgreSQL의 경우는 다음과 같이 사용하기
  , CAST(u.register_date::date + '1 day'::interval AS date)
  -- ■ Redshift의 경우는 다음과 같이 사용하기
  -- , date_add(day, 1, u.register_date::date)
  -- ■ BigQuery의 경우는 다음과 같이 사용하기
  -- , date_add(CAST(u.register_date AS date), interval 1 day)
  -- ■ Hive, SparkSQL의 경우는 다음과 같이 사용하기
  -- , date_add(CAST(u.register_date AS date), 1)
    AS next_day_1
  FROM 
	 mst_users AS u
    LEFT OUTER JOIN
	 action_log AS a
	ON u.user_id = a.user_id
)
, user_action_flag AS(
  SELECT
     user_id
   , register_date
	-- 4. 등록일 다음날엔 액션을 했는지 안 했는지를 플래그로 나타내기
   , SIGN(
	  -- 3. 사용자별로 등록일 다음날에 한 액션의 합계 구하기
	  SUM(
	   -- 1. 등록일 다음날이 로그이 최신 날짜 이전인지 확인하기
	   CASE WHEN next_day_1 <= latest_date THEN
		 -- 2. 등록일 다음날의 날짜에 액션을 했다면 1, 안 했다면 0 지정하기
		 CASE WHEN next_day_1 = action_date THEN 1 ELSE 0 END
	   END
	  )
   )AS next_1_day_action
  FROM
	action_log_with_mst_users
  GROUP BY
	user_id, register_date
)
SELECT
   register_date
 , AVG(100.0 * next_1_day_action) AS repeat_rate_1_day
FROM
 user_action_flag
GROUP BY
 register_date
ORDER BY
 register_date
;
```
'지속률 지표'를 관리하는 마스터 테이블을 작성하는 쿼리문
```python
WITH
repeat_interval(index_name, interval_date) AS (
 -- ■ PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 -- ■ Hive, Redshift, BigQuery, SparkSQL의 경우 UNION ALL등으로 대체 가능
 -- 8강 5절 참고하기
 VALUES
  ('01 day repeat', 1)
 ,('02 day repeat', 2)
 ,('03 day repeat', 3)
 ,('04 day repeat', 4)
 ,('05 day repeat', 5)
 ,('06 day repeat', 6)
 ,('07 day repeat', 7)
)
SELECT *
FROM repeat_interval
ORDER BY index_name
;
```
'지속률'을 세로 기반으로 집계하는 쿼리문
```python
WITH
repeat_interval(index_name, interval_date) AS (
 -- ■ PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 -- ■ Hive, Redshift, BigQuery, SparkSQL의 경우 UNION ALL등으로 대체 가능
 -- 8강 5절 참고하기
 VALUES
  ('01 day repeat', 1)
 ,('02 day repeat', 2)
 ,('03 day repeat', 3)
 ,('04 day repeat', 4)
 ,('05 day repeat', 5)
 ,('06 day repeat', 6)
 ,('07 day repeat', 7)
)
, action_log_with_index_date AS(
  SELECT 
	 u.user_id
   , u.register_date  
   -- 액션의 날짜와 로그 전체의 최신 날짜를 날짜 형식으로 변환하기
   , CAST(a.stamp AS date) AS action_date
   , MAX(CAST(a.stamp AS date)) OVER() AS latest_date
   -- ■ BigQuery의 경우 한번 타임스탬프 자료형으로 변환하고 날짜 자료형으로 변환하기
   -- , date(timestamp(a.stamp)) AS action_date
   -- , MAX(date(timestamp(a.stamp))) OVER() AS latest_date
  
   -- 등록일로부터 n일 후의 날짜 계산하기
   , r.index_name
	
   -- ■ PostgreSQL의 경우는 다음과 같이 사용하기
   , CAST(CAST(u.register_date AS date) + interval '1day' * r.interval_date AS date)
   -- ■ Redshift의 경우는 다음과 같이 사용하기
   --, dateadd(day, r.interval_date, u.register_date::date)
   -- ■ BigQuery의 경우는 다음과 같이 사용하기
   --, date_add(CAST(u.register_date AS date), interval r.interval_date day)
   -- ■ Hive, SparkSQL의 경우는 다음과 같이 사용한다.
   --, date_add(CAST(u.ragister_date AS date), r.interval_date)
	 AS index_date
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
	-- 4. 등록일로부터 n일 후에 액션을 했는지 플래그로 나타내기
  , SIGN(
	 -- 3. 사용자별로 등록일로부터 n일 후에 한 액션의 합계 구하기
	 SUM(
	  -- 1. 등록일부터 n일 후가 로그의 최신 날짜 이전인지 확인하기
	  CASE WHEN index_date <= latest_date THEN
	   -- 2. 등록일로부터 n일 후의 날짜에 액션을 했다면 1, 아니라면 0 지정하기
	   CASE WHEN index_date = action_date THEN 1 ELSE 0 END
	 END
	 )
  )AS index_date_action
FROM
 action_log_with_index_date
GROUP BY
 user_id, register_date, index_name, index_date
)
SELECT 
   register_date
 , index_name
 , AVG(100.0 * index_date_action) AS repeat_rate
FROM 
 user_action_flag
GROUP BY
 register_date, index_name
ORDER BY
 register_date, index_name
;
```

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)
참고 도서 : 데이터 분석을 위한 SQL 레시피
저자 : 가나키 나가토, 다미야 나오토
출판사 : 한빛미디어
