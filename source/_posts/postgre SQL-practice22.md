---
title: postgre SQL-practice22
tag: postgre SQL-practice22
date: 2022-02-25
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)


'데이터 분석을 위하 SQL 레시피' 에서 

오늘은 'Decile'이라는 것을 이용해 사용자의 특징을 분석하고

거기에 따른 그래프를 나타내는 SQL 쿼리문을 

페이지 215 ~ 페이지 220 까지를 보고 실습을 진행했다.

먼저, 'Decile' 분석 과정은 다음과 같다.

1. 사용자를 구매 금액이 많은 순으로 정렬한다.

2. 정렬된 사용자 상위부터 10%씩 Decile1부터 Decile10까지의 그룹을 할당한다.

3. 각 그룹의 구매 합계를 집계한다.

4. 전체 구매 금액에 대해 각 Decile의 구매 금액 비율(구성비) 를 계산합니다.

5. 상위에서 누적으로 어느 정도의 비율을 차지하는가 구성비누계를 집계한다.


'구매액'이 많은 순서로 사용자 그룹을 10등분하는 쿼리문
```python
WITH
user_purchase_amount AS(
 SELECT
	user_id
  , SUM(amount) AS purchase_amount
 FROM
  action_log
 WHERE
  action = 'purchase'
 GROUP BY
  user_id
)
, user_with_decile AS(
 SELECT
	user_id
  , purchase_amount
  , ntile(10) OVER(ORDER BY purchase_amount DESC) AS decile
 FROM
  user_purchase_amount
)
SELECT *
FROM users_with_decile
;
```

'10분할'만 'Decile'들을 집계하는 쿼리문
```python
WITH
user_purchase_amount AS(
 SELECT
	user_id
  , SUM(amount) AS purchase_amount
 FROM
  action_log
 WHERE
  action = 'purchase'
 GROUP BY
  user_id
)
, user_with_decile AS(
 SELECT
	user_id
  , purchase_amount
  , ntile(10) OVER(ORDER BY purchase_amount DESC) AS decile
 FROM
  user_purchase_amount
)
, decile_with_purchase_amount AS (
  SELECT
	decile
	, SUM(purchase_amount) AS amount
	, AVG(purchase_amount) AS avg_amount
	, SUM(SUM(purchase_amount)) OVER (ORDER BY decile) AS cumulative_amount
	, SUM(SUM(purchase_amount)) OVER () AS total_amount
  FROM
   users_with_deile
  GROUP BY
   decile
)
SELECT *
FROM
 decile_with_purchase_amount
;
```

마지막으로 구성비와 구성비누계를 계산한다.

'구매액'이 많은 'Decile' 순서로 '구성비'와 '구성비누계'를 계산하는 쿼리문
```python
WITH
user_purchase_amount AS(
 SELECT
	user_id
  , SUM(amount) AS purchase_amount
 FROM
  action_log
 WHERE
  action = 'purchase'
 GROUP BY
  user_id
)
, user_with_decile AS(
 SELECT
	user_id
  , purchase_amount
  , ntile(10) OVER(ORDER BY purchase_amount DESC) AS decile
 FROM
  user_purchase_amount
)
, decile_with_purchase_amount AS (
  SELECT
	decile
	, SUM(purchase_amount) AS amount
	, AVG(purchase_amount) AS avg_amount
	, SUM(SUM(purchase_amount)) OVER (ORDER BY decile) AS cumulative_amount
	, SUM(SUM(purchase_amount)) OVER () AS total_amount
  FROM
   users_with_deile
  GROUP BY
   decile
)
SELECT
   decile
 , amount
 , avg_amount
 , 100.0 * amount / total_amount AS total_ratio
 , 100.0 * cumulative_amount / total_amount AS cumulative_ratio
FROM
 decile_with_purchase_amount;
```

이번 절에서 소개한 Decile 분석을 시행하고, Decile의 특징을

다른 분석 방법으로 세분화해서 조사하면 사용자의 속성을 자세하게 파악할 수 있다.


예를 들어, Decile 7~10은 정착되지 않은 고객을 나타냅니다. 

따라서 메일 매거진 등으로 리텐션(고객 유지 비율)을 높이는 등의 대책을 세울

수 있다. 만약 메일 매거진을 이미 보내고 있다면, 메일 매거진을 보낼 때 

추가적인 데이터를 수집해서 Decile 7~10에 해당하는 사람들의 속성과 관련된

데이터를 더 수집하고 활용할 수 있을 것이다.

(데이터 분석을 위한 SQL 레시피-5장 사용자를 파악하기 위한 데이터 추출 11강 6.Decile 분석을 사용해 사용자를 10단계 그룹으로 나누기 中)