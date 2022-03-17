---
title: postgre SQL-practice34
tag: postgre SQL-practice34
date: 2022-03-17
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)


'5장  13강 시계열에 따른 사용자의 개별적인 행동 분석하기

2. 카트 추가 후에 구매했는지 파악하기'

(페이지 310 ~ 315)

를 보고 쿼리문 작성 실습을 하였다.

상품들이 카트에 추가된 시각과 구매된 시각을 산출하는 쿼리문
```python
WITH
row_action_log AS (
 SELECT 
  dt
, user_id
, action
-- 쉼표로 구분된 product_id 리스트 전개하기
--■ PostgreSQL의 경우 regexp_split_to_table 함수 사용 가능
, regexp_split_to_table(products,',') AS product_id
--■ Hive, BigQuery, SparkSQL의 경우 FROM 구문으로 전개하고 product_id 추출하기
--, product_id
, stamp
FROM
 action_log
-- ■ BigQuery의 경우는 다음 코드 추가하기
-- CROSS JOIN unnest(split(product, ',')) AS product_id
-- ■ Hive, SparkSQL의 경우는 다음 코드 추가하기
-- LATERAL VIEW explode(split(products,',')) e AS product_id
)
, action_time_stats AS (
  -- 사용자와 상품 조합의 카드 추가 시간과 구매 시간 추출하기
  SELECT
   user_id
 , product_id
 , MIN(CASE action WHEN 'add_cart' THEN dt END) AS dt
 , MIN(CASE action WHEN 'add_cart' THEN stamp END) AS add_cart_time
 , MIN(CASE action WHEN 'purchase' THEN stamp END) AS purchase_time
-- ■ Postgre SQL의 경우 timestamp 자료형으로 변환해서 간격을 구한 뒤
 --    EXTRACT(epoc ~)로 초 단위 변환
 , EXTRACT(epoch from
      MIN(CASE action WHEN 'purchase' THEN stamp::timestamp END)
	 -MIN (CASE action WHEN 'add_cart' THEN stamp::timestamp END))
--■ BigQuery의 경우 unix_seconds 함수로 초 단위 UNIX 시간 추출 후 차이 구하기
--,  MIN(CASE action WHEN 'purchase' THEN unix_seconds(timestamp(stamp)) END)
--  -MIN(CASE action WHEN 'add_cart' THEN unix_seconds(timestamp(stamp)) END)
--■ Hive, SparkSQL의 경우
-- UNIX_timestamp 함수로 초 단위 UNIX 시간 추출 후 차이 구하기
--,  MIN(CASE action WHEN 'purchase' THEN unix_timestamp(stamp) END)
--  -MIN(CASE action WHEN 'add_cart' THEN unix_timestamp(stamp) END)
 AS lead_time

FROM
 row_action_log
GROUP BY
 user_id, prodcut_id
)
SELECT
   user_id
 , product_id
 , add_cart_time
 , purchase_time
 , lead_time
FROM
 action_time_stats
ORDER BY
 user_id, product_id
;
```

카트 추가 후 n시간 이내에 구매된 상품 수와 구매율을 집계하는 쿼리문
```python
WITH
row_action_log AS (
 SELECT 
  dt
, user_id
, action
-- 쉼표로 구분된 product_id 리스트 전개하기
--■ PostgreSQL의 경우 regexp_split_to_table 함수 사용 가능
, regexp_split_to_table(products,',') AS product_id
--■ Hive, BigQuery, SparkSQL의 경우 FROM 구문으로 전개하고 product_id 추출하기
--, product_id
, stamp
FROM
 action_log
-- ■ BigQuery의 경우는 다음 코드 추가하기
-- CROSS JOIN unnest(split(product, ',')) AS product_id
-- ■ Hive, SparkSQL의 경우는 다음 코드 추가하기
-- LATERAL VIEW explode(split(products,',')) e AS product_id
)
, action_time_stats AS (
  -- 사용자와 상품 조합의 카드 추가 시간과 구매 시간 추출하기
  SELECT
   user_id
 , product_id
 , MIN(CASE action WHEN 'add_cart' THEN dt END) AS dt
 , MIN(CASE action WHEN 'add_cart' THEN stamp END) AS add_cart_time
 , MIN(CASE action WHEN 'purchase' THEN stamp END) AS purchase_time
-- ■ Postgre SQL의 경우 timestamp 자료형으로 변환해서 간격을 구한 뒤
 --    EXTRACT(epoc ~)로 초 단위 변환
 , EXTRACT(epoch from
      MIN(CASE action WHEN 'purchase' THEN stamp::timestamp END)
	 -MIN (CASE action WHEN 'add_cart' THEN stamp::timestamp END))
--■ BigQuery의 경우 unix_seconds 함수로 초 단위 UNIX 시간 추출 후 차이 구하기
--,  MIN(CASE action WHEN 'purchase' THEN unix_seconds(timestamp(stamp)) END)
--  -MIN(CASE action WHEN 'add_cart' THEN unix_seconds(timestamp(stamp)) END)
--■ Hive, SparkSQL의 경우
-- UNIX_timestamp 함수로 초 단위 UNIX 시간 추출 후 차이 구하기
--,  MIN(CASE action WHEN 'purchase' THEN unix_timestamp(stamp) END)
--  -MIN(CASE action WHEN 'add_cart' THEN unix_timestamp(stamp) END)
 AS lead_time

FROM
 row_action_log
GROUP BY
 user_id, prodcut_id
)
, purchase_lead_time_flag AS (
SELECT
   user_id 
 , product_id
 , dt
 , CASE WHEN lead_time <= 1 * 60 * 60 THEN 1 ELSE 0 END AS purchase_1_hour
 , CASE WHEN lead_time <= 6 * 60 * 60 THEN 1 ELSE 0 END AS purchase_6_hours
 , CASE WHEN lead_time <= 24 * 60 * 60 THEN 1 ELSE 0 END AS purchase_24_hours
 , CASE WHEN lead_time <= 48 * 60 * 60 THEN 1 ELSE 0 END AS purchase_48_hours
 , CASE
	WHEN lead_time IS NULL OR NOT (lead_time <= 48 * 60 * 60) THEN 1
	ELSE 0
   END AS not_purchase
FROM
 action_time_stats
)
SELECT
   dt
 , COUNT(*) AS add_cart
 , SUM(purchase_1_hour  ) AS purchase_1_hour
 , AVG(purchase_1_hour  ) AS purchase_1_hour_rate
 , SUM(purchase_6_hours  ) AS purchase_6_hours
 , AVG(purchase_6_hours  ) AS purchase_6_hours_rate
 , SUM(purchase_24_hours ) AS purchase_24_hours
 , AVG(purchase_24_hours ) AS purchase_24_hours_rate
 , SUM(purchase_48_hours ) AS purchase_48_hours
 , AVG(purchase_48_hours ) AS purchase_48_hours_rate
 , SUM(not_purchase      ) AS not_purchase
 , AVG(not_purchase      ) AS nor_purchase_rate
FROM 
  purchase_lead_time_flag
 GROUP BY
  dt
;
```

카트 탈락 상품이 있는 사용자에게 메일 매거진 등의 푸시로 쿠폰 또는 

할인 정보를 보내주어 구매를 유도하는 방법 등을 고려해봅시다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 13강 페이지 315 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어

