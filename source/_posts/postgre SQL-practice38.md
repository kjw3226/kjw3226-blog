---
title: postgre SQL-practice38
tag: postgre SQL-practice38
date: 2022-03-21
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'6장  14강 사이트 전체의 특징/경향 찾기

3. 유입원별로 방문 횟수 또는 CVR 집계하기'

페이지 332 ~ 338을 보고 쿼리문을 작성하였다.

유입원별로 방문 횟수를 집계하는 쿼리문
```python
WITH
access_log_with_parse_info AS (
 -- 유입원 정보 추출하기
 SELECT *
  -- ■ PostgreSQL의 경우 정규 표현식으로 유입원 정보 추출하기
  , substring(url from 'http?://([^/])') AS url_domain
  , substring(url from 'utm_source=([^&]*)') AS url_utm_source
  , substring(url from 'utm_medium=([^&]*)') AS url_utm_medium
  , substring(referrer from 'http?://([^/]*)') AS referrer_domain
  -- ■ Redshift의 경우 regexp_substr 함수와 regexp_replace 함수를 조합해서 사용하기
  --, regexp_replace(regexp_substr(url, 'http?://[^/]*'), 'https?://', '')
  --  AS url_domain
  --, regexp_replace(regexp_substr(url, 'utm_source=[^&]*'), 'utm_source=', '')
  --, AS url_utm_source
  --, regexp_replace(regexp_substr(url, 'utm_medium=[^&]*'), 'utm_medium=', '')
  --, regexp_replace(regexp_substr(referrer, 'http?://[^/]*'), 'https?://','')
  --  AS referrer_domain
  -- ■ BigQuery의 경우 정규 표현식 regexp_extract사용하기
  --, regexp_extract(url, 'https?://([^/]*)') AS url_domain
  --, regexp_extract(url,  'utm_source=([^&]*)') AS url_utm_source
  --, regexp_extract(url,  'utm_medium=([^&]*)') AS url_utm_medium
  --, regexp_extract(referrer,  'https?://([^/]*)') AS referrer_domain
  -- ■ Hive,SparkSQL의 경우 parse_url 함수로 URL의 내용 추출하기
  --, parse_url(url, 'HOST') AS url_domain
  --, parse_url(url, 'QUERY', 'utm_source') AS url_utm_source
  --, parse_url(url, 'QUERY', 'utm_medium') AS url_utm_medium
  --, parse_url(referrer, 'HOST') AS referrer_domain
 FROM access_log
)
, access_log_with_via_info AS (
  SELECT *
   , ROW_NUMBER() OVER(ORDER BY stamp) AS log_id
   , CASE
	  WHEN url_utm_source <> '' AND url_utm_medium <> ''
	   --■ PostgreSQL, Hive, BigQuery, SparkSQl의 경우 concat 함수에 여러 매개변수 사용 가능
	   THEN concat(url_utm_source, '-', url_utm_medium)
	   --■ PostgreSQL, Redshift의 경우 문자열 결합에 || 연사자 사용 가능
	   -- THEN url_utm_source || '-' || url_utm_medium
	  WHEN referrer_domain IN ('search.yahoo.co.jp', 'www.google.co.jp') THEN 'search'
	  WHEN referrer_domain IN ('twitter.com', 'www.facebook.com') THEN 'social'
	  ELSE 'other'
	  -- ELSE referrer_domain로 변경하면 도메인별로 집계 가능
   END AS via
  FROM access_log_with_parse_info
  -- 레퍼러가 없는 경우와 우리 사이트 도메인의 경우는 제외
  WHERE COALESCE(referrer_domain, '') NOT IN ('', url_domain)
)
SELECT via, COUNT(1) AS access_count
FROM access_log_with_via_info
GROUP BY via
ORDER BY access_count DESC;
```

