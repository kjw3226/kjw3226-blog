---
title: postgre SQL-practice26
tag: postgre SQL-practice26
date: 2022-03-01
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

오늘은 페이지 251 ~ 257 까지를 보고 실습을 진행하였다.

'정착률 지표'를 관리하는 마스터 테이블을 작성하는 쿼리문
```python
WITH
repeat_interval(index_name, interval_begin_date, interval_end_date) AS (
 --■ PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 --■ Hive, Redshift, BigQuery, SparkSQL의 경우 UNION ALL 등으로 대체 가능
 --8장 5절 참고하기
 VALUES
  ('07 day retention', 1, 7)
, ('14 day retention', 8, 14)
, ('21 day retention', 15, 21)
, ('28 day retention', 22, 28)
)
SELECT *
FROM repeat_interval
ORDER BY index_name
;
```

정착률의 계산하는 쿼리문
```python
WITH
repeat_interval AS (
 -- ■ PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 -- ■ Hive, Redshift, BigQuery, SparkSQL의 경우 UNION ALL 등으로 대체 가능
 --8장 5절 참고하기
 VALUES
  ('07 day retention', 1, 7)
, ('14 day retention', 8, 14)
, ('21 day retention', 15, 21)
, ('28 day retention', 22, 28)
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
SELECT
   register_date
 , index_name
 , AVG(100.0 * index_date_action) AS index_rate
FROM
 user_action_flag
GROUP BY
 register_date, index_name
ORDER BY
 register_date, index_name
;
```
'지속률 지표'를 관리하는 마스터 테이블을 '정착률 형식'으로 수정한 쿼리문
```python
WITH
repeat_interval(index_name, interval_begin_date, interval_end_date) AS (
  -- ■ Postgre SQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
  -- ■ PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
  -- ■ Hive, Redshift, BigQuery, SparkSQL의 경우 UNION ALL 등으로 대체 가능
  --8장 5절 참고하기
  VALUES
	('01 day repeat', 1, 1)
  , ('02 day repeat', 2, 2)
  , ('03 day repeat', 3, 3)
  , ('04 day repeat', 4, 4)
  , ('05 day repeat', 5, 5)
  , ('06 day repeat', 6, 6)
  , ('07 day repeat', 7, 7)
  , ('07 day retention', 1, 7)
  , ('14 day retention', 8, 14)
  , ('21 day retention', 15, 21)
  , ('28 day retention', 22, 28)
)
SELECT *
FROM repeat_interval
ORDER BY index_name
;
```
'n일' '지속률'들을 집계하는 쿼리문
```python
WITH
repeat_interval AS (
 -- ■ PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 -- ■ Hive, Redshift, BigQuery, SparkSQL의 경우 UNION ALL 등으로 대체 가능
 --8장 5절 참고하기
 VALUES
  ('07 day retention', 1, 7)
, ('14 day retention', 8, 14)
, ('21 day retention', 15, 21)
, ('28 day retention', 22, 28)
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
SELECT
   index_name
 , AVG(100.0 * index_date_action) AS repeat_rate
FROM
 user_action_flag
GROUP BY
 index_name
ORDER BY
 index_name
;
```
지속률과 정착률은 모두 등록일 기준으로 n일 후의 행동을 집계하는 것입니다. 

따라서 등록일로부터 n일 경과하지 않은 상태라면 집계가 불가능합니다. 

그러므로 30일 지속률과 60일 지속률처럼 값을 구하기 위해 시간이 오래 걸리는 지표보다는 

1일 지속률, 7일 지속률, 7일 정착률처럼 단기간에 결과를 보고 대책을 세울 수 있는 지표를 

활용하는 것이 좋습니다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 12강 페이지 257 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)
참고 도서 : 데이터 분석을 위한 SQL 레시피
저자 : 가나키 나가토, 다미야 나오토
출판사 : 한빛미디어