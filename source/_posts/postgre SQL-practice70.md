---
title: postgre SQL-pratice70
tag: postgre SQL-pratice70
date: 2022-04-22
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  22강 데이터 마이닝'의

'1. 어소시에이션 분석'으로 넘어갔으며

페이지 504 ~ 512를 참고하였다.


구매 로그 수와 상품별 구매 수를 세는 쿼리문
```python
WITH
purchase_id_count AS (
 --구매 상세 로그에서 유니크한 구매 로그 수 계산하기
 SELECT COUNT(DISTINCT purchase_id) AS purchase_count
 FROM purchase_detail_log
)
, purchase_detail_log_with_counts AS (
  SELECT
	 d.purchase_id
   , p.purchase_count
   , d.product_id
   -- 상품별 구매 수 계산하기
   , COUNT(1) OVER(PARTITION BY d.product_id) AS product_count
  FROM
	 purchase_detail_log AS d
   CROSS JOIN
	-- 구매 로그 수를 모든 레코드 수와 결합하기
	purchase_id_count AS p
)
SELECT
 *
FROM 
 purchase_detail_log_with_counts
ORDER BY
 product_id, purchase_id
;
```

상품 조합별로 구매 수를 세는 쿼리문
```python
WITH
purchase_id_count AS (
 --구매 상세 로그에서 유니크한 구매 로그 수 계산하기
 SELECT COUNT(DISTINCT purchase_id) AS purchase_count
 FROM purchase_detail_log
)
, purchase_detail_log_with_counts AS (
  SELECT
	 d.purchase_id
   , p.purchase_count
   , d.product_id
   -- 상품별 구매 수 계산하기
   , COUNT(1) OVER(PARTITION BY d.product_id) AS product_count
  FROM
	 purchase_detail_log AS d
   CROSS JOIN
	-- 구매 로그 수를 모든 레코드 수와 결합하기
	purchase_id_count AS p
)
, product_pair_with_stat AS (
  SELECT
	l1.product_id AS p1
  , l2.product_id AS p2
  , l1.product_count AS p1_count
  , l2.product_count AS p2_count
  , COUNT(1) AS p1_p2_count
  , l1.purchase_count AS purchase_count
  FROM
	 purchase_detail_log_with_counts AS l1
   JOIN
	 purchase_detail_log_with_counts AS l2
	ON l1.purchase_id = l2.purchase_id
  WHERE
   -- 같은 상품 조합 제외하기
   l1.product_id <> l2.product_id
  GROUP BY
	 l1.product_id
   , l2.product_id
   , l1.product_count
   , l2.product_count
   , l1.purchase_count
)
SELECT
 *
FROM 
 purchase_pair_with_stat
ORDER BY
 p1, p2
;
```

지지도, 확신도, 리프트를 계산하는 쿼리문
```python
WITH
purchase_id_count AS (
 --구매 상세 로그에서 유니크한 구매 로그 수 계산하기
 SELECT COUNT(DISTINCT purchase_id) AS purchase_count
 FROM purchase_detail_log
)
, purchase_detail_log_with_counts AS (
  SELECT
	 d.purchase_id
   , p.purchase_count
   , d.product_id
   -- 상품별 구매 수 계산하기
   , COUNT(1) OVER(PARTITION BY d.product_id) AS product_count
  FROM
	 purchase_detail_log AS d
   CROSS JOIN
	-- 구매 로그 수를 모든 레코드 수와 결합하기
	purchase_id_count AS p
)
, product_pair_with_stat AS (
  SELECT
	l1.product_id AS p1
  , l2.product_id AS p2
  , l1.product_count AS p1_count
  , l2.product_count AS p2_count
  , COUNT(1) AS p1_p2_count
  , l1.purchase_count AS purchase_count
  FROM
	 purchase_detail_log_with_counts AS l1
   JOIN
	 purchase_detail_log_with_counts AS l2
	ON l1.purchase_id = l2.purchase_id
  WHERE
   -- 같은 상품 조합 제외하기
   l1.product_id <> l2.product_id
  GROUP BY
	 l1.product_id
   , l2.product_id
   , l1.product_count
   , l2.product_count
   , l1.purchase_count
)
SELECT
   p1
 , p2
 , 100.0 * p1_p2_count / purchase_count AS support
 , 100.0 * p1_p2_count / p1_count AS confidence
 ,   (100.0 * p1_p2_count / p1.count)
   / (100.0 * p2_count / purchase_count) AS lift
FROM
 product_pair_with_stat
ORDER BY
 p1, p2
;
```

이번 절에서 소개한 어소시에이션 분석은 두 상품의 상관 규칙만을 주목한 

한정적인 분석 방법입니다.

이번 절에서 소개한 쿼리로 상관 규칙 추출과 관련된 내용을 이했다면,

다른 분석 방법도 찾아 도전해보기 바랍니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 22강 데이터 마이닝 503 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어
