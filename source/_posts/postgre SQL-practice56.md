---
title: postgre SQL-practice56
tag: postgre SQL-practice56
date: 2022-04-08
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'7장  18강 이상값 검출하기'의

'3. 데이터 타당성 확인하기'로 넘어갔으며

페이지 429 ~ 431을 참고하였다.


로그 데이터의 요건을 만족하는지 확인하는 쿼리문
```python
SELECT
   action
   
   -- session은 반드시 NULL이 아니어야 함
 , AVG(CASE WHEN session IS NOT NULL THEN 1.0 ELSE 0.0 END) AS session
 
   -- user_id은  반드시 NULL이 아니어야 함
 , AVG(CASE WHEN session IS NOT NULL THEN 1.0 ELSE 0.0 END) AS user_id
 
   --categor는 action=view의 경우 NULL, 이외의 경우는 NULL이 아니어야 함
 , AVG(
	CASE action
	 WHEN 'view' THEN 
	  CASE WHEN category IS NULL THEN 1.0 ELSE 0.0 END
	 ELSE
	  CASE WHEN category IS NOT NULL THEN 1.0 ELSE 0.0 END
    END
 ) AS category
 
 -- products는 action=view의 경우 NULL, 이외의 경우 NULL이 아니어야 함
, AVG(
   CASE action
	WHEN 'view' THEN 
	 CASE WHEN products IS NULL THEN 1.0 ELSE 0.0 END
	ELSE
	 CASE WHEN products IS NOT NULL THEN 1.0 ELSE 0.0 END
   END
) AS products

 --amount는 action=purchase의 경우 NULL이 아니어야 하며 이외의 경우는 NULL
, AVG(
   CASE action
	WHEN 'purchase' THEN 
	 CASE WHEN amount IS NOT NULL THEN 1.0 ELSE 0.0 END
	ELSE
	 CASE WHEN amount IS NULL THEN 1.0 ELSE 0.0 END
   END
) AS amount

 --stamp는 반드시 NULL이 아니어야 함
, AVG(CASE WHEN stamp IS NOT NULL THEN 1.0 ELSE 0.0 END) AS stamp
FROM
 invalid_action_log
GROUP BY 
 action
;
```

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어