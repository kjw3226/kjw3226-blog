---
title: postgre SQL-practice57
tag: postgre SQL-practice57
date: 2022-04-09
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'7장  18강 이상값 검출하기'의

'4. 특정 IP 주소에서의 접근 제외하기'로 넘어갔으며

페이지 431 ~ 439을 참고하였다.

예약 IP 주소를 정의한 마스터 테이블
```python
WITH
mst_reserved_ip AS (
	       SELECT '127.0.0.0/8'     AS network,  'localhost'       AS description
 UNION ALL SELECT '10.0.0.0/8'      AS network,  'Private network' AS description
 UNION ALL SELECT '172.16.0.0/12'   AS network,  'Private network' AS description
 UNION ALL SELECT '192.0.0.0/24'    AS network,  'Private network' AS description
 UNION ALL SELECT '192.168.0.0/16'  AS network,  'Private network' AS description
)
SELECT *
FROM mst_reserved_ip
;
```

inet 자료형을 사용해 IP 주소를 판정하는 쿼리문
```python
WITH
mst_reserved_ip AS (
	       SELECT '127.0.0.0/8'     AS network,  'localhost'       AS description
 UNION ALL SELECT '10.0.0.0/8'      AS network,  'Private network' AS description
 UNION ALL SELECT '172.16.0.0/12'   AS network,  'Private network' AS description
 UNION ALL SELECT '192.0.0.0/24'    AS network,  'Private network' AS description
 UNION ALL SELECT '192.168.0.0/16'  AS network,  'Private network' AS description
)
, action_log_with_reserved_ip AS (
  SELECT
	 l.user_id
   , l.ip
   , l.stamp
   , m.network
   , m.description
  FROM
	 action_log_with_ip AS l
   LEFT JOIN
	mst_reserved_ip AS m
   ON l.ip::inet<<m.network::inet
)
SELECT *
FROM action_log_with_reserved_ip;
```

예약 IP 주소의 로그를 제외하는 쿼리문
```python
WITH
mst_reserved_ip AS (
	       SELECT '127.0.0.0/8'     AS network,  'localhost'       AS description
 UNION ALL SELECT '10.0.0.0/8'      AS network,  'Private network' AS description
 UNION ALL SELECT '172.16.0.0/12'   AS network,  'Private network' AS description
 UNION ALL SELECT '192.0.0.0/24'    AS network,  'Private network' AS description
 UNION ALL SELECT '192.168.0.0/16'  AS network,  'Private network' AS description
)
, action_log_with_reserved_ip AS (
  SELECT
	 l.user_id
   , l.ip
   , l.stamp
   , m.network
   , m.description
  FROM
	 action_log_with_ip AS l
   LEFT JOIN
	mst_reserved_ip AS m
   ON l.ip::inet<<m.network::inet
)
SELECT *
FROM action_log_with_reserved_ip
WHERE network IS NULL;
```

네트워크 범위를 나타내는 처음과 끝 IP 주소를 부여하는 쿼리문
```python
WITH
mst_reserved_ip_with_range AS (
 -- 마스터 테이블에 네트워크 범위에 해당하는 IP 주소의 최솟값과 최댓값 추가하기
   SELECT '127.0.0.0/8'        AS network
        , '127.0.0.0'          AS network_start_ip
	    , '127.255.255.255'    AS network_last_ip
	    , 'localhost'          AS description
   UNION ALL
	 SELECT '10.0.0.0/8'       AS network
	      , '10.0.0.0'         AS network_start_ip
	      , '10.255.255.255'   AS network_last_ip
	      , 'Private network'  AS description
   UNION ALL
	 SELECT '172.16.0.0/12'    AS network
	      , '172.16.0.0'       AS network_start_ip
	      , '172.31.255.255'   AS network_last_ip
	      , 'Private network'  AS description
   UNION ALL
     SELECT '192.0.0.0/24'     AS network
	      , '192.0.0.0'        AS network_start_ip
	      , '192.0.0.255'      AS network_last_ip
	      , 'Private network'  AS description
   UNION ALL
	 SELECT '192.168.0.0/16'   AS network
	      , '192.168.0.0'      AS network_start_ip
	      , '192.168.255.255'  AS network_last_ip
	      , 'Private network'  AS description
)
SELECT *
FROM mst_reserved_ip_with_range;
```

