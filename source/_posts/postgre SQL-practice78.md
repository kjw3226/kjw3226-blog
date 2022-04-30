---
title: postgre SQL-practice78
tag: postgre SQL-practice78
date: 2022-04-30
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'8장  24강 점수 계산하기'의

'3. 각 데이터의 편차값 계산하기'

로 넘어갔으며

페이지 551 ~ 555을 참고하였다.


<표준 편차 구하는 식>

![standard deviation formula](https://user-images.githubusercontent.com/96108301/166101101-2cd7e682-f38c-4439-a047-2a26a894b5fb.jpg)

<편차 값 구하는 식>

![deviation value formula](https://user-images.githubusercontent.com/96108301/166101112-fdcc7654-e306-46a2-bf61-9af02dc8833b.jpg)

<정규 값 구하는 식>

![regular value formula](https://user-images.githubusercontent.com/96108301/166101122-58726a70-522a-467a-8b1c-c62d940f8dd1.jpg)

표준 편차, 기본 값, 편차 값을 계산하는 쿼리문
```python
SELECT
   subject
 , name
 , score
 -- 과목별로 표준편차 구하기
 , stddev_pop(score) OVER(PARTITION BY subject) AS stddev_pop
 -- 과목별로 평균 점수 구하기
 , AVG(score) OVER(PARTITION BY subject) AS avg_score
 -- 점수별로 기준 점수 구하기
 , (score - AVG(score) OVER(PARTITION BY subject))
   / stddev_pop(score) OVER(PARTITION BY subject)
   AS std_value
 -- 점수별로 편차값 구하기
 , 10.0 * (score - AVG(score) OVER(PARTITION BY subject))
   / stddev_pop(score) OVER(PARTITION BY subject)
   + 50
   AS deviation
FROM exam_scores
ORDER BY subject, name;
```


표준편차를 따로 계산하고, 기본값과 편차값을 계산하는 쿼리문
```python
WITH
exam_stddev_pop AS (
 -- 다른 테이블에서 과목별로 표준편차 구해두기
 SELECT
	subject 
  , stddev_pop(score) AS stddev_pop
 FROM exam_scores
 GROUP BY subject
)
SELECT
   s.subject
 , s.name
 , s.score
 , d.stddev_pop
 , AVG(s.score) OVER(PARTITION BY s.subject) AS avg_score
 , (s.score - AVG(s.score) OVER(PARTITION BY s.subject))
   / d.stddev_pop
   AS std_value
 , 10.0 * (s.score - AVG(s.score) OVER(PARTITION BY s.subject))
   / d.stddev_pop
   + 50
   AS deviation
FROM 
   exam_scores AS s
 JOIN
  exam_stddev_pop AS d
  ON s.subject = d.subject
ORDER BY s.subject, s.name;
```

기본값과 편차값 등의 통계 지표를 SQL로 계산하는 방법은 윈도 함수의 등장

덕분에 굉장히 쉬워졌습니다.  하지만 정의를 모르고 함수를 사용하는 것만으로는

데이터 분석을 제대로 할 수 없습니다.

따라서 지표 정의과 의미를 확실하게 확인해서 의미 있는 데이터 분석을 하기 바랍니다.

(데이터 분석을 위한 SQL 레시피-8장 데이터를

무기로 삼기 위한 분석 기술 23강 점수 계산하기 555 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어