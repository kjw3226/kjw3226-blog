---
title: postgre SQL-practice44
tag: postgre SQL-practice44
date: 2022-03-27
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'6장  15강 사이트 내의 사용자 행동 파악하기

5. 검색 조건들의 사용자 행동 가시화하기'

로 넘어갔으며, 페이지는 365 ~ 371을 참고하였다.


클릭 플래그와 컨버전 플래그를 계산하는 쿼리문
```python
WITH
activity_log_with_session_click_conversion_flag AS (
 SELECT 
	session
  , stamp
  , path
  , search_type
	-- 상세 페이지 이전 접근에 플래그 추가하기
  , SIGN(SUM(CASE WHEN path = '/detail' THEN 1 ELSE 0 END)
		OVER(PARTITION BY session ORDER BY stamp DESC
			ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW))
	AS has_session_click
	-- 성과를 발생시키는 페이지의 이전 접근에 플래그 추가하기
  , SIGN(SUM(CASE WHEN path = '/complete' THEN 1 ELSE 0 END)
		OVER(PARTITION BY session ORDER BY stamp DESC
			ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW))
	AS has_session_conversion
 FROM
  activity_log
)
SELECT
   session
 , stamp
 , path
 , search_type
 , has_session_click AS click
 , has_session_conversion AS cnv
FROM
 activity_log_with_session_click_conversion_flag
ORDER BY
 session, stamp
;
```

검색 타입별 CTR(상세페이지로 이동한 비율), 

CVR(상세 페이지 조회 후에 성과로 이어지는 비율)을 집계하는 쿼리문

```python
WITH
activity_log_with_session_click_conversion_flag AS (
 SELECT 
	session
  , stamp
  , path
  , search_type
	-- 상세 페이지 이전 접근에 플래그 추가하기
  , SIGN(SUM(CASE WHEN path = '/detail' THEN 1 ELSE 0 END)
		OVER(PARTITION BY session ORDER BY stamp DESC
			ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW))
	AS has_session_click
	-- 성과를 발생시키는 페이지의 이전 접근에 플래그 추가하기
  , SIGN(SUM(CASE WHEN path = '/complete' THEN 1 ELSE 0 END)
		OVER(PARTITION BY session ORDER BY stamp DESC
			ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW))
	AS has_session_conversion
 FROM
  activity_log
)
SELECT
   search_type
 , COUNT(1) AS count
 , SUM(has_session_click) AS detail
 , AVG(has_session_click) AS ctr
 , SUM(CASE WHEN has_session_click = 1 THEN has_session_conversion END) AS conversion
 , AVG(CASE WHEN has_session_click = 1 THEN has_session_conversion END) AS cvr
FROM
 activity_log_with_session_click_conversion_flag
WHERE
 -- 검색 로그만 추출하기
 path = '/search_list'
-- 검색 조건으로 집약하기
GROUP BY
 search_type
ORDER BY
 count DESC
;
```

클릭 플래그를 직전 페이지에 한정하는 쿼리문
```python
WITH
activity_log_with_session_click_conversion_flag AS (
 SELECT
	session
  , stamp
  , path
  , search_type
	-- 상세 페이지의 직전 접근에 플래그 추가하기
  , CASE
	 WHEN LAG(path) OVER(PARTITION BY session ORDER BY stamp DESC) = '/detail'
	  THEN 1
	 ELSE 0
    END AS has_session_click
	-- 성과가 발생하는 페이지의 이전 접근에 플래그 추가하기
  , SIGN(
     SUM(CASE WHEN path = '/complete' THEN 1 ELSE 0 END)
       OVER(PARTITION BY session ORDER BY stamp DESC
		ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
    ) AS has_session_conversion
 FROM
  activity_log
)
SELECT
   session
 , stamp
 , path
 , search_type
 , has_session_click AS click
 , has_session_conversion AS cnv
FROM
 activity_log_with_session_click_conversion_flag
ORDER BY
 session, stamp
;
```

조건을 상세하게 지정하더라도 검색에 걸리는 항목이 적거나 없으면

사용자가 이탈할 확률이 높습니다. 각각의 검색 조건과 히트되는 항목

수의 균형을 고려해서 카테고리를 어떻게 묶을지 검토하고 개선하기 바랍니다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 15강 페이지 371 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어