---
title: postgre SQL-practice21
tag: postgre SQL-practice21
date: 2022-02-24
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

 '데이터 분석을 위한 SQL 레시피' 이번에는 
 
 '벤다이어그램'으로 '사용자'가 어떤 '액션(Action)'을 취했을 때를 집계하는 쿼리문을 실습해봤다.
 
 페이지 206 ~ 페이지 2014 까지를 보고 실습했다.

'사용자들'의 '액션 플래그'를 집계하는 쿼리문
```python
WITH
user_action_flag AS(
 -- 사용자가 액션을 했으면 1, 안 했으면 0으로 플래그 붙이기
 SELECT
    user_id
  , SIGN(SUM(CASE WHEN action = 'purchase' THEN 1 ELSE 0 END)) AS has_purchase
  , SIGN(SUM(CASE WHEN action = 'review' THEN 1 ELSE 0 END)) AS has_review
  , SIGN(SUM(CASE WHEN action = 'favorite' THEN 1 ELSE 0 END)) AS has_favorite
 FROM
	action_log
   GROUP BY
	user_id
)
SELECT *
FROM user_action_flag;
```

모든 '액션 조합'에 대한 '사용자 수' 계산하는 쿼리문
```python
WITH
user_action_flag AS(
 -- 사용자가 액션을 했으면 1, 안 했으면 0으로 플래그 붙이기
 SELECT
    user_id
  , SIGN(SUM(CASE WHEN action = 'purchase' THEN 1 ELSE 0 END)) AS has_purchase
  , SIGN(SUM(CASE WHEN action = 'review' THEN 1 ELSE 0 END)) AS has_review
  , SIGN(SUM(CASE WHEN action = 'favorite' THEN 1 ELSE 0 END)) AS has_favorite
 FROM
	action_log
   GROUP BY
	user_id
)
, action_venn_diagram AS(
  -- CUBE를 사용해서 모든 액션 조합 구하기
  SELECT
	 has_purchase
   , has_review
   , has_favorite
   , COUNT(1) AS users
  FROM
   user_action_flag
  GROUP BY
   CUBE(has_purchase, has_review, has_favorite)
)
SELECT *
FROM action_venn_diagram
ORDER BY
 has_purchase, has_review, has_favorite
;
```

'CUBE' 구문을 사용하지 않고 '표준 SQL'구문으로 작성하는 쿼리문
```python
WITH
user_action_flag AS(
 -- 사용자가 액션을 했으면 1, 안 했으면 0으로 플래그 붙이기
 SELECT
    user_id
  , SIGN(SUM(CASE WHEN action = 'purchase' THEN 1 ELSE 0 END)) AS has_purchase
  , SIGN(SUM(CASE WHEN action = 'review' THEN 1 ELSE 0 END)) AS has_review
  , SIGN(SUM(CASE WHEN action = 'favorite' THEN 1 ELSE 0 END)) AS has_favorite
 FROM
	action_log
   GROUP BY
	user_id
)
, action_venn_diagram AS(
  -- 모든 액션 조합을 개별적으로 구하고 UNION ALL로 결합
	
	
  -- 3개의 액션을 모두 한 경우 집계
	SELECT has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_flag
	GROUP BY has_purchase, has_review, has_favorite
	
  -- 3개의 액션 중에서 2개의 액션을 한 경우 집계
  UNION ALL
	SELECT NULL AS has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_falg
	GROUP BY has_review, has_favorite
  UNION ALL
	SELECT NULL AS has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_falg
	GROUP BY has_purchase, has_favorite
  UNION ALL
	SELECT NULL AS has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_falg
	GROUP BY has_purchase, has_review
	
  -- 3개의 액션 중에서 1개의 액션을 한 경우 집계
  UNION ALL
	SELECT NULL AS has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_falg
	GROUP BY has_favorite
  UNION ALL
	SELECT NULL AS has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_falg
	GROUP BY has_review
  UNION ALL
	SELECT NULL AS has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_falg
	GROUP BY has_purchase

  -- 액션과 관계 없이 모든 사용자 집계
  UNION ALL
   SELECT 
	NULL AS has_purchase, NULL AS has_review, NULL AS has_favorite, COUNT(1) AS users
   FROM user_action_flag
)

SELECT *
FROM action_venn_diagram
ORDER BY
 has_purchase, has_review, has_favorite
;
```

