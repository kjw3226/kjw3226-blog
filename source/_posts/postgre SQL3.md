----
title: Postgre SQL3 (포스트그리 SQL3)
tag: Postgre SQL3 (포스트그리 SQL3)
date: 2022-01-12
categories:	SQL
----

이번 주는 'Postgre SQL'만 활용한 

실습을 계속 진행 할 것이다.

오늘은 '서브 쿼리'에 대해 알아보고 실습을 해보았다.

아래는 전부 실습 쿼리문이다.
```python
-- 서브쿼리
-- 실제 보유하고 있는 과일 데이터
select * from real_amount;

-- 카운터 컴퓨터에서 추정한 과일 데이터
select * from assumption_amount;

-- 외상 데이터
select * from exception;




-- 메인 쿼리
-- 서브 쿼리
-- 카운터에는 데이터 존재 / 외상 데이터 현재 없음

SELECT * FROM real_amount
WHERE EXISTS (
	SELECT * FROM assumption_amount
);

SELECT * FROM real_amount
WHERE EXISTS (
	SELECT * FROM exception
);

-- IN 연산자 NOT IN 연산자
-- 반드시 하나의 값이 도출이 되어야 함

SELECT * FROM real_amount
WHERE amount NOT IN (
	10, 20, 30
);

-- ANY 연산자
SELECT * FROM real_amount
WHERE 11 = ANY (
	SELECT amount FROM assumption_amount
);
```
조건을 주어서 직접 메인 쿼리문과 서브 쿼리문을 작성 해보기도 했다.
```python
-- populations 
-- 서브쿼리
-- 조건 1. 2015년 전체 국가의 평균 수명을 계산합니다. 
SELECT avg(life_expectancy) FROM populations where year = 2015;

-- 메인쿼리
-- 조건 2. 모든 데이터를 조회합니다. 
-- 조건 3. 2015년 평균 기대수명의 1.15배보다 높도록 조건을 설정합니다. 
-- 기대수명 > 1.15 * 평균 기대수명
-- 기대수명 > 1.15 * 70.980~ and year 
SELECT * 
FROM populations
WHERE life_expectancy > 1.15 * (
		SELECT avg(life_expectancy) FROM populations where year = 2015
	)
	and year = 2015;
```
```python
-- 메인쿼리
-- citi 테이블에서, name, country_code, urban_pop 만 조회
-- urban_pop 내림차순 정렬
-- 상위 5개만 출력
SELECT name, country_code, urbanarea_pop 
FROM cities
WHERE name in (SELECT capital FROM countries)
ORDER BY urbanarea_pop DESC
LIMIT 5;

SELECT capital FROM countries;

-- 서브쿼리
-- city 테이블에 name과 countries capital 매칭이 되는 도시들만 조회


SELECT countries.name AS country, COUNT(*) AS cities_num
  FROM cities
      INNER JOIN countries
      ON countries.code = cities.country_code
GROUP BY country
ORDER BY cities_num DESC, country
LIMIT 9;
```