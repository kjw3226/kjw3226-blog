---
title: postgre SQL-practice77
tag: postgre SQL-practice77
date: 2022-04-29
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  24강 점수 계산하기'의

'2. 값의 범위가 다른 지표를 반정규화해서 비교 가능한 상태로 만들기'

로 넘어갔으며

페이지 546 ~ 551을 참고하였다.


열람 수와 구매 수에 Min-Max 정규화를 적용한 쿼리문
```python
SELECT
   user_id
 , product
 , view_count AS v_count
 , purchase_count AS p_count
 , 1.0 * (View_count - MIN(view_count) OVER())
   --■ PostgreSQL, Redshift, BigQuery, SparkSQL의 경우 NULLIF로 0으로 나누는 것 피하기
   / NULLIF((MAX(view_count) OVER() - MIN(view_count) OVER()), 0)
   --■Hive의 경우 NULLIF 대신 CASE 식 사용하기
   -- / (CASE
   --    WHEN MAX(view_count) OVER() - MIN(view_count) OVER() = 0 THEN NULL
   --    ELSE MAX(view_count) OVER() - MIN(view_count) OVER()
   --   END)
   AS norm_v_count
 , 1.0 * (purchase_count - MIN(purchase) OVER())
   --■PostgreSQL, Redshift, BigQuery, SparkSQL의 경우 NULLIF로 0으로 나누는 것 피하기
   / NULLIF((MAX(purchase_count) OVER() - MIN(purchase_count) OVER()), 0)
   --■Hive의 경우 NULLIF 대신 CASE 식 사용하기
    -- / (CASE
   --    WHEN MAX(purchase_count) OVER() - MIN(purchase_count) OVER() = 0 THEN NULL
   --    ELSE MAX(purchase_count) OVER() - MIN(purchase_count) OVER()
   --   END)
   AS norm_p_count
FROM action_count
ORDER BY user_id, product;
```


시그모이드 함수를 사용해 변환하는 쿼리문
```python
SELECT
   user_id
 , product
 , view_count AS v_count
 , purchase_count AS p_count
   --게인을 0.1로 사용한 시그모이드 함수
 , 2.0 / (1 + exp(-0.1 * view_count)) - 1.0 AS sigm_v_count
   --게인을 10으로 사용한 시그모이드 함수
 , 2.0 / (1 + exp(-0.1 * purchase_count)) - 1.0 AS sigm_p_count
FROM action_counts
ORDER BY user_id, product;
```

값의 범위(스케일)가 다른 지표를 다루는 여러 가지 방법을 살펴보았습니다.

어떠한 방법이 적합할지는 데이터의 특성에 따라서 다릅니다.

직접 사용해보면서 어느 쪽이 더 효율적일지 느껴보기 바랍니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 23강 점수 계산하기 551 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어