'유사적'으로 'NULL'을 포함한 '레코드'를 추가해서 'CUBE' 구문과 같은 결과를 얻는 쿼리문
```python
WITH
user_action_flag AS(
 -- 사용자가 액션을 했으면 1, 안 했으면 0으로 플래그 붙이기
 SELECT
    user_id
  , SIGN(SUM(CASE WHEN action = 'purchase' THEN 1 ELSE 0 END)) AS has_purchase
  , SIGN(SUM(CASE WHEN action = 'review' THEN 1 ELSE 0 END)) AS has_review
  , SIGN(SUM(CASE WHEN action = 'favorite' THEN 1 ELSE 0 END)) AS has_favorite
 FROM
	action_log
   GROUP BY
	user_id
)
, action_venn_diagram AS(
  SELECT
	mod_has_purchase AS has_purchase
  , mod_has_review AS has_review
  , mod_has_favorite AS has_favorite
  , COUNT(1) AS users
  FROM
	user_action_flag
   -- 각 칼럼에 NULL을 포함하는 레코드를 유사적으로 추가하기
   -- ■ BigQuery의 경우 CROSS JOIN unnest 함수 사용하기
   CROSS JOIN unnest(array[has_purchase, NULL]) AS mod_has_purchase
   CROSS JOIN unnest(array[has_review, NULL]) AS mod_has_review
   CROSS JOIN unnest(array[has_favorite, NULL]) AS mod_has_favorite
   -- ■ Hive, SparkSQL의 경우 LATERAL VIEW와 explode 함수 사용하기
   -- LATERAL VIEW explode(array(has_purchase, NULL)) e1 AS mod_has_purchase
   -- LATERAL VIEW explode(array(has_review, NULL)) e1 AS mod_has_review
   -- LATERAL VIEW explode(array(has_favorite, NULL)) e1 AS mod_has_favorite
  GROUP BY
	mod_has_purchase, mod_has_review, mod_has_favorite
)
SELECT *
FROM action_venn_diagram
ORDER BY
 has_purchase, has_review, has_favorite
;
```

