---
title: postgre SQL-practice14
tag: postgre SQL-practice14
date: 2022-02-15
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'데이터 분석을 위한 SQL 레시피'
오늘은 '10강 - 2.ABC 분석으로 잘 팔리는 상품 판별하기' 부분을 보고 
실습을 진행 했다.

매출 구성비누계와 ABC 등급을 계산하는 쿼리문
```python
WITH
monthly_sales AS(
  SELECT
	 category1
	 -- 항목별 매출 계산하기
   , SUM(amount) AS amount
  FROM
   purchase_log
 -- 대상 1개월 동안의 로그를 조건으로 걸기
 WHERE
  dt BETWEEN '2015-12-01' AND '2015-12-31'
 GROUP BY
  category1
)
, sales_composition_ratio AS(
  SELECT
	 category1
   , amount
	
   
   -- 구성비: 100.0* <항목별 매출> / <전체 매출>
   , 100.0 * amount / SUM(amount) OVER() AS composition_ratio
	
	
   -- 구성비 누계: 100.0*<항목별 구계 매출> / <전체 매출>
   , 100.0 * SUM(amount) OVER(ORDER BY amount DESC
   ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
   / SUM(amount) OVER() AS cumulative_ratio
  FROM
   monthly_sales
)
SELECT
   *
 -- 구성비누계 범위에 따라 순위 붙이기
 , CASE
    WHEN cumulative_ratio BETWEEN 0  AND 70  THEN 'A'
	WHEN cumulative_ratio BETWEEN 70 AND 90  THEN 'B'
	WHEN cumulative_ratio BETWEEN 70 AND 100 THEN 'C'
   END AS abc_rank
FROM 
 sales_composition_ratio
ORDER BY
 amount DESC
;
```

이번 절에서는 상품을 대상으로 ABC 분석했지만, 상품 카테고리별로 집계하면 또 다른 발견을 할 수 있습니다.

ABC 분석을 뺴더라도 구성비와 구성비누계 자체는 데이터 분석에 굉장히 많이 사용된다. 

따라서 이런 것을 구하는 방법을 확실하게 기억해라.

('데이터 분석을 위한 SQL레시피' 4장 '10강'中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어
