----
title: PostgreSQL-WINDOW FUNCTION(포스트그리SQL-윈도우 펑션)
tag: PostgreSQL-WINDOW FUNCTION(포스트그리SQL-윈도우 펑션)
date: 2022-01-14
categories:	SQL
----

SQL 쿼리문 형태 중 'WINDOW FUNCTION'에 대해 알아보고

직접 실습도 해봤다.

아래는 실습 쿼리문을 정리 놓은 것이다.

```python
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
먼저 '테이블'을 새로 두개를 추가 하고 

'import/Export'를 눌러 위의 'langusges'와 'economies'의 'csv'파일

있는 경로로 이동해 'csv'파일을 선택하고 안에 넣어서 '테이블'안에 

데이터를 채워준다.

그런데 이 방법말고 다른 방법으로 '테이블'안에 데이터를 넣는 것을 

알아내어 실습 해봤다.

먼저 'Pycharm'을 실행시키고 'Terminal' 창을 열어서

'ls' 명령어로 현재 경로에 'summer_medals.sql' 파일이 있는지 확인하고

없다면 있는 경로로 이동해서 있다면 그 경로에서

'psql -U postgres'를 입력하고 '비번'을 입력해 'Postgre SQL'에 

접속한다. 

그리고 '\i summer_medals.sql'명령어를 입력한다.

그런 다음 'Postgre SQL'을 실행해 '확인' 해보면 

'summer_medals' 테이블이 추가 된걸 확인 할 수있다.

이러한 방법으로도 테이블을 추가 해 줄수 있다는걸 알게되었다.

그 다음으로 'WINDOW FUNCTION' 쿼리문을 실습했다.

![Window function](https://user-images.githubusercontent.com/96108301/149721377-8570fd45-b553-4aba-9b37-4e11d6e4d5cc.PNG)

일반 쿼리문과 'WINDOW FUNCTION'의 가장 큰 차이점은 

연산을 해서 출력을 할 때에 일반 쿼리문을 실행하게 되면 행이 사라지지만

'WINDOW FUNCTION'을 쓰게 되면 행이 사라지지 않는다는 점이다.

```python
select * from summer_medals;

SELECT 
	ROW_NUMBER() OVER() AS ROW_NUM
	, * 
FROM summer_medals;

SELECT DISTINCT year
	FROM summer_medals
	ORDER BY year ASC;

SELECT 
	year,
	ROW_NUMBER() OVER() AS ROW_NUM
FROM (
	SELECT DISTINCT year
	FROM summer_medals
	ORDER BY year ASC
) AS years;
```
조건을 주고 거기에 맞는 조건문 쿼리를 작성해 봤다.