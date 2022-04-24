---
title: postgre SQL-practice72
tag: postgre SQL-practice72
date: 2022-04-24
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  23강 추천'의


'3.  당신을 위한 추천 상품' 으로 넘어갔다.

페이지 526 ~ 531를 참고하였다.


사용자끼리의 유사도를 계산하는 쿼리문
```python
WITH
ratings AS (
 SELECT 
	user_id
  , product
	
	-- 상품 열람 수
  , SUM(CASE WHEN action = 'view'      THEN 1 ELSE 0 END) AS view_count
	
	-- 상품 구매 수
  , SUM(CASE WHEN action = 'purchase'      THEN 1 ELSE 0 END) AS purchase_count
	
	-- 열람 수와 구매 수에 3:7의 비율의 가중치 주어 평균 구하기
  ,  3.0 * SUM(CASE WHEN action = 'view'     THEN 1 ELSE 0 END)
	+0.7 * SUM(CASE WHEN action = 'purchase' THEN 1 ELSE 0 END)
	AS score
 FROM
  action_log
 GROUP BY
  user_id, product
)
, user_base_normalized_ratings AS (
  -- 사용자 벡터 정규화하기
  SELECT
	 user_id
   , product
   , score
	 -- PARTITION BY user_id으로 사용자별 벡터 노름 계산하기
   , SQRT(SUM(score * score) OVER(PARTITION BY user_id)) AS norm
   , score / SQRT(SUM(score * score) OVER(PARTITION BY user_id)) AS norm_score
  FROM
	ratings
)
, related_users AS (
 --경향이 비슷한 사용자 찾기
 SELECT
	r1.user_id
  , r2.user_id AS related_user
  , COUNT(r1.product) AS products
  , SUM(r1.norm_score * r2.norm_score) AS score
  , ROW_NUMBER()
	  OVER(PARTITION BY r1.user_id ORDER BY SUM(r1.norm_score * r2.norm_score) DESC)
    AS rank
 FROM
	user_base_normalized_ratings AS r1
  JOIN
	user_base_normalized_ratings AS r2
	ON r1.product = r2.product
 WHERE
  r1.user_id <> r2.user_id
 GROUP BY
  r1.user_id, r2.user_id
)
SELECT *
FROM
 related_users
ORDER BY 
 user_id, rank
;
```

순위가 높은 유사 사용자를 기반으로 추천 시스템을 추출하는 쿼리문
```python
WITH
ratings AS (
 SELECT 
	user_id
  , product
	
	-- 상품 열람 수
  , SUM(CASE WHEN action = 'view'      THEN 1 ELSE 0 END) AS view_count
	
	-- 상품 구매 수
  , SUM(CASE WHEN action = 'purchase'      THEN 1 ELSE 0 END) AS purchase_count
	
	-- 열람 수와 구매 수에 3:7의 비율의 가중치 주어 평균 구하기
  ,  3.0 * SUM(CASE WHEN action = 'view'     THEN 1 ELSE 0 END)
	+0.7 * SUM(CASE WHEN action = 'purchase' THEN 1 ELSE 0 END)
	AS score
 FROM
  action_log
 GROUP BY
  user_id, product
)
, user_base_normalized_ratings AS (
  -- 사용자 벡터 정규화하기
  SELECT
	 user_id
   , product
   , score
	 -- PARTITION BY user_id으로 사용자별 벡터 노름 계산하기
   , SQRT(SUM(score * score) OVER(PARTITION BY user_id)) AS norm
   , score / SQRT(SUM(score * score) OVER(PARTITION BY user_id)) AS norm_score
  FROM
	ratings
)
, related_users AS (
 --경향이 비슷한 사용자 찾기
 SELECT
	r1.user_id
  , r2.user_id AS related_user
  , COUNT(r1.product) AS products
  , SUM(r1.norm_score * r2.norm_score) AS score
  , ROW_NUMBER()
	  OVER(PARTITION BY r1.user_id ORDER BY SUM(r1.norm_score * r2.norm_score) DESC)
    AS rank
 FROM
	user_base_normalized_ratings AS r1
  JOIN
	user_base_normalized_ratings AS r2
	ON r1.product = r2.product
 WHERE
  r1.user_id <> r2.user_id
 GROUP BY
  r1.user_id, r2.user_id
)
, related_user_base_products AS (
  SELECT
	 u.user_id
   , r.product
   , SUM(u.score * r.score) AS score
   , ROW_NUMBER()
      OVER(PARTITION BY u.user_id ORDER BY SUM(u.score * r.score) DESC)
	 AS rank
  FROM
	 related_users AS u
   JOIN
	 ratings AS r
	 ON u.related_user = r.user_id
  WHERE
   u.rank <= 1
  GROUP BY 
   u.user_id, r.product
)
SELECT *
FROM
 related_user_base_products
ORDER BY
 user_id
;
```