각 방문에서 구매한 비율(CVR)을 집계하는 쿼리문
```python
WITH
access_log_with_parse_info AS (
 -- 유입원 정보 추출하기
 SELECT *
  -- ■ PostgreSQL의 경우 정규 표현식으로 유입원 정보 추출하기
  , substring(url from 'http?://([^/])') AS url_domain
  , substring(url from 'utm_source=([^&]*)') AS url_utm_source
  , substring(url from 'utm_medium=([^&]*)') AS url_utm_medium
  , substring(referrer from 'http?://([^/]*)') AS referrer_domain
  -- ■ Redshift의 경우 regexp_substr 함수와 regexp_replace 함수를 조합해서 사용하기
  --, regexp_replace(regexp_substr(url, 'http?://[^/]*'), 'https?://', '')
  --  AS url_domain
  --, regexp_replace(regexp_substr(url, 'utm_source=[^&]*'), 'utm_source=', '')
  --, AS url_utm_source
  --, regexp_replace(regexp_substr(url, 'utm_medium=[^&]*'), 'utm_medium=', '')
  --, regexp_replace(regexp_substr(referrer, 'http?://[^/]*'), 'https?://','')
  --  AS referrer_domain
  -- ■ BigQuery의 경우 정규 표현식 regexp_extract사용하기
  --, regexp_extract(url, 'https?://([^/]*)') AS url_domain
  --, regexp_extract(url,  'utm_source=([^&]*)') AS url_utm_source
  --, regexp_extract(url,  'utm_medium=([^&]*)') AS url_utm_medium
  --, regexp_extract(referrer,  'https?://([^/]*)') AS referrer_domain
  -- ■ Hive,SparkSQL의 경우 parse_url 함수로 URL의 내용 추출하기
  --, parse_url(url, 'HOST') AS url_domain
  --, parse_url(url, 'QUERY', 'utm_source') AS url_utm_source
  --, parse_url(url, 'QUERY', 'utm_medium') AS url_utm_medium
  --, parse_url(referrer, 'HOST') AS referrer_domain
 FROM access_log
)
, access_log_with_via_info AS (
  SELECT *
   , ROW_NUMBER() OVER(ORDER BY stamp) AS log_id
   , CASE
	  WHEN url_utm_source <> '' AND url_utm_medium <> ''
	   --■ PostgreSQL, Hive, BigQuery, SparkSQl의 경우 concat 함수에 여러 매개변수 사용 가능
	   THEN concat(url_utm_source, '-', url_utm_medium)
	   --■ PostgreSQL, Redshift의 경우 문자열 결합에 || 연사자 사용 가능
	   -- THEN url_utm_source || '-' || url_utm_medium
	  WHEN referrer_domain IN ('search.yahoo.co.jp', 'www.google.co.jp') THEN 'search'
	  WHEN referrer_domain IN ('twitter.com', 'www.facebook.com') THEN 'social'
	  ELSE 'other'
	  -- ELSE referrer_domain로 변경하면 도메인별로 집계 가능
   END AS via
  FROM access_log_with_parse_info
  -- 레퍼러가 없는 경우와 우리 사이트 도메인의 경우는 제외
  WHERE COALESCE(referrer_domain, '') NOT IN ('', url_domain)
)
, access_log_with_purchase_amount AS (
 SELECT
	a.log_id
  , a.via
  , SUM(
	  CASE
	    -- ■ PostgreSQL의 경우 interval 자료형의 데이터로 날짜와 시간 사칙연산 가능
	    WHEN p.stamp::date BETWEEN a.stamp::date AND a.stamp::date + '1day'::interval
	    -- ■ Redshift의 경우 dateadd 함수 사용하기
	    -- WHEN p.stamp::date BETWEEN a.stamp::date AND dateadd(day, 1, a.stamp::date)
        -- ■ BigQuery의 경우 date_add 함수 사용하기
	    -- WHEN date(timestamp(p.stamp))
	    --   BETWEEN date(timestamp(a.stamp))
	    --     AND date_add(date(timestamp(a.stamp)), interval 1 day)
	    -- ■ Hive, SparkSQL의 경우 date_add 함수 사용하기
	    -- ※ BigQuery의 경우는 서식이 조금 다름
	    -- WHEN to_date(p.stamp)
	    --  BETWEEN to_date(a.stamp) AND date_add(to_date(a.stamp), 1)
	      THEN amount
	    END
	  ) AS amount
 FROM
	access_log_with_via_info AS a
  LEFT OUTER JOIN  
   purchase_log AS p
   ON a.long_session = p.long_session
 GROUP BY a.log_id, a.via
)
SELECT
   via
 , COUNT(1) AS via_count
 , COUNT(amount) AS conversions
 , AVG(100.0*SIGN(COALESCE(amount, 0))) AS cvr
 , SUM(COALESCE(amount, 0)) AS amount
 , AVG(1.0*(COALESCE(amount, 0)) AS avg_amount
FROM
 access_log_with_purchase_amount
GROUP BY via
ORDER BY cvr DESC
;
```
앞의 결과를 사용하면, 어떤 유입 경로에 더 신경써야 하는지 등을 

판단할 수 있습니다.

추가로 극단적으로 유입이 낮은 경로는 원인을 찾아내 해결하고,

비용이 너무 많이 지출되는 경우라면 경로 자체를 제거하는 등의

판단을 내리도록 합시다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 14강 페이지 338 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어