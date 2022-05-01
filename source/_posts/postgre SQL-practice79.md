---
title: postgre SQL-practice79
tag: postgre SQL-practice79
date: 2022-05-01
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  24강 점수 계산하기'의

'4. 거대한 숫자 지표를 직감적으로 이해하기 쉽게 가공하기'

로 넘어갔으며

페이지 556 ~ 562을 참고하였다.

사용자들의 최종 접근일과 각 레코드와의 날짜 차이를 계산하는 쿼리문
```python
WITH
action_counts_with_diff_date AS (
  SELECT *
    -- 사용자별로 최종 접근과 각 레코드의 날짜 차이 계산하기
	--■ Posgre SQL, Redshift의 경우 날짜끼리 빼기 연산 가능
	, MAX(dt::date) OVER(PARTITION BY user_id) AS last_access
	, MAX(dt::date) OVER(PARTITION BY user_id) - dt::date AS diff_date
	--■BigQuery의 경우 date_diff 함수 사용하기
	--, MAX(date(timestamp(dt))) OVER(PARTITION BY user_id) AS last_access
	--, date_diff(MAX(date(timestamp(dt))) OVER(PARTITION BY user_id),
	--    date(timestamp(dt)), day) AS diff_date
	--■Hive, SparkSQL의 경우 datediff 함수 사용하기
	--, MAX(to_date(dt)) OVER(PARTITION BY user_id) AS last_access
	--, datediff(MAX(to_date(dt)) OVER(PARTITION BY user_id), to_date(dt))
	--  AS diff_date
  FROM
   action_counts_with_date
)
SELECT *
FROM action_counts_with_diff_date;
```

날짜 차이에 따른 가중치를 계산하는 쿼리문
```python
WITH
action_counts_with_diff_date AS (
  SELECT *
    -- 사용자별로 최종 접근과 각 레코드의 날짜 차이 계산하기
	--■ Posgre SQL, Redshift의 경우 날짜끼리 빼기 연산 가능
	, MAX(dt::date) OVER(PARTITION BY user_id) AS last_access
	, MAX(dt::date) OVER(PARTITION BY user_id) - dt::date AS diff_date
	--■BigQuery의 경우 date_diff 함수 사용하기
	--, MAX(date(timestamp(dt))) OVER(PARTITION BY user_id) AS last_access
	--, date_diff(MAX(date(timestamp(dt))) OVER(PARTITION BY user_id),
	--    date(timestamp(dt)), day) AS diff_date
	--■Hive, SparkSQL의 경우 datediff 함수 사용하기
	--, MAX(to_date(dt)) OVER(PARTITION BY user_id) AS last_access
	--, datediff(MAX(to_date(dt)) OVER(PARTITION BY user_id), to_date(dt))
	--  AS diff_date
  FROM
   action_counts_with_date
)
, action_counts_with_weight AS (
  SELECT *
    -- 날짜 차이에 따른 가중치 계산하기(매개 변수 a = 0.1)
	--■PostgreSQL, Hive, SparkSQL의 경우 log(<밑수>,<진수>) 함수 사용하기
	 , 1.0 / log(2, 0.1 * diff_date + 2) AS weight
	--■Redshift의 경우 log 함수는 상용 로그밖에 되지 않으므로, log(2)로 나눠주기
	--, 1.0 / (log(CAST(0.1 * diff_date + 2 AS double precision)) / log(2))
	--AS weight
	--■BigQuery의 경우 log(<진수>,<밑수>) 함수 사용하기
	--, 1.0 / log(0.1 * diff_date + 2,2) AS weight
  FROM action_counts_with_diff_date
)
SELECT
   user_id
 , product
 , v_count
 , p_count
 , diff_date
 , weight
FROM action_counts_with_weight
ORDER BY 
 user_id, product, diff_date DESC
;
```

일수차에 따른 중첩을 사용해 열람 수와 구매 수 점수를 계산하는 쿼리문
```python
WITH
action_counts_with_diff_date AS (
  SELECT *
    -- 사용자별로 최종 접근과 각 레코드의 날짜 차이 계산하기
	--■ Posgre SQL, Redshift의 경우 날짜끼리 빼기 연산 가능
	, MAX(dt::date) OVER(PARTITION BY user_id) AS last_access
	, MAX(dt::date) OVER(PARTITION BY user_id) - dt::date AS diff_date
	--■BigQuery의 경우 date_diff 함수 사용하기
	--, MAX(date(timestamp(dt))) OVER(PARTITION BY user_id) AS last_access
	--, date_diff(MAX(date(timestamp(dt))) OVER(PARTITION BY user_id),
	--    date(timestamp(dt)), day) AS diff_date
	--■Hive, SparkSQL의 경우 datediff 함수 사용하기
	--, MAX(to_date(dt)) OVER(PARTITION BY user_id) AS last_access
	--, datediff(MAX(to_date(dt)) OVER(PARTITION BY user_id), to_date(dt))
	--  AS diff_date
  FROM
   action_counts_with_date
)
, action_counts_with_weight AS (
  SELECT *
    -- 날짜 차이에 따른 가중치 계산하기(매개 변수 a = 0.1)
	--■PostgreSQL, Hive, SparkSQL의 경우 log(<밑수>,<진수>) 함수 사용하기
	 , 1.0 / log(2, 0.1 * diff_date + 2) AS weight
	--■Redshift의 경우 log 함수는 상용 로그밖에 되지 않으므로, log(2)로 나눠주기
	--, 1.0 / (log(CAST(0.1 * diff_date + 2 AS double precision)) / log(2))
	--AS weight
	--■BigQuery의 경우 log(<진수>,<밑수>) 함수 사용하기
	--, 1.0 / log(0.1 * diff_date + 2,2) AS weight
  FROM action_counts_with_diff_date
)
, action_scores AS (
  SELECT
	 user_id
   , prodcut
   , SUM(v_count) AS v_count
   , SUM(v_count * weight) AS v_score
   , SUM(p_count) AS p_count
   , SUM(p_count * weight) AS p_score
  FROM action_counts_with_weight
  GROUP BY
	user_id, product
)
SELECT *
FROM action_scores
ORDER BY
 user_id, product;
```

열람 수와 구매 수처럼 '어떤 것을 세어 집계한 숫자'는 점수를 계산할 때,

로그를 취해서 값의 변화를 완만하게 표현 할 수 있습니다.

이를 활용하면 사람이 더 직감적으로 쉽게 값의 변화를 인지할 수 있습니다.

로그는 굉장히 기본적인 수학적 요소이지만, 그 활용 범위는 굉장히 넓답니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 23강 점수 계산하기 562 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어