이미 구매한 아이템을 필터링하는 쿼리문
```python
WITH
ratings AS (
 SELECT 
	user_id
  , product
	
	-- 상품 열람 수
  , SUM(CASE WHEN action = 'view'      THEN 1 ELSE 0 END) AS view_count
	
	-- 상품 구매 수
  , SUM(CASE WHEN action = 'purchase'      THEN 1 ELSE 0 END) AS purchase_count
	
	-- 열람 수와 구매 수에 3:7의 비율의 가중치 주어 평균 구하기
  ,  3.0 * SUM(CASE WHEN action = 'view'     THEN 1 ELSE 0 END)
	+0.7 * SUM(CASE WHEN action = 'purchase' THEN 1 ELSE 0 END)
	AS score
 FROM
  action_log
 GROUP BY
  user_id, product
)
, user_base_normalized_ratings AS (
  -- 사용자 벡터 정규화하기
  SELECT
	 user_id
   , product
   , score
	 -- PARTITION BY user_id으로 사용자별 벡터 노름 계산하기
   , SQRT(SUM(score * score) OVER(PARTITION BY user_id)) AS norm
   , score / SQRT(SUM(score * score) OVER(PARTITION BY user_id)) AS norm_score
  FROM
	ratings
)
, related_users AS (
 --경향이 비슷한 사용자 찾기
 SELECT
	r1.user_id
  , r2.user_id AS related_user
  , COUNT(r1.product) AS products
  , SUM(r1.norm_score * r2.norm_score) AS score
  , ROW_NUMBER()
	  OVER(PARTITION BY r1.user_id ORDER BY SUM(r1.norm_score * r2.norm_score) DESC)
    AS rank
 FROM
	user_base_normalized_ratings AS r1
  JOIN
	user_base_normalized_ratings AS r2
	ON r1.product = r2.product
 WHERE
  r1.user_id <> r2.user_id
 GROUP BY
  r1.user_id, r2.user_id
)
, related_user_base_products AS (
  SELECT
	 u.user_id
   , r.product
   , SUM(u.score * r.score) AS score
   , ROW_NUMBER()
      OVER(PARTITION BY u.user_id ORDER BY SUM(u.score * r.score) DESC)
	 AS rank
  FROM
	 related_users AS u
   JOIN
	 ratings AS r
	 ON u.related_user = r.user_id
  WHERE
   u.rank <= 1
  GROUP BY 
   u.user_id, r.product
)
SELECT
   p.user_id
 , p.product
 , p.score
 , ROW_NUMBER()
    OVER(PARTITION BY p.user_id ORDER BY p.socre DESC)
   AS rank
FROM
   related_user_base_products AS p
 LEFT JOIN
   ratings AS r
   ON p.user_id = r.user_id
   AND p.product = r.product
WHERE
 -- 대상 사용자가 구매하지 않은 상품만 추천하기
 COALESCE(r.purchase_count, 0) = 0
ORDER BY
 p.user_id
;
```

이번 절에서 소개한 사용자 행동 로그를 기반으로 유사 아이템을 찾고

추천하는 등의 기능은 '협업 필터링'이라고 부르는 개념의 한 가지 구현

방법입니다. 협업 필터링에는 기계 학습을 활용한 더 발전적인 방법도 

많으므로 다른 방법도 활용해서 다양한 추천에 도전 해보기 바랍니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 23강 추천 531 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어