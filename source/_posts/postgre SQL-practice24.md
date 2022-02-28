---
title: postgre SQL-practice23
tag: postgre SQL-practice23
date: 2022-02-27
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

이제 '5장 사용자를 파악하기 위한 데이터 추출'에서

'11강'이 끝나 오늘부터 '12강 시계열에 따른 사용자 전체의 상태 변화 찾기'를 

보고 실습을 진행한다.

페이지 '233~239' 까지를 보고 쿼리문을 작성했다.

사용자는 서비스 사용 시작일로부터 시간이 지나면 

'충성도 높은 사용자로 성장', '사용을 중지', '가입은 되어 있지만 사용하지 않는 상태(휴면)'등으로 

상태 변화가 일어납니다.

- 사용자가 계속해서 사용 (리피트)

- 사용자가 사용을 중단(탈퇴/휴면)

서비스를 운영하는 입장에서는 당연히 사용자가 계속해서 사용하기를 원할 것입니다.

그러려면 사용자가 어느 정도 계속해서 사용하고 있는지 파악하고, 목표와의 괴리를 어떻게 해결할지

검토해야 합니다.

추가로 잠시 서비스를 사용하지 않게 되어버린 휴면 사용자를 어떻게 하면 다시 

사용하게 만들지도 계속해서 생각해야 합니다.

이번 절에서는 사용자의 서비스 사용을 시계열로 수치화하고 변화를 

시각화하는 방법을 소개 하겠습니다.

이를 활용하면 현재 상태를 파악할 수 있으며, 대책의 효과를 

파악하거나 이후의 계획을 세울 때 큰 도움이 될 것입니다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 12강 시작 페이지 233 中)

'페이지 235 1. 등록 수의 추이와 경향 보기 - 날짜별 등록 수의 추이'

날짜별 등록 수의 추이를 집계하는 쿼리문
```python
SELECT 
   register_date
 , COUNT(DISTINCT user_id) AS register_count
FROM
 mst_users
GROUP BY
 register_date
ORDER BY
 register_date
;
```
'페이지 236 1. 등록 수의 추이와 경향 보기 - 월별 등록 수의 추이'

매달 등록 수와 전월비를 계산하는 쿼리문
```python
WITH
mst_users_with_year_month AS (
  SELECT
	 *
-- ■ PostgreSQL, Hive, Redshift, SparkSQL의 경우 substring으로 연-월 부분 추출하기
   , substring(register_date, 1, 7) AS year_month
   -- ■ PostgreSQL, Hive, BigQuery, SparkSQL의 경우 substr 사용하기
   -- , substr(register_date, 1, 7) AS year_month
  FROM
   mst_users
)
  SELECT
     year_month
   , COUNT(DISTINCT user_id) AS register_count
   , LAG(COUNT(DISTINCT user_id)) OVER(ORDER BY year_month)
   -- ■ SparkSQL의 경우는 다음과 같이 사용하기
   --, LAG(COUNT(DISTINCT user_id))
   --    OVER(ORDER BY year_month ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING)
     AS last_month_count
   , 1.0
     * COUNT(DISTINCT user_id)
	 / LAG(COUNT(DISTINCT user_id)) OVER(ORDER BY year_month)
    -- ■ SparkSQL의 경우는 다음과 같이 사용하기
	-- / LAG(COUNT(DISTINCT user_id))
	--     OVER(ORDER BY year_month ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING)
	 AS month_over_month_ratio
  FROM
   mst_users_with_year_month
  GROUP BY
   year_month
;
```
'페이지 238 1. 등록 수의 추이와 경향 보기 - 등록 디바이스별 추이'

디바이스들의 등록 수를 집계하는 쿼리문
```python
WITH
mst_users_with_year_month AS (
  SELECT
	 *
-- ■ PostgreSQL, Hive, Redshift, SparkSQL의 경우 substring으로 연-월 부분 추출하기
   , substring(register_date, 1, 7) AS year_month
   -- ■ PostgreSQL, Hive, BigQuery, SparkSQL의 경우 substr 사용하기
   -- , substr(register_date, 1, 7) AS year_month
  FROM
   mst_users
)
SELECT
   year_month
 , COUNT(DISTINCT user_id) AS register_count
 , COUNT(DISTINCT CASE WHEN register_device = 'pc' THEN user_id END) AS register_pc
 , COUNT(DISTINCT CASE WHEN register_device = 'sp' THEN user_id END) AS register_sp
 , COUNT(DISTINCT CASE WHEN register_device = 'app' THEN user_id END) AS register_app
FROM 
 mst_users_with_year_month
GROUP BY
 year_month
;
```
등록한 디바이스에 따라 사용자 행동이 다를 수 있습니다. 

이후에 설명할 분석을 등록 디바이스별로 실시해보면 재미있는 경향이 나올 것입니다.

추가로 여러 장치를 사용하는 사용자(멀티 디바이스 사용자)가 있을 수 있습니다.

이러한 사용자의 존재도 파악해두면 여러 도움이 될 것입니다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 12강 페이지 239 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)
참고 도서 : 데이터 분석을 위한 SQL 레시피
저자 : 가나키 나가토, 다미야 나오토
출판사 : 한빛미디어
