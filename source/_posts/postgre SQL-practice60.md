---
title: postgre SQL-practice60
tag: postgre SQL-practice60
date: 2022-04-12
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'7장  20강 여러 개의 데이터셋 비교하기'의

'1. 데이터의 차이 추출하기'로 넘어갔으며

페이지 452 ~ 458을 참고하였다.


추가된 마스터 데이터를 추출하는 쿼리문
```python
SELECT
 new_mst.*
FROM
   mst_products_20170101 AS new_mst
 LEFT OUTER JOIN
   mst_products_20161201 AS old_mst
  ON
   new_mst.product_id = old_mst.product_id
WHERE
  old_mst.product_id IS NULL
;
```

제거된 마스터 데이터를 추출하는 쿼리문
```python
SELECT
 old_mst.*
FROM
   mst_products_20170101 AS new_mst
  RIGHT OUTER JOIN
   mst_products_20161201 AS old_mst
  ON
   new_mst.product_id = old_mst.product_id
WHERE
 new_mst.product_id IS NULL
;
```


변경된 마스터 데이터를 추출하는 쿼리문
```python
SELECT
   new_mst.product_id
 , old_mst.name AS old_name
 , old_mst.price AS old_price
 , new_mst.name AS new_name
 , new_mst.price AS new_price
 , new_mst.updated_at
FROM
   mst_products_20170101 AS new_mst
  JOIN
   mst_products_20161201 AS old_mst
  ON
   new_mst.product_id = old_mst.product_id
WHERE
 -- 갱신 시점이 다른 레코드만 추출하기
 new_mst.updated_at <> old_mst.updated_at
;
```


변경된 마스터 데이터를 모두 추출하는 쿼리문
```python
SELECT
   COALESCE(new_mst.product_id, old_mst.porduct_id) AS product_id
 , COALESCE(new_mst.name      , old_mst.name      ) AS name
 , COALESCE(new_mst.price     , old_mst.price     ) AS price
 , COALESCE(new_mst.updated_at, old_mst.updated_at) AS updated_at
 , CASE
   WHEN old_mst.updated_at IS NULL THEN 'added'
   WHEN new_mst.updated_at IS NULL THEN 'deleted'
   WHEN new_mst.updated_at <> old_mst.updated_at THEN 'updated'
  END AS status
FROM
   mst_products_20170101 AS new_mst
 FULL OUTER JOIN
   mst_products_20161201 AS old_mst
 ON
   new_mst.product_id = old_mst.product_id
WHERE
 --■Postgre SQL의 경우 IS DISTINCT FROM 연산자를 사용해 NULL을 포함한 비교 가능
 new_mst.updated_at IS DISTINCT FROM old_mst.updated_at
 --■Redshift, BigQuery의 경우
 -- IS DISTINCT FROM 구문 대신 COALESCE 함수로 NULL을 디폴트 값으로 변환하고 비교하기
 --  COLASCE(nwe_mst.updated_at, 'infinity')
 --<> COALASCE(old_mst.updated_at, 'infinity')
;
```

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어