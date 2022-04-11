---
title: postgre SQL-practice59
tag: postgre SQL-practice59
date: 2022-04-11
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'7장  19강 데이터 중복 검출하기'의

'2. 로그 중복 검출하기'로 넘어갔으며

페이지 444 ~ 451을 참고하였다.


사용자와 상품의 조합에 대한 중복을 확인하는 쿼리문
```python
SELECT
   user_id
 , products
 --데이터를 배열로 집약하고, 쉼표로 구분된 문자열로 변환하기
 --■PostgreSQL, BigQuery의 경우는 string_agg 사용하기
 , string_agg(session, ',') AS session_list
 , string_agg(stamp, ',') AS stamp_list
 --■Redshift의 경우는 listagg 사용하기
 --, listagg(session,',') AS session_list
 --, listagg(stamp,',') AS stamp_list
 --■Hive, SparkSQL의 경우는 collect_list와 concat_ws 사용하기
 --, concat_ws(',', collect_list(session)) AS session_list
 --, concat_ws(',', collect_list(stamp )) AS stamp_list
 
FROM
 dup_action_log
GROUP BY
 user_id, products
HAVING
 COUNT(*) > 1
;
```

GROUP BY와 MIN을 사용해 중복을 배제하는 쿼리문
```python
SELECT
   session
 , user_id
 , action
 , products
 , MIN(stamp) AS stamp
FROM
 dup_action_log
GROUP BY
 session, user_id, action, products
;
```


ROW_NUMBER를 사용해 중복을 배제하는 쿼리문
```python
WITH
dup_action_log_with_order_num AS (
 SELECT
	*
	
	--중복된 데이터에 순번 붙이기
  , ROW_NUMBER()
	 OVER(
	  PARTITION BY session, user_id, action, products
	  ORDER BY stamp
	 ) AS order_num
 FROM
  dup_action_log
)
SELECT
   session
 , user_id
 , action
 , products
 , stamp
FROM
 dup_action_log_with_order_num
WHERE 
 order_num = 1 --순번이 1인 데이터(중복된 것 중에서 가장 앞의 것)만 남기기
;
```


이전 액션으로부터의 경과 시간을 계산하는 쿼리문
```python
WITH
dup_action_log_with_lag_seconds AS (
 SELECT
	user_id
  , action
  , products
  , stamp
  --같은 사용자와 상품 조합에 대한 이전 액션으로부터의 경과 시간 계산하기
  --■PostgreSQL의 경우 timestamp 자료형으로 변환하고 차이를 구한 뒤
  --  EXTRACT(epoc~)를 사용해 초 단위로 변경하기
   , EXTRACT(epoc from stamp::timestamp - LAG(stamp::timestamp)
	  OVER(
	    PARTITION BY user_id, action, products
	    ORDER BY stamp
	  )) AS lag_seconds
  --■Redshift의 경우 datediff 함수를 초 단위로 지정하기
  --, datediff(second, LAG(stamp::timestamp)
  --   OVER(
  --    PARTITION BY user_id, action, products
  --    ORDER BY stamp
  --   ), stamp::timestamp) AS lag_seconds
  --■BigQuery의 경우 unix_seconds 함수로 초단위 UNIX 타임으로 변환하고 차이 구하기
  --, unix_seconds(timestamp(stamp)) - LAG(unix_seconds(timestamp(stamp)))
  -- OVER(
  --   PARTITION BY user_id, action, products
  --    ORDER BY stamp
  --  ) AS lag_seconds
  --■Hive, SparkSQL의 경우 unix_timestamp 함수 초 단위 UNIX 타임으로 변환하고 차이 구하기
  --, unix_timestamp(stamp) - LAG(unix_timestamp(stamp))
  --   OVER(
  --    PARTITION BY user_id, action, products
  --    ORDER BY stamp
  --■SparkSQL의 경우 다음과 같이 프레임 지정 추가하기
  --    ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING 
  --  ) AS lag_seconds
 FROM
  dup_action_log
)
SELECT
   *
FROM
 dup_action_log_with_lag_seconds
ORDER BY
 stamp;
```


30분 이내의 같은 액션을 중복으로 보고 배제하는 쿼리문
```python
WITH
dup_action_log_with_lag_seconds AS (
 SELECT
	user_id
  , action
  , products
  , stamp
  --같은 사용자와 상품 조합에 대한 이전 액션으로부터의 경과 시간 계산하기
  --■PostgreSQL의 경우 timestamp 자료형으로 변환하고 차이를 구한 뒤
  --  EXTRACT(epoc~)를 사용해 초 단위로 변경하기
   , EXTRACT(epoc from stamp::timestamp - LAG(stamp::timestamp)
	  OVER(
	    PARTITION BY user_id, action, products
	    ORDER BY stamp
	  )) AS lag_seconds
  --■Redshift의 경우 datediff 함수를 초 단위로 지정하기
  --, datediff(second, LAG(stamp::timestamp)
  --   OVER(
  --    PARTITION BY user_id, action, products
  --    ORDER BY stamp
  --   ), stamp::timestamp) AS lag_seconds
  --■BigQuery의 경우 unix_seconds 함수로 초단위 UNIX 타임으로 변환하고 차이 구하기
  --, unix_seconds(timestamp(stamp)) - LAG(unix_seconds(timestamp(stamp)))
  -- OVER(
  --   PARTITION BY user_id, action, products
  --    ORDER BY stamp
  --  ) AS lag_seconds
  --■Hive, SparkSQL의 경우 unix_timestamp 함수 초 단위 UNIX 타임으로 변환하고 차이 구하기
  --, unix_timestamp(stamp) - LAG(unix_timestamp(stamp))
  --   OVER(
  --    PARTITION BY user_id, action, products
  --    ORDER BY stamp
  --■SparkSQL의 경우 다음과 같이 프레임 지정 추가하기
  --    ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING 
  --  ) AS lag_seconds
 FROM
  dup_action_log
)
SELECT
   user_id
 , action
 , products
 , stamp
FROM
 dup_action_log_with_lag_seconds
WHERE
 (lag_seconds IS NULL OR lag_seconds >= 30 * 60)
ORDER BY
  stamp
;
```

로그 데이터에 중복이 포함된 상태로 리포트를 작성하면, 실제와 다른 값으로

리포트가 만들어져 잘못된 판단을 할 수 있습니다.

따라서 분석하는 데이터를 잘 확인하고 어떤 방침으로 이러한 중복을

제거해야 할지 검토하기 바랍니다.

(데이터 분석을 위한 SQL 레시피-7장 데이터 활용의

정밀도를 높이는 분석 기술 19강 로그 중복 검출하기 451 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어