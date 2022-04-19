---
title: postgre SQL-practice67
tag: postgre SQL-practice67
date: 2022-04-19
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  21강 검색 기능 평가하기'의

'6. 검색 결과의 포괄성을 지표화하기'로 넘어갔으며

페이지 486 ~ 493를 참고하였다.


검색 결과와 정답 아이템을 결합하는 쿼리문
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
SELECT *
FROM 
 search_result_with_correct_items
ORDER BY
 keyword, rank
;
```


검색 결과 상위 n개의 재현율을 계산하는 쿼리문
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
, search_result_with_recall AS (
  SELECT 
	 *
    -- 검색 결과 상위에서 정답 데이터에 포함되는 아이템 수의 누계 구하기
	, SUM(correct)
	   --rank가 NULL이라면 정렬 순서의 마지막에 위치하므로
	   --편의상 굉장히 큰 값으로 변환해서 넣기
	   OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
		 ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_corrent
	, CASE
	   -- 검색 결과에 포함되지 않은 아이템은 편의상 적합률을 0으로 다루기
	   WHEN rank IS NULL THEN 0.0
	   ELSE
	     100.0
	     * SUM(correct)
	        OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
			  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
	     / SUM(correct) OVER(PARTITION BY keyword)
	  END AS recall
  FROM
    search_result_with_correct_items
)
SELECT *
FROM 
 search_result_with_recall
ORDER BY
  keyword, rank
;
```


검색 결과 상위 5개의 재현율을 키워드별로 추출하는 쿼리문
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
, search_result_with_recall AS (
  SELECT 
	 *
    -- 검색 결과 상위에서 정답 데이터에 포함되는 아이템 수의 누계 구하기
	, SUM(correct)
	   --rank가 NULL이라면 정렬 순서의 마지막에 위치하므로
	   --편의상 굉장히 큰 값으로 변환해서 넣기
	   OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
		 ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_corrent
	, CASE
	   -- 검색 결과에 포함되지 않은 아이템은 편의상 적합률을 0으로 다루기
	   WHEN rank IS NULL THEN 0.0
	   ELSE
	     100.0
	     * SUM(correct)
	        OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
			  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
	     / SUM(correct) OVER(PARTITION BY keyword)
	  END AS recall
  FROM
    search_result_with_correct_items
)
, recall_over_rank_5 AS (
  SELECT
	 keyword
   , rank
   , recall
     --검색 결과 순위가 높은 순서로 번호 붙이기
	 --검색 결과에 나오지 않는 아이템은 편의상 0으로 다루기
   , ROW_NUMBER()
	   OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 0) DESC)
	 AS desc_number
  FROM
	search_result_with_recall
  WHERE
    -- 검색 결과 상위 5개 이하 또는 검색 결과에 포함되지 않은 아이템만 출력하기\
	COALESCE(rank, 0) <= 5
)
SELECT 
   keyword
 , recall AS recall_at_5
FROM recall_over_rank_5
--검색 결과 상위 5개 중에서 가장 순위가 높은 레코드 추출하기
WHERE desc_number = 1
;
```


검색 엔진 전체의 평균 재현율을 계산하는 쿼리문
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
, search_result_with_recall AS (
  SELECT 
	 *
    -- 검색 결과 상위에서 정답 데이터에 포함되는 아이템 수의 누계 구하기
	, SUM(correct)
	   --rank가 NULL이라면 정렬 순서의 마지막에 위치하므로
	   --편의상 굉장히 큰 값으로 변환해서 넣기
	   OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
		 ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_corrent
	, CASE
	   -- 검색 결과에 포함되지 않은 아이템은 편의상 적합률을 0으로 다루기
	   WHEN rank IS NULL THEN 0.0
	   ELSE
	     100.0
	     * SUM(correct)
	        OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 100000) ASC
			  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
	     / SUM(correct) OVER(PARTITION BY keyword)
	  END AS recall
  FROM
    search_result_with_correct_items
)
, recall_over_rank_5 AS (
  SELECT
	 keyword
   , rank
   , recall
     --검색 결과 순위가 높은 순서로 번호 붙이기
	 --검색 결과에 나오지 않는 아이템은 편의상 0으로 다루기
   , ROW_NUMBER()
	   OVER(PARTITION BY keyword ORDER BY COALESCE(rank, 0) DESC)
	 AS desc_number
  FROM
	search_result_with_recall
  WHERE
    -- 검색 결과 상위 5개 이하 또는 검색 결과에 포함되지 않은 아이템만 출력하기\
	COALESCE(rank, 0) <= 5
)
SELECT
  AVG(recall) AS average_recall_at_5
FROM recall_over_rank_5
-- 검색 결과 상위 5개 중에서 가장 순위가 높은 레코드 추출하기
WHERE desc_number = 1
;
```

재현율은 정답 아이템에 포함되는 아이템을 어느 정도 망라할 수 있는지를 

나타내는 지표입니다. 재현율은 의학 또는 법 관련 정보를 다룰 때도 

굉장히 많이 사용되는 지료랍니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 21강 검색 기능 평가하기 493 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어