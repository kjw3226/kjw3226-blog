---
title: Postgre SQL2(포스트그리 SQL2)
tag: Postgre SQL2(포스트그리 SQL2)
date: 2022-01-11
categories:	SQL
----
 'SQL'의 쿼리문(명령문)의 기초 문법들과 
 
 'Table(테이블)'의 생성과 삭제, 조회, 작업한 파일을 'CSV' 엑셀 파일로 
 
 내보내는 법 등을 실습해봤다.

 아래의 쿼리문들은 오늘 실습한 것들이다.

 기존에 만들어 놓은 'Table'을 조회 하는 코드이다.
```python
SELECT * FROM temp;
```
 생성, 삭제, 조회, 다시 생성, 여러 개의 자료 삽입 등의 '쿼리문'들이다.

 
```python
-- 테이블 생성
CREATE TABLE develop_book(
    book_id INTEGER,
    date DATE,
    name VARCHAR(80)
);

-- 등록된 테이블 리스트 조회
-- CMD 창에서는 \dt 실행하면 확인 가능
SELECT * FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND
    schemaname != 'information_schema';

-- 테이블 삭제
DROP TABLE develop_book;

-- 데이터 생성 및 추가
CREATE TABLE develop_book(
    book_id INTEGER,
    date DATE,
    name VARCHAR(80)
);

-- 데이터 자료 추가하기
INSERT INTO develop_book VALUES(1, '2021-12-22', 'SQL 레시피');

-- 큰 따옴표 입력
INSERT INTO develop_book VALUES(2, '2021-12-23', '"자바의 정석"');

-- 작은 따옴표 입력
INSERT INTO develop_book values(3, '2021-12-24', '''자바의 정석''');

-- Let's go 입력
INSERT INTO develop_book values(4, '2021-12-25', 'I''am book');

-- 조회 하기
SELECT * FROM develop_book;

-- 테이블에 자료 여러 개 추가하기
INSERT INTO develop_book values
(5, '2021-12-30', '책1'),
(6, '2021-12-30', '책2'),
(7, '2021-12-30', '책3'),
(8, '2021-12-30', '책4');

-- 조회하기
SELECT * FROM develop_book;

-- 컬럼 선택 조회
SELECT book_id, name FROM develop_book;

-- Limit 명령어
SELECT * FROM develop_book LIMIT 3;

-- OFFSET 명령어 추가
-- 시작 인덱스
-- 시작 인덱스가 0번째 부터 시작
SELECT * FROM develop_book LIMIT 5 OFFSET 2;

-- ORDER BY
-- 오름차순
SELECT * FROM develop_book
ORDER BY name ASC;

-- 내림차순
SELECT * FROM develop_book
ORDER BY name DESC;

-- WHERE 조건문
SELECT * FROm develop_book
WHERE book_id = 5;

SELECT * FROm develop_book
WHERE book_id <> 5;

-- AS 명령어
SELECT name AS 책제목 from develop_book;
```
다음의 '쿼리문'을 실행하기 위해서는 

[여기][source/Lecture/db_dump.zip]에서 

'db_dump.zip'파일을 다운 받고 따고 폴더를 만들어서

그 안에 압축을 풀고 'postgre SQL'을 실행해야 실습이 가능한 

'쿼리문'이다.

