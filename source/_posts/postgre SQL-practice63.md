---
title: postgre SQL-practice63
tag: postgre SQL-practice63
date: 2022-04-15
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  21강 검색 기능 평가하기'의

'2. 재검색 비율과 키워드 집계하기'로 넘어갔으며

페이지 472 ~ 477 을 참고하였다.


검색 화면과 상세 화면의 접근 로그에 다음 줄의 액션을 기록하는 쿼리문
```python
WITH
access_log_with_next_action AS (
 SELECT
	stamp
  , session
  , action
  , LEAD(action)
	 --■PostgreSQL, Hive, Redshift, BigQuery의 경우는 다음과 같이 하기
	 OVER(PARTITION BY session ORDER BY stamp ASC)
	 --■SparkSQL의 경우 프레임 지정 필요
	 --OVER(PARTITION BY session ORDER BY stamp ASC
     --  ROWS BETWEEN 1 FOLLOWING AND 1 FOLLOWING)
    AS next_action
 FROM
  access_log
)
SELECT *
FROM access_log_with_next_action
ORDER BY
 session, stamp
;
```


재검색 비율을 집계하는 쿼리문
```python
WITH
access_log_with_next_action AS (
 SELECT
	stamp
  , session
  , action
  , LEAD(action)
	 --■PostgreSQL, Hive, Redshift, BigQuery의 경우는 다음과 같이 하기
	 OVER(PARTITION BY session ORDER BY stamp ASC)
	 --■SparkSQL의 경우 프레임 지정 필요
	 --OVER(PARTITION BY session ORDER BY stamp ASC
     --  ROWS BETWEEN 1 FOLLOWING AND 1 FOLLOWING)
    AS next_action
 FROM
  access_log
)
SELECT
 --■PostgreSQL, Hive, Redshift, SparkSQL의 경우 substring으로 날짜 부분 추출하기
  substring(stamp, 1, 10) AS dt
 --■PostgreSQL, Hive, BigQuery, SparkSQL의 경우 substr 사용하기
 --substr(stamp, 1, 10) AS dt
 , COUNT(1) AS search_count
 , SUM(CASE WHEN next_action = 'search' THEN 1 ELSE 0 END) AS retry_count
 , AVG(CASE WHEN next_action = 'search' THEN 1.0 ELSE 0.0 END) AS retry_rate
FROM
 access_log_with_next_action
GROUP BY
 --■PostgreSQL, Redshift, BigQuery의 경우
 -- SELECT 구문에서 정의한 별칭을 GROUP BY에 지정 할 수 있음
 dt
 --■PostgreSQL, Hive, Redshift, SparkSQL의 경우
 -- SELECT 구문에서 별칭을 지정하기 이전의 식을 GROUP BY에 지정 할 수 있음
 -- substring(stamp, 1, 10)
ORDER BY
 dt
;
```


재검색 키워드를 집계하는 쿼리문
```python
WITH
access_log_with_next_search AS (
 SELECT
	stamp
  , session
  , action
  , keyword
  , result_num
  , LEAD(action)
	 --■PostgreSQL, Hive, Redshift, BigQuery의 경우는 다음과 같이 하기
	 OVER(PARTITION BY session ORDER BY stamp ASC)
	 --■SparkSQL의 경우 프레임 지정 필요
	 --OVER(PARTITION BY session ORDER BY stamp ASC
     --  ROWS BETWEEN 1 FOLLOWING AND 1 FOLLOWING)
    AS next_keyword
  , LEAD(result_num)
	 --■PostgreSQL, Hive, Redshift, BigQuery의 경우는 다음과 같이 하기
	 OVER(PARTITION BY session ORDER BY stamp ASC)
	 --■SparkSQL의 경우 프레임 지정 필요
	 --OVER(PARTITION BY session ORDER BY stamp ASC
     --  ROWS BETWEEN 1 FOLLOWING AND 1 FOLLOWING)
	AS next_result_num
 FROM
  access_log
)
SELECT
   keyword
 , result_num
 , COUNT(1) AS retry_count
 , next_keyword
 , next_result_num
FROM
 access_log_with_next_search
WHERE
     action = 'search'
 AND next_action = 'search'
GROUP BY
 keyword, result_num, next_keyword, next_result_num
;
```

동의어 사전을 사람이 직접 관리하는 것은 굉장히 힘들며, 담당자의 실수로

인해 흔들림을 제거하지 못할 수도 있습니다.

따라서 재검색 키워드를 집계하고, 검색 시스템이 자동으로 이러한 흔들림을

제거하게 개선하는 방법도 고려하면 좋을 것입니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 21강 검색 기능 평가하기 477 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어
