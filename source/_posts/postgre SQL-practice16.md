---
title: postgre SQL-practice16
tag: postgre SQL-practice16
date: 2022-02-17
categories:	SQL
---
 히스토그램을 만드는 쿼리문을 실습해보았다.

 이 부분은 '데이터 분석을 위한 SQL 레시피' '4장-10강 4.히스토그램으로 구매 가격대 집계하기'를

 참고 하였다.
 
'임의의 계층 수로 히스토그램 만들기' 부분이다.

 먼저 히스토그램을 만들기 위해서는 구매 로그 내부에서 매출 금액의 최댓값(max_amount)과 최솟값(min_amount),
 
 금액 범위(range_amount)를 구한다. 

'최댓값', '최솟값', '범위'를 구하는 쿼리문
```python
WITH
stats AS(
SELECT
   -- 금액의 최댓값
   MAX(price) AS max_price
   -- 금액의 최솟값
 , MIN(price) AS min_price
   -- 금액의 범위
 , MAX(price) - MIN(price) AS range_price
   -- 계층의 수
 , 10 AS bucket_num
FROM
 purchase_detail_log
)
SELECT *
FROM stats
;
```

그 다음으로는 최소 금액에서 최대 금액의 범위를 계층으로 구분해야 한다.

데이터의 '계층'을 구하는 쿼리문
```python
WITH
stats AS (
SELECT
   -- 금액의 최댓값
   MAX(price) AS max_price
   -- 금액의 최솟값
 , MIN(price) AS min_price
   -- 금액의 범위
 , MAX(price) - MIN(price) AS range_price
   -- 계층의 수
 , 10 AS bucket_num
FROM
 purchase_detail_log
)
, purchase_log_with_bucket AS (
  SELECT
	 price
   , min_price
	 -- 정규화 금액: 대상 금액에서 최소 금액을 뺀 것
   , price - min_price AS diff
	 -- 계층 범위: 금액 범위를 계층 수로 나눈 것
   , 1.0 * range_price / bucket_num AS bucket_range
	
	
   -- 계층 판정: FLOOR(<정규화 금액> / <계층 범위>)
   , FLOOR(
	  1.0 * (price - min_price)
	  / (1.0 * range_price / bucket_num)
      -- index가 1부터 시작하므로 1만큼 더하기
   ) + 1 AS bucket
	
  -- PostgreSQL의 경우 width_bucket 함수 사용 가능
  -- , width_bucket(price, min_price, max_price, bucket_num) AS bucket
FROM
 purchase_detail_log, stats
)
SELECT *
FROM purchase_log_with_bucket
ORDER BY diff
;
```
참고로 맨 마지막 부분은 원래 'amount'이지만 책의 코드를 그대로 치니 

