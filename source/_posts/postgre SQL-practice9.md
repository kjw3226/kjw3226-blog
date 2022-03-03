---
title: postgre SQL-practice9
tag: postgre SQL-practice9
date: 2022-02-10
categories:	SQL
----
'예제 코드'는 여기서 다운 받아 실행하면 된다.

[SQL CODE](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

분석을 하다가 보면 '이런 테이블을 만들면, 이런 리포트를 만들 수 있을지도 몰라'
등의 생각이 떠오르는 경우가 종종 있다.
그런데 그럴 때마다 사용자에 따라 테이블 생성 권한이 없어서 그냥 포기하고
넘어가는 경우가 생깁니다.
이러한 문제는 '유사 테이블'을 만들어 테스트를 하면 '작업 효율'이
크게 향상된다. ('데이터 분석을 위한 SQL레시피' 3장 中)

'유사 테이블 만들기 - 임의의 레코드를 가진 유사 테이블 만들기'

디바이스 ID와 이름의 마스터 테이블을 만드는 쿼리문
```python
WITH
mst_devices AS(
	         SELECT 1 AS device_id, 'PC' AS device_name
   UNION ALL SELECT 2 AS device_id, 'SP' AS device_name
   UNION ALL SELECT 3 AS device_id, '애플리케이션' AS device_name
)
SELECT *
FROM mst_devices
;
```

의사 테이블을 사용해 코드를 레이블로 변환하는 쿼리문
```python
WITH 
mst_devices AS (
	         SELECT 1 AS device_id, 'PC' AS device_name
   UNION ALL SELECT 2 AS device_id, 'SP' AS device_name
   UNION ALL SELECT 3 AS device_id, '애플리케이션' AS device_name
)
SELECT
   u.user_id
 , d.device_name
FROM
   mst_users AS u
  LEFT JOIN
   mst_devices AS d
   ON u.register_device = d.device_id
;
```

'유사 테이블 만들기 - VALUES 구문을 사용한 유사 테이블 만들기'

VALUES 구문을 사용해 동적으로 테이블을 만드는 쿼리문
```python
WITH
mst_devices(device_id, device_name) AS ( 
 VALUES
   (1, 'PC')
 , (2, 'SP') 
 , (3, '애플리케이션')
)
SELECT*
FROM mst_devices
;
```

'유사 테이블 만들기 - 배열형 테이블 함수를 사용한 유사 테이블 만들기'

배열과 explode 함수를 사용해 동적으로 테이블을 만드는 쿼리문
```python
WITH
mst_devices AS(
 SELECT
	-- 배열를 열로 전개하기
	d[0] AS device_id
  , d[1] AS device_name
 FROM
	-- 배열를 테이블로 전개하기
	(SELECT explode(
	 array(
	  array('1','PC')
	, array('2','SP')
    , array('3','애플리케이션')
	 )) d
	)AS t 
   )
SELECT*
FROM mst_devices
;
```
map 자료형과 explode 함수를 사용해 동적으로 테이블을
작성하는 쿼리
```python
WITH
mst_device AS(
 SELECT 
	-- map 자료형의 데이터를 열로 전개하기
	d['device_id'] AS device_id
  , d['device_name'] AS device_name
FROM 
   -- 배열를 테이블로 전개하기
  (SELECT explode(
	array(
	 map('device_id','1','device_name','PC')
   , map('device_id','2','device_name','SP')
   , map('device_id','3','device_name','애플리케이션')
	))d
  )AS t
)
SELECT *
FROM mst_devices
;
```

'순번을 사용해 테이블 작성하기'

순번을 가진 유사 테이블을 작성하는 쿼리문
```python
WITH
series AS(
  -- 1부터 5까지의 순번 생성하기
  -- ■ Postgre SQL의 경우 generate_series 사용하기
  SELECT generate_series(1,5) AS idx
-- ■ BigQuery의 경우 generate_array 사용하기
  --SELECT idx FROM unnest(generate_array(1,5)) AS idx
)
SELECT *
FROM series
;
```

repeat 함수를 응용해서 순번을 작성하는 쿼리문
```python
SELECT
  ROW_NUMBER() OVER(ORDER BY x)AS idx
FROM
  -- repeat 함수와 split 함수를 조합해서 임의의 길이를 가진 배열을 생성하고
  -- explode로 전개하기
 (SELECT explode(split(repeat('x' , 5 - 1), 'x'))AS x)AS t
;
```

유사 테이블이 편리하다고 해서 같은 유사 테이블을 여러 SQL에서
활용하면 SQL을 일괄 관리하기 힘들어질 수 있다.
따라서 많이 사용되는 유사 테이블은 별도의 일반 테이블로 
정의해두도록 하자.('데이터 분석을 위한 SQL레시피' 3장 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어

