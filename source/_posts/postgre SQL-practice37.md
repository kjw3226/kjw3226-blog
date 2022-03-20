---
title: postgre SQL-practice37
tag: postgre SQL-practice37
date: 2022-03-20
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'6장  14강 사이트 전체의 특징/경향 찾기

2. 페이지별 쿠키/방문횟수/페이지 뷰 집계하기'

페이지 324 ~ 328을 보고 쿼리문을 작성하였다.

URL별로 집계하는 쿼리문
```python
SELECT
   url
 , COUNT(DISTINCT short_session) AS access_count
 , COUNT(DISTINCT long_session) AS access_count
 , COUNT(*) AS page_view
FROM
 access_log
GROUP BY
 url
;
```
경로별로 집계하는 쿼리문
```python
WITH
access_log_with_path AS (
 -- URL에서 경로 추출하기
 SELECT *
  -- ■ PostgreSQL의 경우 정규 표현식으로 경로 부분 추출하기
   , substring(url from '//[^/]+([^?#])') AS url_path
  -- ■ Redshift의 경우 regexp_substr 함수와 regexp_replace 함수를 조합해서 사용하기
  --, regexp_replace(regexp_substr(url, '//[^/]+([^?#]+'), '//[^/]+', '') AS url_path
  -- ■ BigQuery의 경우 정규 표현식에 regexp_extract 사용하기
  --, regexp_extract(url, '//[^/]+([^?#]+)') AS url_path
  -- ■ Hive, SparkSQL의 경우는 parse_url 함수로 URL 경로 부분 추출하기
  --, parse_url(url, 'PATH') AS url_path
 FROM access_log
)
SELECT
   url_path
 , COUNT(DISTINCT short_session) AS access_count
 , COUNT(DISTINCT long_session) AS access_users
 , COUNT(*) AS page_view
FROM
 access_log_with_path
GROUP BY
 url_path
;
```

URL에 의미를 부여해서 집계하는 쿼리문
```python
WITH
access_log_with_path AS (
 -- URL에서 경로 추출하기
 SELECT *
  -- ■ PostgreSQL의 경우 정규 표현식으로 경로 부분 추출하기
   , substring(url from '//[^/]+([^?#])') AS url_path
  -- ■ Redshift의 경우 regexp_substr 함수와 regexp_replace 함수를 조합해서 사용하기
  --, regexp_replace(regexp_substr(url, '//[^/]+([^?#]+'), '//[^/]+', '') AS url_path
  -- ■ BigQuery의 경우 정규 표현식에 regexp_extract 사용하기
  --, regexp_extract(url, '//[^/]+([^?#]+)') AS url_path
  -- ■ Hive, SparkSQL의 경우는 parse_url 함수로 URL 경로 부분 추출하기
  --, parse_url(url, 'PATH') AS url_path
 FROM access_log
)
, access_log_with_split_path AS (
  -- 경로의 첫 번째 요소와 두 번째 요소 추출하기
  SELECT *
   -- ■ PostgreSQL, Redshift의 경우 split_part로 n번째 요소 추출하기
   , split_part(url_path, '/', 2) AS path1
   , split_park(url_path, '/', 3) AS path2
   -- ■ BigQuery의 경우 split 함수로 배열로 분해하고 추출하기
   --, split(url_path, '/')[1] AS path1
   --, split(url_path, '/')[2] AS path2
  FROM access_log_with_path
)
, access_log_with_page_name AS (
  -- 경로를 슬래시로 분할하고, 조건에 따라 페이지 이름 붙이기
  SELECT *
	, CASE
	   WHEN path1 = 'list' THEN
	    CASE
	     WHEN path2 = 'newly' THEN 'newly_list'
	     ELSE
	  END
	   -- 이외의 경우는 경로를 그대로 사용하기
	  ELSE url_path
	END AS page_naem
 FROM access_log_with_split_path
)
SELECT
   page_name
 , COUNT(DISTINCT short_session) AS access_count
 , COUNT(DISTINCT long_session) AS access_users
 , COUNT(*) AS page_view
FROM access_log_with_page_name
GROUP BY page_name
ORDER BY page_name
;
```
로그를 저장 할 때 해당 페이지에 어떤 의미가 있는지 알려주는 

'페이지 이름'을 따로 전송하면, 집계할 때 굉장히 편리해집니다.

로그를 설계할 때 이후의 집계작업을 내다보고 설계하고 검토하도록 

합니다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 14강 페이지 332 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어