---
title: postgre SQL-practice2
tag: postgre SQL-practice2
date: 2022-02-04
categories:	SQL
----
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

오늘은 '데이터 분석을 위하 SQL 레시피'를

보고 기재되어 있는 예제 코드로 실습을 했다.

아래의 쿼리들은 

'ip' 주소를 다룰 때 사용되는 쿼리들이다.

'inet' 자료형을 사용한 ip 주소 비교 쿼리
```python
SELECT 
   cast('127.0.0.1' AS inet) < cast('127.0.0.2' AS inet)AS lt
 , cast('127.0.0.1' AS inet) < cast('192.168.0.1' AS inet) AS gt
;
```
'inet' 자료형을 사용해 ip 주소 범위를 다루는 쿼리
```python
SELECT CAST('127.0.0.1' AS inet) << CAST('127.0.0.0/8' AS inet) AS is_contained;
```
ip 주소에서 4개의 10진수 부분을 추출하는 쿼리
```python
SELECT 
   ip
  -- ■ PostgreSQL, Redshift의 경우 split_part로 문자열 분해하기
  , CAST(split_part(ip,'.',1) AS integer) AS ip_part_1
  , CAST(split_part(ip,'.',2) AS integer) AS ip_part_2
  , CAST(split_part(ip,'.',3) AS integer) AS ip_part_3
  , CAST(split_part(ip,'.',4) AS integer) AS ip_part_4
  
  -- ■ BigQuery의 경우 split 함수로 배열로 분해하고 n번째 추출하기
  --, CAST(split(ip,'.')[SAFE_ORDINAL(1)] AS int64) AS ip_part_1
  --, CAST(split(ip,'.')[SAFE_ORDINAL(2)] AS int64) AS ip_part_2
  --, CAST(split(ip,'.')[SAFE_ORDINAL(3)] AS int64) AS ip_part_3
  --, CAST(split(ip,'.')[SAFE_ORDINAL(4)] AS int64) AS ip_part_4
  
  -- ■ Hive, SparkSQL의 경우 split 함수로 배열하고 n번째 요소 추출하기
  -- 이때 피리어드(점)가 특수 문자이므로 역 슬래시로 이스케이프 처리해야 함
  --, CAST(split(ip,'\\.')[0] AS int) AS ip_part_1
  --, CAST(split(ip,'\\.')[1] AS int) AS ip_part_2
  --, CAST(split(ip,'\\.')[2] AS int) AS ip_part_3
  --, CAST(split(ip,'\\.')[3] AS int) AS ip_part_4
FROM
  (SELECT '192.168.0.1' AS ip) AS t
  -- ■ PostgreSQL의 경우 명시적으로 자료형 변환을 해줘야 함
  --(SELECT CAST('192.168.0.1' AS text) AS ip) AS t
;
```
ip 주소를 정수 자료형 표기로 변환하는 쿼리
```python
SELECT
   ip
 -- ■ PostgreSQL, Redshift의 경우 split_part로 문자열 분해하기
 ,  CAST(split_part(ip,'.',1) AS integer) * 2^24
  + CAST(split_part(ip,'.',2) AS integer) * 2^16
  + CAST(split_part(ip,'.',3) AS integer) * 2^8
  + CAST(split_part(ip,'.',4) AS integer) * 2^0
  AS ip_integer
 
 -- ■ BigQuery의 경우 split 함수로 배열로 분해하고 n번째 요소 추출하기
 --, CAST(split(ip,'.')[SAFE_ORDINAL(1)] AS int64) * pow(2,24)
 -- +CAST(split(ip,'.')[SAFE_ORDINAL(2)] AS int64) * pow(2,16)
 -- +CAST(split(ip,'.')[SAFE_ORDINAL(3)] AS int64) * pow(2,8)
 -- +CAST(split(ip,'.')[SAFE_ORDINAL(4)] AS int64) * pow(2,0)
 -- AS ip_integer
 
 -- ■ Hive, SparkSQL의 경우 split 함수로 배열로 분해하고 n번째 요소 추출하기
 -- 다만 피리어드(점)가 특수 문자이므로 역 슬래시로 이스케이프 처리 해야 함
 --, CAST(split(ip,'\\.')[0] AS int) * pow(2,24)
 --+ CAST(split(ip,'\\.')[1] AS int) * pow(2,16)
 --+ CAST(split(ip,'\\.')[2] AS int) * pow(2,8)
 --+ CAST(split(ip,'\\.')[2] AS int) * pow(2,0)
 -- AS ip_integer
FROM
  (SELECT '192.168.0.1'AS ip) AS t
  -- ■ PostgreSQL의 경우 명시적으로 자료형 변환을 해줘야함
  -- (SELECT CAST('192.168.0.1' AS text) AS ip) AS t
;
```
ip 주소를 0으로 메운 문자열로 변환하는 쿼리
```python
SELECT 
   ip
 -- ■ PostgreSQL, Redshift의 경우 lpad 함수로 0으로 메우기
 ,    lpad(split_part(ip,'.',1),3,'0')
  || lpad(split_part(ip,'.',2), 3, '0')
  || lpad(split_part(ip,'.',3), 3, '0')
  || lpad(split_part(ip,'.',4), 3, '0')
  AS ip_padding

 -- ■ BigQuery의 경우 split 함수로 배열로 분해하고 n번째 요소 추출하기
 --, CONCAT(
 --  lpad(split(ip,'.')[SAFE_ORDINAL(1)],3,'0')
 --, lpad(split(ip,'.')[SAFE_ORDINAL(2)],3,'0')
 --, lpad(split(ip,'.')[SAFE_ORDINAL(3)],3,'0')	  
 --, lpad(split(ip,'.')[SAFE_ORDINAL(4)],3,'0')
 -- ) AS ip_padding

 -- ■ Hive, SparkSQL의 경우 split 함수로 배열로 분해로 n번째 요소 추출하기
 -- 다만 피리어드(점)가 특수 문자이므로 역 슬래시로 이스케이프 처리해야 함
 --, CONCAT(
 --   lpad(split(ip,'\\.')[0],3,'0')
 --,  lpad(split(ip,'\\.')[1],3,'0')
 --,  lpad(split(ip,'\\.')[2],3,'0')
 --,  lpad(split(ip,'\\.')[3],3,'0')		 
 -- ) AS ip_padding
FROM
  (SELECT '192.168.0.1' AS ip) AS t
  -- ■ PostgreSQL의 경우 명시적으로 자료형 변환을 해줘야함
  -- (SELECT CAST('192.168.0.1' AS text) AS ip) AS t
;
```
[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어
