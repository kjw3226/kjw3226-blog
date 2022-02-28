---
title: postgre SQL-practice7
tag: postgre SQL-practice7
date: 2022-02-09
categories:	SQL
----
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

어제까지 실습했던 예제 쿼리문들은 하나의 테이블을 다루는 쿼리문

이었다. 

그래서 오늘부터는 한번에 여러개의 테이블을 다루는 쿼리문을 주로

실습할 것이다.

아래의 쿼리문들은 오늘 실습한 것들이다.

여러 개의 테이블을 세로로 결합하기
=> 1. UNION ALL 구문을 사용해 테이블을 세로로 결합하는 쿼리문
```python
SELECT 'app1' AS app_name, user_id, name, email FROM app1_mst_users
UNION ALL
SELECT 'app2' AS app_name, user_id, name, NULL AS email FROM app2_mst_users;
```

여러 개의 테이블을 가로로 결합하기
=> 1. 여러 개의 테이블을 결합해서 가로로 정렬하는 쿼리
```python
SELECT
  m.category_id
, m.name
, s.sales
, r.product_id AS sale_product
FROM 
   mst_categories AS m
  JOIN
   -- 카테고리별로 매출액 결합하기
   category_sales AS s
   ON m.category_id = s.category_id
  JOIN
   -- 카테고리별로 상품 결합하기
   product_sale_ranking AS r
   ON m.category_id = r.category_id
;
```


여러 개의 테이블을 가로로 결합하기
=> 2. 마스터 테이블의 행 수를 변경하지 않고 여러 개의 테이블을
      가로로 정렬하는 쿼리문
```python
SELECT
  m.category_id
, m.name
, s.sales
, r.product_id AS top_sale_product
FROM
   mst_categories AS m
  -- LEFT JOIN을 사용해서 결합한 레코드를 남김
 LEFT JOIN
   -- 카테고리별 매출액 결합하기
   category_sales AS s
   ON m.category_id = s.category_id
  --LEFT JOIN을 사용해 결합하지 못한 레코드 남김
  LEFT JOIN 
   -- 카테고리별 최고 매출 상품 하나만 추출해서 결합하기
   product_sale_ranking AS r
   ON m.category_id = r.category_id
   AND r.rank = 1
;
```
여러 개의 테이블을 가로로 결합하기
=> 3. 상관 서브쿼리로 여러 개의 테이블을 가로로 정렬하는 쿼리문
```python
SELECT
   m.category_id
 , m.name
    -- 상관 서브쿼리를 사용해 카테고리별로 매출액 추출하기
 , (SELECT s.sales
	FROM category_sales AS s
	WHERE m.category_id = s.category_id
	) AS sales
	-- 상관 서브쿼리를 사용해 카테고리별로 최고 매출 상품을
	-- 하나 추출하기(순위로 따로 압축하지 않아도 됨)
 ,  (SELECT r.product_id
	 FROM product_sale_ranking AS r
	 WHERE m.category_id = r.category_id
	 ORDER BY sales DESC
	 LIMIT 1
	 ) AS top_sale_product
FROM 
   mst_categories AS m
;
```

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)
참고 도서 : 데이터 분석을 위한 SQL 레시피
저자 : 가나키 나가토, 다미야 나오토
출판사 : 한빛미디어
