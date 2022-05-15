---
title: postgre SQL-practice53
tag: postgre SQL-practice53
date: 2022-04-05
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'7장  17강 데이터를 조합해서 새로운 데이터 만들기'의

'3. 하루 집계 범위 변경하기'로 넘어갔으며

페이지 417 ~ 419를 참고하였다.

```python
WITH
action_log_with_mod_stamp AS (
 SELECT *
  --4시간 전의 시간 계산하기
  --■PostgreSQL의 경우 interval 자료형의 데이터를 사용해 날짜를 사칙연산 할 수 있음
  --, CAST(stamp::timestamp - '4 hours'::interval AS text) AS mod_stamp
  --■Redshift의 경우 dateadd 함수 사용하기
  --, CAST(dateadd(hour, -4, stamp::timestamp) AS text) AS mod_stamp
  --■BigQuery의 경우 timestamp_sub 함수 사용하기
  --, CAST(timestamp_sub(timestamp(stamp), interval 4 hour) AS string) AS mod_stamp
  --■Hive, SparkSQL의 경우 한 번 unixtime으로 변환한 뒤 초 단위로 계산하고
  --  다시 타임스탬프로 변환하기
  --, from_unixtime(unix_timestamp(stamp) - 4 * 60 * 60) AS mod_stamp
 FROM action_log
)
SELECT 
   session
 , user_id
 , action
 ,stamp
 --원래 타임스탬프(raw_date)와, 4시간 후에 나타내는 타임스탬프(mod_date) 추출하기
 --■PostgreSQL, Hive, Redshift, SparkSQL의 경우 다음과 같이 사용하기
 , substring(stamp, 1, 10) AS raw_date
 , substring(mod_stamp, 1, 10) AS mod_date
 --■BigQuery의 경우 substring을 substr로 수정하기
 --, substr(stamp, 1, 10) AS raw_date
 --, substr(mod_stamp, 1, 10) AS mod_date
FROM action_log_with_mod_stamp;
```

하루 집계 범위를 모든 리포트에 적용한다면, 

로그 수집과 데이터 집계와 관련한 

배치 처리 시간을 집계 범위에 맞게 변경해야 합니다.

참고로 날짜를 기반으로 무언가를 집계/변경하는 경우 원래 데이터를

꼭 따로 백업한 뒤 가공하기 바랍니다.

(데이터 분석을 위한 SQL 레시피-7장 데이터 활용의

정밀도를 높이는 분석 기술 17강 데이터를 조합해서

새로운 데이터 만들기 페이지 419 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어