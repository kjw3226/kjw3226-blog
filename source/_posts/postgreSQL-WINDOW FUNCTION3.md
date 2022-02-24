----
title: PostgreSQL-WINDOW FUNCTION3(포스트그리SQL-윈도우 펑션3)
tag: PostgreSQL-WINDOW FUNCTION3(포스트그리SQL-윈도우 펑션3)
date: 2022-01-18
categories:	SQL
----
오늘은 'WINDOW FUNCTION'으로 기존의 쿼리문에 조건을 걸기도하고

'PARTITION BY'에 조건을 걸어서 연습문제를 풀어보기도 하고 

'RANK','DENSE RANK'를 활용해 실습도 해보았다.

아래는 실습한 쿼리문들이다.

```python
SELECT * FROM summer_medals;

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
      (ORDER BY Event ASC, Year ASC) AS Last_Champion
FROM Discus_Gold_Medal
  ORDER BY Event ASC, Year ASC;
```
```python
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
```python
-- 성별, 연도 (2004, 2008, 2012), 현재 시점 국가 (champion), 지난 대회 챔피언
-- Men, 2000                ,CZE                  ,null
-- Woman,
-- 조건: event 'Javelin Throw', Medal = 'Gold'
-- 수원 --> 서울역
-- 코딩 잘할려면 
-- 가장 좋은건 수원역에서 전철타고 서울역으로 가는 것
-- 가다가 안양역에서 막혀서 기다리다...다른 방법을 찾아서 갈 것
-- 코딩도 똑같은 것이다. 다른 방법도 많으니 그 방법을 찾아서 그거대로 하면 된다.

WITH Discus_Gold_Medal AS (
SELECT 
	DISTINCT gender, year, country
FROm summer_medals
WHERE
	year >= 2000 AND
	EVENT = 'Javelin Throw' AND
	Medal = 'Gold')
	
SELECT 
	gender
	, year
	, country as champion,
	LAG(Country) OVER (PARTITION BY gender ORDER BY year ASC) AS last_champion
FROM tennis_gold;

-- 경기종목을 2개로 추가 ('10000M', '100M')

WITH Athletics_Gold AS (
  SELECT DISTINCT
    Gender, Year, Event, Country
  FROM Summer_Medals
  WHERE
    Year >= 2000 AND
    --Discipline = 'Athletics' AND
    Event IN ('100M', '10000M') AND
    Medal = 'Gold')

SELECT
  Gender, Year, Event,
  Country AS Champion,
  -- Fetch the previous year's champion by gender and event
  LAG(Country) OVER (PARTITION BY Gender, Event
                         ORDER BY Year ASC) AS Last_Champion
FROM Athletics_Gold
ORDER BY Event ASC, Gender ASC, Year ASC;
-- LIMIT10;
```
```python
-- year, athlete, future_champion
-- 조건: 1 Medal = Gold / Event = Discus Throw / Gender Women / Year >= 1992
-- future_champion: LEAD(컬럼명, 3) over()

WITH Discus_Throw_champion AS (
SELECT 
      year
     , athlete 
FROM summer_medals
WHERE
      year >= 1992 AND
     event = 'Discus Throw' AND
     gender = 'Women' AND
     medal = 'Gold'
)
SELECT 
       year
      , athlete
      , LEAD(athlete, 3) OVER (ORDER BY year ASC) AS futuer_champion
FROM Discus_Throw_champion
ORDER BY year ASC;
```
```python
WITH Country_Games AS (
   SELECT 
       Country, COUNT(DISTINCT Year) AS Games
       FROM summer_medals
       Where 
          Country IN ('GBR', 'DEN', 'FRA', 
                              'ITA', 'AUT', 'BEL', 
                            'NOR', 'JPN', 'KOR')
        GROUP BY Country
        ORDER BY GAMES DESC)
SELECT 
     Country, Games, 
         ROW_NUMBER()
    OVER (ORDER BY Games DESC) AS Row_N,
         RANK()
    OVER (ORDER BY Games DESC) AS Rank_N, 
         DENSE_RANK()
    OVER (ORDER BY Games DESC) AS Dense_Rank_N
FROM Country_Games
ORDER BY Games DESC, Country ASC;
```