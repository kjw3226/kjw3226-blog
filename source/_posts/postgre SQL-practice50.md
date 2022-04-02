---
title: postgre SQL-practice50
tag: postgre SQL-practice50
date: 2022-04-02
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'6장  16강 입력 양식 최적화하기'로 넘어갔으며

'3. 입력 양식 직귀율 집계하기'에서  '4. 오류가 발생하는 항목과 내용 집계하기'

까지 참고하였다.

입력 양식 재귀율을 집계하는 쿼리문
```python
WITH
form_with_progress_flag AS (
  SELECT
  --■PostgreSQL, Hive, Redshift, SparkSQL의 경우 substring으로 날짜 부분 추출하기
   substring(stamp, 1, 10) AS dt
  --■PostgreSQL, Hive, BigQuery, SparkSQL의 경우 substr 사용하기
  --substr(stamp, 1, 10) AS dt
	
  , session
  -- 입력 화면으로의 방문 플래그계산하기
  , SIGN(
	   SUM(CASE WHEN path IN ('/regist/input') THEN 1 ELSE 0 END)
  )AS has_input
 --입력 확인 화면 또는 완료 화면으로의 방문 플래그 계산하기
  , SIGN(
	 SUM(CASE WHEN path IN ('/regist/confirm', '/regist/complete') THEN 1 ELSE 0 END)   
  )AS has_progress
 FROM form_log
 GROUP BY
 -- ■PostgreSQL, Redshift, BigQuery의 경우
 -- SELECT 구문에서의 정의한 별칭을 GROUP BY에 지정할 수 있음
 dt, session
 -- ■PostgreSQL, Hive, Redshift, SparkSQL의 경우
 -- SELECT 구문에서 별칭을 지정하기 이전의 식을 GROUP BY에 지정할 수 있음
 -- substring(stamp, 1, 10), session
)
SELECT
   dt
 , COUNT(1) AS input_count
 , SUM(CASE WHEN has_progress = 0 THEN 1 ELSE 0 END) AS bounce_count
 , 100.0 * AVG(CASE WHEN has_progress = 0 THEN 1 ELSE 0 END) AS bounce_rate
FROM
 form_with_progress_flag
WHERE 
 -- 입력 화면에 방문했던 세션만 추출하기
 has_input = 1
GROUP BY
 dt
;
```

페이지 열람 로그를 사용해서 앞의 리포트를 작성해도, 입력 시작 후에 

이탈했는지 또는 입력고 하지 않고 이탈했는지는 판별할 수 없습니다.

앞서 16강 2절에서 설명했듯이 처음 입력한 항목을 클릭할 때 또는 

처음 입력한 때에 자바스크립트로 로그를 송신해서 활용해야만 더 정밀하게

직귀율을 계산할 수 있습니다.


(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 15강 페이지 402 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어


각 입력 양식의 오류 발생 장소와 원인을 집계하는 쿼리문
```python
SELECT
   form
 , field
 , error_type
 , COUNT(1) AS count
 , 100.0 * COUNT(1) / SUM(COUNT(1)) OVER(PARTITION BY form) AS share
FROM
 form_error_log
GROUP BY
 form, field, error_type
ORDER BY
 form, count DESC
;
```

오류 발생율이 높은 항목부터 16상 첫 소절에서 설명한 대책을 실시하면 

좋습니다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 15강 페이지 405 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어