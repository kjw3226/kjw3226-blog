---
title: postgre SQL-practice66
tag: postgre SQL-practice66
date: 2022-04-18
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  21강 검색 기능 평가하기'의

'5. 검색 키워드 관련 지표의 집계 효율화하기'로 넘어갔으며

페이지 484 ~ 485를 참고하였다.


검색과 관련된 지표를 집계하기 쉽게 중간 데이터를 생성하는 쿼리문
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
, search_log_with_next_action(
SELECT *
FROM
access_log_with_next_search
WHERE
action = 'search'
)
SELECT *
FROM search_log_with_next_action
ORDER BY
 session, stamp
;
```

앞의 출력 결과를 사용하면 NoMatch 수, 재검색 수, 검색 이탈 수를 포함해

키워드 등을 간단하게 집계할 수 있습니다. 이러한 출력 결과를 테이블로 

저장하거나, 검색과 관련된 지표를 전처리하는 정형화된 WITH구문으로 

활용하면 작업 효율을 높일 수 있을 것입니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 21강 검색 기능 평가하기 485 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어