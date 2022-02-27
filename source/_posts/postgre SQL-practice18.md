---
title: postgre SQL-practice18
tag: postgre SQL-practice18
date: 2022-02-21
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

 이번에는 '데이터 분석을 위한 SQL 레시피' p192~198 까지를 보고
 
 실습을 진행하였다.
 
 '회원'과 '비회원'을 구분해서 집계하기(p192)
 
회원 상태를 판별하는 쿼리문
```python
WITH
action_log_with_status AS(
 SELECT
	session
  , user_id
  , action
  -- 로그를 타임스탬프 순서로 나열하고, 한 번이라도 로그인한 사용자일 경우,
  -- 이후의 모든 로그 상태를 member로 설정
  , CASE
	 WHEN
	   COALESCE(MAX(user_id)
		OVER(PARTITION BY session ORDER BY stamp
		 ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)	   
     , '') <>''
	THEN 'member'
  ELSE 'none'
 END AS member_status
, stamp
FROM 
 action_log
)
SELECT *
FROM 
 action_log_with_status
;
```
COALESCE 함수 또는 NULLIF 함수를 사용해 서로 변환하는 방법을 기억해두면 유용할 것이다.

(데이터 분석을 위한 SQL 레시피 5장 페이지 194 中)


 '연령별' 구분 집계하기 (p194)
'사용자'의 '생일'을 계산하는 쿼리문
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
SELECT
   user_id, sex, birth_date, age
FROM
 mst_users_with_age
;
```
 
 '성별'과 '연령'으로 '연령별' 구분을 계산하는 쿼리문
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
SELECT *
FROM
 mst_users_with_category
;
```
'연령별' 구분의 '사람 수'를 계산하는 쿼리문
```python
WITH
mst_users_with_age AS(
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
   category
 , COUNT(1) AS user_count
FROM
 mst_users_with_category
GROUP BY
 category
;
```
연령을 단순하게 계산하면 특징을 파악하기 힘들다. 데모그래픽 등에 활용하기 힘듭니다.

참고로 서비스에 따라서 M1,F1처럼 사용자 속성을 정의하는 것이 적절하지 않을 수 있다. 이러한 때는

독자적으로 새로운 기준을 정의하라.

(데이터 분석을 위한 SQL 레시피 5장 페이지 199 中)
