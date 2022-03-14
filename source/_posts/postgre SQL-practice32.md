---
title: postgre SQL-practice32
tag: postgre SQL-practice32
date: 2022-03-14
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

페이지 288-300을 참고하였다.

'5장  12강 시계열에 따른 사용자 전체의 상태 변화 찾기

7. 방문 빈도를 기반으로 사용자 속성을 정의하고 집계하기 - MAU 속성별 반복률 계산하기'

부터 시작해서 

'5장  12강 시계열에 따른 사용자 전체의 상태 변화 찾기

8. 방문 종류를 기반으로 성장지수 집계하기' 를 참고해서

쿼리문 작성 실습을 하였다.

MAU 내역과 MAU 속성들의 반복률을 계산하는 쿼리문
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
   action_month
 , mau
 , new_users
 , repeat_users
 , come_back_users
 , new_repeat_users
 , continuous_repeat_users
 , come_back_repeat_users
 -- ■ PostgreSQL, Redshift, BigQuery의 경우 다음과 같이 사용하기
 -- ■ Hive의 경우 NULLIF를 CASE 식으로 변경하기
 -- ■ SparkSQL의 경우,
 --   LAG 함수의 프레임에 ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING 지정하기
 -- 이전 달에 신규 사용자이면서 해당 월에 신규 리피트 사용자인 사용자의 비율
 , 100.0 * new_repeat_users
   / NULLIF(LAG(new_users) OVER(ORDER BY action_month), 0)
   AS priv_new_repeat_ratio
   
   
 -- 이전 달에 리피트 사용자이면서 해당 월에 기존 리피트 사용자인 사용자의 비율
 , 100.0 * continuous_repeat_users
   / NULLIF(LAG(repeat_users) OVER(ORDER BY action_month), 0)
   AS priv_continuous_repeat_ratio
   
   
 -- 이전 달에 컴백 사용자이면서 해당 월에 컴백 리피트 사용자인 사용자의 비율
 , 100.0 * come_back_repeat_users
   / NULLIF(LAG(come_back_users) OVER(ORDER BY action_month), 0)
   AS priv_come_back_repeat_ratio


FROM
 monthly_users
ORDER BY
 action_month
;
```
이번 절의 리포트는 월 단위로 집계하므로, 1일에 등록한 사용자가 30일 이상

사용하지 않으면 리피트 사용자가 되지 않지만, 월의 마지막 날에 

등록한 사용자는 2일만 사용해도 리피트 사용자가 된다는 문제가 있습니다.

판정 기간에 약간 문제가 있기는 하지만, 간단하게 추이를 확인하거나 

서비스끼리 비교할 때는 굉장히 유용한 리포트입니다.

판정 기간의 차이가 신경쓰인다면 독자적인 정의를 추가로 만들고

집계하기 바랍니다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 12강 페이지 292 中


성장지수 산출을 위해 사용자 상태를 집계하는 쿼리문
```python
WITH
unique_action_log AS (
 -- 같은 날짜 로그를 중복해 세지 않도록 중복 배제하기
 SELECT DISTINCT
	user_id
   , substring(stamp, 1, 10) AS action_date
  -- ■ BigQuery의 경우 다음과 같이 사용하기
  --, substr(stamp, 1, 10) AS action_date
 FROM
  action_log
)
, mst_calender AS (
  -- 집계하고 싶은 기간을 캘린더 테이블로 만들어주기
  -- generate_series 등으로 동적 생성도 가능
	        SELECT '2016-10-01' AS dt
  UNION ALL SELECT '2016-10-02' AS dt
  UNION ALL SELECT '2016-10-03' AS dt
  -- 생략
  UNION ALL SELECT '2016-11-04' AS dt
)
, target_date_with_users AS (
  -- 사용자 마스터에 캘린더 테이블의 날짜를 target_date로 추가하기
  SELECT
	 c.dt AS target_date
   , u.user_id
   , u.register_date
   , u.withdraw_date
  FROM
	 mst_users AS u
   CROSS JOIN
	mst_calender AS c
)
, user_status_log AS (
  SELECT
	 u.target_date
   , u.user_id
   , u.register_date
   , u.withdraw_date
   , a.action_date
   , CASE WHEN u.register_date = a.action_date THEN 1 ELSE 0 END AS is_new
   , CASE WHEN u.withdraw_date = a.action_date THEN 1 ELSE 0 END AS is_exit
   , CASE WHEN u.target_date   = a.action_date THEN 1 ELSE 0 END AS is_access
   , LAG(CASE WHEN u.target_date = a.action_date THEN 1 ELSE 0 END)
	 OVER(
	  PARTITION BY u.user_id
	  ORDER BY u.target_date
	  -- ■ SparkSQL의 경우 다음과 같이 프레임 지정하기
	  -- ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING
	 ) AS was_access
  FROM
	 target_date_with_user AS u
    LEFT JOIN
	 unique_action_log AS a
	 ON u.user_id = a.user_id
	 AND u.target_date = a.action_date
  WHERE
   -- 집계 기간을 등록일 이후로만 필터링하기
   u.register_date <= u.target_date
   -- 탈퇴 날짜가 포함되어 있으면, 집계 기간을 탈퇴 날짜 이전만으로 필터링하기
   AND(
	   u.withdraw_date IS NULL
	OR u.target_date <= u.withdraw_date
   )
)
SELECT
   target_date
 , user_id
 , is_new
 , is_exit
 , is_access
 , was_access
