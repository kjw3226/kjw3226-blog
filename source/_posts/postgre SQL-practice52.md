---
title: postgre SQL-practice52
tag: postgre SQL-practice52
date: 2022-04-04
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'7장  17강 데이터를 조합해서 새로운 데이터 만들기'의

'2. 주말과 공휴일 판정하기'로 넘어갔으며

페이지 414 ~ 417를 참고하였다.

PostgreSQL에서의 주말과 공휴일을 정의하는 방법 예
```python
CREATE TABLE mst_calendar(
   year        integer
 , month       integer
 , day         integer
 , dow         varchar(10)
 , dow_num     integer
 , holiday_name varchar(255)
);
```

주말과 공휴일을 판정하는 쿼리문
```python
SELECT 
   a.action
 , a.stamp
 , c.dow
 , c.holiday_name
   --주말과 공휴일 판정
 , c.dow_num IN (0, 6) -- 토요일과 일요일 판정하기
  OR c.holiday_name IS NOT NULL -- 공휴일 판정하기
  AS is_day_off
FROM
   access_log AS a
 JOIN
  mst_calendar AS c
  -- 액션 로그의 타임스탬프에서 연, 월, 일을 추출하고 결합하기
  --■ PostgreSQL, Hive, Redshift, SparkSQL의 경우 다음과 같이 사용
  --■ BigQuery의 경우 substring를 substr, int를 int64로 수정하기
  ON CAST(substring(a.stamp, 1, 4) AS int) = c.year
  AND CAST(substring(a.stamp, 6, 2) AS int) = c.month
  AND CAST(substring(a.stamp, 9, 2) AS int) = c.day
;
```
