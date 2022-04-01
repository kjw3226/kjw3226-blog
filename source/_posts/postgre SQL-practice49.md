---
title: postgre SQL-practice49
tag: postgre SQL-practice49
date: 2022-04-01
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'6장  16강 입력 양식 최적화하기'로 넘어갔으며

'1. 오류율 집계하기'에서  '2. 입력~확인~완료까지의 이동률 집계하기'

까지 참고하였다.

확인 화면에서의 오류율을 집계하는 쿼리문
```python
SELECT
  COUNT(*) AS confirm_count
, SUM(CASE WHEN status = 'error' THEN 1 ELSE 0 END) AS error_count
, AVG(CASE WHEN status = 'error' THEN 1.0 ELSE 0.0 END) AS error_rate
, SUM(CASE WHEN status = 'error' THEN 1.0 ELSE 0.0 END) / COUNT(DISTINCT session)
  AS error_per_user
FROM form_log
WHERE
-- 확인 화면 페이지 판정하기
path = '/regist/confirm'
;
```

입력 양식의 폴아웃 리포트 쿼리문
```python
WITH
mst_fallout_step AS (
 -- /regist 입력 양식의 폴아웃 단계와 경로 마스터
	       SELECT 1 AS step, '/regist/input'    AS path 
 UNION ALL SELECT 2 AS step, '/regist/confirm'  AS path
 UNION ALL SELECT 3 AS step, '/regist/complete' AS path
)
, form_log_with_fallout_step AS (
SELECT
   l.session
 , m.step
 , m.path
 -- 특정 단계 경로의 처음/마지막 접근 시간 추가하기
 , MAX(l.stamp) AS max_stamp
 , MIN(l.stamp) AS min_stamp
FROM
   mst_fallout_step AS m
 JOIN
   form_log AS l
   ON m.path = l.path
-- 확인 화면의 상태가 오류인 것만 추출하기
WHEN status = ''
-- 세션별로 단계 순서와 경로 집약하기
GROUP BY l.session, m.step, m.path
)
, form_log_with_mod_fallout_step AS (
 SELECT
	session
  , step
  , path
  , max_stamp
	-- 직전 단계 경로의 첫 접근 시간
  , LAG(min_stamp)
	 OVER(PARTITION BY session ORDER BY step)
	--■ SparkSQL의 경우 LAG 함수에 프레임 지정 필요
	--OVER(PARTITION BY session AND 1 PRECEDING)
	AS lag_min_stamp
	--세션 내부에서 단계 순서 최솟값
  , MIN(step) OVER(PARTITION BY session) AS min_step
	-- 해당 단계에 도달할 때까지의 누계 단계 수
  , COUNT(1)
	 OVER(PARTITION BY session ORDER BY step
	   ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
    AS cum_count
FROM form_log_with_fallout_step
)
, fallout_log AS(
-- 폴아웃 리포트에 필요한 정보 추출하기
 SELECT
	session
  , step
  , path
FROM
  form_log_with_mod_fallout_step
WHERE
	 --세션 내부에서 단계 순서가 1인 URL에 접근하는 경우
	 min_step = 1
	 -- 현재 단계 순서가 해당 단계의 도착할 때까지의 누계 단계 수와 같은 경우
 AND step = cum_count
	--직전 단계의 첫 접근 시간이 
	--NULL 또는 현재 단계의 최종 접근 시간보다 앞인 경우
 AND (lag_min_stamp IS NULL
	 OR max_stamp >= lag_min_stamp)
)
SELECT
  step
, path
, count(1) AS count
 -- <단계 순서> = 1인 URL로부터의 이동률
 , 100.0 * COUNT(1)
 / FIRST_VALUE(COUNT(1))
    OVER(ORDER BY step ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
 AS first_trans_rate
 -- 직전 단계로 부터의 이동률
, 100.0 * COUNT(1)
 / LAG(COUNT(1)) OVER(ORDER BY step ASC)
 --■ SparkSQL의 경우 LAG 함수에 프레임 지정 필요
 -- / LAG(count(1)) OVER(ORDER BY step ASC ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING)
 AS step_trans_rate
FROM
 fallout_log
GROUP BY
 step, path
ORDER BY
 step
;
```

다만 앞의 리포트는 입력 화면에서 사용자가 압력의 의사가 있었는지 

없었는지는 판별할 수 없습니다.

따라서 입력 의사를 확인하고 싶다면 최초 입력 항목을 클릭할 때 또는

최초 입력 시 자바스크립트를 사용해서 추가 로그를 전송하게 해야 합니다.

이렇게 하면 확실하게 '입력 화면 출력 ~ 입력 시작~ 완료 화면 출력'

까지의 폴아웃 리포트를 작성할 수 있습니다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 15강 페이지 400 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어