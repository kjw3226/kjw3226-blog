---
title: postgre SQL-practice19
tag: postgre SQL-practice19
date: 2022-02-22
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

어제에 이서서 오늘은

'데이터 분석을 위한 SQL 레시피' 페이지 199~202를 보고 

실습을 진행했다. 

이 부분은 '5장 사용자를 파악하기 위한 데이터 추출' 중 '3. 연령별 구분의 특징 추출하기' 부분이다.

'연령별' 구분과 '카테고리'를 집계하는 쿼리문
```python
WITH
mst_users_with_int_birth_date AS (
 SELECT
	*
   -- 특정 날짜(2017년 1월 1일)의 정수 표현
   , 20170101 AS int_specific_date
   -- 문자열로 구성된 생년월일을 정수 표현을 변환하기
   -- ■ PostgreSQL, Redshift의 경우는 다음과 같이 작성
   , CAST(replace(substring(birth_date, 1, 10), '-', '') AS integer)AS int_birth_date
   -- ■ BigQuery의 경우는 다음과 같이 작성
   -- , CAST(replace(substr(birth_date, 1, 10), '-', '') AS int64)AS int_birth_date
   -- ■ Hive, SparkSQL의 경우는 다음과 같이 작성
   -- , CAST(regexp_replace(substring(birth_date, 1, 10), '-', '')AS int)
   --   AS int_birth_date
 FROM
  mst_users 
)
, mst_users_with_age AS (
  SELECT
   *
	
   -- 특정 날짜(2017년 1월 1일)의 나이
 , floor((int_specific_date - int_birth_date) / 10000) AS age
  FROM
   mst_users_with_int_birth_date
)
, mst_users_with_category AS (
  SELECT
	 user_id,
   , sex
   , age
   , CONCAT(
	   CASE
	     WHEN 20 <= age THEN sex
	     ELSE ''
	   END
	 , CASE
	    WHEN age BETWEEN 4  AND 12 THEN 'C'
	    WHEN age BETWEEN 13 AND 19 THEN 'T'
	    WHEN age BETWEEN 20 AND 34 THEN '1'
	    WHEN age BETWEEN 35 AND 49 THEN '2'
	   END
   ) AS category
  FROM
	mst_users_with_age
)
SELECT 
   p.category AS product_category
 , u.category AS user_category
 , COUNT(*) AS purchase_count
FROM
   action_log AS p
  JOIN
    mst_users_with_category AS u
  ON p.user_id = u.user_id
WHERE 
 -- 구매 로그만 선택하기
 action = 'purchase'
GROUP BY
p.category, u.category
ORDER BY
 p.category, u.category
;
```
10강 2절에서 설명한 ABC 분석과 구성비누계를 리포트에 추가하면, 리포트의 내용 전달성을 

향상시킬 수 있다. 

('데이터 분석을 위한 SQL레시피' 5장 '11강'中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어

