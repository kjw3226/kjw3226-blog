---
title: postgre SQL-practice43
tag: postgre SQL-practice43
date: 2022-03-26
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'6장  15강 사이트 내의 사용자 행동 파악하기

4. 페이지 가치 산출하기'

로 넘어갔으며, 페이지는 358 ~ 365를 참고하였다.

페이지 가치 할당을 계산하는 쿼리문
```python
WITH
activity_log_with_conversion_flag AS (
 SELECT
	session
  , stamp
  , path
	-- 성과를 발생시키는 컨버전 페이지의 이전 접근에 플래그 추가하기
  , SIGN(SUM(CASE WHEN path = '/complete' THEN 1 ELSE 0 END)
		OVER(PARTITION BY session ORDER BY stamp DESC
		  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW))
	AS has_conversion
 FROM
  activity_log
)
, activity_log_with_conversion_assing AS (
  SELECT
	 session
   , stamp
   , path
   -- 성과에 이르기까지의 접근 로그를 오름차순으로 정렬하기
   , ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp ASC) AS asc_order
   -- 성과에 이르기까지의 접근 로그에 내림차순으로 순번 붙이기
   , ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp ASC) AS desc_order
   -- 성과에 이르기까지의 접근 수 세기
   , COUNT(1) OVER(PARTITION BY session) AS page_count
	
	
   -- 1. 성과에 이르기까지의 접근 로그에 균등한 가치 부여하기
   , 1000.0 / COUNT(1) OVER(PARTITION BY session) AS fair_assign
   
   -- 2. 성과에 이르기까지의 접근 로그의 첫 페이지에 가치 부여하기
   , CASE
	  WHEN ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp ASC) = 1
	    THEN 1000.0
	  ELSE 0.0
	 END AS first_asssign
	
   -- 3. 성과에 이르기까지의 접근 로근의 마지막 페이지에 가치 부여하기
   , CASE
	  WHEN ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp DESC) = 1
	   THEN 1000.0
	  ELSE 0.0
	 END AS last_assign
	
   -- 4. 성과에 이르기까지의 접근 로그의 성과 지점에서 가까운 페이지에 높은 가치 부여하기
   , 1000.0
     * ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp ASC)
	   -- 순번 합계로 나누기(N*(N+1)/2)
	 / (  COUNT(1) OVER(PARTITION BY session)
	   * (COUNT(1) OVER(PARTITION BY session)+1)
	   /2)
	   AS decrease_assign
	
   -- 5. 성과에 이르기까지의 접근 로그의 성과 지점에서 먼 페이지에 높은 가치 부여하기
   , 1000.0
     * ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp DESC)
	   -- 순번 합계로 나누기(N*(N+1)/2)
	 / (    COUNT(1) OVER(PARTITION BY session)
	  * (COUNT(1) OVER(PARTITION BY session)+1)
	   /2)
	   AS increase_assign
	FROM activity_log_with_conversion_flag
	WHERE
	 -- 컨버전으로 이어지는 세션 로그만 추출하기
	 has_conversion = 1
	 -- 입력, 확인, 완료 페이지 제외하기
	 AND path NOT IN('/input', '/confirm', '/complete')
)
SELECT
   session
 , asc_order
 , path
 , fair_assign AS fair_a
 , first_assign AS first_a
 , last_assign AS last_a
 , decrease_assign AS dec_a
 , increase_assign AS inc_a
FROM
 activity_log_with_conversion_assing
ORDER BY
 session, asc_order;
```

경로별 페이지 가치 합계를 구하는 쿼리문
```python
WITH
activity_log_with_conversion_flag AS (
 SELECT
	session
  , stamp
  , path
	-- 성과를 발생시키는 컨버전 페이지의 이전 접근에 플래그 추가하기
  , SIGN(SUM(CASE WHEN path = '/complete' THEN 1 ELSE 0 END)
		OVER(PARTITION BY session ORDER BY stamp DESC
		  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW))
	AS has_conversion
 FROM
  activity_log
)
, activity_log_with_conversion_assing AS (
  SELECT
	 session
   , stamp
   , path
   -- 성과에 이르기까지의 접근 로그를 오름차순으로 정렬하기
   , ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp ASC) AS asc_order
   -- 성과에 이르기까지의 접근 로그에 내림차순으로 순번 붙이기
   , ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp ASC) AS desc_order
   -- 성과에 이르기까지의 접근 수 세기
   , COUNT(1) OVER(PARTITION BY session) AS page_count
	
	
   -- 1. 성과에 이르기까지의 접근 로그에 균등한 가치 부여하기
   , 1000.0 / COUNT(1) OVER(PARTITION BY session) AS fair_assign
   
   -- 2. 성과에 이르기까지의 접근 로그의 첫 페이지에 가치 부여하기
   , CASE
	  WHEN ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp ASC) = 1
	    THEN 1000.0
	  ELSE 0.0
	 END AS first_asssign
	
   -- 3. 성과에 이르기까지의 접근 로근의 마지막 페이지에 가치 부여하기
   , CASE
	  WHEN ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp DESC) = 1
	   THEN 1000.0
	  ELSE 0.0
	 END AS last_assign
	
   -- 4. 성과에 이르기까지의 접근 로그의 성과 지점에서 가까운 페이지에 높은 가치 부여하기
   , 1000.0
     * ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp ASC)
	   -- 순번 합계로 나누기(N*(N+1)/2)
	 / (  COUNT(1) OVER(PARTITION BY session)
	   * (COUNT(1) OVER(PARTITION BY session)+1)
	   /2)
	   AS decrease_assign
	
   -- 5. 성과에 이르기까지의 접근 로그의 성과 지점에서 먼 페이지에 높은 가치 부여하기
   , 1000.0
     * ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp DESC)
	   -- 순번 합계로 나누기(N*(N+1)/2)
	 / (    COUNT(1) OVER(PARTITION BY session)
	  * (COUNT(1) OVER(PARTITION BY session)+1)
	   /2)
	   AS increase_assign
	FROM activity_log_with_conversion_flag
	WHERE
	 -- 컨버전으로 이어지는 세션 로그만 추출하기
	 has_conversion = 1
	 -- 입력, 확인, 완료 페이지 제외하기
	 AND path NOT IN('/input', '/confirm', '/complete')
)
, page_total_values AS (
  -- 페이지 가치 합계 계산하기
  SELECT
	 path
   , SUM(fair_assign) AS fair_assign
   , SUM(first_assign) AS first_assign
   , SUM(last_assign) AS last_assign
  FROM
   activity_log_with_conversion_assing
  GROUP BY
	path
)
SELECT * FROM page_total_values;
```

