---
title: postgre SQL-practice31
tag: postgre SQL-practice31
date: 2022-03-13
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

페이지 279 ~ 287를 참고했다.

'5장  12강 시계열에 따른 사용자 전체의 상태 변화 찾기 

 7. 방문 빈도를 기반으로 사용자 속성을 정의하고 집계하기'

를 보고 쿼리문 작성 실습을 하였다.


신규 사용자 수, 리피트 사용자 수, 컴백 사용자 수를 집계하는 쿼리문
```python
WITH
monthly_user_action AS ( 
 -- 월별 사용자 액션 집약하기
 SELECT DISTINCT
	u.user_id
   -- ■ PostgreSQL의 경우 다음과 같이 사용하기
   , substring(u.register_date, 1, 7) AS register_month
   , substring(l.stamp, 1, 7) AS action_month
   , substring(CAST(
	  l.stamp::date - interval '1 month' AS text
   ), 1, 7) AS action_month_priv
 -- ■ Redshift의 경우 다음과 같이 사용하기
 --, substring(u.register_date, 1, 7) AS register_month
 --, substring(l.stamp, 1, 7) AS action_month
 --, substring(
 --  CAST(dateadd(month, -1, l.stamp::date) AS text), 1, 7)
 -- AS action_month_priv
 -- ■ BigQuery의 경우 다음과 같이 사용하기
 --, subst(u.register_date, 1, 7) AS register_month
 --, substr(l.stamp, 1, 7) AS action_month
 --, substr(CAST(
 --   date_sub(date(timestamp(l.stamp)), interval 1 month)
 --  AS string), 1, 7) AS action_month_priv
 -- ■ Hive, SparkSQL의 경우 다음과 같이 사용하기
 --, substring(u.register_date, 1, 7) AS register_month
 --, substring(l.stamp, 1, 7) AS action_month
 --, substring(
 --,  CAST(add_months(to_date(l.stamp), -1) AS string), 1, 7)
 --  AS action_month_priv
 FROM 
	mst_users AS u
   JOIN
	action_log AS l
	ON u.user_id = l.user_id
)
, monthly_user_with_type AS (
  -- 월별 사용자 분류 테이블
  SELECT
	 action_month
   , user_id
   , CASE
	  -- 등록 월과 액션월이 일치하면 신규 사용자
	  WHEN action_month_priv
	      = LAG(action_month)
	
	         OVER(PARTITION BY user_id ORDER BY action_month)
             -- ■ SparkSQL의 경우는 다음과 같이 사용하기
	         -- OVER(PARTITION BY user_id ORDER BY action_month
             --  ROW BETWEEN 1 PREVEDING AND 1 PRECEDING)
	
	      THEN 'repeat_user'
	 -- 이외의 경우는 컴백 사용자
	 ELSE 'come_back_user'
   END AS c
 , action_month_priv
FROM 
 monthly_user_action
)
SELECT
   action_month
   
   
   -- 특정 달의 MAU 
 , COUNT(user_id) AS mau
 
 
 -- ==============================================
 -- new_users:           특정 달의 신규 사용자 수
 -- repeat_users:         특정 달의 리피트 사용자 수
 -- come_back_uesers:      특정 달의 컴백 사용자 수
 -- ==============================================
, COUNT(CASE WHEN c = 'new_user'             THEN 1 END) AS new_users
, COUNT(CASE WHEN c = 'repeat_user'           THEN 1 END) AS repeat_users
, COUNT(CASE WHEN c = 'come_back_user'         THEN 1 END) AS come_back_users
FROM
   monthly_user_with_type
GROUP BY
 action_month
ORDER BY
 action_month
;
```

리피트 사용자를 세분화해서 집계하는 쿼리문
```python
WITH
monthly_user_action AS ( 
 -- 월별 사용자 액션 집약하기
 SELECT DISTINCT
	u.user_id
   -- ■ PostgreSQL의 경우 다음과 같이 사용하기
   , substring(u.register_date, 1, 7) AS register_month
   , substring(l.stamp, 1, 7) AS action_month
   , substring(CAST(
	  l.stamp::date - interval '1 month' AS text
   ), 1, 7) AS action_month_priv
, monthly_user_with_type AS (
  -- 월별 사용자 분류 테이블
  SELECT
	 action_month
   , user_id
   , CASE
	  -- 등록 월과 액션월이 일치하면 신규 사용자
	  WHEN action_month_priv
	      = LAG(action_month)
	
	         OVER(PARTITION BY user_id ORDER BY action_month)
             -- ■ SparkSQL의 경우는 다음과 같이 사용하기
	         -- OVER(PARTITION BY user_id ORDER BY action_month
             --  ROW BETWEEN 1 PREVEDING AND 1 PRECEDING)
	
	      THEN 'repeat_user'
	 -- 이외의 경우는 컴백 사용자
	 ELSE 'come_back_user'
   END AS c
 , action_month_priv
FROM 
 monthly_user_action
)
, monthly_users AS (
  SELECT
	 m1.action_month
	
   , COUNT(m1.user_id) AS mau
	
	
   , COUNT(CASE WHEN m1.c = 'new_user'             THEN 1 END) AS new_users
   , COUNT(CASE WHEN m1.c = 'repeat_user'           THEN 1 END) AS repeat_users
   , COUNT(CASE WHEN m1.c = 'come_back_user'         THEN 1 END) AS come_back_users
    --========================================================
	-- new_repeat_users:
	--  해당 월에 리피트 사용자이면서, 이전 달에 신규 사용자였던 사용자 수
	-- comtinuous_repeat_users:
	--  해당 월에 리피트 사용자이면서, 이전 달에 리피트 사용자였던 사용자 수
	-- come_back_repeat_users:
	--  해당 월에 리피트 사용자이면서, 이전 달에 컴백 사용자였던 사용자 수
	--========================================================
   , COUNT(
	  CASE WHEN m1.c = 'repeat_user'  AND m0.c = 'new_user' THEN 1 END
   ) AS new_repeat_users
   , COUNT(
	  CASE WHEN m1.c = 'repeat_user'  AND m0.c = 'repeat_user' THEN 1 END
   ) AS continuous_repeat_users
   , COUNT(
	  CASE WHEN m1.c = 'repeat_user'  AND m0.c = 'come_back_user' THEN 1 END
   ) AS come_back_repeat_users

FROM 
  -- m1: 해당 월의 사용자 분류 테이블
  monthly_user_with_type AS m1
 LEFT OUTER JOIN
  -- m0: 이전 달의 사용자 분류 테이블
  monthly_user_with_type AS m0
  ON m1.user_id = m0.user_id
  AND m1.action_month_priv = m0.action_month
GROUP BY
 m1.action_month
)
SELECT
 *
FROM
 monthly_users
ORDER BY
 action_month;
```