IP 주소를 0으로 메운 문자열로 변환하고, 특정 IP 로그를 배제하는 쿼리문
```python
WITH
mst_reserved_ip_with_range AS (
 -- 마스터 테이블에 네트워크 범위에 해당하는 IP 주소의 최솟값과 최댓값 추가하기
   SELECT '127.0.0.0/8'        AS network
        , '127.0.0.0'          AS network_start_ip
	    , '127.255.255.255'    AS network_last_ip
	    , 'localhost'          AS description
   UNION ALL
	 SELECT '10.0.0.0/8'       AS network
	      , '10.0.0.0'         AS network_start_ip
	      , '10.255.255.255'   AS network_last_ip
	      , 'Private network'  AS description
   UNION ALL
	 SELECT '172.16.0.0/12'    AS network
	      , '172.16.0.0'       AS network_start_ip
	      , '172.31.255.255'   AS network_last_ip
	      , 'Private network'  AS description
   UNION ALL
     SELECT '192.0.0.0/24'     AS network
	      , '192.0.0.0'        AS network_start_ip
	      , '192.0.0.255'      AS network_last_ip
	      , 'Private network'  AS description
   UNION ALL
	 SELECT '192.168.0.0/16'   AS network
	      , '192.168.0.0'      AS network_start_ip
	      , '192.168.255.255'  AS network_last_ip
	      , 'Private network'  AS description
)
, action_log_with_ip_varchar AS (
  -- 액션 로그의 IP 주소를 0으로 메운 문자열로 표현하기
  SELECT
	 *
   --■PostgreSQL, Redshif의 경우 lpad 함수로 0 메우기
   ,   lpad(split_part(ip,'.',1), 3, '0')
	 ||lpad(split_part(ip,'.',2), 3, '0')
	 ||lpad(split_part(ip,'.',3), 3, '0')
	 ||lpad(split_part(ip,'.',4), 3, '0')
	 AS ip_varchar
	
   --■BigQuery의 경우 split 함수를 사용해 배열로 분해하고 n번째 요소 추출하기
   --, CONCAT(
   --    lpad(split(ip, '.')[SAFE_ORDINAL(1)], 3, '0')
   --  , lpad(split(ip, '.')[SAFE_ORDINAL(2)], 3, '0')
   --  , lpad(split(ip, '.')[SAFE_ORDINAL(3)], 3, '0')
   --  , lpad(split(ip, '.')[SAFE_ORDINAL(4)], 3, '0')
   --) AS ip_varchar
	
   --■Hive, SparkSQL의 경우 split 함수로 배열로 분해하고 n번째 요소 추출하기
   --다만 콜론(마침표)은 측수 문자이므로 역슬래시로 이스케이프 처리해야 함
   --, CONCAT(
   --    lpad(split(ip, '\\.')[0], 3, '0')
   --  , lpad(split(ip, '\\.')[1], 3, '0')
   --  , lpad(split(ip, '\\.')[2], 3, '0')
   --  , lpad(split(ip, '\\.')[3], 3, '0')
   --) AS ip_varchar
  FROM
	action_log_with_ip
)
, mst_reserved_ip_with_varchar_range AS (
  -- 마스터 테이블의 IP 주소를 0으로 메운 문자열로 표현하기
  SELECT
	 *
	--■PostgreSQL, Redshift의 경우 lpad 함수로 0 메우기
	,  lpad(split_part(network_start_ip, '.', 1), 3, '0')
	 ||lpad(split_part(network_start_ip, '.', 2), 3, '0')
	 ||lpad(split_part(network_start_ip, '.', 3), 3, '0')
	 ||lpad(split_part(network_start_ip, '.', 4), 3, '0')
	AS network_start_ip_varchar
  ,    lpad(split_part(network_last_ip, '.', 1), 3, '0')
	 ||lpad(split_part(network_last_ip, '.', 2), 3, '0')
	 ||lpad(split_part(network_last_ip, '.', 3), 3, '0')
	 ||lpad(split_part(network_last_ip, '.', 4), 3, '0')
	AS network_last_ip_varchar
	
	
   --■BigQuery의 경우 split 함수를 사용해 배열로 분해하고 n번째 요소 추출하기
   --, CONCAT(
   --   lpad(split(network_start_ip, '.')[SAFE_ORDINAL(1)], 3, '0')
   -- , lpad(split(network_start_ip, '.')[SAFE_ORDINAL(2)], 3, '0')
   -- , lpad(split(network_start_ip, '.')[SAFE_ORDINAL(3)], 3, '0')
   -- , lpad(split(network_start_ip, '.')[SAFE_ORDINAL(4)], 3, '0')
   --) AS network_start_ip_varchar
   --, CONCAT(
   --   lpad(split(network_last_ip, '.')[SAFE_ORDINAL(1)], 3, '0')
   -- , lpad(split(network_last_ip, '.')[SAFE_ORDINAL(2)], 3, '0')
   -- , lpad(split(network_last_ip, '.')[SAFE_ORDINAL(3)], 3, '0')
   -- , lpad(split(network_last_ip, '.')[SAFE_ORDINAL(4)], 3, '0')
   --) AS network_last_ip_varchar
	
   --■Hive, SparkSQL의 경우 split 함수를 사용해 배열로 분해하고 n번째 요소 추출하기
   -- 다만 콜론(마침표)은 특수 문자이므로 역슬래시로 이스케이프 처리해야 함
   --, CONCAT(
   --   lpad(split(network_start_ip, '\\.')[0], 3, '0')
   -- , lpad(split(network_start_ip, '\\.')[1], 3, '0')
   -- , lpad(split(network_start_ip, '\\.')[2], 3, '0')
   -- , lpad(split(network_start_ip, '\\.')[3], 3, '0')
   --) AS network_start_ip_varchar
   --, CONCAT(
   --   lpad(split(network_last_ip, '\\.')[0], 3, '0')
   -- , lpad(split(network_last_ip, '\\.')[1], 3, '0')
   -- , lpad(split(network_last_ip, '\\.')[2], 3, '0')
   -- , lpad(split(network_last_ip, '\\.')[3], 3, '0')
   --) AS network_last_ip_varchar
 FROM
  mst_reserved_ip_with_range
)
-- 0으로 메운 문자열로 표현한 IP 주소로, 네트워크 범위를 포함되는지 판정하기
SELECT
   l.user_id
 , l.ip
 , l.ip_varchar
 , l.stamp
FROM
   action_log_with_ip_varchar AS l
  CROSS JOIN
   mst_reserved_ip_with_varchar_range AS m
GROUP BY
l.user_id, l.ip, l.ip_varchar, l.stamp
-- 예약된 IP 주소 마스터에 포함되지 않은 IP 로그만 HAVING 구문으로 추출하기
HAVING
  SUM(CASE WHEN l.ip_varchar
	BETWEEN m.network_start_ip_varchar AND m.network_last_ip_varchar
    THEN 1 ELSE 0 END) = 0
;
```

IP 주소를 대소비교 가능한 형식으로 변환하는 처리를 쿼리에서 반복해

실행하면 비용이 굉장히 많이 듭니다. 따라서 처음부터 원래 IP 주소와

변환된 IP 주소를 모두 저장하고 사용하는 것이 좋습니다.

(데이터 분석을 위한 SQL 레시피-7장 데이터 활용의

정밀도를 높이는 분석 기술 18강 이상값 검출하기 439 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어