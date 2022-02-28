---
title: postgre SQL-practice6
tag: postgre SQL-practice6
date: 2022-02-08
categories:	SQL
----
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

 어제에 이어 오늘은 
 '가로 기반 데이터를 세로 기반으로 변환하기'와 
 'Redshift에서 문자열을 행으로 전개하기'
  에 대해 예제 쿼리문을 활용해 실습을 진행했다.
 
일련 번호를 가진 피벗 테이블을 사용해 행으로 변환하는 쿼리문
```python
SELECT 
   q.year
  -- Q1부터 Q4까지의 레이블 이름 출력하기
, CASE 
   WHEN p.idx = 1 THEN 'q1'
   WHEN p.idx = 2 THEN 'q2'
   WHEN p.idx = 3 THEN 'q3'
   WHEN p.idx = 4 THEN 'q4'
  END AS quarter
  -- Q1부터 Q4까지의 매출 출력하기
, CASE
   WHEN p.idx = 1 THEN q.q1
   WHEN p.idx = 2 THEN q.q2
   WHEN p.idx = 3 THEN q.q3
   WHEN p.idx = 4 THEN q.q4
  END AS sales
FROM 
   quarterly_sales AS q
 CROSS JOIN
  -- 행으로 전개하고 싶은 열의 수만큼 순번 테이블 만들기
  (          SELECT 1 AS idx
   UNION ALL SELECT 2 AS idx
   UNION ALL SELECT 3 AS idx
   UNION ALL SELECT 4 AS idx
    ) AS p
;
```

테이블 함수를 사용해서 배열을 행으로 전개하는 쿼리문
```python
-- ■ Postgre SQL의 경우 unnest 함수 사용하기
SELECT unnest(ARRAY['A001', 'A002', 'A003']) AS product_id;


-- ■ BigQuery의 경우 unnest 함수를 사용하지만
--    테이블 함수는 FROM 구문 내부에서만 사용 할 수 있음
-- SELECT*FROM unnest(ARRAY['A001', 'A002', 'A003']) AS product_id;


-- ■ Hive, SparkSQL의 경우 explode 함수 사용하기
-- SELECT explode(ARRAY['A001', 'A002', 'A003']) AS product_id;
```

테이블 함수를 사용해 쉼표로 구분된 문자열 데이터를 행으로 
전개하는 쿼리문
```python
SELECT 
   purchase_id
 , product_id
FROM 
   purchase_log AS p
  --string_to_array 함수로 문자열을 배열로 변환하고, unnest 함수로 테이블로 변환하기
  CROSS JOIN unnest(string_to_array(product_ids, ',')) AS product_id
  
  
  -- ■ BigQuery의 경우 문자열 분해에 split 함수 사용하기
  -- CROSS JOIN unnest(split('product_id',',')) AS product_id
  
  
  -- ■ Hive와 SparkSQL의 경우 LATERAL VIEW explode 사용하기
  -- LATERAL VIEW explode(split('product_id',',')) e AS product_id;
```

Postgre SQL에서 쉼표로 구분된 데이터를 행으로 전개하는 쿼리문
```python
SELECT 
   purchase_id
   -- 쉼표로 구분된 문자열을 한 번에 행으로 전개하기
 , regexp_split_to_table(product_ids,',') AS product_id
FROM purchase_log;
```

여기서부터는 '''Redshift'를 활용 한다면 이렇게 된다.'라는 걸
보여 주는 쿼리문들이다.

일련 번호를 가진 피벗 테이블을 만드는 쿼리문
```python
SELECT*
FROM(
	       SELECT 1 AS idx
 UNION ALL SELECT 2 AS idx
 UNION ALL SELECT 3 AS idx	
) AS pivot
;
```

split_part 함수의 사용 예
```python
SELECT
   split_part('A001,A002,A003',',',1) AS part_1
 , split_part('A001,A002,A003',',',2) AS part_2
 , split_part('A001,A002,A003',',',3) AS part_3
;
```

문자 수의 차이를 사용해 상품 수를 계산하는 쿼리문
```python
SELECT
   purchase_id
  , product_ids
  -- 상품 ID 문자열을 기반으로 쉼표를 제거하고,
  -- 문자 수의 차이를 계산해서 상품 수 구하기
, 1 + char_length(product_ids)
    - char_length(replace(product_ids,',',''))
  AS product_cum
FROM 
  purchase_log
;
```

피벗 테이블을 사용해 문자열을 행으로 전개하는 쿼리문
```python
SELECT
  l.purchase_id
 , l.product_ids
  -- 상품 수만큼 순번 붙이기
 , p.idx
  -- 문자열을 쉼표로 구분해서 분할하고, idx번째 요소 추출하기
 , split_part(l.product_ids,',',p.idx) AS product_id
FROM 
   purchase_log AS l
  JOIN
    (          SELECT 1 AS idx
	 UNION ALL SELECT 2 AS idx
	 UNION ALL SELECT 3 AS idx
	) AS p
	-- 피벗 테이블의 id가 상품 수 이하의 경우 결합하기
	ON p.idx <=
	   (1 + char_length(l.product_ids)
	      - char_length(replace(l.product_ids,',','')))
;
```

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)
참고 도서 : 데이터 분석을 위한 SQL 레시피
저자 : 가나키 나가토, 다미야 나오토
출판사 : 한빛미디어
