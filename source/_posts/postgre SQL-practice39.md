---
title: postgre SQL-pratice39
tag: postgre SQL-pratice39
date: 2022-03-22
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'6장  14강 사이트 전체의 특징/경향 찾기

4. 접근 요일, 시간대 파악하기'

페이지 339 ~ 342을 보고 쿼리문을 작성하였다.

요일/시간대별 방문자 수를 집계하는 쿼리문
```python
WITH
access_log_with_dow AS (
 SELECT
	stamp
  -- 일요일(0)부터 토요일(6)까지의 요일 번호 추출하기
  -- ■ PostgreSQL, Redshift의 경우 date_part 함수 사용하기
  , date_part('dow', stamp::timestamp) AS dow
  -- ■ BigQuery의 경우 EXTRACT(dayofqeek from ~)함수 사용하기
  --, EXTRACT(dayofweek from timestamp(stamp)) - 1 AS dow
  -- ■ Hive, SparkSQL의 경우 from_unixtime 함수 사용하기
  --, from_unixtime(unix_timestamp(stamp), 'u') % 7 AS dow


  --00:00:00 부터의 경과 시간을 초 단위로 계산하기
  -- ■ PostgreSQL, Hive, Redshift, SparkSQL의 경우
  --   substring 함수를 사용해 시,분,초를 추출하고 초 단위로 환산해서 더하기
  -- ■ BigQuery의 경우 substring을 substr, int를 int64로 수정하기
  ,  CAST(substring(stamp, 12, 2) AS int) * 60 * 60
    +CAST(substring(stamp, 15, 2) AS int) * 60
	+CAST(substring(stamp, 18, 2) AS int)
    AS whole_seconds
	
	
  --시간 간격 정하기
  --현제 예제에는 30분(1800초)으로 지정했음
  , 30 * 60 AS interval_aeconds
 FROM access_log
)
, access_log_with_floor_seconds AS (
  SELECT
	stamp
  , dow
  --00:00:00부터의 경과 시간을 interval_seconds로 나누기
  --■ PostgreSQL, Hive, Redshift, SparkSQL의 경우는 다음과 같이 사용하기
  --■ BigQuery의 경우 int를 int64로 수정하기
   , CAST((floor(whole_seconds / interval_seconds) * interval_seconds) AS int)
	AS floor_seconds
  FROM access_log_with_dow
)
, access_log_with_index AS (
  SELECT
	 stamp
   , dow
   -- 초를 다시 타임스탬프 형식으로 변환하기
   -- ■ PostgreSQL, Redshift의 경우는 다음과 같이 하기
   ,    lpad(floor(floor_seconds / (60 * 60))::text           ,2,'0') || ':'
           || lpad(floor(floor_seconds % (60 * 60) / 60)::text, 2, '0') || ':'
		   || lpad(floor(floor_seconds % 60)::text            , 2, '0')
   -- ■ BigQuery의 경우는 다음과 같이 하기
   --, concat(
   --    lpad(CAST(floor_seconds / (60 * 60))                   AS string), 2, '0'), ':'
   --   ,lpad(CAST(floor(mod(floor_seconds, 60 * 60)) / 60 AS string), 2, '0'), ':'
   --   ,lpad(CAST(floor(mod(floor_seconds % 60)           AS string), 2,  '0')
     AS index_time
  FROM access_log_with_floor_seconds
)
SELECT
   index_time
 , COUNT(CASE dow WHEN 0 THEN 1 END) AS sun
 , COUNT(CASE dow WHEN 1 THEN 1 END) AS mon
 , COUNT(CASE dow WHEN 2 THEN 1 END) AS tue
 , COUNT(CASE dow WHEN 3 THEN 1 END) AS wed
 , COUNT(CASE dow WHEN 4 THEN 1 END) AS thu
 , COUNT(CASE dow WHEN 5 THEN 1 END) AS fri
 , COUNT(CASE dow WHEN 6 THEN 1 END) AS sat
FROM 
 access_log_with_index
GROUP BY
  index_time
ORDER BY
  index_time
;
```

사용자의 방문이 많은 시간대에 캠페인을 실시하는 것이 안정적이며 일반적인 

경우라고 할 수 있습니다. 반대로 사용자가 적은 시간대를 사용하면

EC 사이트의 경우 타임 세일, 소셜 게임의 경우 아이템 획득율 상승 등의

이벤트를 검토할 수도 있습니다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 14강 페이지 342 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어