---
title: postgre SQL-practice12
tag: postgre SQL-practice12
date: 2022-02-13
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

오늘은 '4장 中 6.매출을 파악할 때 중요 포인트' 부분을 

보고 실습도 진행했다.

![SQL1 수정](https://user-images.githubusercontent.com/96108301/153744622-68e3ea87-3555-47a6-a806-c029cda87fe8.jpg)

아래는 실습 쿼리문이다.

매출과 관련된 지표를 집계하는 쿼리문
```python
WITH
daily_purchase AS(
	SELECT
	dt
	-- '연', '월', '일'을 각각 추출하기
    -- ■ postgreSQL, Hive, Redshift, SparkSQL의 경우 다음과 같이 작성하기
	-- ■ BigQuery의 경우 substring을 substr로 수정하기
  , substring(dt, 1, 4) AS year
  , substring(dt, 6, 2) AS month
  , substring(dt, 9, 2) AS date
  , SUM(purchase_amount) AS purchase_amount
  , COUNT(order_id) AS orders
 FROM purchase_log
 GROUP BY dt
)
, monthly_purchase AS(
 SELECT
	year
  , month
  , SUM(orders) AS orders
  , AVG(purchase_amount) AS avg_amount
  , SUM(purchase_amount) AS monthly
FROM daily_purchase
GROUP BY year, month
)
SELECT
  concat(year, '-', month) AS year_month
  -- ■ Redshift의 경우는 concat 함수를 조합해서 사용하기 또는 || 연산자 사용하기
  -- concat(concat(year, '-'), month) AS year_month
  -- year || '-' || month AS year_month
, orders
, avg_amount
, monthly
, SUM(monthly)
   OVER(PARTITION BY year ORDER BY month ROWS UNBOUNDED PRECEDING)
  AS agg_amount
  -- 12개월 전의 매출 구하기
, LAG(monthly, 12)
   OVER(ORDER BY year, month)
   -- ■ SparkSQL의 경우는 다음과 같이 사용하기
   -- OVER(ORDER BY year, month ROWS BETWEEN 12 PRECEDING AND 12 PRECEDING)
  AS last_year
   -- 12개월 전의 매출과 비교해서 비율 구하기
  , 100.0
    * monthly
	/ LAG(monthly, 12)
	   OVER(ORDER BY year, month)
	   -- ■ Spark SQL의 경우는 다음과 같이 사용하기
	   -- OVER(ORDER BY year, month ROWS BETWEEN 12 PRECEDING AND 12 PRECEDING)
	AS rate
FROM 
 monthly_purchase
ORDER BY
 year_month
;
```