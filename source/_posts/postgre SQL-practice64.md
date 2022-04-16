---
title: postgre SQL-practice64
tag: postgre SQL-practice64
date: 2022-04-16
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  21강 검색 기능 평가하기'의

'3. 재검색 키워드를 분류해서 집계하기'로 넘어갔으며

페이지 477 ~ 481 을 참고하였다.

NoMatch에서 재검색 키워드를 집계하는 쿼리문
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
  --NoMatch 로그만 필터링 하기
  AND result_num = 0
GROUP BY
 keyword, result_num, next_keyword, next_result_num
;
```

검색 결과 필터링 시의 재검색 키워드를 집계하는 쿼리문
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
 --원래 키워드를 포함하는 경우만 추출하기
 --■PostgreSQL, Hive, BigQuery, SparkSQL의 경우 concat 함수 사용하기
 AND next_keyword, LIKE concat('%', keyword, '%')
 --■PostgreSQL, Redshift의 경우 || 연산자 사용하기
 --AND next_keyword LIKE '%' || keyword || '%'
GROUP BY
 keyword, result_num, next_keyword, next_result_num
;
```


검색 키워드 변경 때 검색엔진을 집계하는 쿼리문
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
 --원래 키워드를 포함하는 않는 검색 결과만 추출하기
 --■PostgreSQL, Hive, BigQuery, SparkSQL의 경우 concat 함수 사용하기
 AND next_keyword, NOT LIKE concat('%', keyword, '%')
 --■PostgreSQL, Redshift의 경우 || 연산자 사용하기
 --AND next_keyword NOT LIKE '%' || keyword || '%'
GROUP BY
 keyword, result_num, next_keyword, next_result_num
;
```

이번 절에서 소개한 세가지 경우는 모두 굉장히 다른 결과를 냅니다.

따라서 세가지를 모두 집계해서 활용하기 바랍니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 21강 검색 기능 평가하기 481 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어