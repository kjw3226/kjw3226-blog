---
title: postgre SQL-practice42
tag: postgre SQL-practice42
date: 2022-03-25
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'6장  15강 사이트 내의 사용자 행동 파악하기

3. 성과로 이어지는 페이지 파악하기'

로 넘어가 실습을 진행했다.

페이지 354 ~ 358을 참고하였다.

컨버전 페이지보다 이전 접근에 플래그를 추가하는 쿼리문
```python
WITH
, activity_log_with_conversion_flag AS (
 SELECT
	session
  , stamp
  , path
	-- 성과를 발생시키는 컨버전 페이지의 이전 접근에 플래그 추가하기
  , SIGN(SUM(CASE WHEN path = '/complete' THEN 1 ELSE 0 END)
		OVER(PARTITION BY session ORDER BY stamp DESC
		  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW))
	AS has_conversion
 FROM
  activity_log
)
SELECT *
FROM
 activity_log_with_conversion_flag
ORDER BY
 session, stamp
;
```

경로들의 방문 횟수와 구성 수를 집계하는 쿼리문
```python
WITH
activity_log_with_conversion_flag AS (
 SELECT
	session
  , stamp
  , path
	-- 성과를 발생시키는 컨버전 페이지의 이전 접근에 플래그 추가하기
  , SIGN(SUM(CASE WHEN path = '/complete' THEN 1 ELSE 0 END)
		OVER(PARTITION BY session ORDER BY stamp DESC
		  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW))
	AS has_conversion
 FROM
  activity_log
)
SELECT
   path
  -- 방문 횟수
  , COUNT(DISTINCT session) AS session
  -- 성과 수
  , SUM(has_conversion) AS conversion
  -- <성과 수> / <방문 횟수>
  , 1.0 * SUM(has_conversion) / COUNT(DISTINCT session) AS cvr
FROM
 activity_log_with_conversion_flag
-- 경로별로 집약하기
GROUP BY path
;
```

상품 구매, 자료 청구, 회원 등록 등을 성과라고 하면, 성과 직전에 있는

페이지는 CVR이 굉장히 높게 측정됩니다.

같은 계층의 콘텐츠, 유사한 콘텐츠들을 비교해보기 바랍니다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 15강 페이지 358 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어