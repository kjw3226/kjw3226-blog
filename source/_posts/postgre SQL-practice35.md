---
title: postgre SQl-practice35
tag: postgre SQl-practice35
date: 2022-03-18
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'5장  13강 시계열에 따른 사용자의 개별적인 행동 분석하기

3. 등록으로부터의 매출을 날짜별로 집계하기'

(페이지 315 ~ 321)

를 보고 쿼리문 작성 실습을 하였다.

사용자들의 등록일로부터 경과한 일수별 매출을 계산하는 쿼리문
```python
WITH
index_interval(index_name, interval_begin_date, interval_end_date) AS (
 --■PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 --■Hive, Redshift, BigQuery, SparkSQL의 경우 UNION ALL등으로 대체 가능
 -- 8강 5절 참고하기
VALUES
  ('30 day sales amount'  ,  0, 30)
, ('45 day sales amount'  ,  0, 45)
, ('60 day sales amount'  ,  0, 60)
)
, mst_user_with_base_date AS (
  SELECT
	 user_id
	
	
   -- 기준일로 등록일 사용하기
   , register_date AS base_date
   

   -- 처음 구매한 날을 기준으로 삼고 싶다면 다음과 같이 사용하기
   --, first_purchase_date AS base_date
 FROM
  mst_users
)
, purchase_log_with_index_date AS (
  SELECT
	 u.user_id
   , u.base_date
   --액션의 날짜와 로그 전체의 최신 날짜를 날짜 자료형으로 변환하기
   , CAST(p.stamp AS date) AS action_date
   , MAX(CAST(p.stamp AS date)) OVER() AS latest_date
   , substring(p.stamp, 1, 7) AS month
   -- ■ BigQuery의 경우 한번 타임스탬프 자료형으로 변환하고 날짜 자료형으로 변환하기
   --, date(timestamp(p.stamp)) AS action_date
   --, MAX(date(timestamp(p.stamp))) OVER() AS latest_date
   --, substring(p.stamp, 1, 7) AS month
   
   
   , i.index_name
   -- 지표 대상 기간의 시작일과 종료일 계산하기
   --■ PostgreSQL의 경우는 다음과 같이 사용하기
   , CAST(u.base_date::date + '1 day'::interval * i.interval_begin_date AS date)
	 AS index_begin_date
   --■ Redshift의 경우는 다음과 같이 사용하기
   --, dateadd(day, r.interval_begin_date, u.base_date::date) AS index_begin_date
   --, dateadd(day, r.interval_end_date  , u.base_date::date) AS index_end_date
   --■ BigQuery의 경우는 다음과 같이 사용하기
   --, date_add(CAST(u.base_date AS date), interval r.interval_begin_date day)
   --  AS index_begin_date
   --, date_add(CAST(u.base_date AS date), interval r.interval_end_date day)
   --  AS index_end_date
   --■ Hive, SparkSQL의 경우는 다음과 같이 사용하기
   --, date_add(CAST(u.base_date AS date), r.interval_begin_date)
   --  AS index_begin_date
   --, date_add(CAST(u.base_date AS date), r.interval_end_date)
   --  AS index_end_date
   , p.amount
FROM
   mst_users_with_vase_date AS u
  LEFT OUTER JOIN
	action_lag AS p
	 ON u.user_id = p.user_id
	AND p.action = 'purchase'
  CROSS JOIN
	index_interval AS i
)
SELECT *
FROM
 purchase_log_with_index_date
;
```

