---
title: postgre SQL-practice36
tag: postgre SQL-practice36
date: 2022-03-19
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

5장이 끝나고 오늘 부터 6장으로 넘어간다.

'6장  14강 사이트 전체의 특징/경향 찾기

1. 날짜별 방문자 수/ 방문 횟수 / 페이지 뷰 집계하기'

페이지 324 ~ 328을 보고 쿼리문을 작성하였다.

날짜별 접근 데이터를 집계하는 쿼리문
```python
SELECT
 -- ■ PostgreSQL, Hive, Redshift, SparkSQL의 경우 substring으로 날짜 부분 추출하기
  substring(stamp, 1, 10) AS dt
 --■ PostgreSQL, Hive, BigQuery, SparkSQL의 경우 substr 사용하기
-- substr(stamp, 1, 10) AS dt
-- 쿠키 계산하기
, COUNT(DISTINCT long_session) AS access_users
-- 방문 횟수 계산하기
, COUNT(DISTINCT short_session) AS access_count
-- 페이지 뷰 계산하기
, COUNT(*) AS page_view


-- 1인당 페이지 뷰 수
-- ■ PostgreSQL, Redshift, BigQuery, SparkSQL의 경우 NULLIF 함수 사용 가능
 , 1.0 * COUNT(*) / NULLIF(COUNT(DISTINCT long_session), 0) AS pv_per_user
-- ■ Hive의 경우 NULLIF 함수 대신 CASE 식 사용하기
--, 1.0 * COUNT(*)
-- / CASE
--    WHEN COUNT(DISTINCT long_session) <> 0 THEN COUNT(DISTINCT long_session)
--  END
-- AS pv_per_user
FROM 
 access_log
GROUP BY
 -- ■ PostgreSQL, Redshift, BigQuery의 경우
 --   SELECT 구문에서 정의한 별칭을 GROUP BY에 지정할 수 있음
 dt
 -- ■ PostgreSQL, Hive, Redshift, SparkSQL의 경우
 --   SELECT 구문에서 별칭을 지정하기 이전의 식을 GROUP BY에 지정할 수 있음
 --substring(stamp, 1, 10)
ORDER BY
  dt
;
```
페이지 뷰 정보만 필요하다고 해도, 그 이외의 지표를 집계할 때마다 

별도의 SQL을 새로 작성해서 실행하기란 굉장히 귀찮은 일입니다.

따라서 한번에 모든 정보를 추출할 수 있는 SQL을 만들어두고 사용하기

바랍니다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의 

행동을 파악하는 데이터 추출하기 14강 페이지 328 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어

