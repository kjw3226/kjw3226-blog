---
title: postgre SQL-practice23
tag: postgre SQL-practice23
date: 2022-02-26
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'데이터 분석을 위한 SQL 레시피'

페이지 220 ~ 페이지 223까지 보고 실습을 진행했다.

'제 5 장 사용자를 파악하기 위한 데이터 추출' - 11강 사용자 전체의 특징과 경향 찾기

'7. RFM 분석으로 사용자를 3가지 관점의 그룹으로 나누기'

오늘은 이 부분을 참고하여 쿼리문을 작성했다.

먼저 'RFM' 이란

- Recency : 최근 구매일
 -> 최근 무언가를 구매한 사용자를 우량 고객으로 취급

- Frequency : 구매 횟수
 -> 사용자가 구매한 횟수를 세고, 많을수록 우량 고객으로 취급

- Monetary : 구매 금액 합계
 -> 사용자의 구매 금액 합계를 집계하고, 금액이 높을수록 우량 고객으로 취급

이렇게 3가지를 통틀어서 'RFM' 이라고 한다.

사용자별로 'RFM'을 집계하는 쿼리문
```python
WITH
purchase_log AS(
 SELECT 
	user_id
  , amount
  -- 타임 스탬프를 기반으로 날짜 추출하기
  -- ■ PostgreSQL, Hive, Redshift, SparkSQL의 경우 substring으로 부분 추출하기
  , substring(stamp, 1, 10) AS dt
  -- ■ PostgreSQL, Hive, BigQuery, SparkSQL의 경우 substr 사용하기
  -- , substr(stamp, 1, 10) AS dt
 FROM
  action_log
 WHERE 
  action = 'purchase'
)
, user_rfm AS (
  SELECT 
     user_id
   , MAX(dt) AS recent_date
   -- ■ PostgreSQL, Redshift의 경우 날짜 형식끼리 빼기 연산 가능
   , CURRENT_DATE - MAX(dt::date) AS recency
   -- ■ BigQuery의 경우 date_diff 함수 사용하기
   -- , date_diff(CUREENT_DATE, date(timestamp(MAX(dt))), day) AS recency
   -- ■ Hive, SparkSQL의 경우 datediff 함수 사용하기
   -- , datediff(CURRENT_DATE(), to_date(MAX(dt))) AS recency
   , COUNT(dt) AS frequency
   , SUM(amount) AS monetary
  FROM
    purchase_log
  GROUP BY
   user_id
)
SELECT *
FROM 
 user_rfm
;
```

사용자들의 'RFM' 랭크를 계산하는 쿼리문
```python
WITH
user_rfm AS (
  SELECT 
     user_id
   , MAX(dt) AS recent_date
   -- ■ PostgreSQL, Redshift의 경우 날짜 형식끼리 빼기 연산 가능
   , CURRENT_DATE - MAX(dt::date) AS recency
   -- ■ BigQuery의 경우 date_diff 함수 사용하기
   -- , date_diff(CUREENT_DATE, date(timestamp(MAX(dt))), day) AS recency
   -- ■ Hive, SparkSQL의 경우 datediff 함수 사용하기
   -- , datediff(CURRENT_DATE(), to_date(MAX(dt))) AS recency
   , COUNT(dt) AS frequency
   , SUM(amount) AS monetary
  FROM
    purchase_log
  GROUP BY
   user_id
)
, user_rfm_rank AS (
  SELECT
	 user_id
   , recent_date
   , recency
   , frequency
   , monetary
   , CASE
	  WHEN recency < 14 THEN 5
	  WHEN recency < 28 THEN 4
	  WHEN recency < 60 THEN 3
	  WHEN recency < 90 THEN 2
	  ELSE 1
	END AS r
  , CASE
	 WHEN 20 <= frequency THEN 5
	 WHEN 10 <= frequency THEN 4
	 WHEN 5  <= frequency THEN 3
	 WHEN 2  <= frequency THEN 2
	 WHEN 1   = frequency THEN 1
   END AS f
  , CASE
	 WHEN 300000 <= monetary THEN 5
	 WHEN 100000 <= monetary THEN 4
	 WHEN  30000 <= monetary THEN 3
	 WHEN   5000 <= monetary THEN 2
	 ELSE 1
   END AS m
  FROM
   user_rfm
)
SELECT *
FROM 
 user_rfm_rank
;
```

