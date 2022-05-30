---
title: practice while watching SAS 'wikidocs'-2
tag: practice while watching SAS 'wikidocs'-2
date: 2022-05-28
categories: SAS
---

오늘은 

'wikidocs' 홈페이지를 보고 sas의 '숫자 포맷'이라고 하는 것에 대해 알아보았다.

아래 사진과 코드는 내가 직접 실습한 코드와 'wikidocs' 홈페이지에 

나와있는 코드에 대한 추가 설명들이다.

![sas-number format1](https://user-images.githubusercontent.com/96108301/170916808-27052a04-4a25-4f82-b1b8-d564ef364aef.PNG)
![sas-number format2](https://user-images.githubusercontent.com/96108301/170916814-29959c5f-9896-4301-a82c-dbcfc4ab034e.PNG)

```python
DATA TEST;
INPUT NAME $ AGE;
CARDS;
라이올라 324.5678 /* 이 코드를 입력하면 '라이올라'에서 '라이'만 출력됨.*/
;


DATA TEST;
INPUT NAME: $14. AGE $;
CARDS;
라이올라 324.5678 /* 이 코드를 입력하면 '라이올라' 전부 출력됨.*/
;
RUN;


PROC PRINT DATA=TEST;
VAR AGE;
FORMAT AGE 5.;    /*1번 사례*/
FORMAT AGE 6.2;   /*2번 사례*/
FORMAT AGE BEST5.;   /*3번 사례*/
FORMAT AGE COMMA5.;   /*4번 사례*/
FORMAT AGE PERCENT8.2;   /*5번 사례*/
FORMAT AGE Z7.2;   /*6번 사례*/
RUN;
```

