---
title: SAS Program Practice2
tag: SAS Program Practice2
date: 2022-05-20
categories: SAS
---

오늘은 SAS 프로그램으로 

텍스트를 한번 나눠보는 것을 연습해 보았다.

아래는 내가 검색해서 

찾은 연습 코드고 이걸 응용해서 코딩한게 

그 아래 코드이다.

```python
DATA a1;
bbb=BYTE(65);        /* bbb에는 문자 A 가 저장 */
ccc="안녕 하세요"; /* 안녕 하세요 가운데 빈칸이 하나 있다 */
nccc=COMPRESS(ccc,' '); /* 빈칸이 없어진다 */
size1=LENGTH(ccc); /* 길이가 11; 한글 5글짜에 빈칸 하나 */
size2=LENGTH(nccc); /* 빈칸이 없어졌으므로 길이가 10 */
size3=LENGTH(bbb); /* 길이가 1 */
large=UPCASE('Good Morning'); /* 이 부분은 Good Morning을 모두 대문자로 바꿔준다. */
small=LOWCASE('Good Morning'); /* 이 부분은 Good Morning을 모두 소문자로 바꿔준다. */
str=SUBSTR(large,2,4); /* 변수 large의 2번째부터 4문자를 선택 */
PROC PRINT;  => 이 부분을 입력하면 결과라는 것이 하나 더 출력된다. 지우면 출력 데이터만 나온다.
RUN;
```

아래는 출력결과 창과 결과 창 부분의 사진이다.

![Split text-output data](https://user-images.githubusercontent.com/96108301/169632940-9e7e39a5-55e3-457e-b016-1ff30efc2dbd.PNG)


![Break text - result](https://user-images.githubusercontent.com/96108301/169632942-b0df0bbb-e868-44ba-9986-9427e0a129fa.PNG)

```python
DATA D1;
ddd=BYTE(75);
eee="날씨가 좋네요";
neee=COMPRESS(eee,' ');
size1=LENGTH(eee);
size2=LENGTH(neee);
size3=LENGTH(ddd);
large=UPCASE('The Weather Is Good');
small=LOWCASE('The Weather Is Good');
str=SUBSTR(large,2,4);
PROC PRINT;
RUN;
```

![Split text-output data2](https://user-images.githubusercontent.com/96108301/169633378-5c50baab-b16c-4fc0-9c00-415ab47ac0f9.PNG)


![Break text - result2](https://user-images.githubusercontent.com/96108301/169633379-b9541af8-3dc0-426f-9fee-c969decb6e6e.PNG)