경로들의 평균 페이지 가치를 구하는 쿼리문
```python
WITH
activity_log_with_conversion_flag AS (
 SELECT
	session
  , stamp
  , path
	-- 성과를 발생시키는 컨버전 페이지의 이전 접근에 플래그 추가하기
  , SIGN(SUM(CASE WHEN path = '/complete' THEN 1 ELSE 0 END)
		OVER(PARTITION BY session ORDER BY stamp DESC
		  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW))
	AS has_conversion
 FROM
  activity_log
)
, activity_log_with_conversion_assing AS (
  SELECT
	 session
   , stamp
   , path
   -- 성과에 이르기까지의 접근 로그를 오름차순으로 정렬하기
   , ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp ASC) AS asc_order
   -- 성과에 이르기까지의 접근 로그에 내림차순으로 순번 붙이기
   , ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp ASC) AS desc_order
   -- 성과에 이르기까지의 접근 수 세기
   , COUNT(1) OVER(PARTITION BY session) AS page_count
	
	
   -- 1. 성과에 이르기까지의 접근 로그에 균등한 가치 부여하기
   , 1000.0 / COUNT(1) OVER(PARTITION BY session) AS fair_assign
   
   -- 2. 성과에 이르기까지의 접근 로그의 첫 페이지에 가치 부여하기
   , CASE
	  WHEN ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp ASC) = 1
	    THEN 1000.0
	  ELSE 0.0
	 END AS first_asssign
	
   -- 3. 성과에 이르기까지의 접근 로근의 마지막 페이지에 가치 부여하기
   , CASE
	  WHEN ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp DESC) = 1
	   THEN 1000.0
	  ELSE 0.0
	 END AS last_assign
	
   -- 4. 성과에 이르기까지의 접근 로그의 성과 지점에서 가까운 페이지에 높은 가치 부여하기
   , 1000.0
     * ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp ASC)
	   -- 순번 합계로 나누기(N*(N+1)/2)
	 / (  COUNT(1) OVER(PARTITION BY session)
	   * (COUNT(1) OVER(PARTITION BY session)+1)
	   /2)
	   AS decrease_assign
	
   -- 5. 성과에 이르기까지의 접근 로그의 성과 지점에서 먼 페이지에 높은 가치 부여하기
   , 1000.0
     * ROW_NUMBER() OVER(PARTITION BY session ORDER BY stamp DESC)
	   -- 순번 합계로 나누기(N*(N+1)/2)
	 / (    COUNT(1) OVER(PARTITION BY session)
	  * (COUNT(1) OVER(PARTITION BY session)+1)
	   /2)
	   AS increase_assign
	FROM activity_log_with_conversion_flag
	WHERE
	 -- 컨버전으로 이어지는 세션 로그만 추출하기
	 has_conversion = 1
	 -- 입력, 확인, 완료 페이지 제외하기
	 AND path NOT IN('/input', '/confirm', '/complete')
)
, page_total_values AS (
  -- 페이지 가치 합계 계산하기
  SELECT
	 path
   , SUM(fair_assign) AS fair_assign
   , SUM(first_assign) AS first_assign
   , SUM(last_assign) AS last_assign
  FROM
   activity_log_with_conversion_assing
  GROUP BY
	path
)
, page_total_cnt AS (
  -- 페이지 뷰 계산하기
  SELECT
	 path
   , COUNT(1) AS access_cnt  -- 페이지 뷰
   -- 방문 횟수로 나누고 싶은 경우는 다음 코드 사용하기
   --, COUNT(DISTINCT session) AS access_cnt
  FROM
   activity_log
  GROUP BY
   path
)
SELECT
 -- 한 번의 방문에 따른 페이지 가치 계산하기
  s.path
, s.assess_cnt
, v.sum_fair  / s.access_cnt AS avg_fair
, v.sum_first / s.access_cnt AS avg_first
, v.sum_last  / s.access_cnt AS avg_last
, v.sum_dec   / s.access_cnt AS avg_dec
, v.sum_inc   / s.access_cnt AS avg_inc
FROM
   page_total_cnt AS s
JOIN
   page_total_values AS v
   ON s.path = v.path
ORDER BY
 s.access_cnt DESC;
```

대부분의 접근 분석 도구는 페이지의 평가를 산출하는 로직이 한정되는

경우가 많습니다.

무엇을 평가하고 싶은지를 명확하게 생각하고 자유롭게 계산할 수 있게 되면,

접근 분석 도구의 제한 없이 새로운 가치를 분석할 수 있을 것입니다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 15강 페이지 365 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어