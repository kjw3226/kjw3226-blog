----
title: Postgre SQL4 (포스트그리 SQL4)
tag: Postgre SQL4 (포스트그리 SQL4)
date: 2022-01-13
categories:	SQL
----
오늘은 '서브쿼리문'에 대해 실습을 진행했다.

아래는 실습한 '서브쿼리문'이다.
```python
---- 테이블 생성
CREATE TABLE languages (
  lang_id               INTEGER     PRIMARY KEY,
  code                  VARCHAR,
  name                  VARCHAR,
  percent               REAL,
  official              BOOLEAN
);

CREATE TABLE economies (
  econ_id               INTEGER     PRIMARY KEY,
  code                  VARCHAR,
  year                  INTEGER,
  income_group          VARCHAR,
  gdp_percapita         REAL,
  gross_savings         REAL,
  inflation_rate        REAL,
  total_investment      REAL,
  unemployment_rate     REAL,
  exports               REAL,
  imports               REAL
);
```
이렇게 테이블을 생성하고 'Table'목록에 있는 해당 테이블을 선택하고

오른 쪽 마우스를 클릭해 'Import'를 누르고 'import','Export' 라고 

표시되는 버튼을 눌러 'Import' 로 바꿔놓고

테이블명의 'csv'파일이 있는 경로를 들어가서 csv 파일을 선택후 'ok'를 누른다 

그리고 'Header'를 누르고 ','를 선택하고 'ok'를 누른다.

'Table'을 2개 생성했으니 이 작업을 2번 반복한다.

테이블이 잘 생성되었는지 확인한다.

```python
select * from languages;

select * from economies;
```

```python
--- 질문: 각 나라별 언어의 갯수 구하기
--- Table: languages
select code, count(*) as lang_num
FROM languages
GROUP BY code;

--- 질문, code를 country로 변경, 언어의 갯수 구하기
--- lang_num 내림차순 정렬함

SELECT * FROM countries;

SELECT code, count(*) as lang_num
FROM languages
GROUP BY code;

--- 질문, code를 country로 변경, 언어의 갯수 구하기
--- lang_num 내림차순 정렬함

Select local_name, lang_num, subquery.lang_num
FROM countries
	, (SELECT code, count(*) as lang_num
       FROM languages
       GROUP BY code) as subquery
WHERE countries.code = subquery.code
ORDER BY lang_num DESC;

-- 
SELECT * FROM economies
WHERE year = 2015;


-- 코드별 inflation_rate
-- 각 대륙별, 각 나라별 inflation_rate
-- 각 대륙에서 inflation_rate가 가장 높은 나라를 구하고, inflation_rate
ASIA, KOREA, 10.0
Europe, England, 20.0
Africa
North America

SELECT name, continent, inflation_rate
  -- From countries
  FROM countries
    -- INNER JOIN economies
    INNER JOIN economies
    -- ON
    ON countries.code = economies.code
  -- Where year is 2015
  WHERE year = 2015
    -- (alias as subquery)
    AND inflation_rate IN (
        SELECT MAX(inflation_rate) AS max_inf
        FROM (
             SELECT name, continent, inflation_rate
             FROM countries
             INNER JOIN economies
             -- Using(code) 대신 ON 쿼리를 작성합니다.
             ON countries.code = economies.code
             WHERE year = 2015) AS subquery
      -- Group by continent
        GROUP BY continent);
```
정리하면 실습을 통해 알수 있는 것은 아래와 같이 

3가지 방법으로 '서브쿼리문'을 작성 할 수 있다는 것이다.

```python
서브쿼리 3가지 방법
- WHERE 서브쿼리
- SELECT 서브쿼리
- FROM 서브쿼리
```