---
title: postgre SQL-practice62
tag: postgre SQL-practice62
date: 2022-04-14
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  21강 검색 기능 평가하기'의

'1. NoMatch 비율과 키워드 집계하기'로 넘어갔으며

페이지 466 ~ 472을 참고하였다.


NoMath 비율을 집계하는 쿼리문
```python
SELECT
 --■PostgreSQL, Hive, Redshift, SparkSQL의 경우 substring으로 날짜 부분 추출하기
   substring(stamp, 1, 10) AS dt
 --■PostgreSQL, Hive, BigQuery, SparkSQL의 경우 substr 사용하기
 --substr(stamp, 1, 10) AS dt
 , COUNT(1) AS search_count
 , SUM(CASE WHEN result_num = 0 THEN 1 ELSE 0 END) AS no_match_count
 , AVG(CASE WHEN result_num = 0 THEN 1.0 ELSE 0.0 END) AS no_match_count
FROM
 access_log
WHERE
 action = 'search'
GROUP BY
 --■PostgreSQL, Redshift, BigQuery의 경우
 --SELECT 구문에서 정의한 별칭을 GROUP BY에 지정할 수 있음
 dt
 --■PostgreSQL, Hive, Redshift, SparkSQL의 경우 
 --SELECT 구문에서 별칭을 지정하기 이전의 식을 GROUP BY에 지정할 수 있음
 --substring(stamp, 1, 10)
;
```


NoMath 키워드를 집계하는 쿼리문
```python
WITH
search_keyword_stat AS (
 -- 검색 키워드 전체 집계 결과
 SELECT
	keyword
  , result_num
  , COUNT(1) AS search_count
  , 100.0 * COUNT(1) / COUNT(1) OVER() AS search_share
FROM
 access_log
WHERE
 action = 'search'
GROUP BY
 keyword, result_num
)
-- NoMatch 키워드 집계 결과
SELECT
   keyword
 , search_count
 , search_share
 , 100.0 * search_count / SUM(search_count) OVER() AS no_match_share
FROM
 search_keyword_stat
WHERE
 --검색 결과가 0개인 키워드만 추출하기
 result_num = 0
;
```

이번 절에서는 프리 키워드 검색을 전제로 설명했지만,

조건을 선택하는 카테고리 검색에서는 NoMatch 비율이 중요한 지표가 될 수

있습니다. 어떤 경우에도 검색결과가 0이 나오지 않게 여러 가지 대책을

세우기 바랍니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를 

무기로 삼기 위한 분석 기술 21강 검색 기능 평가하기 472 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어