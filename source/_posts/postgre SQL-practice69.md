---
title: postgre SQL-practice69
tag: postgre SQL-practice69
date: 2022-04-21
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  21강 검색 기능 평가하기'의

'8. 검색 결과 순위와 관련된 지표 계산하기'로 넘어갔으며

페이지 497 ~ 503를 참고하였다.


정답 아이템별로 적합률을 추출하는 쿼리문
```python
WITH
search_result_with_correct_item AS (
  SELECT
	 COALESCE(r.keyword, c.keyword) AS keyword
   , r.rank
   , COALESCE(r.item, c.item) AS item
   , CASE WHEN c.item IS NOT NULL THEN 1 ELSE 0 END AS correct
  FROM
	 search_result AS r
   FULL OUTER JOIN 
	 correct_result AS c
	 ON r.keyword = c.keyword
	 AND r.item = c.item
)
, search_result_with_precision AS (
  SELECT
	 *
    --검색 결과의 상위에서 정답 데이터에 포함되는 아이템 수의 누계 구하기
	, SUM(correct)
	   --rank가 NULL이라면 정렬 순서의 마지막에 위치하므로
	   --편의상 굉장히 큰 값으로 변환해서 넣기
	   OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
		ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_correct
	, CASE
	   -- 검색 결과에 포함되지 않은 아이템은 편의상 적합률을 0으로 다루기
	   WHEN rank IS NULL THEN 0.0
	   ELSE 
	    100.0
	    * SUM(correct)
	       OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
			 ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
	    -- 재현률과 다르게 분모에 검색 결과 순위까지의 누계 아이템 수 지정하기
	    / COUNT(1)
	       OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
   END AS precision
  FROM
   search_result_with_correct_items
)
SELECT 
   keyword
 , rank
 , precision
FROM
 search_result_with_precision
WHERE
 correct = 1
;
```

검색 키워드별로 정확률의 평균을 계산하는 쿼리문
```python
WITH
search_result_with_correct_item AS (
  SELECT
	 COALESCE(r.keyword, c.keyword) AS keyword
   , r.rank
   , COALESCE(r.item, c.item) AS item
   , CASE WHEN c.item IS NOT NULL THEN 1 ELSE 0 END AS correct
  FROM
	 search_result AS r
   FULL OUTER JOIN 
	 correct_result AS c
	 ON r.keyword = c.keyword
	 AND r.item = c.item
)
, search_result_with_precision AS (
  SELECT
	 *
    --검색 결과의 상위에서 정답 데이터에 포함되는 아이템 수의 누계 구하기
	, SUM(correct)
	   --rank가 NULL이라면 정렬 순서의 마지막에 위치하므로
	   --편의상 굉장히 큰 값으로 변환해서 넣기
	   OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
		ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_correct
	, CASE
	   -- 검색 결과에 포함되지 않은 아이템은 편의상 적합률을 0으로 다루기
	   WHEN rank IS NULL THEN 0.0
	   ELSE 
	    100.0
	    * SUM(correct)
	       OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
			 ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
	    -- 재현률과 다르게 분모에 검색 결과 순위까지의 누계 아이템 수 지정하기
	    / COUNT(1)
	       OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
   END AS precision
  FROM
   search_result_with_correct_items
)
, average_precision_for_keywords AS (
  SELECT
	 keyword
   , AVG(precision) AS average_precision
  FROM
   search_result_with_precision
  WHERE
   correct = 1
  GROUP BY
   keyword
)
SELECT *
FROM
 average_precision_for_keywords
;
```

검색 엔진의 MAP을 계산하는 쿼리문
```python
WITH
search_result_with_correct_item AS (
  SELECT
	 COALESCE(r.keyword, c.keyword) AS keyword
   , r.rank
   , COALESCE(r.item, c.item) AS item
   , CASE WHEN c.item IS NOT NULL THEN 1 ELSE 0 END AS correct
  FROM
	 search_result AS r
   FULL OUTER JOIN 
	 correct_result AS c
	 ON r.keyword = c.keyword
	 AND r.item = c.item
)
, search_result_with_precision AS (
  SELECT
	 *
    --검색 결과의 상위에서 정답 데이터에 포함되는 아이템 수의 누계 구하기
	, SUM(correct)
	   --rank가 NULL이라면 정렬 순서의 마지막에 위치하므로
	   --편의상 굉장히 큰 값으로 변환해서 넣기
	   OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
		ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_correct
	, CASE
	   -- 검색 결과에 포함되지 않은 아이템은 편의상 적합률을 0으로 다루기
	   WHEN rank IS NULL THEN 0.0
	   ELSE 
	    100.0
	    * SUM(correct)
	       OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
			 ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
	    -- 재현률과 다르게 분모에 검색 결과 순위까지의 누계 아이템 수 지정하기
	    / COUNT(1)
	       OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
   END AS precision
  FROM
   search_result_with_correct_items
)
, average_precision_for_keywords AS (
  SELECT
	 keyword
   , AVG(precision) AS average_precision
  FROM
   search_result_with_precision
  WHERE
   correct = 1
  GROUP BY
   keyword
)
SELECT
 AVG(average_precision) AS mean_average_precision
FROM 
 average_precision_for_keywords
;
```

검색 엔진을 정량적으로 평가하기 위한 지표는 이 책에서 모두 소개할 수

없을 만큼 굉장히 많은 것이 고안되어 있습니다. 이 책에서 소개한 쿼리

들을 참고하면서, NDCG와 BPREF와 같은 다른 지표에 대해서도 정의와

적용 범위를 확인해 보고, 어떻게 쿼리를 작성하면 구할수 있는지 생각

해보세요.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 21강 검색 기능 평가하기 503 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어
