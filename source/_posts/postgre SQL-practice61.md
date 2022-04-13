----
title: postgre SQL-practice61
tag: postgre SQL-practice61
date: 2022-04-13
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'7장  20강 여러 개의 데이터셋 비교하기'의

'2. 두 순위의 유사도 계산하기'로 넘어갔으며

페이지 459 ~ 464을 참고하였다.

3개의 지표를 기반으로 순위를 작성하는 쿼리문
```python
WITH
path_stat AS (
 -- 경로별 방문 횟수, 방문자 수, 페이지 뷰 계산하기
 SELECT
	path
  , COUNT(DISTINCT long_session) AS access_users
  , COUNT(DISTINCT short_session) AS access_count
  , COUNT(*) AS page_view
FROM
 access_log
GROUP BY
 path
)
, path_ranking AS (
 --방문 횟수, 방문자 수, 페이지 뷰별로 순위 붙이기
 SELECT 'access_user'  AS type, path, RANK() OVER(ORDER BY access_users DESC) AS rank
 FROM path_stat
UNION ALL
 SELECT 'access_count' AS type, path, RANK() OVER(ORDER BY access_count DESC) AS rank
 FROM path_stat
UNION ALL
 SELECT 'page_view'    AS type, path, RANK() OVER(ORDER BY page_view    DESC) AS rank
 FROM path_stat
)
SELECT *
FROM
 path_ranking
ORDER BY
 type, rank
;
```

경로들의 순위 차이를 계산하는 쿼리문
```python
WITH
path_stat AS (
 -- 경로별 방문 횟수, 방문자 수, 페이지 뷰 계산하기
 SELECT
	path
  , COUNT(DISTINCT long_session) AS access_users
  , COUNT(DISTINCT short_session) AS access_count
  , COUNT(*) AS page_view
FROM
 access_log
GROUP BY
 path
)
, path_ranking AS (
 --방문 횟수, 방문자 수, 페이지 뷰별로 순위 붙이기
 SELECT 'access_user'  AS type, path, RANK() OVER(ORDER BY access_users DESC) AS rank
 FROM path_stat
UNION ALL
 SELECT 'access_count' AS type, path, RANK() OVER(ORDER BY access_count DESC) AS rank
 FROM path_stat
UNION ALL
 SELECT 'page_view'    AS type, path, RANK() OVER(ORDER BY page_view    DESC) AS rank
 FROM path_stat
)
, pair_ranking AS (
SELECT 
   r1.path
 , r1.type AS type1
 , r1.rank AS rank1
 , r1.type AS type2
 , r1.rank AS rank2
   --순위 차이 계산하기
 , POWER(r1.rank - r2.rank, 2) AS diff
FROM
   path_ranking AS r1
  JOIN
   path_ranking AS r2
   ON r1.path = r2.path
)
SELECT
 *
FROM
 pair_ranking
ORDER BY
 type1, type2, rank1
;
```


스피어만 상관계수로 순위의 유사도를 계산하는 쿼리문
```python
WITH
path_stat AS (
 -- 경로별 방문 횟수, 방문자 수, 페이지 뷰 계산하기
 SELECT
	path
  , COUNT(DISTINCT long_session) AS access_users
  , COUNT(DISTINCT short_session) AS access_count
  , COUNT(*) AS page_view
FROM
 access_log
GROUP BY
 path
)
, path_ranking AS (
 --방문 횟수, 방문자 수, 페이지 뷰별로 순위 붙이기
 SELECT 'access_user'  AS type, path, RANK() OVER(ORDER BY access_users DESC) AS rank
 FROM path_stat
UNION ALL
 SELECT 'access_count' AS type, path, RANK() OVER(ORDER BY access_count DESC) AS rank
 FROM path_stat
UNION ALL
 SELECT 'page_view'    AS type, path, RANK() OVER(ORDER BY page_view    DESC) AS rank
 FROM path_stat
)
, pair_ranking AS (
SELECT 
   r1.path
 , r1.type AS type1
 , r1.rank AS rank1
 , r1.type AS type2
 , r1.rank AS rank2
   --순위 차이 계산하기
 , POWER(r1.rank - r2.rank, 2) AS diff
FROM
   path_ranking AS r1
  JOIN
   path_ranking AS r2
   ON r1.path = r2.path
)
SELECT
   type1
 , type2
 , 1 - (6.0 * SUM(diff) / (POWER(COUNT(1), 3) - COUNT(1))) AS spearman
FROM
 ir_ranking
GROUP BY
 type1, type2
ORDER BY
 type1, spearman DESC
;
```

두 순위의 유사도를 수치로 표현할 수 있으면, 서로 다른 점수를 기반으로

만든 쉬운가 어떤 유사성을 갖는지 확인할 수 있습니다. 이를 활용하면

순위를 기반으로 다른 지표와의 유사성을 구하고, 

이를 기반으로 이상적인 순위를 자동 생성할 수 있습니다.

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어