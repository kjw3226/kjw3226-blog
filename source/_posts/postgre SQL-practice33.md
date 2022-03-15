---
title: postgre SQL-practice33
tag: postgre SQL-practice33
date: 2022-03-15
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'5장  13강 시계열에 따른 사용자의 개별적인 행동 분석하기

1. 사용자의 액션 간격 집계하기'

로 오늘 넘어갔다.

페이지 303 ~ 310을 참고하였다.

신청일과 숙박일의 리드 타임을 계산하는 쿼리문
```python
WITH
reservations(reservation_id, register_date, visit_date, days) AS (
 -- ■ PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 -- ■ Hive, Redshift, BigQuery, SparkSQL의 경우 UNION ALL 등으로 대체 가능
 -- 8강 5정 참고하기
 VALUES
  (1, date '2016-09-01', date '2016-10-01', 3)
, (2, date '2016-09-20', date '2016-10-01', 2)
, (3, date '2016-09-30', date '2016-11-20', 2)
, (4, date '2016-10-01', date '2017-01-03', 2)
, (5, date '2016-11-01', date '2016-12-28', 3)
)
SELECT
   reservation_id
 , register_date
 , visit_date
 ---■ PostgreSQL, Redshift의 경우 날짜끼리 뺄셈 가능
 , visit_date::date - register_date::date AS lead_time
 ---■ BigQuery의 경우 date_diff 함수 사용하기
 ---, date_diff(date(timestamp(visit_date)), date(timestamp(register_date)), day)
 --- AS lead_time
 ---■ Hive, SparkSQl의 경우 datediff 함수 사용하기
 ---, datediff(to_date(visit_date), to_date(register_date)) AS lead_time
 FROM
  reservations
;
```

각 단계에서의 리드 타임과 토탈 리드 타임을 계산하는 쿼리문
```python
WITH
requests(user_id, product_id, request_date) AS (
 -- ■Postgre SQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 -- ■Hive, Redshift, BigQuery, SparkSQL의 UNION ALL 등으로 대체 가능
 -- 8강 5절 참고하기
 VALUES
  ('U001', '1', date '2016-09-01')
, ('U001', '2', date '2016-09-20')
, ('U002', '3', date '2016-09-30')
, ('U003', '4', date '2016-10-01')
, ('U004', '5', date '2016-11-01')
)
, estimates(user_id, product_id, estimate_date) AS (
 VALUES
  ('U001', '2', date '2016-09-21')
, ('U002', '3', date '2016-10-15')
, ('U003', '4', date '2016-10-15')
, ('U004', '5', date '2016-12-01')
)
, orders(user_id, product_id, order_date) AS (
 VALUES
   ('U001', '2', date '2016-10-01')
 , ('U002', '5', date '2016-12-05')
)
SELECT
     r.user_id
   , r.product_id
   -- ■ Postgre SQL, Redshift의 경우 날짜까지 뺄샘가능
   , e.estimate_date::date - r.request_date::date AS estimate_lead_time
   , o.order_date::date    - e.estimate_date::date AS order_lead_time
   , o.order_date::date    - r.request_date::date AS total_lead_time
   -- ■ BigQuery의 경우 date_diff 함수 사용하기
   --, date_diff(date(timestamp(e.estimate_date)),
   --    date(timestamp(r.request_date)), day)
   --  AS estimate_lead_time
   --, date_diff(date(timestamp(o.order_date)),
   --    date(timestamp(e.estimate_date)), day)
   --  AS order_lead_time
   --, date_diff(date(timestamp(o.order_date)),
   --    date(timestamp(r.request_date)), day)
   --  AS total_lead_time
   -- ■ Hive, SparkSQL의 경우 datediff 함수 사용하기
   --, datediff(to_date(e.stimate_date), to_date(r.request_date))
   --  AS estimate_lead_time
   --, datediff(to_date(o.order_date), to_date(e.estimate_date)
   --  AS order_lead_time
   --, datediff(to_date(o.order_date), to_date(r.request_date))
   --  AS total_lead_time
FROM
   requests AS r
 LEFT OUTER JOIN
  estimates AS e
  ON r.user_id   = e.user_id
  AND r.product_id = e.product_id
 LEFT OUTER JOIN
  orders AS o
  ON r.user_id   = o.user_id
  AND r.product_id = o.product_id
;
```

이전 구매일로부터의 일수를 계산하는 쿼리문
```python
WITH
purchase_log(user_id, product_id, purchase_date) AS
 -- ■ PostgreSQL의 경우 VALUES 구문으로 일시 테이블 생성 가능
 -- ■ Hive, Redshift, BigQuery, SparkSQL의 경우 UNION ALL 등으로 대체 가능
 -- 8강 5절 참조하기
 VALUES
  ('U001', '1', '2016-09-01')
, ('U002', '2', '2016-09-20')
, ('U003', '3', '2016-09-30')
, ('U001', '4', '2016-10-01')
, ('U002', '5', '2016-11-01')
)
SELECT
   user_id
 , purchase_date
 -- ■ PostgreSQL, Redshift의 경우 날짜끼리 뺄셈 가능
 , purchase_date::date
   - LAG(purchase_date::date)
     OVER(
      PARTITION BY user_id
	  ORDER BY purchase_date
	 )
   AS lead_time
 -- ■ BigQuery의 경우 date_diff 함수 사용하기
 --, date_diff(date(timestamp(purchase_date)),
 --   LAG(date(timestamp(purchase_date))))
 --    OVER(PARTITION BY user_id ORDER BY purchase_date)
 --  , day) AS lead_time
 -- ■ Hive의 경우 datediff 함수 사용하기
 --, datediff(to_date(purchase_date),
 --   LAG(to_date(purchase_date))
 --     OVER(PARTITION BY user_id ORDER BY purchase_date))
 --  AS lead_time
 -- ■ SparkSQL의 경우 datediff 함수에 LAG 함수의 프레임 지정이 필요함
 --, datediff(to_date(purchase_date),
 --    LAG(to_date(purchase_date))
 --     OVER(PARTITION BY user_id ORDER BY purchase_date
 --       ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING))
 --  AS lead_time
FROM
 purchase_log
;
```
리드 타임을 집계했다면 사용자의 데모그래픽 정보를 사용해 비교해보기 

바랍니다. EC 사이트라면 수도권보다 지방이 이전 구매일로부터의 리드 타임이

짧거나, 연령별로 구분이 되는 등 다양한 경향이 나타날 것입니다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 13강 페이지 310 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어