FROM 
 user_status_log
;
```

매일의 성장지수를 계산하는 쿼리문
```python
WITH
unique_action_log AS (
 -- 같은 날짜 로그를 중복해 세지 않도록 중복 배제하기
 SELECT DISTINCT
	user_id
   , substring(stamp, 1, 10) AS action_date
  -- ■ BigQuery의 경우 다음과 같이 사용하기
  --, substr(stamp, 1, 10) AS action_date
 FROM
  action_log
)
, mst_calender AS (
  -- 집계하고 싶은 기간을 캘린더 테이블로 만들어주기
  -- generate_series 등으로 동적 생성도 가능
	        SELECT '2016-10-01' AS dt
  UNION ALL SELECT '2016-10-02' AS dt
  UNION ALL SELECT '2016-10-03' AS dt
  -- 생략
  UNION ALL SELECT '2016-11-04' AS dt
)
, target_date_with_users AS (
  -- 사용자 마스터에 캘린더 테이블의 날짜를 target_date로 추가하기
  SELECT
	 c.dt AS target_date
   , u.user_id
   , u.register_date
   , u.withdraw_date
  FROM
	 mst_users AS u
   CROSS JOIN
	mst_calender AS c
)
, user_status_log AS (
  SELECT
	 u.target_date
   , u.user_id
   , u.register_date
   , u.withdraw_date
   , a.action_date
   , CASE WHEN u.register_date = a.action_date THEN 1 ELSE 0 END AS is_new
   , CASE WHEN u.withdraw_date = a.action_date THEN 1 ELSE 0 END AS is_exit
   , CASE WHEN u.target_date   = a.action_date THEN 1 ELSE 0 END AS is_access
   , LAG(CASE WHEN u.target_date = a.action_date THEN 1 ELSE 0 END)
	 OVER(
	  PARTITION BY u.user_id
	  ORDER BY u.target_date
	  -- ■ SparkSQL의 경우 다음과 같이 프레임 지정하기
	  -- ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING
	 ) AS was_access
, user_growth_index AS (
  SELECT
	 *
	, CASE
	   -- 어떤 날짜에 신규 등록 또는 탈퇴한 경우 signup 또는 exit으로 판정하기
	   WHEN is_new + is_exist = 1 THEN
	     CASE
	       WHEN is_new = 1 THEN 'signup'
	   WHEN is_exit = 1 THEN 'exit'
	 END
	-- 신규 등록과 탈퇴가 아닌 경우 reactivation 또는 deactivation으로 판정하기
	-- 이때 reactivation, deactivation의 정의에 맞지 않는 경우는 NULL로 지정
	WHEN is_new + is_exit = 0 THEN
	 CASE 
	  WHEN was_access = 0 AND is_access = 1 THEN 'reactivation'
	  WHEN was_access = 1 AND is_access = 1 THEN 'deactivation'
	 END
   -- 어떤 날짜에 신규 등록과 탈퇴를 함께 했다면(is_nes + is_exit = 2) NULL로 지정
  END AS growth_index
FROM 
 user_status_log
)
SELECT
   target_date
 , SUM(CASE growth_index WHEN 'signup'      THEN 1 ELSE 0 END) AS signup
 , SUM(CASE growth_index WHEN 'reactivation'THEN 1 ELSE 0 END) AS reactivation
 , SUM(CASE growth_index WHEN 'deactivation'THEN -1 ELSE 0 END) AS reactivation
 , SUM(CASE growth_index WHEN 'exit'        THEN -1 ELSE 0 END) AS exit
   -- 성장지수 정의에 계산하기
, SUM(
	 CASE growth_index
	   WHEN 'signup'     THEN 1
	   WHEN 'reactivation' THEN 1
	   WHEN 'deactivation' THEN -1
	   WHEN 'exit'        THEN-1
	   ELSE 0
	 END
  ) AS growth_index
FROM
 user_growth_index
GROUP BY
 target_date
ORDER BY
 target_date
;
```

일상적으로 사용하는 서비스(뉴스 사이트 또는 소셜 게임 등)와, 특정 목적이

발생했을 때 사용하는 서비스(음식점 검색 서비스 또는 EC사이트)는 사용 빈도가

서로 다릅니다.

따라서 성장지수 계산을 위해 사용하는 지표를 집계할 때는 서비스의 특성에 

맞게 날짜별, 주차, 월차 등의 적절한 집계 기간을 선택하기 바랍니다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 12강 페이지 300 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어
