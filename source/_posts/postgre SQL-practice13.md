---
title: postgre SQL-practice13
tag: postgre SQL-practice13
date: 2022-02-14
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

 오늘은 '10강 다면적인 축을 사용해 데이터 집약하기'
 
 를 보고 쿼리문을 실습하였다.

카테고리별 매출과 소계를 동시에 구하는 쿼리문
```python
WITH
sub_category_amount AS(
 -- 소 카테고리의 매출 집계하기
 SELECT
	category      AS category
  , sub_category AS sub_category
  , SUM(price) AS amount
FROM
 purchase_detail_log
GROUP BY
 category, sub_category
)
, category_amount AS (
  -- 대 카테고리의 매출 집계하기
  SELECT
	 category
   , 'all' AS sub_category
   , SUM(price) AS amount
  FROM
   purchase_detail_log
  GROUP BY
   category
)

, total_amount AS (
  -- 전체 매출 집계하기
  SELECT
	 'all' AS category
   , 'all' AS sub_category
   , SUM(price) AS amount
  FROM
   purchase_detail_log
)
         SELECT category, sub_category, amount FROM sub_category_amount
UNION ALL SELECT category, sub_category, amount FROM category_amount
UNION ALL SELECT category, sub_category, amount FROM total_amount
;
```

ROLLUP 을 사용해서 카테고리별 매출과 소계를 동시에 구하는 쿼리문
```python
SELECT
   COALESCE(category, 'all')    AS category
 , COALESCE(sub_category, 'all') AS sub_category
 , SUM(price) AS amount
FROM 
 purchase_detail_log
GROUP BY
 ROLLUP(category, sub_category)
 -- Hive의 경우는 다음과 같이 사용하기
 -- category, sub_category WITH ROLLUP
 ;
```
대부분의 리포트 작성 도구는 소계를 계산해주는 기능이 있다.

따라서 최소 단위로 집계해두면, 이후에 소계를 따로 계산할 수 있다.

그런데 매출이 아니라 다른 것을 다룰 경우, 중복 등이 발생해서

리포트 작성 도구로는 총계와 소계가 제대로 구해지지 않는 경우가 있습니다.

그때 이번에 배운 SQL을 활용해 데이터를 추출하기 바란다.

('데이터 분석을 위한 SQL레시피' 4장 '10강'中)