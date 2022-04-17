---
title: postgre SQL-practice65
tag: postgre SQL-practice65
date: 2022-04-17
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  21강 검색 기능 평가하기'의

'4. 검색 이탈 비율과 키워드 집계하기'로 넘어갔으며

페이지 481 ~ 484를 참고하였다.


검색 이탈 비율을 집계하는 쿼리문
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
  substring(stamp, 1, 10)AS dt
 --■PostgreSQL, Hive, BigQuery, SparkSQL의 경우 substr 사용하기
 --substr(stamp, 1, 10) AS dt
 , COUNT(1) AS search_count
 , SUM(CASE WHEN next_action IS NULL THEN 1 ELSE 0 END) AS exit_count
 , AVG(CASE WHEN next_action IN NULL THEN 1.0 ELSE 0.0 END) AS exit_rate
FROM
 access_log_with_next_action
WHERE
 action = 'search'
GROUP BY
 --■PostgreSQL, Redshift, BigQuery의 경우
 --SELECT 구문에서 정의한 별칭을 GROUP BY에서 지정할 수 있음
 dt
 --■PostgreSQL, Hive, Redshift, SparkSQL의 경우
 --SELECT구문에서 별칭을 지정하기 이전의 식을 GROUP BY에 지정할 수 있음
 --substring(stamp, 1, 10)
ORDER BY
 dt
;
```


검색 이탈 키워드를 집계하는 쿼리문
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
 , COUNT(1) AS search_count
 , SUM(CASE WHEN next_action IS NULL THEN 1 ELSE 0 END) AS exit_count
 , AVG(CASE WHEN next_action IS NULL THEN 1.0 ELSE 0.0 END) AS exit_rate
 , result_num
FROM
 access_log_with_next_search
WHERE
 action = 'search'
GROUP BY
 keyword, result_num
 --키워드 전체의 이탈률을 계산한 후, 이탈률이 0보다 큰 키워드만 추출하기
HAVING
 SUM(CASE WHEN next_action IS NULL THEN 1 ELSE 0 END) > 0
;
```

검색에서 이탈한 사용자가 검색 결과에 만족하지 못한 이유는 굉장히

다양합니다. 예를 들어 원하는 상품이 상위에 표시되지 않는 등 출력 순서와

관련된 경우도 있습니다. 참고로 정렬 순서 평가 지표와 관계된 내용은 

21강 6절부터 차근근 설명하겠습니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 21강 검색 기능 평가하기 484 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어