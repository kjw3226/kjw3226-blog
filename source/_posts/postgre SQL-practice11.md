---
title: postgre SQL-practice11
tag: postgre SQL-practice11
data: 2022-02-12
categories:	SQL
----
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

 어제에 이어서 오늘은 
 '월별 매출과 작대비 구하기', 'Z차트 구하기'를 
 실습하였다.
 
'월별 매출'과 '작대비'를 계산하는 쿼리문
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
SELECT
   month
 , SUM(CASE year WHEN '2014' THEN purchase_amount END) AS amount_2014
 , SUM(CASE year WHEN '2015' THEN purchase_amount END) AS amount_2015
 , 100.0
   * SUM(CASE year WHEN '2015' THEN purchase_amount END)
   / SUM(CASE year WHEN '2014' THEN purchase_amount END)
   AS rate
FROM 
 daily_purchase
GROUP BY month
ORDER BY month
;
```
<원포인트>

매출이 늘어났다고 해도 계절의 영향을 받아 늘었는지, 이벤트 등으로 
인해 늘었는지 판단 할 수 없다. 이렇게 작년과 비교했을 때 계절 트랜드로 매출이
늘어난 경우라도 전년대비 떨어졌다면 성장이 둔화했다고 판단 할 수 있다.

('데이터 분석을 위한 SQL레시피' 4장 '9강'中)

'2015년' 매출에 대한 'Z차트'를 작성하는 쿼리문
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
, monthly_amount AS(
 -- 월별 매출 집계하기
 SELECT
	year
  , month
  , SUM(purchase_amount) AS amount
FROM daily_purchase
GROUP BY year, month
)
, calc_index AS(
 SELECT
	year
  , month 
  , amount
	-- 2015년의 누계 매출 집계하기
  , SUM(CASE WHEN year = '2015' THEN amount END)
     OVER(ORDER BY year, month ROWS UNBOUNDED PRECEDING)
    AS agg_amount
	-- 당월부터 11개월 이전까지의 매출 합계(이동년계) 집계하기
	, SUM(amount)
	   OVER(ORDER BY year, month ROWS BETWEEN 11 PRECEDING AND CURRENT ROW)
	  AS year_avg_amount
 FROM
  monthly_purchase
 ORDER BY
  year, month
)
--  마지막으로 2015년 데이터만 압축하기
SELECT
  concat(year, '-', month) AS year_month
  -- ■ Redshift의 경우는 concat 함수를 조합해서 사용하기 또는 || 연산자 사용하기
  -- concat(concat(year, '-'), month) AS year_month
  -- year || '-' || month AS year_month
 , amount
 , agg_amount
 , year_avg_amount
FROM
 calc_index
WHERE
 year = '2015'
ORDER BY
 year_month
;
```
<원포인트>

계절 트랜드 영향을 제외하고, 매출의 성장 또는 쇠퇴를 다양한 각도에서 살펴볼 때는
Z차트를 사용하는 것이 좋다. 매일 확인해야 할 그래프는 아니지만 주시젹으로는
살펴보기 바란다.

('데이터 분석을 위한 SQL레시피' 4장 '9강'中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)
참고 도서 : 데이터 분석을 위한 SQL 레시피
저자 : 가나키 나가토, 다미야 나오토
출판사 : 한빛미디어

