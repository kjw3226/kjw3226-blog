---
title: postgre SQL-practice10
tag: postgre SQL-practice10
date: 2022-02-11
categories:	SQL
----
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

 오늘 부터는 실무에서 'SQL'을 사용해 '매출'을 알아보는 쿼리문을
 실습한다.
 
'시계열 기반으로 데이터 집계하기-날짜별 매출 집계하기'
날짜별 매출과 평균 구매액을 집계하는 쿼리문
```python
SELECT
   dt
 , COUNT(*) AS purchase_count
 , SUM(purchase_amount) AS total_amount
 , AVG(purchase_amount) AS avg_amount
FROM purchase_log
GROUP BY dt
ORDER BY dt
;
```

'시계열 기반으로 데이터 집계하기-이동평균을 사용한 날짜별 추이 보기'
날짜별 매출과 7일 이동평균을 집계하는 쿼리문
```python
SELECT
   dt
 , SUM(purchase_amount) AS total_amount
 
 
 -- 최근 최대 7일 동안의 평균 계산하기
 , AVG(SUM(purchase_amount))
   OVER(ORDER BY dt ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
   AS saven_day_avg
   
   
 -- 최근 7일 동안의 평균을 확실하게 계산하기
 , CASE
    WHEN
	 7 = COUNT(*)
	 OVER(ORDER BY dt ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
	THEN
	 AVG(SUM(purchase_amount))
	 OVER(ORDER BY dt ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
  END
  AS seven_day_avg_strict
FROM purchase_log
GROUP BY dt
ORDER BY dt
;
```
'시계열 기반으로 데이터 집계하기-당월 매출 누계 구하기'
날짜별 매출과 당월 누계 매출을 집계하는 쿼리문
```python
SELECT
   dt
 -- '연-월' 추출하기
 -- ■ PosrgreSQL,Hive,Redshift,SparkSQL의 경우 substring로 '연-월' 부분 추출하기
 , substring(dt, 1, 7) AS year_month
 -- ■ PosrgreSQL,Hive,Redshift,SparkSQL의 경우 substr 사용하기
 --, substr(dt, 1, 7) AS yesr_month
 , SUM(purchase_amount)AS total_amount
 , SUM(SUM(purchase_amount))
    -- ■ PostgreSQL,Hive,Redshift,SparkSQL의 경우는 다음과 같다.
	OVER(PARTITION BY substring(dt, 1, 7) ORDER BY dt ROWS UNBOUNDED PRECEDING)
	-- ■ BingQuery의 경우 substing를 substr로 수정하기
	-- OVER(PARTITION BY substr(dt, 1, 7) ORDER BY dt ROWS UNBOUNDED PRECEDING)
  AS agg_amount
FROM
  purchase_log
GROUP BY dt
ORDER BY dt
;
```
이 쿼리문은 위 쿼리문을 'WITH'구문을 사용해 나타낸 것이다.

날짜별 매출을 일시 테이블로 만드는 쿼리문
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
 *
FROM
 daily_purchase
ORDER BY dt
;
```
daily_purchase 테이블에 대해 당월 누계 매출을 집계하는 쿼리문
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
  dt
, concat(year,'-',month) AS year_month
  -- ■ Redshift의 경우는 concat 함수를 조합해서 사용하기 또는 || 연산자 사용하기
  --, concat(concat(year,'-'), month) AS year_month
  --, year || '-' || month AS year_month
, purchase_amount
, SUM(purchase_amount)
   OVER(PARTITION BY year, month ORDER BY dt ROWS UNBOUNDED PRECEDING)
  AS agg_amount
FROM daily_purchase
ORDER BY dt
;
```
서비스를 운용, 개발하기 위해 사용하는 SQL과 비교했을 때, 빅데이터 분석 SQL은
성능이 조금 떨어지더라고 가독성과 재사용성을 중시해서 작성하는 
경우가 많다. 추가로 빅데이터 분석을 할 때는 SQL에 프로그램 개발 때
사용하는 '전처리'라는 사고 방식을 도입하는 경우도 많다.
('데이터 분석을 위한 SQL레시피' 4장 '9강'中)