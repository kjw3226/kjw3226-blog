---
title: postgre SQL-practice
tag: postgre SQL-practice
date: 2022-01-20 ~ 2022-01-29
categories: SQL
---

'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'데이터 분석을 위한 SQL 레시피'의 예제를

직접 쿼리문을 작성하며 연습했다.

아래는 연습한 쿼리문들이다.

```python
SELECT 
	stamp
   , url
   -- 경로를 슬래시로 잘라 배열로 분할하기
   -- 경로가 반드시 슬래시로 시작하므로 2번째 요소가 마지막 계층
   -- ■ Postgre SQL의 경우 split_part로 n번째 요소 추출하기
   , split_part(substring(url from '//[^/]+([^?#]+)'), '/',2)AS path1
   , split_part(substring(url from '//[^/]+([^?#]+)'), '/',3)AS path2
   -- ■ Redshift도 split_part로 n번째 요소 추출하기
   -- , split_part(regexp_replace(
   --    regexp_substr(url, '//[^/]+[^?#]+'), '//[^/]+', ''), '/',2) AS path1
   -- , split_part(regexp_replace(
   --    regexp_substr(url, '//[^/]+[^?#]+'), '//[^/]+', ''), '/',2) AS path2
   -- ■ BigQuery의 경우 split 함수를 사용해 배열로 자름(별도 인덱스 지정 필요)
   -- , split(regexp_extract(url, '//[^/]+([^?#]+)'), '/')[SAFE_ORDINAL(2)] AS path1
   -- , split(regexp_extract(url, '//[^/]+([^?#]+)'), '/')[SAFE_ORDINAL(3)] AS path2
   -- ■ Hive, SparkSQL도 split 함수를 사용해 배열로 자름
   -- 다만 배열의 인덱스가 0부터 시작하므로 주의하기
   -- , split(parse_url(url, 'PATH'), '/')[1] AS path1
   -- , split(parse_url(url, 'PATH'), '/')[2] AS path2
FROM access_log
;


DROP TABLE IF EXISTS purchase_log_with_coupon;
CREATE TABLE purchase_log_with_coupon (
    purchase_id varchar(255)
  , amount      integer
  , coupon      integer
);

INSERT INTO purchase_log_with_coupon
VALUES
    ('10001', 3280, NULL)
  , ('10002', 4650,  500)
  , ('10003', 3870, NULL)
;

SELECT 
 -- ■ PostgreSQL, Hive, Bigquery의 경우
 -- CURRENT_DATE 상수와 CURRENT_TIMESTAMP 상수 사용하기
   CURRENT_DATE AS dt
  , CURRENT_TIMESTAMP AS stamp
 -- ■ Hive, Bigquery, SparkSQL의 경우
 -- CURRENT_DATE() 함수와 CURRENT_TIMESTAMP() 함수 사용하기
 -- CURRENT_DATE () AS dt
 --,CURRENT_TIMESTAMP() AS stamp
 -- ■ PostgreSQL의 경우 CURRENT_TIMESTAMP는 타임존이 적용된 타임존이 적용된 타임스탬프
 -- 타임존을 적용하고 싶지 않으면 LOCALTIMESTAMP 사용하기
 --, LOCALTIMESTAMP AS stamp
;
```
```python
DROP TABLE IF EXISTS mst_users;
CREATE TABLE mst_users(
    user_id         varchar(255)
  , register_date   varchar(255)
  , register_device integer
);

INSERT INTO mst_users
VALUES
    ('U001', '2016-08-26', 1)
  , ('U002', '2016-08-26', 2)
  , ('U003', '2016-08-27', 3)
;

SELECT 
	user_id
	, CASE
		WHEN register_device = 1 THEN '데스크톱'
		WHEN register_device = 2 THEN '스마트폰'
		WHEN register_device = 3 THEN '애플리케이션'
		-- 디폴트 값을 지정할 경우 ELSE 구문 사용
		-- ELSE ''
	END AS device_name
FROM mst_users
;


DROP TABLE IF EXISTS access_log ;
CREATE TABLE access_log (
    stamp    varchar(255)
  , referrer text
  , url      text
);

INSERT INTO access_log 
VALUES
    ('2016-08-26 12:02:00', 'http://www.other.com/path1/index.php?k1=v1&k2=v2#Ref1', 'http://www.example.com/video/detail?id=001')
  , ('2016-08-26 12:02:01', 'http://www.other.net/path1/index.php?k1=v1&k2=v2#Ref1', 'http://www.example.com/video#ref'          )
  , ('2016-08-26 12:02:01', 'https://www.other.com/'                               , 'http://www.example.com/book/detail?id=002' )
;

SELECT 
	stamp
	-- referrer의 호스트 이름 부분 추출하기
	-- ■ PostgreSQL의 경우 substring 함수와 정규 표현식 사용하기
 , substring(referrer from 'https?://([^/]*)') AS referrer_host
   -- ■ Redshift의 경우 정규 표현식에 그룹을 사용할 수 없으므로
   -- , regexp_substr 함수와 regexp_replace 함수를 조합해서 사용
   -- , regexp_replace(regexp_substr(referrer, 'https?://[^/]*'), 'https?://', '')
   -- AS referrer_host
   -- Hive, SparkSQL의 경우 parse_url 함수로 호스트 이름 추출하기
   -- , parse_url(referrer, 'HOST') AS referrer_host
   -- ■ BigQuery의 경우는 host 함수 사용하기
   -- , host(referrer) AS referrer_host
 FROM access_log
 ;

DROP TABLE IF EXISTS access_log ;
CREATE TABLE access_log (
    stamp    varchar(255)
  , referrer text
  , url      text
);

INSERT INTO access_log 
VALUES
    ('2016-08-26 12:02:00', 'http://www.other.com/path1/index.php?k1=v1&k2=v2#Ref1', 'http://www.example.com/video/detail?id=001')
  , ('2016-08-26 12:02:01', 'http://www.other.net/path1/index.php?k1=v1&k2=v2#Ref1', 'http://www.example.com/video#ref'          )
  , ('2016-08-26 12:02:01', 'https://www.other.com/'                               , 'http://www.example.com/book/detail?id=002' )
;

SELECT 
	stamp
	, url
	-- URL 경로 또는 GET 매개변수의 id 추출하기
	-- ■ PostgreSQL의 경우 substring 함수와 정규 표현식 사용하기
	, substring(url from '//[^/]+([^?#]+)') AS path
	, substring(url from 'id=([^&]*)') AS id
	-- ■ Redshift의 경우 regexp_substr 함수와 regexp_replace 함수를 조합해서 사용하기
	-- , regexp_replace(regexp_substr(url, '//[^/]+[^?#]+'), '//[^/]+', '') AS path
	-- , regexp_replace(regexp_substr(url, 'id=[^&]*'), 'id=', '') AS id
	-- ■ BigQuery의 경우 정규 표현식과 regexp_extract 함수 사용하기
	-- , regexp_extract(url, '//[^/]+([^?#]+)') AS path
	-- , regexp_extract(url, 'id=([^&]*)') AS id
	-- ■ Hive, SparkSQL의 경우 parse_url 함수로 URL 경로 부분 또는 쿼리 매개변수 부분의 값 추출하기
	-- , parse_url(url, 'PATH') AS path
	-- , parse_url(url, 'QUERY', 'id') AS id
FROM access_log
;
```
```python
-- 문자열을 날짜/타임스탬프로 변환하기
SELECT 
	-- ■ PostgreSQL, Hive, Redshift, BigQuery, SparkSQL 모두 'CAST(value AS type)' 사용하기
	CAST('2016-01-30'AS date) AS dt
	, CAST('2016-01-30 12:00:00' AS timestamp) AS stamp
	
	-- ■ Hive, BigQuery의 경우 'type(value)' 사용하기
	-- date('2016-01-30') AS dt
	--, timestamp('2016-01-30 12:00:00')AS stamp
	
	-- ■ PostgreSQl, Hive, Redshift, BigQuery, SparkSQL 모두 'type value' 사용하기
	-- ※ 다만 value는 상수이므로 컬럼 이름으로 지정 할수 없음
	-- date '2016-01-30' AS dt
	--, timestamp '2016-01-30 12:00:00' AS stamp
	
	-- ■ PostgreSQl, Redshift의 경우 'value::type'사용하기
	-- '2016-01-30'::date AS dt
	--, '2016-01-30 12:00:00'::timestamp AS stamp
;
```
```python
SELECT 	
	stamp
   -- ■ PorstgteSQL, Redshift, BigQuery의 경우 EXTRACT 함수 사용
   , EXTRACT(YEAR FROM stamp) AS year
   , EXTRACT(MONTH FROM stamp) AS month
   , EXTRACT(DAY FROM stamp) AS day
   , EXTRACT(HOUR FROM stamp) AS hour
   
   -- ■ Hive, SparkSQL의 경우 EXTRACT 함수 대신 다음과 같은 함수 사용
   --, YEAR(stamp) AS year
   --, MONTH(stamp) AS month
   --, DAY(stamp) AS day
   --, HOUR(stamp) AS hour
FROM
 (SELECT CAST('2016-01-30 12:00:00' AS timestamp) AS stamp) AS t
;

SELECT 
	stamp 
   -- ■PostgreSQL, Hive, Redshift, SparkSQL에서는 substring함수 사용
   , substring(stamp, 1, 4) AS year
   , substring(stamp, 6, 2) AS month
   , substring(stamp, 9, 2) AS day
   , substring(stamp, 12, 2) AS hour
   -- 연과 월을 함께 추출하기
   , substring(stamp 1, 7) AS year_month
   
    -- ■PostgreSQL, Hive, Redshift, SparkSQL에서는 substr함수 사용
	--, substr(stamp, 1, 4) AS year
	--, substr(stamp, 6, 2) AS month
	--, substr(stamp, 9, 2) AS day
	--, substr(stamp, 12, 2) AS hour
	--, substr(stamp, 1, 7) AS year_month
FROM
	-- ■PostgreSQL,Redshift의 경우 문자열 자료형으로 text 사용
	(SELECT CAST('2016-01-30 12:00:00' AS text) AS stamp) AS t
	-- ■Hive, BigQuery, SparkSQL의 경우 문자열 자료형으로 string 사용
	-- (SELECT CAST('2016-01-30 12:00:00' AS string) AS stamp) AS t
;
```
```python
DROP TABLE IF EXISTS access_log ;
CREATE TABLE access_log (
    stamp    varchar(255)
  , referrer text
  , url      text
);

INSERT INTO access_log 
VALUES
    ('2016-08-26 12:02:00', 'http://www.other.com/path1/index.php?k1=v1&k2=v2#Ref1', 'http://www.example.com/video/detail?id=001')
  , ('2016-08-26 12:02:01', 'http://www.other.net/path1/index.php?k1=v1&k2=v2#Ref1', 'http://www.example.com/video#ref'          )
  , ('2016-08-26 12:02:01', 'https://www.other.com/'                               , 'http://www.example.com/book/detail?id=002' )
;

SELECT 
	purchase_id
  , amount
  , coupon
  , amount - coupon AS discount_amount1
  , amount - COALESCE(coupon, 0) AS discount_amount2
FROM 
	purchase_log_with_coupon
;


DROP TABLE IF EXISTS mst_user_location;
CREATE TABLE mst_user_location (
    user_id   varchar(255)
  , pref_name varchar(255)
  , city_name varchar(255)
);

INSERT INTO mst_user_location
VALUES
    ('U001', '서울특별시', '강서구')
  , ('U002', '경기도수원시', '장안구'  )
  , ('U003', '제주특별자치도', '서귀포시')
;

SELECT 
	user_id
	-- ■ PostgreSQL, Hive, Redshift, BigQuery, SparkSQL 모두 CONCAT 함수 사용 가능
	-- 다만 Redshift의 경우는 매개변수를 2개 밖에 못 받음
   , CONCAT(pref_name, city_name) AS pref_city
    -- ■ PostgreSQL, Redshift의 경우는 || 연산자도 사용 가능
	--, pref_name || city_name AS pref_city
FROM 
	mst_user_location
;


DROP TABLE IF EXISTS quarterly_sales;
CREATE TABLE quarterly_sales (
    year integer
  , q1   integer
  , q2   integer
  , q3   integer
  , q4   integer
);

INSERT INTO quarterly_sales
VALUES
    (2015, 82000, 83000, 78000, 83000)
  , (2016, 85000, 85000, 80000, 81000)
  , (2017, 92000, 81000, NULL , NULL )
;

SELECT 
	year
  , q1
  , q2
  	-- Q1과 Q2의 매출 변화 평가하기
  , CASE
  	 WHEN q1 < q2 THEN '+'
	 WHEN q1 = q2 THEN ' '
	 ELSE '-'
   END AS judge_q1_q2
   -- Q1과 Q2의 매출액의 차이 계산하기
  , q2 - q1 AS diff_q2_q1
   -- Q1과 Q2의 매출 변화를 1, 0, -1로 표현하기
  , SIGN(q2 - q1)  AS sign_q2_q1
FROM
 quarterly_sales
ORDER BY
 year
;
```
```python
DROP TABLE IF EXISTS quarterly_sales;
CREATE TABLE quarterly_sales (
    year integer
  , q1   integer
  , q2   integer
  , q3   integer
  , q4   integer
);

INSERT INTO quarterly_sales
VALUES
    (2015, 82000, 83000, 78000, 83000)
  , (2016, 85000, 85000, 80000, 81000)
  , (2017, 92000, 81000, NULL , NULL )
;

SELECT 
	year
  , q1
  , q2
    -- Q1과 Q2의 매출 변화 평가하기
  , CASE
    WHEN q1 < q2 THEN '+'
	WHEN q1 = q2 THEN ' '
	ELSE '-'
  END AS judge_q1_q2
  -- Q1과 Q2의 매출액의 차이 계산하기
  , q2 - q1 AS diff_q2_q2
  -- Q1과 Q2의 매출 변화를 1, 0, -1로 표현하기
  , SIGN(q2-q1) AS sign_q2_q1
FROM 
 quarterly_sales
ORDER BY
 year
;

SELECT
	year
	-- Q1~Q4의 최대 매출 구하기
  , greatest(q1, q2, q3, q4) AS greatest_sales
    -- Q1~Q4의 최소 매출 구하기
  , least(q1, q2, q3, q4)    AS least_sales
FROM
 quarterly_sales
ORDER BY
 year
;	

SELECT 
	year
  , (q1 + q2 + q3 + q4) / 4 AS average
FROM 
 quarterly_sales
ORDER BY
 year
;	

SELECT 
	year
  , (COALESCE(q1, 0) + COALESCE(q2, 0) + COALESCE(q3, 0) + COALESCE(q4, 0)) / 4
   AS average
FROM 
 quarterly_sales
ORDER BY
 year
;	

SELECT 
	year
  , (COALESCE(q1, 0) + COALESCE(q2, 0) + COALESCE(q3, 0) + COALESCE(q4, 0))
    / (SIGN(COALESCE(q1, 0)) + (SIGN(COALESCE(q2, 0)) + (SIGN(COALESCE(q3, 0)) + (SIGN(COALESCE(q4, 0))))))
AS average
FROM 
 quarterly_sales
ORDER BY
 year
;	
```
```python
DROP TABLE IF EXISTS advertising_stats;
CREATE TABLE advertising_stats (
    dt          varchar(255)
  , ad_id       varchar(255)
  , impressions integer
  , clicks      integer
);

INSERT INTO advertising_stats
VALUES
    ('2017-04-01', '001', 100000,  3000)
  , ('2017-04-01', '002', 120000,  1200)
  , ('2017-04-01', '003', 500000, 10000)
  , ('2017-04-02', '001',      0,     0)
  , ('2017-04-02', '002', 130000,  1400)
  , ('2017-04-02', '003', 620000, 15000)
;

SELECT
   dt
 , ad_id
 
   -- ■ Hive, Redshift, BigQuery, SparkSQL의 경우
   -- 정수를 나눌 때는 자동적으로 실수로 변환
 , clicks / impressions AS ctr
   -- ■ PorstgreSQL의 경우 정수를 나누면 소수점이 잘리므로 명시적으로 자료형 변환
   -- , CAST(clicks AS double precision) / impressions AS ctr
   -- 실수를 상수로 앞에 두고 계산하면 암묵적으로 자료형 변환이 일어남
 , 100.0 * clicks / impressions AS ctr_as_percent
 FROM 
 advertising_stats
 WHERE 
 dt = '2017-04-01'
 ORDER BY
 dt, ad_id
;

SELECT 
   dt
 , ad_id
   -- CASE 식으로 분모가 0일 경우를 분기해서, 0으로 나누지 않게 만드는 방법
 , CASE
    WHEN impressions > 0 THEN 100.0 * clicks / impressions
   END AS ctr_as_percent_by_case
   
   -- 분모가 0이라면 NULL로 변환해서, 0으로 나누지 않게 만드는 방법
   -- ■ PorstgreSQL, Redshift, BigQuery, SparkSQL의 경우 NULLIF 함수 사용하기
 , 100.0 * clicks / NULLIF(impressions, 0) AS ctr_as_percent_by_null
   -- ■ Hive의 경우 NULLIF 대신 CASE 식 사용하기
   -- , 100.0 * clicks
   --   / CASE WHEN impressions = 0 THEN NULL ELSE impressions END
   --   AS ctr_as_percent_by_null
 FROM 
 advertising_stats
 ORDER BY
 dt, ad_id
;
```
```python
DROP TABLE IF EXISTS location_1d;
CREATE TABLE location_1d (
    x1 integer
  , x2 integer
);

INSERT INTO location_1d
VALUES
    ( 5 , 10)
  , (10 ,  5)
  , (-2 ,  4)
  , ( 3 ,  3)
  , ( 0 ,  1)
;

DROP TABLE IF EXISTS location_2d;
CREATE TABLE location_2d (
    x1 integer
  , y1 integer
  , x2 integer
  , y2 integer
);

INSERT INTO location_2d
VALUES
    (0, 0, 2, 2)
  , (3, 5, 1, 2)
  , (5, 3, 2, 1)
;

SELECT
 abs(x1 - x2) AS abs
 , sqrt(power(x1 - x2, 2)) AS rms
FROM location_1d
;

DROP TABLE IF EXISTS mst_users_with_dates;
CREATE TABLE mst_users_with_dates (
    user_id        varchar(255)
  , register_stamp varchar(255)
  , birth_date     varchar(255)
);

INSERT INTO mst_users_with_dates
VALUES
    ('U001', '2016-02-28 10:00:00', '2000-02-29')
  , ('U002', '2016-02-29 10:00:00', '2000-02-29')
  , ('U003', '2016-03-01 10:00:00', '2000-02-29')
;

SELECT 
   sqrt(power(x1 - x2, 2) + power(y1 - y2, 2)) AS dist
   -- ■ PostgreSQL의 경우 point 자료형과 거리 연산자 <-> 사용하기
   -- , point(x1,y1) <-> point(x2,y2) AS dist
FROM location_2d
;
```
```python
DROP TABLE IF EXISTS mst_users_with_dates;
CREATE TABLE mst_users_with_dates (
    user_id        varchar(255)
  , register_stamp varchar(255)
  , birth_date     varchar(255)
);

INSERT INTO mst_users_with_dates
VALUES
    ('U001', '2016-02-28 10:00:00', '2000-02-29')
  , ('U002', '2016-02-29 10:00:00', '2000-02-29')
  , ('U003', '2016-03-01 10:00:00', '2000-02-29')
;

SELECT 
   user_id
  --■ PostgreSQL의 경우 interval 자료형의 데이터에 사칙 연산 적용하기
  , register_stamp::timestamp AS register_stamp
  , register_stamp::timestamp + '1 hour'::interval    AS after_1hour
  , register_stamp::timestamp - '30 minutes'::interval AS before_30_minutes
  
  
  , register_stamp::date AS register_date
  , (register_stamp::date + '1 day'::interval  )::date AS after_1_day
  , (register_stamp::date - '1 month'::interval)::date AS before_1_month
  
  
  --■ Redshift의 경우 dateadd 함수 사용하기
  --, register_stamp::timestamp AS register_stamp
  --, dateadd(hour, 1, register_stamp::timestamp) AS after_1_hour
  --, dateadd(minute, -30, register_stamp::timestamp) AS before_30_minutes
  --
  --, register_stamp::date AS register_date
  --, dateadd(day, 1, register_stamp::date) AS after_1_day
  --, dateadd(month, -1, register_stamp::date) AS before_1_month
  
  --■ BigQuery의 경우 timestamp_add/sub, date_add/sub 등의 함수 사용하기
  --, timestamp(register_stamp) AS register_stamp
  --, timestamp(timestamp(register_stamp), interval 1 hour) AS after_1_hour
  --, timestamp(timestamp(register_stamp), interval 30 minute) AS before_30_minutes
  --
  -- 타임스탬프 문자열을 기반으로 직접 날짜 계산을 할 수 없으므로 타임스탬프 자료형을 날짜/시간
  -- 자료형으로 변환한 뒤 계산하기
  --, date(timestamp(register_stamp)) AS register_date
  --, date_add(date(timestamp(register_stamp)), interval 1 day) AS after_1_day
  --, date_add(date(timestamp(register_stamp)), interval 1 month) AS before_1_month
  
  --■ Hive, SparkSQL의 경우 날짜/시각을 계산하기 함수가 제공되지 않으므로
  -- 한번 unixtime으로 변환하고 초 단위로 계산을 적용한 뒤 다시 타임스탬프로 변환하기
  --, CAST(register_stamp AS timestamp) AS register_stamp
  --, from_unixtime(unix_timestamp(register_stamp)+60*60) AS after_1_hour
  --, from_unixtime(unix_timestamp(register_stamp)-30*60) AS before_30_minutes
  --
  -- 타임스탬프 문자열을 날짜로 변환할 때는  to_date 함수 사용하기
  -- ※ 다만 Hive 2.1.0 이전 버전에서는  문자열 자료형으로 리턴함
  --, to_date(register_stamp) AS register_date
  --
  -- 일과 월을 계산할 때는 date_add 함수와 add_months 함수 사용하기
  -- 다만 연을 계산하는 함수는 구현되어 있지 않음
  --, date_add(to_date(register_stamp), 1) AS after_1_day
  --, add_month(to_date(register_stamp), -1) AS before_1_month
FROM mst_users_with_dates
;
```
```python
SELECT 
  user_id
 
 
 -- ■ PostgreSQL, Redshift의 경우 날짜 자료형끼리 뺄 수 있음
 , CURRENT_DATE AS today
 , register_stamp::date AS register_date
 , CURRENT_DATE - register_stamp::date AS diff_days
 
 
 -- ■ BigQuery의 경우 date_diff 함수 사용하기
 --, CURRENT_DATE AS today
 --, date(timestamp(register_stamp)) AS register_date
 --, date_diff(CURRENT_DATE, date(timestamp(register_stamp)), day) AS diff_days
 
 
 -- ■ Hive, SparkSQL의 경우 datediff 함수 사용하기
 --, CURRENT_DATE() AS today
 --, to_date(register_stamp) AS register_date
 --, datediff(CURRENT_DATE(), to_date(register_stmap)) AS diff_days
FROM mst_users_with_dates
;

SELECT 
   user_id
  
 -- ■ PostgreSQL의 경우 age 함수와 EXTRACT 함수를 사용해 나이 집계하기
 , CURRENT_DATE AS today
 , register_stamp::date AS register_date
 , birth_date::date AS birth_date
 , EXTRACT(YEAR FROM age(birth_date::date)) AS current_age
 , EXTRACT(YEAR FROM age(register_stamp::date, birth_date::date)) AS register_age
FROM mst_users_with_dates
;

SELECT 
   user_id
   
 -- ■ Redshift의 경우 datediff 함수로 yesr을 지정하더라도, 연 부분에서의 차이를 계산할 수 없음
 , CURRENT_DATE AS today
 , register_stamp::date AS register_date
 , birth_date::date AS birth_date
 , datediff(year, birth_date::date, CURRENT_DATE)
 , datediff(year, bireh_date::date, register_stamp::date)
 
 -- ■ BigQuery의 경우 date_diff 함수로 year을 지정하더라도, 연 부분에서의 차이를 계산할 수 없음
 --, CURRENT_DATE AS today
 --, date(timestmap(register_stamp)) AS register_date
 --, date(timestmap(birth_date)) AS birth_date
 --, date_diff(CURRENT_DATE, date(timestmap(birth_date)), year) AS current_age
 --, date_diff(date(timestamp(register_stamp)), date(timestamp(birth_date)), year)
      AS register_age
FROM mst_users_with_dates
;
```
```python
-- 생일이 2000년 2월 29일인 사람의 2016년 2월 28일 시점의 나이 계산하기
SELECT floor((20160228 - 20000229) / 10000) AS age;


SELECT 
   user_id
 , substring(register_stamp, 1, 10) AS register_date
 , birth_date
  -- 등록 시점의 나이 계산하기
 , floor(
    ( CAST(replace(substring(register_stamp, 1, 10), '-', '') AS integer)
	  - CAST(replace(birth_date, '-', '') AS integer)
	) / 10000
   ) AS register_age
   -- 현재 시점의 나이 계산하기
 , floor(
   (CAST(replace(CAST(CURRENT_DATE AS text), '-', '') AS integer)
    - CAST(replace(birth_date, '-', '') AS integer)  
    ) / 10000
   ) AS current_age
   
   
   -- ■ BigQuery의 경우 text를 string, integer를 int64로 바꾸자
   -- (CAST(replace(CAST(CURRENT_DATE AS string), '-', '') AS int64)
   --  - CAST(replace(birth_date, '-', '') AS int64)
   -- ) / 10000
   
   
   -- ■ Hive, SparkSQL의 경우 replace를 regexp_replace, text를 string,
   -- integer를 int로 바꾸기
   -- SparkSQL의 경우는 추가로 CURRENT_DATE를 CURRENT_DATE()로 바꾸기
   -- (CAST(regexp_replace(CAST(CURRENT_DATE() AS string), '-', '') AS int)
   --  - CAST(regexp_replace(birth_date, '-', '') AS int)
   -- ) / 10000
FROM mst_users_with_dates
;
```
