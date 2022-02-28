---
title: postgre SQL-practice15
tag: postgre SQL-practice15
date: 2022-02-16
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

 '데이터 분석을 위한 SQL 레시피' 4장 10강 3. 팬 차트로 상품의 매출 증가율 확인하기
  를  보고 실습을 진해하였다.
 
팬 차트 작성 때 필요한 데이터를 구하는 쿼리문
```python
WITH
daily_category_amount AS(
 SELECT
	dt
  , category
  -- ■ PostgreSQL, Hive, Redshift, SparkSQL의 경우는 다음과 같이 구성
  -- ■ BigQuery의 경우 substring을 substr로 수정하기
  , substring(dt,1,4) AS year
  , substring(dt,6,2) AS month	
  , substring(dt,9,2) AS date
  , SUM(price) AS amount
FROM purchase_detail_log
GROUP BY dt, category
)
, monthly_category_amount AS (
 SELECT
	concat(year, '-',month) AS year_month
	-- ■ Redshift의 경우는 concat 함수를 조합해서 사용하기 또는 || 연산자 사용하기
	-- concat(concat(year, '-'),month) AS year_month
	-- year || '-' || month AS year_month
	, category
	, SUM(amount) AS amount
 FROM 
  daily_category_amount
 GROUP BY 
  year, month, category
)
SELECT
  year_month
, category
, amount
, FIRST_VALUE(amount)
   OVER(PARTITION BY category ORDER BY year_month, category ROWS UNBOUNDED PRECEDING)
  AS base_amount
, 100.0
  * amount
  / FIRST_VALUE(amount)
     OVER(PARTITION BY category ORDER BY year_month, category ROWS UNBOUNDED PRECEDING)
  AS rate
FROM
 monthly_category_amount
ORDER BY
 year_month, category
;
```
'base_amount' 컬럼에 FIRST_VALUE 윈도 함수를 사용해 구한 2017년 1월의 매출을 넣었고,

그러한 base_amount에 대한 비율을 rate 컬럼에 계산했다.




팬 차트를 만들 때 확실히 해두어야 하는 것이 있다면, 어떤 시점에서의 매출 금액을 기준점으로 채택할 것인가이다.

이에 따라서 성장 경향인지 또는 쇠퇴 경향인지 판단이 크게 달라지기 때문이다.

예를 들어 8월에 매출이 매년 늘어나는 상품이 있다면, 8월을 기준으로 잡았을 경우 해당 상품은 이후로 계속 감소하는

그래프가 될 것이다. 결과적으로 8월에 매출이 증가하는 현산을 그래프로 제대로 확인 할수 없다. 따라서 계절변동이 

적은 평균적인 달을 기준으로 선택해야 하는 것이 좋습니다. 7~8월의 매출 변화를 확인하다는 명백한 목적이 있을 경우에는 

직전인 6월을 기준점으로 선택하는 것이 좋습니다. 이처럼 반드시 근거를 가지고 기준점을 채택해야 하므로 신경 쓰기 

바랍니다. 

('데이터 분석을 위한 SQL레시피' 4장 '10강'中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)
참고 도서 : 데이터 분석을 위한 SQL 레시피
저자 : 가나키 나가토, 다미야 나오토
출판사 : 한빛미디어
