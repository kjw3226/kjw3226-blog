---
title: postgre SQL-practice80
tag: postgre SQL-practice80
date: 2022-05-02
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  24강 점수 계산하기'의

'5. 독자적인 점수 계산 방법을 정의해서 순위 작성하기'

로 넘어갔으며

페이지 562 ~ 566을 참고하였다.


분기별 상품 매출액과 매출 합계를 집계하는 쿼리문
```python
WITH
item_sales_per_quarters AS (
  SELECT
	 item
	 --2016년 1분기의 상품 매출 모두 더하기
   , SUM(
      CASE WHEN year_month IN ('2016-01', '2016-02', '2016-03') THEN amount ELSE 0 END
     ) AS sales_2016_q1
	 --2016년 4분기의 상품 매출 모두 더하기
   , SUM(
      CASE WHEN year_month IN ('2016-10', '2016-11', '2016-12') THEN amount ELSE 0 END
     ) AS sales_2016_q4
  FROM monthly_sales
  GROUP BY
    item
)
SELECT
   item
  --2016년 1분기의 상품 매출
  , sales_2016_q1
  --2016년 1분기의 상품 매출 합계
  , SUM(sales_2016_q1) OVER() AS sum_sales_2016_q1
  --2016년 4분기의 상품 매출
  , sales_2016_q4
  --2016년 4분기의 상춤 매출 합계
  , SUM(sales_2016_q4) OVER() AS sum_sales_2016_q4
FROM item_sales_per_quarters
;
```

분기별 상품 매출액을 기반으로 점수를 계산하는 쿼리문
```python
WITH
item_sales_per_quarters AS (
  SELECT
	 item
	 --2016년 1분기의 상품 매출 모두 더하기
   , SUM(
      CASE WHEN year_month IN ('2016-01', '2016-02', '2016-03') THEN amount ELSE 0 END
     ) AS sales_2016_q1
	 --2016년 4분기의 상품 매출 모두 더하기
   , SUM(
      CASE WHEN year_month IN ('2016-10', '2016-11', '2016-12') THEN amount ELSE 0 END
     ) AS sales_2016_q4
  FROM monthly_sales
  GROUP BY
    item
)
, item_scores_per_quarters AS (
   SELECT
	  item
    , sales_2016_q1
	, 1.0
	  * (sales_2016_q1 - MIN(sales_2016_q1) OVER())
	  --■Postgre SQL, Redshift, BigQuery, SparkSQL의 경우 NULLIF로 0으로 나누는것 피하기
	  / NULLIF(MAX(sales_2016_q1) OVER() - MIN(sales_2016_q1) OVER(), 0)
	  --■Hive의 경우 NULLIF 대신 CASE 식 사용하기
	  -- / (CASE
      --    WHEN MAX(sales_2016_q1) OVER() - MIN(sales_2016_q1) OVER() = 0 THEN NULL
      --    END)
	  AS score_2016_q1
    , sales_2016_q4
	, 1.0
	  * (sales_2016_q4 - MIN(sales_2016_q4) OVER())
	  --■PostgreSQL, Redshift, BigQuery, SparkSQL의 경우 NULLIF로 0으로 나누는 것 피하기
	  / NULLIF(MAX(sales_2016_q4) OVER() - MIN(sales_2016_q4) OVER(), 0)
	  --■Hive의 경우 NULLIF 대신 CASE 식 사용하기
	  -- / (CASE
      --    WHEN MAX(sales_2016_q4) OVER() - MIN(sales_2016_q4) OVER() = 0 THEN NULL
      --    END)
	  AS score_2016_q4
   FROM item_sales_per_quarters
)
SELECT *
FROM item_scores_per_quarters
;
```

분기별 상품 점수 가중 평균으로 순위를 생성하는 쿼리문
```python
WITH
item_sales_per_quarters AS (
  SELECT
	 item
	 --2016년 1분기의 상품 매출 모두 더하기
   , SUM(
      CASE WHEN year_month IN ('2016-01', '2016-02', '2016-03') THEN amount ELSE 0 END
     ) AS sales_2016_q1
	 --2016년 4분기의 상품 매출 모두 더하기
   , SUM(
      CASE WHEN year_month IN ('2016-10', '2016-11', '2016-12') THEN amount ELSE 0 END
     ) AS sales_2016_q4
  FROM monthly_sales
  GROUP BY
    item
)
, item_scores_per_quarters AS (
   SELECT
	  item
    , sales_2016_q1
	, 1.0
	  * (sales_2016_q1 - MIN(sales_2016_q1) OVER())
	  --■Postgre SQL, Redshift, BigQuery, SparkSQL의 경우 NULLIF로 0으로 나누는것 피하기
	  / NULLIF(MAX(sales_2016_q1) OVER() - MIN(sales_2016_q1) OVER(), 0)
	  --■Hive의 경우 NULLIF 대신 CASE 식 사용하기
	  -- / (CASE
      --    WHEN MAX(sales_2016_q1) OVER() - MIN(sales_2016_q1) OVER() = 0 THEN NULL
      --    END)
	  AS score_2016_q1
    , sales_2016_q4
	, 1.0
	  * (sales_2016_q4 - MIN(sales_2016_q4) OVER())
	  --■PostgreSQL, Redshift, BigQuery, SparkSQL의 경우 NULLIF로 0으로 나누는 것 피하기
	  / NULLIF(MAX(sales_2016_q4) OVER() - MIN(sales_2016_q4) OVER(), 0)
	  --■Hive의 경우 NULLIF 대신 CASE 식 사용하기
	  -- / (CASE
      --    WHEN MAX(sales_2016_q4) OVER() - MIN(sales_2016_q4) OVER() = 0 THEN NULL
      --    END)
	  AS score_2016_q4
   FROM item_sales_per_quarters
)
SELECT
   item
 , 0.7 * score_2016_q1 + 0.3 * score_2016_q4 AS score
 , ROW_NUMBER()
    OVER(ORDER BY 0.7 * score_2016_q1 + 0.3 * score_2016_q4 DESC)
   AS rank
FROM item_socres_per_quarters
ORDER BY rank
;
```

이번 절에서 소개한 방법에 따라 주기 요소가 있는 상품과 트렌드 상품을

균형있게 조합한 순위를 생성할 수 있습니다.

추가로 여러 가지 점수 계산 방신을 조합하면 다양한 분야에 활용할 수 있습니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 23강 점수 계산하기 566 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어