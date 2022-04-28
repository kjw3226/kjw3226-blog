---
title: postgre SQL-practice76
tag: postgre SQL-practice76
date: 2022-04-28
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  24강 점수 계산하기'의

'1. 여러 값을 균형있게 조합해서 점수 계산하기'

로 넘어갔으며

페이지 538 ~ 546을 참고하였다.


세로 데이터의 평균을 구하는 쿼리문
```python
SELECT
   *
   --산술평균
 , (recall + precision) / 2 AS arithmetic_mean
   --기하평균
 , POWER(recall + precision, 1.0 / 2) AS geometic_mean
   --조화평균
 , 2.0 / ((1.0 / recall) + (1.0 / precision)) AS harmonic_mean
FROM
 search_evaluation_by_col
 --값이 0보다 큰 것만으로 한정하기
WHERE recall * precision > 0
ORDER BY path
;
```


가로 기반 데이터의 평균을 계산하는 쿼리문
```python
SELECT
   path
  --산술평균
 , AVG(value) AS arithmetic_mean
 -- 기하 평균(대수의 산술 평균)
 --■Postgre SQL, Redshift의 경우 상용 로그로 log 함수 사용하기
 , POWER(10, AVG(log(value))) AS geometic_mean
 --■Hive, BigQuery, SparkSQL의 경우 상용 로그로 log10 함수 사용하기
 --, POWER(10, AVG(log10(value))) AS geometic_mean
 --조화평균
 , 1.0 / (AVG(1.0 / value)) AS harmonic_mean
FROM
 search_evaluation_by_row
 --값이 0보다 큰 것만으로 한정하기
WHERE value > 0
GROUP BY path
  -- 빠진 데이터가 없게 path로 한정하기
HAVING COUNT(*) = 2
ORDER BY path
;
```




세로 기반 데이터의 가중 평균을 계산하는 쿼리문
```python
SELECT
   *
   -- 가중치가 추가된 산술 평균
 , 0.3 * recall + 0.7 * precision AS weighted_a_mean
   -- 가중치가 추가된 기하 평균
 , POWER(recall, 0.3) * POWER(precision, 0.7) AS weighted_g_mean
   -- 가중치가 추가된 조화 평균
 , 1.0 / ((0.3/ recall) + (0.7 / precision)) AS weighted_h_mean
FROM
 search_evaluation_by_col
 --값이 0보다 큰 것만으로 한정하기
WHERE recall * precision > 0
ORDER BY path
;
```



가로 기반 테이블의 가중 평균을 계산하는 쿼리문
```python
WITH
weights AS (
 -- 가중치 마스터 테이블(가중치 합계가 1.0이 되게 설정)
	       SELECT 'recall'      AS index, 0.3 AS weight
 UNION ALL SELECT 'precision'   AS index, 0.7 AS weight
)
SELECT 
   e.path
 -- 가중치가 추가된 산술 평균
 , SUM(w.weight * e.value) AS weighted_a_mean
 -- 가중치가 추가된 기하 평균
 --■Postgre SQL, Redshift의 경우 로그 log 함수 사용하기
 , POWER(10, SUM(w.weight * log(e.value))) AS weighted_g_mean
 --■Hive, BigQuery, SparkSQL의 경우 로그로 log10 함수 사용하기
 --, POWER(10, SUM(w.weight * log10(e.value))) AS weighted_g_mean
 
 
 --가중치가 추가된 조화 평균
 , 1.0 / (SUM(w.weight / e.value)) AS weighted_h_mean
FROM
   search_evaluation_by_row AS e
  JOIN
   weigths AS w
   ON e.index = w.index
  -- 값이 0보다 크다는 것만으로 한정하기
WHERE e.value > 0
GROUP BY e.path
  --빠진 데이터가 없게 path로 한정하기
HAVING COUNT(*) = 2
ORDER BY e.path
;
```

이번 절에서 소개한 예는 2개의 값에 대한 산술 평균, 기하 평균, 조화 평균이었습니다.

조금 활용하면, 3개 이상의 값에 대해서도 같은 쿼리로 평균을 구할 수 있습니다.

이러한 3개의 평균을 사용하면 다양한 지표의 데이터 활용에 큰 도움이

될 것입니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 23강 점수 계산하기 546 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어