월별 등록자 수와 경과일수별 매출을 집계하는 쿼리문
```python
WITH
index_interval(index_name, interval_begin_date, interval_end_date) AS (
 --■PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 --■Hive, Redshift, BigQuery, SparkSQL의 경우 UNION ALL등으로 대체 가능
 -- 8강 5절 참고하기
VALUES
  ('30 day sales amount'  ,  0, 30)
, ('45 day sales amount'  ,  0, 45)
, ('60 day sales amount'  ,  0, 60)
)
, mst_user_with_base_date AS (
  SELECT
	 user_id
	
	
   -- 기준일로 등록일 사용하기
   , register_date AS base_date
   

   -- 처음 구매한 날을 기준으로 삼고 싶다면 다음과 같이 사용하기
   --, first_purchase_date AS base_date
 FROM
  mst_users
)
, purchase_log_with_index_date AS (
  SELECT
	 u.user_id
   , u.base_date
   --액션의 날짜와 로그 전체의 최신 날짜를 날짜 자료형으로 변환하기
   , CAST(p.stamp AS date) AS action_date
   , MAX(CAST(p.stamp AS date)) OVER() AS latest_date
   , substring(p.stamp, 1, 7) AS month
   -- ■ BigQuery의 경우 한번 타임스탬프 자료형으로 변환하고 날짜 자료형으로 변환하기
   --, date(timestamp(p.stamp)) AS action_date
   --, MAX(date(timestamp(p.stamp))) OVER() AS latest_date
   --, substring(p.stamp, 1, 7) AS month
   
   
   , i.index_name
   -- 지표 대상 기간의 시작일과 종료일 계산하기
   --■ PostgreSQL의 경우는 다음과 같이 사용하기
   , CAST(u.base_date::date + '1 day'::interval * i.interval_begin_date AS date)
	 AS index_begin_date
   --■ Redshift의 경우는 다음과 같이 사용하기
   --, dateadd(day, r.interval_begin_date, u.base_date::date) AS index_begin_date
   --, dateadd(day, r.interval_end_date  , u.base_date::date) AS index_end_date
   --■ BigQuery의 경우는 다음과 같이 사용하기
   --, date_add(CAST(u.base_date AS date), interval r.interval_begin_date day)
   --  AS index_begin_date
   --, date_add(CAST(u.base_date AS date), interval r.interval_end_date day)
   --  AS index_end_date
   --■ Hive, SparkSQL의 경우는 다음과 같이 사용하기
   --, date_add(CAST(u.base_date AS date), r.interval_begin_date)
   --  AS index_begin_date
   --, date_add(CAST(u.base_date AS date), r.interval_end_date)
   --  AS index_end_date
   , p.amount
FROM
   mst_users_with_vase_date AS u
  LEFT OUTER JOIN
	action_lag AS p
	 ON u.user_id = p.user_id
	AND p.action = 'purchase'
  CROSS JOIN
	index_interval AS i
)
, user_purchase_amount AS (
  SELECT
	 user_id
   , month
   , index_name
	 -- 3. 지표의 대상 기간에 구매한 금액을 사용자별로 합계 내기
   , SUM(
	  -- 1. 지표의 대상 기간의 종료일이 로그의 최신 날짜에 포함되었는지 확인하기
	  CASE WHEN index_end_date <= latest_date THEN
	   -- 2. 지표의 대상 기간에 구매한 경우에는 구매 금액, 이외의 경우 0 지정하기
	   CASE
	    WHEN action_date BETWEEN index_begin_date AND index_end_date THEN amount
	    ELSE 0
	   END
	  END
   ) AS index_date_amount
  FROM
   purchase_log_with_index_date
  GROUP BY
	user_id, month, index_name, index_begin_date, index_end_date
)
SELECT
   month
 -- 등록자수 세기
 -- 다만 지표의 대상 기간의 종료일이 로그의 최신 날짜 이전에 표함되지 않게 조건 달기
 , COUNT(index_date_amount) AS users
 , index_name
 -- 지표의 대상 기간 동안 구매한 사용자 수
 , COUNT(CASE WHEN index_date_amount > 0 THEN user_id END) AS purchase_uu
 -- 지표의 대상 기간 동안의 합계 매출
 , SUM(index_date_amount) AS total_amount
 -- 등록자별 평균매출
 , AVG(index_date_amount) AS avg_amount
FROM
 user_purchase_amount
GROUP BY
 month, index_name
ORDER BY
 month, index_name
;
```
이번 절의 SQL은 사용자 등록일을 기준으로 1인당 n일 매출 금액을

집계하는 것이지만,

제휴의 성과 지점이 아닌 최초 판매 시점으로 설정해 등록하면,

광고 담당자의 운용에 도움을 주는 지표를 새롭게 찾을 수 있습니다.

이런 리포트를 만들고 싶다면 WITH 구문에 있는 

mst_users_with_base_date 테이블의 base_date 컬럼을 

최초 판매 시점으로 전환하면 됩니다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 13강 페이지 321 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어

