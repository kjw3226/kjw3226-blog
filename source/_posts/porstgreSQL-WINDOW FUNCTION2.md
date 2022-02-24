----
title: PostgreSQL-WINDOW FUNCTION2(포스트그리SQL-윈도우 펑션2)
tag: PostgreSQL-WINDOW FUNCTION2(포스트그리SQL-윈도우 펑션2)
date: 2022-01-17
categories:	SQL
----
 지난 주에 이어 오늘도 'WINDOW FUNCTION 함수'에 대해 
 
 알아보고 실습하는 시간을 가졌다.
 
 지난 주 '금요일'에 만든 'summer_medals' 테이블을 

 이용해 실습을 진행했다.

 참고로 'summer_medals' 테이블에는 '올림픽' 관련 데이터가 들어있다.

 아래는 관련 쿼리문들이다.
```python
-- 올림픽 연도를 오름차순 순번대로 작성
-- 연도 중복값 제거
SELECT DISTINCT year
	FROM summer_medals;
	
SELECT DISTINCT year
	FROM summer_medals
	ORDER BY year ASC;

-- 서브 쿼리: SELECT DISTINCT year FROM summer_medals ORDER BY year ASC;
SELECT 
	year,
	ROW_NUMBER() OVER() AS ROW_NUM
FROM (
	SELECT DISTINCT year
	FROM summer_medals
	ORDER BY year ASC
) AS years;

SELECT 
	year,
	ROW_NUMBER() OVER() AS ROW_NUM
FROM (SELECT DISTINCT year FROM summer_medals ORDER BY year ASC) AS years
ORDER BY year ASC;

SELECT 
	ROW_NUMBER() OVER() as row_num
	, year
FROM (SELECT DISTINCT year FROM summer_medals ORDER BY year ASC) AS years
ORDER BY year ASC;

select * FROM summer_medals;
```
조건을 주어서 쿼리문을 진행 해보기도 했다.

```python
-- 질문: 올림픽 선수 별로 획득 메달 수를 구하시오.

WITH athlete_medals AS (
	SELECT 
 	athlete
	, count(*) as medal_counts
	FROM summer_medals
	GROUP BY athlete
)

SELECT
	year
	, athlete
	, country 
FROM 
	summer_medals
WHERE 
	discipline = 'Weightlifting' AND
	event = '69KG' AND
	gender = 'men' AND
	medal = 'Gold';

SELECT
	year
	, country as champion
FROM 
	summer_medals
WHERE 
	discipline = 'Weightlifting' AND
	event = '69KG' AND
	gender = 'men' AND
	medal = 'Gold';


SELECT 
	athlete
	, medal_counts
	, ROW_NUMBER() OVER (ORDER BY medal_counts DESC)as row_num
FROM athlete_medals
ORDER BY medal_counts DESC;
```
```python
SELECT 
 	athlete
	, count(*) as medal_counts
FROM summer_medals
GROUP BY athlete
ORDER BY medal_counts DESC
LIMIT 5;

-- 질문: 남자 69kg 역도 경기에서 금메달 리스트를 뽑습니다.
-- Discipline = 'Weightlifting'
-- Event 69KG,
-- Gender
-- Medal


SELECT * FROM summer_medals;

SELECT DISTINCT discipline FROM summer_medals ORDER BY discipline DESC;
SELECT DISTINCT event FROM summer_medals WHERE discipline = 'Weightlifting';
SELECT DISTINCT event FROM summer_medals WHERE event = '69kg';


WITH weightlifting_69_men_gold as (

SELECT
	year
	, country as champion
FROM 
	summer_medals
WHERE 
	discipline = 'Weightlifting' AND
	event = '69KG' AND
	gender = 'men' AND
	medal = 'Gold'
)

SELECT 
	year
	, champion
	, LAG(champion) OVER(ORDER BY year ASC) as last_champion
FROM weightlifting_69_men_gold
ORDER BY year ASC;

-- Athletics, 20미터, 여자, 금메달 목록 가져오기
-- 나라 대신에, 선수이름 출력
-- lag
SELECT
	year
	, athlete as champion
FROM 
	summer_medals
WHERE 
	discipline = 'Athletics' AND
	event = '200M' AND
	gender = 'Women'AND
	medal = 'Gold';
	
	
	
	
WITH women_gold_200m as (
	SELECT
	year
	, athlete as champion
FROM 
	summer_medals
WHERE 
	discipline = 'Athletics' AND
	event = '200M' AND
	gender = 'Women'AND
	medal = 'Gold'
)

SELECT 
	year
	, champion
	, LAG(champion) OVER(ORDER BY year ASC) as last_champion
FROM women_gold_200m
ORDER BY year ASC;

WITH Discus_Gold_Medal AS (
SELECT 
Year, Event, Country AS Champion
FROM summer_medals
	WHERE 
Year IN (2004, 2008, 2012)
	AND Gender = 'Men' AND Medal = 'Gold'
	AND Event IN ('Discus Throw', 'Triple Jump')
	AND Gender = 'Men')
SELECT 
YEAR, Event, Champion, 
	LAG(Champion) OVER(ORDER BY Event ASC, Year ASC) AS Last_Champion
FROM Discus_Gold_Medal
	ORDER BY Event ASC, Year ASC

WITH Discus_Gold_Medal AS (
SELECT 
Year, Event, Country AS Champion
	FROM summer_medals
	WHERE 
Year IN (2004, 2008, 2012)
	AND Gender = 'Men' AND Medal = 'Gold'
	AND Event IN ('Discus Throw', 'Triple Jump')
	AND Gender = 'Men')
SELECT 
YEAR, Event, Champion, 
	LAG(Champion) OVER
	(PARTITION BY Event ORDER BY Event ASC, Year ASC) AS Last_Champion
FROM Discus_Gold_Medal
	ORDER BY Event ASC, Year ASC;
```