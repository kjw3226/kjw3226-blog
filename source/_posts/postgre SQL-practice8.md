---
title: postgre SQL-pratice8
tag: postgre SQL-pratice8
date: 2022-02-09
categories:	SQL
----
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

 이번에는 'WITH'구문('CTE')을 활용한 쿼리문에 대해  
 한번 실습해봤다.
 
'계산한 테이블에 이름 붙여 재사용하기'

카테고리별 순위를 추가한 테이블에 이름 붙이기
```python
SELECT
   m.user_id
 , m.card_number
 , COUNT(p.user_id) AS purchase_count
  -- 신용 카드 번호를 등록한 경우 1, 등록하지 않은 경우 0으로 표현하기
 , CASE WHEN m.card_number IS NOT NULL THEN 1 ELSE 0 END AS has_card
  -- 구매 이력이 있는 경우 1, 구매 이력이 없을 경우 0으로 표현하기
 , SIGN(COUNT(p.user_id)) AS has_purchased
FROM
   mst_users_with_card_number AS m
 LEFT JOIN
  purchase_log AS p
  ON m.user_id = p.user_id
GROUP BY m.user_id, m.card_number
;
```

카테고리들의 순위에서 유니크한 순위 목록을 계산하는 쿼리문
```python
WITH
product_sale_ranking AS (
 SELECT
category_name
, product_id
, sales
, ROW_NUMBER() OVER(PARTITION BY category_name ORDER BY sales DESC) AS rank
FROM
product_sales
)
, mst_rank AS (
 SELECT DISTINCT rank
FROM product_sale_ranking
)
SELECT*
FROM mst_rank
;
```

카테고리들의 순위를 횡단적으로 출력하는 쿼리문
```python
WITH
product_sale_ranking AS (
	SELECT
	   category_name
	 , product_id
	 , sales
	 , ROW_NUMBER() OVER(PARTITION BY category_name ORDER BY sales DESC) AS rank
	FROM
	 product_sales
)
, mst_rank AS (
  SELECT DISTINCT rank
  FROM product_sale_ranking
)
SELECT
   m.rank
 , r1.product_id AS dvd
 , r1.sales     AS dvd_sales
 , r2.product_id AS cd
 , r2.sales     AS cd_sales
 , r3.product_id AS book
 , r3.sales     AS book_sales
FROM
   mst_rank AS m
  LEFT JOIN
   product_sale_ranking AS r1
   ON m.rank = r1.rank
   AND r1.category_name = 'dvd'
  LEFT JOIN
   product_sale_ranking AS r2
   ON m.rank = r2.rank
   AND r1.category_name = 'cd'
  LEFT JOIN
   product_sale_ranking AS r3
   ON m.rank = r3.rank
   AND r3.category_name = 'book'
ORDER BY m.rank
;
```

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)
참고 도서 : 데이터 분석을 위한 SQL 레시피
저자 : 가나키 나가토, 다미야 나오토
출판사 : 한빛미디어