'''amount'라는 컬럼이 존재하지 않습니다.'라는 에러가 떠서 

'diff'로 수정해 주었다.

이번에는 모든 레코드가 범위 내부에 들어갈 수 있게 쿼리문을 개선하였다.

계급 상한 값을 조정한 쿼리문
```python
WITH
stats AS (
SELECT
   -- <금액의 최댓값> + 1
   MAX(price) + 1 AS max_price
   -- 금액의 최솟값
 , MIN(price) AS min_price
   -- <금액의 범위> + 1(실수)
 , MAX(price) + 1 - MIN(price) AS range_price
   -- 계층 수
 , 10 AS bucket_num
FROM
 purchase_detail_log
)
, purchase_log_with_bucket AS(
SELECT
	 price
   , min_price
	 -- 정규화 금액: 대상 금액에서 최소 금액을 뺀 것
   , price - min_price AS diff
	 -- 계층 범위: 금액 범위를 계층 수로 나눈 것
   , 1.0 * range_price / bucket_num AS bucket_range
	
	
   -- 계층 판정: FLOOR(<정규화 금액> / <계층 범위>)
   , FLOOR(
	  1.0 * (price - min_price)
	  / (1.0 * range_price / bucket_num)
      -- index가 1부터 시작하므로 1만큼 더하기
   ) + 1 AS bucket
	
  -- PostgreSQL의 경우 width_bucket 함수 사용 가능
  -- , width_bucket(price, min_price, max_price, bucket_num) AS bucket
FROM
 purchase_detail_log, stats
)
SELECT *
FROM purchase_log_with_bucket
ORDER BY price
;
```

마지막으로는 구한 계층을 사용해 도수를 계산하여 각 계층의 하한과 상한을 출력해 준다.

'lower_limit' 과 'upper_limit' 을 구해 하한과 상한을 계산하면 된다.

히스토그램을 구하는 쿼리문
```python
WITH
stats AS (
SELECT
   -- 금액의 최댓값
   MAX(price) AS max_price
   -- 금액의 최솟값
 , MIN(price) AS min_price
   -- 금액의 범위
 , MAX(price) - MIN(price) AS range_price
   -- 계층의 수
 , 10 AS bucket_num
FROM
 purchase_detail_log
)
, purchase_log_with_bucket AS(
SELECT
	 price
   , min_price
	 -- 정규화 금액: 대상 금액에서 최소 금액을 뺀 것
   , price - min_price AS diff
	 -- 계층 범위: 금액 범위를 계층 수로 나눈 것
   , 1.0 * range_price / bucket_num AS bucket_range
	
	
   -- 계층 판정: FLOOR(<정규화 금액> / <계층 범위>)
   , FLOOR(
	  1.0 * (price - min_price)
	  / (1.0 * range_price / bucket_num)
      -- index가 1부터 시작하므로 1만큼 더하기
   ) + 1 AS bucket
	
  -- PostgreSQL의 경우 width_bucket 함수 사용 가능
  -- , width_bucket(price, min_price, max_price, bucket_num) AS bucket
FROM
 purchase_detail_log, stats
)
SELECT
   bucket
   -- 계층의 하한과 상한 계산하기
 , min_price + bucket_range * (bucket -1) AS lower_limit
 , min_price + bucket_range * bucket AS upper_limit
   -- 도수 세기
 , COUNT(price) AS num_purchase
   -- 합계 금액 계산하기
 , SUM(price) AS total_amount
FROM 
 purchase_log_with_bucket
GROUP BY
 bucket, min_price, bucket_range
ORDER BY bucket
;
```
'임의의 계층 너비로 히스토그램 작성하기'

쿼리문을 응용해서 금액의 최솟값, 최댓값, 금액의 범위 등의 고정값을 기반으로 임의의 계층 너비로 

변경할 수 있는 기능을 넣어보겠다.

히스토그램의 상한과 하한을 수동으로 조정하는 쿼리문
```python
WITH
stats AS (
SELECT
   -- 금액의 최댓값
   50000 AS max_price
   -- 금액의 최솟값
 , 0 AS min_price
   -- 금액의 범위
 , 50000 AS range_price
   -- 계층 수
 , 10 AS bucket_num
FROM
 purchase_detail_log
)
, purchase_log_with_bucket AS(
SELECT
	 price
   , min_price
	 -- 정규화 금액: 대상 금액에서 최소 금액을 뺀 것
   , price - min_price AS diff
	 -- 계층 범위: 금액 범위를 계층 수로 나눈 것
   , 1.0 * range_price / bucket_num AS bucket_range
	
	
   -- 계층 판정: FLOOR(<정규화 금액> / <계층 범위>)
   , FLOOR(
	  1.0 * (price - min_price)
	  / (1.0 * range_price / bucket_num)
      -- index가 1부터 시작하므로 1만큼 더하기
   ) + 1 AS bucket
	
  -- PostgreSQL의 경우 width_bucket 함수 사용 가능
  -- , width_bucket(price, min_price, max_price, bucket_num) AS bucket
FROM
 purchase_detail_log, stats
)
SELECT
   bucket
   -- 계층의 하한과 상한 계산하기
 , min_price + bucket_range * (bucket - 1) AS lower_limit
 , min_price + bucket_range * bucket AS upper_limit
   -- 도수 세기
 , COUNT(price) AS num_purchase
   -- 합계 금액 계산하기
 , SUM(price) AS total_amount
FROM
 purchase_log_with_bucket
GROUP BY
 bucket, min_price, bucket_range
ORDER BY bucket
;
```

히스토그램은 데이터 분포를 확인할 때 유용하게 사용할 수 있으므로 꼭 기억해 두자.

('데이터 분석을 위한 SQL레시피' 4장 '10강'中)