'벤다이어그램'을 만들기 위해 '데이터'를 가공하는 쿼리문
```python
WITH
user_action_flag AS(
 -- 사용자가 액션을 했으면 1, 안 했으면 0으로 플래그 붙이기
 SELECT
    user_id
  , SIGN(SUM(CASE WHEN action = 'purchase' THEN 1 ELSE 0 END)) AS has_purchase
  , SIGN(SUM(CASE WHEN action = 'review' THEN 1 ELSE 0 END)) AS has_review
  , SIGN(SUM(CASE WHEN action = 'favorite' THEN 1 ELSE 0 END)) AS has_favorite
 FROM
	action_log
   GROUP BY
	user_id
)
, action_venn_diagram AS(
  -- CUBE를 사용해서 모든 액션 조합 구하기
  SELECT
	 has_purchase
   , has_review
   , has_favorite
   , COUNT(1) AS users
  FROM
   user_action_flag
  GROUP BY
   CUBE(has_purchase, has_review, has_favorite)

	-- 3개의 액션을 모두 한 경우 집계
	SELECT has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_flag
	GROUP BY has_purchase, has_review, has_favorite
	
  -- 3개의 액션 중에서 2개의 액션을 한 경우 집계
  UNION ALL
	SELECT NULL AS has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_falg
	GROUP BY has_review, has_favorite
  UNION ALL
	SELECT NULL AS has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_falg
	GROUP BY has_purchase, has_favorite
  UNION ALL
	SELECT NULL AS has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_falg
	GROUP BY has_purchase, has_review
	
  -- 3개의 액션 중에서 1개의 액션을 한 경우 집계
  UNION ALL
	SELECT NULL AS has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_falg
	GROUP BY has_favorite
  UNION ALL
	SELECT NULL AS has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_falg
	GROUP BY has_review
  UNION ALL
	SELECT NULL AS has_purchase, has_review, has_favorite, COUNT(1) AS users
	FROM user_action_falg
	GROUP BY has_purchase

  -- 액션과 관계 없이 모든 사용자 집계
  UNION ALL
   SELECT 
	NULL AS has_purchase, NULL AS has_review, NULL AS has_favorite, COUNT(1) AS users
   FROM user_action_flag
  SELECT
	mod_has_purchase AS has_purchase
  , mod_has_review AS has_review
  , mod_has_favorite AS has_favorite
  , COUNT(1) AS users
  FROM
	user_action_flag
   -- 각 칼럼에 NULL을 포함하는 레코드를 유사적으로 추가하기
   -- ■ BigQuery의 경우 CROSS JOIN unnest 함수 사용하기
   CROSS JOIN unnest(array[has_purchase, NULL]) AS mod_has_purchase
   CROSS JOIN unnest(array[has_review, NULL]) AS mod_has_review
   CROSS JOIN unnest(array[has_favorite, NULL]) AS mod_has_favorite
   -- ■ Hive, SparkSQL의 경우 LATERAL VIEW와 explode 함수 사용하기
   -- LATERAL VIEW explode(array(has_purchase, NULL)) e1 AS mod_has_purchase
   -- LATERAL VIEW explode(array(has_review, NULL)) e1 AS mod_has_review
   -- LATERAL VIEW explode(array(has_favorite, NULL)) e1 AS mod_has_favorite
  GROUP BY
	mod_has_purchase, mod_has_review, mod_has_favorite
)
SELECT
 -- 0, 1 플래그를 문자열로 가공하기
  CASE has_purchase
   WHEN 1 THEN 'purchase' WHEN 0 TEN 'not purchase' ELSE 'any'
  END AS has_review
, CASE has_review
   WHEN 1 THEN 'review' WHEN 0 THEN 'not review' ELSE 'any'
  END AS has_review
, CASE has_favorite
   WHEN 1 THEN 'favorite' WHEN 0 THEN 'not favorite' ELSE 'any'
  END AS has_favorite
, users
  -- 전체 사용자 수를 기반으로 비율 구하기
, 100.0 * users
  / NULLIF(
  -- 모든 액션이 NULL인 사용자 수가 전체 사용자 수를 나타내므로
  -- 해당 레코드의 사용자 수를 Window 함수로 구하기
	 SUM(CASE WHEN has_purchase IS NULL
		     AND has_review   IS NULL
		     AND has_favorite IS NULL
		    THEN users ELSE 0 END) OVER()
	    , 0)
	AS ratio
FROM 
 action_venn_diagram
ORDER BY
 has_purchase, has_review, has_favorite
;
```
이번 절에서는 'EC사이트'를 기준으로 했지만 'SNS'등의 사이트도 다음과 같은 형태로 적용할 수 있습니다.

####-글을 작성하지 않고 다른 사람의 글만 확인하는 사용자
####- 글을 많이 작성하는 사용자
####- 글을 거의 작성하지 않지만 댓글은 많이 작성하는 사용자
####- 글과 댓글 모두 적극적으로 작성하는 사용자

어떠한 대책을 수행했을 때, 해당 대책으로 효과가 발생한 사용자가 얼마나 되는지

'밴다이어그램'으로 확인하면, 대책을 제대로 세웠는지(대상을 제대로 가정했는지 등)

확인할 수 있습니다. 

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 11강 5.밴다이어그램으로 사용자 액션 집계하기 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)
참고 도서 : 데이터 분석을 위한 SQL 레시피
저자 : 가나키 나가토, 다미야 나오토
출판사 : 한빛미디어