각 그룹의 사람 수를 확인하는 쿼리문
```python
WITH 
user_rfm AS (
 SELECT 
     user_id
   , MAX(dt) AS recent_date
   -- ■ PostgreSQL, Redshift의 경우 날짜 형식끼리 빼기 연산 가능
   , CURRENT_DATE - MAX(dt::date) AS recency
   -- ■ BigQuery의 경우 date_diff 함수 사용하기
   -- , date_diff(CUREENT_DATE, date(timestamp(MAX(dt))), day) AS recency
   -- ■ Hive, SparkSQL의 경우 datediff 함수 사용하기
   -- , datediff(CURRENT_DATE(), to_date(MAX(dt))) AS recency
   , COUNT(dt) AS frequency
   , SUM(amount) AS monetary
 FROM
   purchase_log
 GROUP BY
   user_id
)
, user_rfm_rank AS (
  SELECT
	 user_id
   , recent_date
   , recency
   , frequency
   , monetary
   , CASE
	  WHEN recency < 14 THEN 5
	  WHEN recency < 28 THEN 4
	  WHEN recency < 60 THEN 3
	  WHEN recency < 90 THEN 2
	  ELSE 1
	END AS r
  , CASE
	 WHEN 20 <= frequency THEN 5
	 WHEN 10 <= frequency THEN 4
	 WHEN 5  <= frequency THEN 3
	 WHEN 2  <= frequency THEN 2
	 WHEN 1   = frequency THEN 1
   END AS f
  , CASE
	 WHEN 300000 <= monetary THEN 5
	 WHEN 100000 <= monetary THEN 4
	 WHEN  30000 <= monetary THEN 3
	 WHEN   5000 <= monetary THEN 2
	 ELSE 1
   END AS m
  FROM
   user_rfm
)
, mst_rfm_index AS(
  -- 1부터 5까지의 숫자를 가지는 테이블 만들기
  -- PostgreSQL의 generate_series 등수 등으로도 대체 가능
	        SELECT 1 AS rfm_index
  UNION ALL SELECT 2 AS rfm_index
  UNION ALL SELECT 3 AS rfm_index
  UNION ALL SELECT 4 AS rfm_index
  UNION ALL SELECT 5 AS rfm_index
)
, rfm_flag AS(
  SELECT
	 m.rfm_index
   , CASE WHEN m.rfm_index = r.r THEN 1 ELSE 0 END AS r_flag
   , CASE WHEN m.rfm_index = r.f THEN 1 ELSE 0 END AS f_flag
   , CASE WHEN m.rfm_index = r.m THEN 1 ELSE 0 END AS m_flag
  FROM 
	 mst_rfm_index AS m
	CROSS JOIN
	 user_rfm_rank AS r
)
SELECT
   rfm_index
 , SUM(r_flag) AS r
, SUM(f_flag) AS f
 , SUM(m_flag) AS m
FROM 
 rfm_flag
GROUP BY
 rfm_flag
ORDER BY
 rfm_index DESC
;
```

■ 사용자를 1차원으로 구분하기

통합 랭크를 계산하는 쿼리문
```python
WITH
user_rfm AS (
 SELECT 
     user_id
   , MAX(dt) AS recent_date
   -- ■ PostgreSQL, Redshift의 경우 날짜 형식끼리 빼기 연산 가능
   , CURRENT_DATE - MAX(dt::date) AS recency
   -- ■ BigQuery의 경우 date_diff 함수 사용하기
   -- , date_diff(CUREENT_DATE, date(timestamp(MAX(dt))), day) AS recency
   -- ■ Hive, SparkSQL의 경우 datediff 함수 사용하기
   -- , datediff(CURRENT_DATE(), to_date(MAX(dt))) AS recency
   , COUNT(dt) AS frequency
   , SUM(amount) AS monetary
 FROM
   purchase_log
 GROUP BY
   user_id
)
, user_rfm_rank AS (
  SELECT
	 user_id
   , recent_date
   , recency
   , frequency
   , monetary
   , CASE
	  WHEN recency < 14 THEN 5
	  WHEN recency < 28 THEN 4
	  WHEN recency < 60 THEN 3
	  WHEN recency < 90 THEN 2
	  ELSE 1
	END AS r
  , CASE
	 WHEN 20 <= frequency THEN 5
	 WHEN 10 <= frequency THEN 4
	 WHEN 5  <= frequency THEN 3
	 WHEN 2  <= frequency THEN 2
	 WHEN 1   = frequency THEN 1
   END AS f
  , CASE
	 WHEN 300000 <= monetary THEN 5
	 WHEN 100000 <= monetary THEN 4
	 WHEN  30000 <= monetary THEN 3
	 WHEN   5000 <= monetary THEN 2
	 ELSE 1
   END AS m
  FROM
   user_rfm
)
SELECT
   r + f + m AS total_rank
 , r , f , m
 , COUNT(user_id)
FROM 
 user_rfm_rank
GROUP BY
 r, f, m
ORDER BY
 total_rank DESC, r DESC, f DESC, m DESC;
```

