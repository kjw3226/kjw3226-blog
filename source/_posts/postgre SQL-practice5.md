---
title: postgre SQL-practice5
tag: postgre SQL-practice5
date: 2022-02-07
categories:	SQL
----
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

오전에 이어 오후에도

'데이터 분석을 위한 SQL 레시피'를 보고 

이번에도 예제 코드를 보며 실습을 진행했다.

행으로 저장된 지표 값을 열로 변환하는 쿼리문
```python
SELECT
   dt
 , MAX(CASE WHEN indicator = 'impressions' THEN val END) AS impressions
 , MAX(CASE WHEN indicator = 'sessions'   THEN val END) AS sessions
 , MAX(CASE WHEN indicator = 'users'     THEN val END) AS users
FROM daily_kpi
GROUP BY dt
ORDER BY dt
;
```
행을 집약해서 쉼표로 구분된 문자열로 변환해주는 쿼리문
```python
SELECT 
   purchase_id
   
   
   -- 상품 ID를 배열에 집약하고 쉼표로 구분된 문자열로 변환하기
   -- ■ Postgre SQL, BigQuery의 경우는 string_agg 사용하기
 , string_agg(product_id, ',') AS product_ids
 
 
   -- ■ Redshift의 경우는 listagg 사용하기
   --, listagg(product_id, ',') AS product_ids
   
   
   -- ■ Hive, SparkSQL의 경우는  collect_list와 concat_ws 사용하기
   --, concat_ws(',', collect_list(product_id)) AS product_ids
   , SUM(price) AS amount
 FROM purchase_detail_log
 GROUP BY purchase_id
 ORDER BY purchase_id
;
```