```python
CREATE TABLE populations (
  pop_id                INTEGER     PRIMARY KEY,
  country_code          VARCHAR,
  year                  INTEGER,
  fertility_rate        REAL,
  life_expectancy       REAL,
  size                  REAL
);

CREATE TABLE cities (
  name                    VARCHAR   PRIMARY KEY,
  country_code            VARCHAR,
  city_proper_pop         REAL,
  metroarea_pop           REAL,
  urbanarea_pop           REAL
);

CREATE TABLE countries (
  code                  VARCHAR     PRIMARY KEY,
  name                  VARCHAR,
  continent             VARCHAR,
  region                VARCHAR,
  surface_area          REAL,
  indep_year            INTEGER,
  local_name            VARCHAR,
  gov_form              VARCHAR,
  capital               VARCHAR,
  cap_long              REAL,
  cap_lat               REAL
);
```
'csv'파일을 생성해 내보내는 '쿼리문'이다.
```python
psql -U postgres -d postgres -f student_grade.sql -o grade.csv -F ',' -A -t
```
비교 연산자..& NULL 값 처리...'쿼리문'이다.
```python
SELECT * FROM student_score;

-- 조건문
-- 성적표 만들기
SELECT 
	id
	, name
	, score
	, CASE
		WHEN score <= 100 AND score >= 90 THEN 'A'
		WHEN score <= 89 AND score >= 80 THEN 'B'
		WHEN score <= 79 AND score >= 70 THEN 'C'
		WHEN score <= 69 THEN 'F' 
	  END
FROM student_score;

-- Coalesce 함수
-- 데이터 조회 시, NULL 값을 다른 기본 값으로 치환
-- NULL --> "데이터 없음"

INSERT INTO student_score(name, score)
VALUES ('Hello', NULL), ('Hi', NULL);


SELECT * FROM student_score;

-- COALESCE() 
-- 조회
SELECT 
	id
	, name
	, score
	, CASE
		WHEN score <= 100 AND score >= 90 THEN 'A'
		WHEN score <= 89 AND score >= 80 THEN 'B'
		WHEN score <= 79 AND score >= 70 THEN 'C'
		WHEN COALESCE(score, 0) <= 69 THEN 'F' 
	  END
FROM student_score;

-- NULLIF
-- NULL값 반환
SELECT NULLIF(10, 10) AS column1; 

-- 첫번째 인수만 가져오기
SELECT NULLIF(11, 12) AS column2;

-- SELECT 절 사칙연산
SELECT 100 + 10 AS column3;
SELECT 100 + 10 AS column3;
SELECT 100 + 10 AS column3;
SELECT 100 + 10 AS column3;

SELECT 100/0 AS column4;


SELECT * FROM division_by_zero;

SELECT 
	students 
	, COALESCE((12/NULLIF(students, 0))::char, '나눌 수 없음') AS column7	
FROM division_by_zero;
```
아래는 오늘 실습하기 전 했던 환경세팅의 내용들이다.

먼저 맨 처음 받은 'db_dump.zip'파일을 바탕화면에 'SQL'이라는 폴더를
별도로 만들고 그안에 압축을 풀어준다.

그리고 'Postgre SQL' 프로그램을 켜둔뒤 

다시 'SQL' 폴더로 가서 압축을 푼 폴더를 오른쪽 마우스로 클릭하고,

'Git Bash here'로 연다. 그리고 'cd sample_data'를 치고 

아래의 코드를 쳐서 'db_dump' 폴더의 파일을 테이블로 
'Postgre SQL'안에 넣어줘서 생성 시킨다.

```python
psql -U postgres -d green -f function_example.dump
```


< postgres SQL 환경 변수 세팅>
- 'File' 메뉴에서 'Preferances'를 들어가서 'PostgreSQL Binary Path' 에서 자신이 
  설치한 버전에 해당되는 곳에 프로그램이 설치된 경로를 복,붙 한다.
  (EX 14버전이면 'C:\Program Files\PostgreSQL\14\bin\' 이렇게 복,붙.)

< 환경 세팅 후에는....>
- Table 목록에 있는 불러온 Table을 선택하고 오른쪽 마우스를 클릭, 'import'를 누르고 
  'import/Export'를 눌러 'import'로 바꾸고, 'Filename'에서 '...'을 눌러 파일이 있는 경로로 이동해 
  해당 파일을 선택한다.
  밑에 'Header' 를 클릭해 'YES'로 바꾸고 'Delimiter'에서 ','를 선택하고 'ok'를 누르면 끝!!

<pychram DB 환경 세팅>
- 'File'을 누르고 'Setthing'을 클릭, 'Plugin'에서 'data base'를 검색해서 'install' 누른다.
- 그리고 'View'에서 'DB Browser'를 선택하고 '+'를 눌러 'Postgre SQL'을 클릭한다. 
- 그런 다음 창이 뜨면 'User'에는 'postgres'를 입력하고 'Password'에는 자신이 설정한 비번(나는 '531014')를
  입력한다. 
- 'Test Connection' 눌러서 'DB Navigtor - Connecton successful'이라는 창이 뜨면 'DB' 와 연결이 된거다.
- 'apply'를 누르고 'ok'를 누른다.
- 이제 마지막 단계다. 'Schemas'를 누르고 'public'을 누르면 'Tables'가 보인다. 눌러서 
  'DB'에 있는 'Table' 목록과 일치하면 세팅이 끝난다.
