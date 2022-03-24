---
title: postgre SQL-practice41
tag: postgre SQL-practice41
date: 2022-03-24
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'6장  15강 사이트 내의 사용자 행동 파악하기

2. 이탈률과 직귀율 계산하기'

로 넘어가서 쿼리문 작성 실습을 했습니다.

페이지 350 ~ 354까지를 참고하였다.

경력별 이탈률을 집계하는 쿼리문
```python
WITH
activity_log_with_exit_flag AS (
 SELECT
	*
  --출구 페이지 판정
  , CASE
	 WHEN ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp DESC) = 1 THEN 1
	 ELSE 0
	END AS is_exit
 FROM
  activity_log
)
SELECT
  path
, SUM(is_exit) AS exit_count
, COUNT(1) AS page_view
, AVG(100.0 * is_exit) AS exit_ratio
FROM
 activity_log_with_exit_flag
GROUP BY path
;
```

경로들의 직귀율을 집계하는 쿼리문
```python
WITH
activity_log_with_landing_bounce_flag AS (
 SELECT 
	*
  --입구 페이지 판정
  , CASE
	 WHEN COUNT(1) OVER(PARTITION BY session) = 1 THEN 1  
	 ELSE 0
    END AS is_bounce
 FROM
  activity_log
)
SELECT
  path
, SUM(is_bounce) AS bounce_count
, SUM(is_landing) AS landing_count
, AVG(100.0 * CASE WHEN is_landing = 1 THEN is_bounce END) AS bonuce_ratio
FROM
 activity_log_with_landing_bounce_flag
GROUP BY path
;
```

컴퓨터 전용 사이트와 스마트폰 전용 사이트가 개별적으로 존해하는 경우,

사용자가 원하는 컨텐츠나 콘텐츠 배치에 차이가 있을 수  있습니다.

따라서 이러한 경우에는 컴퓨터 전용 사이트와 스마트폰 전용 사이트를

따로 따로 집계해보기 바랍니다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 15강 페이지 354 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어