종합 랭크별로 사용자 수를 집계하는 쿼리문
```python
WITH
user_rfm AS (
 SELECT 
     user_id
   , MAX(dt) AS recent_date
   -- ■ PostgreSQL, Redshift의 경우 날짜 형식끼리 빼기 연산 가능
   , CURRENT_DATE - MAX(dt::date) AS recency
   -- ■ BigQuery의 경우 date_diff 함수 사용하기
   -- , date_diff(CUREENT_DATE, date(timestamp(MAX(dt))), day) AS recency
   -- ■ Hive, SparkSQL의 경우 datediff 함수 사용하기
   -- , datediff(CURRENT_DATE(), to_date(MAX(dt))) AS recency
   , COUNT(dt) AS frequency
   , SUM(amount) AS monetary
 FROM
   purchase_log
 GROUP BY
   user_id
)
, user_rfm_rank AS (
  SELECT
	 user_id
   , recent_date
   , recency
   , frequency
   , monetary
   , CASE
	  WHEN recency < 14 THEN 5
	  WHEN recency < 28 THEN 4
	  WHEN recency < 60 THEN 3
	  WHEN recency < 90 THEN 2
	  ELSE 1
	END AS r
  , CASE
	 WHEN 20 <= frequency THEN 5
	 WHEN 10 <= frequency THEN 4
	 WHEN 5  <= frequency THEN 3
	 WHEN 2  <= frequency THEN 2
	 WHEN 1   = frequency THEN 1
   END AS f
  , CASE
	 WHEN 300000 <= monetary THEN 5
	 WHEN 100000 <= monetary THEN 4
	 WHEN  30000 <= monetary THEN 3
	 WHEN   5000 <= monetary THEN 2
	 ELSE 1
   END AS m
  FROM
   user_rfm
)
SELECT
   r + f + m AS total_rank
 , COUNT(user_id)
FROM 
 user_rfm_rank
GROUP BY
 -- ■ PostgreSQL, Redshift, BigQuery의 경우
-- SELECT 구문에서 정의한 별칭을 GROUP BY 구문에 지정할 수 있음
   total_rank
 -- ■ PostgreSQL, Hive, Redshift, SparkSQL의 경우
-- SELECT 구문에서 별칭을 지정하기 전의 식을 GROUP BY 구문에 지정할 수 있음
 -- r + f + m
ORDER BY
  total_rank DESC;
```

■ 2차원으로 사용자 인식하기

R과 F를 사용해 2차원 사용자 층의 사용자 수를 집계하는 쿼리문
```python
WITH
user_rfm AS (
 SELECT 
     user_id
   , MAX(dt) AS recent_date
   -- ■ PostgreSQL, Redshift의 경우 날짜 형식끼리 빼기 연산 가능
   , CURRENT_DATE - MAX(dt::date) AS recency
   -- ■ BigQuery의 경우 date_diff 함수 사용하기
   -- , date_diff(CUREENT_DATE, date(timestamp(MAX(dt))), day) AS recency
   -- ■ Hive, SparkSQL의 경우 datediff 함수 사용하기
   -- , datediff(CURRENT_DATE(), to_date(MAX(dt))) AS recency
   , COUNT(dt) AS frequency
   , SUM(amount) AS monetary
 FROM
   purchase_log
 GROUP BY
   user_id
)
, user_rfm_rank AS (
  SELECT
	 user_id
   , recent_date
   , recency
   , frequency
   , monetary
   , CASE
	  WHEN recency < 14 THEN 5
	  WHEN recency < 28 THEN 4
	  WHEN recency < 60 THEN 3
	  WHEN recency < 90 THEN 2
	  ELSE 1
	END AS r
  , CASE
	 WHEN 20 <= frequency THEN 5
	 WHEN 10 <= frequency THEN 4
	 WHEN 5  <= frequency THEN 3
	 WHEN 2  <= frequency THEN 2
	 WHEN 1   = frequency THEN 1
   END AS f
  , CASE
	 WHEN 300000 <= monetary THEN 5
	 WHEN 100000 <= monetary THEN 4
	 WHEN  30000 <= monetary THEN 3
	 WHEN   5000 <= monetary THEN 2
	 ELSE 1
   END AS m
  FROM
   user_rfm
)
SELECT 
   CONCAT('r_', r) AS r_rank
-- ■ BigQuery의 경우 CONCAT 함수의 매개 변수를 string으로 변환해야 함
  --CONCAT('r_', CAST(r AS string)) AS r_rank
  , COUNT(CASE WHEN f = 5 THEN 1 END) AS f_5
  , COUNT(CASE WHEN f = 4 THEN 1 END) AS f_4
  , COUNT(CASE WHEN f = 3 THEN 1 END) AS f_3
  , COUNT(CASE WHEN f = 2 THEN 1 END) AS f_2
  , COUNT(CASE WHEN f = 1 THEN 1 END) AS f_1
FROM
 user_rfm_rank
GROUP BY
 r
ORDER BY
 r_rank DESC;
```

RFM 분석의 각 지표 Recency, Frequency, Monetary에 따라 

사용자의 속성을 정의하고 1차원, 2차원, 3차원으로 표현하는 방법을 살펴봤다.

서비스 개선 검토, 사용자에 따른 메일 최적화 등 다양한 용도로 활용하기 바란다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 11강 7. RFM 분석으로 사용자를 3가지 관점의 그룹으로 나누기 中)