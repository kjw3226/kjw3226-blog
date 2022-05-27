---
title: practice while watching SAS 'wikidocs'-1
tag: practice while watching SAS 'wikidocs'-1
date: 2022-05-26
categories: Everyday life (일상 생활)
---

오늘은 'wikidocs' 홈페이지에 나와있는 

'SAS' 기본 프로그래밍 코드들을 

보며 직접 코딩을 해보면서

각 각의 코드가 어떤 역할을 하는지 

알아보는 시간을 가졌다.

아래의 코드는 내가 실습한 코드들이다.

```python
PROC SORT DATA=SASHELP.CLASS OUT=TEST;
BY AGE;
RUN;
PROC PRINT DATA=TEST;
VAR AGE NAME;
ID AGE;
BY AGE;
RUN;
PROC CONTENTS DATA=SASHELP.CLASS;/*라이브러리SASHELP의 테이블CLASS의 속성정보를 불러옴(CONTENTS)*/
RUN;/*SAS명령어 종료*/
PROC CONTENTS DATA=WORK._ALL_;/*라이브러리 XXX(XXX._ALL_)에 대한 속성정보와 라이브러리 내부에 있는 테이블 전체(XXX._ALL_)에 대한 속성정보를 불러옴(CONTENTS).*/
RUN;/*SAS명령어 종료*/
PROC FREQ DATA=SASHELP.CLASS;
/*FREQ PROCEDURE를 사용하여(PROC FREQ) SASHELP 라이브러리의 CLASS테이블을 불러옴(DATA=SASHELP.CLASS).*/
TABLE AGE NAME;/*변수 AGE와 NAME을 조회함*/
RUN;/*모든 명령어를 종료*/



DATA TEST;/*데이터 TEST를 생성함(DATA)*/
INPUT NAME $ AGE SEX $;/*문자 변수 NAME과 SEX, 숫자 변수 AGE를 생성함(INPUT)*/
CARDS;
OK 1 남
YOU 2 녀
RUN;/*SAS명령어 종료*/

DATA TEST2;/*데이터 TEST를 생성함(DATA)*/
INPUT NAME $ AGE SEX $;/*문자 변수 NAME과 SEX, 숫자 변수 AGE를 생성함(INPUT)*/
CARDS;
OK 1 남 
YOU 2 녀
호날두화이팅 3 남 /*'호날'까지만 출력되고 뒤의 문자는 출력x*/
RUN;/*SAS명령어 종료*/


DATA TEST;/*데이터 TEST를 생성함(DATA)*/
INPUT NAME: $18. AGE SEX $;/*문자 변수 NAME의 포맷을 최대 18글자(알파벳 기준)까지 받아들일 수 있도록 변경합니다(NAME: $18.)  */
CARDS;/*변수별 데이터를 입력함(CARDS)*/
OK 1 남 
YOU 2 녀
호날두화이팅 3 남
;/*변수별로 들어갈 데이터 입력, 이렇게 하면 전체 문자가 출력됨.*/
RUN;/*SAS명령어 종료*/
```


