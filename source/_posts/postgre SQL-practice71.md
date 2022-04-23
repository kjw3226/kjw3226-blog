---
title: postgre SQL-pratice71
tag: postgre SQL-pratice71
date: 2022-04-23
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  23강 추천'의

'1. 추천 시스템의 넓은 의미'와 

'2.  특정 아이템에 흥미가 있는 사람이 함께 찾아보는 아이템 검색'

으로 넘어갔으며

페이지 513 ~ 526를 참고하였다.

추천 시스템(Recommendation System)이란 사용자의 흥미 기호를 분석해서

사용자가 관심을 가질 만한 정보를 출력해주는 정도로 생각하기 쉽습니다.

이 책에서는 추천 시스템을 더 광범위한 의미로 '사용자에게 가치 있는 정보를 추천하는 것'

이라고 정의하겠습니다.

추천 시스템은 크게 두 가지 종류로 구분할 수 있습니다.

첫 번째는 열람/구매한 아이템을 기반으로 다룬 아이템을 추천해주는 'Item to Item',

두 번째는 과거의 행동 또는 데모그래픽 정보를 기반으로 흥미와 기호를 유추하고 아이템을

추천하는 'User to Item'입니다.
```
<추천의 종류>

1. Item to Item : 아이템과 관련한 개별적인 아이템 제안  

   ex) 이 상품을 본 사람들은 다음 상품도 보았습니다.

2. User to Item : 사용자 개인에 최적화된 아이템 제안
   
   ex) 당신을 위한 추천 아이템
```

```
<모듈의 종류>

1. 리마인드 : 사용자의 과거 행동을 기반으로 아이템을 다시 제안

            하는 것  예) 최근 보았던 상품, 한 번 더 구매하기

2. 순위 : 열람 수, 구매 수 등을 기반으로 인기 있는 아이템을 

         제안해주는 것  예) 인기 순위, 급상승 순위

3. 콘텐츠 베이스 : 아이템의 추가 정보를 기반으로 다른 아이템을

                추천해 주는 것  예) 해당 배우가 출연한 다른 작품

4. 추천 : 서비스를 사용하는 사용자 전체의 행동 이력을 기반으로,

         다음에 볼만한 아이템 또는 관련된 아이템을 추측해 
   
         제안하는 것  예) 이 상품을 보았던 사람들은 이러한 

                        상품들도 함께 보았습니다.

5. 개별 추천 : 사용자 개인의 행동 이력을 기반으로 흥미 기호를 추측하고,

              흥미 있어 할 만한 아이템을 제안해주는 것
              
              예) 당신만을 위한 추천
```

```
<추천의 효과>

1. 다운셀 : 가격이 높아 구매를 고민하는 사용자에게 더 저렴한 아이템을

           제안해서 구매 수를 올리는 것 
           
           예) 이전 모델이 가격 할인을 시작했습니다.
           
2. 크로스셀 : 관련 상품을 함께 구매하게 해서 구매 단가를 올리는 것

             예) 함께 구매되는 상품이 있습니다.
             
3. 업셀  :  상위 모델 또는 고성능의 아이템을 제안해서 구매 단가를 

           올리는 것  예) 이 상품의 최신 모델이 있습니다.
```

추천 시스템에는 다양한 목적, 효과, 모듈이 있습니다. 추천 시스템의 정의를 

확실하게 하고, 어떤 효과를 기대하는지 등을 구체화한 뒤 시스템을 구축하는 것을

추천합니다.


열람 수와 구매 수를 조합한 점수를 계산하는 쿼리문
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
SELECT *
FROM
 ratigs
ORDER BY
 user_id, score DESC
;
```


아이템 사이의 유사도를 계산하고 순위를 생성하는 쿼리문
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
SELECT
   r1.porduct AS target
 , r2.product AS related
   -- 모든 아이템을 열람/구매한 사용자 수
 , COUNT(r1.user_id)AS users
   -- 스코어들을 곱하고 합계를 구해 유사도 계산하기
 , SUM(r1.score * r2.score) AS score
   -- 상품의 유사도 순위 구하기
 , ROW_NUMBER()
    OVER(PARTITION BY r1.product ORDER BY SUM(r1.score * r2.score) DESC)
   AS rank
FROM
   ratings AS r1
 JOIN 
   ratings AS r2
   -- 공통 사용자가 존재하는 상품의 페어 만들기
   ON r1.user_id = r2.user_id
WHERE
 -- 같은 아이템의 경우에는 페어 제외하기
 r1.product <> r2.product
GROUP BY 
 r1.product, r2.product
ORDER BY
 target, rank
;
```



아이템 벡터를 L2 정규화하는 쿼리문
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
, purchase_base_normalized_ratings AS (
  -- 아이템 벡터 정규화하기
  SELECT
	 user_id
   , product
   , score
   , SQRT(SUM(score * score) OVER(PARTITION BY product)) AS norm
   , score / SQRT(SUM(score * score) OVER(PARTITION BY product)) AS norm_score
  FROM
   ratings
)
SELECT *
FROM
 product_base_normalized_ratings
;
```


정규화된 점수로 아이템의 유사도를 계산하는 쿼리문
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
, purchase_base_normalized_ratings AS (
  -- 아이템 벡터 정규화하기
  SELECT
	 user_id
   , product
   , score
   , SQRT(SUM(score * score) OVER(PARTITION BY product)) AS norm
   , score / SQRT(SUM(score * score) OVER(PARTITION BY product)) AS norm_score
  FROM
   ratings
)
SELECT
   r1.product AS target
 , r2.product AS related
   --모든 아이템을 열람/구매한 사용자 수
 , COUNT(r1.user_id) AS users
   --스코어들을 곱하고 합계를 구해 유사도 계산하기
 , SUM(r1.score * r2.score) AS score
 , SUM(r1.norm_score * r2.norm_score) AS norm_score
   --상품의 유사도 순위 구하기
 , ROW_NUMBER()
    OVER(PARTITION BY r1.product ORDER BY SUM(r1.norm_score * r2.norm_score) DESC)
   AS rank
FROM
   product_base_normalized_ratings AS r1
 JOIN
   product_base_normalized_ratings AS r2
   --공통 사용자가 존재하면 상품 페어 만들기
   ON r1.user_id = r2.user_id
GROUP BY
 r1.product, r2.product
ORDER BY
 target, rank
;
```

이번 절에서 소개한 아이템 유사도를 계산하는 방법은 벡터의 내적을

사용합니다. 이때 벡터로 아이템 조회 수와 구매 수를 사용했는데요,

실제 서비스 추천에 활용하려면 서비스의 특성을 고려해서 벡터를 

만들어야 합니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 23강 추천 526 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어
