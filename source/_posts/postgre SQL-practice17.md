---
title: postgre SQL-practice17
tag: postgre SQL-practice17
date: 2022-02-18
categories:	SQL
---
 이제 '데이터 분석을 위한 SQL레시피' '4장'에서 '5장'으로 넘어간다.
 
 5장의 큰 주제는 '사용자를 파악하기 위한 데이터 추출'이다.
 
 '사용자'가 로그인 했는지 안했는지, 그 다음 '행동(ACTION)'은 무엇을 했는지 
 
 알아보는 쿼리문을 실습해봤다.

'액션' 수와 비율을 계산하는 쿼리문
```python
WITH
stats AS (
 -- 로그 전체의 유니크 사용자 수 추가하기
 SELECT COUNT(DISTINCT session) AS total_uu
 FROM action_log
)
SELECT
   l.action
 -- 액션 UU
, COUNT(DISTINCT l.session) AS action_uu
 -- 액션의 수
, COUNT(1) AS action_count
 -- 전체 UU
, s.total_uu
 -- 사용률: <액션 UU> / <전체 UU>
, 100.0 * COUNT(DISTINCT l.session) / s.total_uu AS usage_rate
 -- 1인당 액션 수: <액션 수> / <액션 UU>
, 1.0 * COUNT(1) / COUNT(DISTINCT l.session) AS count_per_user
FROM
   action_log AS l
  --로그 전체의 유니크 사용자 수를 모든 레코드에 결합하기
  CROSS JOIN
   stats AS s
GROUP BY
 l.action, s.total_uu
;
```
다음 쿼리문은 '사용자'를 '로그인 사용자'와 '비로그인 사용자' 이렇게 구분해서 

집계하는 쿼리문이다.

로그린 상태를 판별하는 쿼리문
```python
WITH
action_log_with_status AS (
 SELECT 
	session
  , user_id
  , action
  -- user_id가 NULL 또는 빈 문자가 아닌 경우 login이라고 판정하기
  , CASE WHEN COALESCE(user_id, '') <> '' THEN 'login' ELSE 'quest' END
	AS login_status
 FROM
  action_log
)
SELECT *
FROM
 action_log_with_status
;
```

이어서 '사용자'가 '로그인' 후에 '행동(ACTION)'을 취한 수를 집계하는 쿼리문이다.

로그인 상태에 따라 액션 수 등을 따로 집계하는 쿼리문
```python
WITH
action_log_with_status AS(
 SELECT 
	session
  , user_id
  , action
  -- user_id가 NULL 또는 빈 문자가 아닌 경우 login이라고 판정하기
  , CASE WHEN COALESCE(user_id, '') <> '' THEN 'login' ELSE 'quest' END
	AS login_status
 FROM
  action_log
)
SELECT
   COALESCE(action, 'all') AS action
 , COALESCE(login_status, 'all') AS login_status
 , COALESCE(DISTINCT session) AS action_uu
 , COUNT(1) AS action_count
FROM
 action_log_with_status
GROUP BY
  -- ■ PostgreSQL, SparkSQL의 경우는 다음과 같이 작성하기
  ROLLUP(action, login_status)
  -- ■Hive의 경우는 다음과 같이 작성하기
  -- action, login_status WITH ROLLUP
;
```