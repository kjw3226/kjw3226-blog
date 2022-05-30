---
title: practice while watching SAS 'wikidocs'-3
tag: practice while watching SAS 'wikidocs'-3
date: 2022-05-29
categories: SAS
---

어제와 달리 오늘은 

SAS의 '문자 포맷'과 '날짜 포맷'이라는 것에 대해 알아보았다.

아래 사진과 코드는 모두 'wikidocs'를 참고하였다.

```python
DATA TEST;
INPUT NAME $ AGE;
CARDS;
라이올라 324.5678
;
RUN;
PROC PRINT DATA=TEST;
VAR NAME;
FORMAT NAME $6.;    /*1번 사례*/
RUN;
```

![sas-character format1](https://user-images.githubusercontent.com/96108301/170917836-14511230-f8d5-4f14-894f-8f2f976105d0.PNG)
![sas-character format2](https://user-images.githubusercontent.com/96108301/170917839-8f843a82-04e1-4132-ba29-d1273d48e2c9.PNG)


```python
DATA TEST;
INPUT NAME $ NUMBER;
CARDS;
날짜 3
;
RUN;


PROC PRINT DATA=TEST;
VAR NUMBER;
FORMAT NUMBER DATE10.;    /*1번 사례*/
FORMAT NUMBER YYMMDD10.;    /*2번 사례*/
FORMAT NUMBER WEEKDATE.;    /*3번 사례*/
FORMAT NUMBER WORDDATE.;    /*4번 사례*/
FORMAT NUMBER NLDATE20.;    /*5번 사례*/
FORMAT NUMBER YYMMN6.;    /*6번 사례*/
FORMAT NUMBER MONYY7.;    /*7번 사례*/
FORMAT NUMBER YEAR4.;    /*8번 사례*/
FORMAT NUMBER DATETIME20. ;    /*9번 사례*/
FORMAT NUMBER TIME8. ;    /*10번 사례*/
FORMAT NUMBER HHMM5. ;    /*11번 사례*/
FORMAT NUMBER HOUR5. ;    /*12번 사례*/
RUN;
```

![sas-date format1](https://user-images.githubusercontent.com/96108301/170917954-889ff9e9-1742-49e8-a9b8-f3697165c406.PNG)
![sas-date format2](https://user-images.githubusercontent.com/96108301/170917958-4c7e1de9-0b6d-48e7-a0fe-da6d3399f4fd.PNG)
