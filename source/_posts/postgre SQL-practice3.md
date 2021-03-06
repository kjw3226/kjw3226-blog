---
title: postgre SQL-practice3
tag: postgre SQL-practice3
date: 2022-02-06
categories:	SQL
----
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

오늘은 '윈도우 함수'를 사용하는 예제를 본격적으로 

들어가서 

- 테이블 전체의 특징량 계산
- 그루핑한 데이터의 특징량 계산
- 집약 함수를 적용한 값과 집약 전의 값을 동시에 다루기
- <그룹 내부의 순서> - 'ORDER BY' 구문으로 순서 정의 하기 

까지 4개의 쿼리문을 
'데이터 분서을 위한 SQL 레시피' 책을 보며 실습 해봤다.

집약 함수를 사용해서 테이블 전체의 특징량을 계산하는 쿼리
```python
SELECT 
   COUNT(*) AS total_count
 , COUNT(DISTINCT user_id) AS user_count
 , COUNT(DISTINCT product_id) AS product_count
 , SUM(score) AS sum
 , AVG(score) AS avg
 , MAX(score) AS max
 , MIN(score) AS min
FROM 
 review
;
```
사용자 기반으로 데이터를 분할하고 집약 함수를 적용하는 쿼리
```python
SELECT
   user_id
 , COUNT(*) AS total_count
 , COUNT(DISTINCT product_id) AS product_count
 , SUM(score) AS sum
 , AVG(score) AS avg
 , MAX(score) AS max
 , MIN(score) AS min
FROM
 review
GROUP BY
 user_id
;
```
윈도우 함수를 사용해 집약 함수의 결과와 
원래 값을 동시에 다루는 쿼리
```python
SELECT 
   user_id
 , product_id
  -- 개별 리뷰 점수
 , score
  -- 전체 평균 리뷰 점수
 , AVG(score) OVER() AS avg_score
  -- 사용자의 평균 리뷰 점수
 , AVG(score) OVER(PARTITION BY user_id) AS user_avg_score
  -- 개별 리뷰 점수와 사용자 평균 리뷰 점수의 차이
 , score - AVG(score) OVER(PARTITION BY user_id) AS user_avg_score_diff
FROM
 review
;
```
윈도우 함수의 'ORDER BY' 구문을 사용해 
테이블 내부의 순서를 다루는 쿼리
```python
SELECT
   product_id
 , score
 
 
   -- 점수 순서로 유일한 순위를 붙임
 , ROW_NUMBER()            OVER(ORDER BY score DESC) AS row
   -- 같은 순위를 허용해서 순위를 붙임
 , RANK()                  OVER(ORDER BY score DESC) AS rank
   -- 같은 순위가 있을 때 같은 순위 다음에 있는 순위를 건너 뛰고 순위를 붙임
 , DENSE_RANK()            OVER(ORDER BY score DESC) AS dense_rank
 
 
   -- 현재 행보다 앞에 있는 행의 값 추출하기
 , LAG(product_id)         OVER(ORDER BY score DESC) AS lag1
 , LAG(product_id, 2)      OVER(ORDER BY score DESC) AS lag2
 
 
   -- 현재 행보다 뒤에 있는 행의 값 추출하기
 , LEAD(product_id)        OVER(ORDER BY score DESC) AS lead1
 , LEAD(product_id, 2)     OVER(ORDER BY score DESC) AS lead2
FROM popular_products
ORDER BY row
;
```

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어
