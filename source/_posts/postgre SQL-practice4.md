---
title: postgre SQL-practice4
tag: postgre SQL-practice4
date: 2022-02-07
categories:	SQL
----
 어제에 이어서 오늘 오전에 
 '데이터 분석을 위한 SQL 레시피'를 보며
 
 예제 쿼리문으로 실습을 했다.
 
윈도우 함수로 프레임 지정별 상품 ID를
집약하는 쿼리문
```python
SELECT
product_id


-- 점수 순서로 유일한 순위를 붙임
, ROW_NUMBER() OVER(ORDER BY score DESC) AS row


-- 가장 앞 순위부터 가장 뒷 순위까지의 범위를 대상으로 상품 ID 집약하기
-- ■ PostgreSQL의 경우는 array_agg, Hive, SparkSQL의 경우는 collect_list 사용하기
, array_agg(product_id)
-- , collect_list(product_id)
OVER(ORDER BY score DESC
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
AS whole_agg


-- 가장 앞 순위부터 현재 순위까지의 범위를 대상으로 상품 ID 집약하기
-- ■ PostgreSQL의 경우는 array_agg, Hive, SparkSQL의 경우는 collect_list 사용하기
, array_agg(product_id)
-- , collect_list(product_id)
OVER(ORDER BY score DESC
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
AS cum_agg


-- 순위 하나 앞과 하나 뒤까지의 범위를 대상으로 ID 집약하기
-- ■ PostgreSQL의 경우는 array_agg, Hive, SparkSQL의 경우는 collect_list 사용하기
, array_agg(product_id)
-- , collect_list(product_id)
OVER(ORDER BY score DESC
ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)
AS local_agg
FROM popular_products
WHERE category = 'action'
ORDER BY row
;
```
윈도우 함수를 사용해 카테고리들의 순위를 계산하는 쿼리문
```python
SELECT
category
, product_id
, score
-- 카테고리별로 점수 순서로 유일한 순위를 붙임
, ROW_NUMBER()
OVER(PARTITION BY category ORDER BY score DESC)
AS row
-- 카테고리별로 같은 순위를 허가하고 순위를 붙임
, RANK()
OVER(PARTITION BY category ORDER BY score DESC)
AS rank
-- 카테고리별로 같은 순위가 있을 때
-- 같은 순위 다음에 있는 순위를 건너 뛰고 순위를 붙임
, DENSE_RANK()
OVER(PARTITION BY category ORDER BY score DESC)
AS dense_rank
FROM popular_products
ORDER BY category, row
;
```
카테고리들의 순위 상위 2개까지의 상품을 추출하는 쿼리문
```python
SELECT *
FROM
-- 서브 쿼리 내부에서 순위 계산하기
( SELECT
  category
  , product_id
  , score
  -- 카테고리별로 점수 순서로 유일한 순위를 붙임
  , ROW_NUMBER()
OVER(PARTITION BY category ORDER BY score DESC)
AS rank
FROM popular_products
) AS popular_products_with_rank
-- 외부 쿼리에서 순위 활용해 압축하기
WHERE rank <= 2
ORDER BY category, rank
;
```
카테고리별 순위 최상위 상품을 추출하는 쿼리문
```python
  -- DISTINCT 구문을 사용해 중복 제거하기
  SELECT DISTINCT
     category
	 -- 카테고리별로 순위 최상위 상품 ID 추출하기
   , FIRST_VALUE(product_id)
      OVER(PARTITION BY category ORDER BY score DESC
	   ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
	 AS product_id
  FROM popular_products
;
```