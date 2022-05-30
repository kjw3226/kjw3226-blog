---
title: practice while watching SAS 'wikidocs'-4
tag: practice while watching SAS 'wikidocs'-4
date: 2022-05-30
categories: SAS
---

오늘은 'wikidocs' 홈페이지를 참고해서 

'SAS 데이터 전처리 명령어'에 대해서 알아보았다.

아래의 사진은 'wikidocs' 홈페이지에 있는 코드에 대한 추가적인 설명이고

코드도 'wikidocs' 홈페이지에 있는 것이지만 실습은 내가 직접 코딩하면서 진행했다.

![sas data-preprocessing command](https://user-images.githubusercontent.com/96108301/170959519-587b7abd-524d-4e4c-bddb-edd16b60e72f.PNG)


![sas data-preprocessing command2](https://user-images.githubusercontent.com/96108301/170959522-246be4dc-2cca-4355-ba1a-19ad04f5856c.PNG)

![sas data-preprocessing command3](https://user-images.githubusercontent.com/96108301/170959524-916eaf2e-185d-4894-a626-38eb357dc068.PNG)

```python
DATA TEST;/*테이블 TEST를 생성합니다.*/
SET SASHELP.CLASS(KEEP=NAME AGE);/*테이블 SASHELP.CLASS를 불러오되 칼럼AGE와 NAME만을 유지합니다.*/
RUN;/*SAS명령어를 종료합니다.*/

DATA TEST;/*테이블 TEST를 생성합니다.*/
SET SASHELP.CLASS(DROP=NAME AGE);/*테이블 SASHELP.CLASS를 불러오되 칼럼 AGE와 NAME을 버립니다.*/
RUN;/*SAS명령어를 종료합니다.*/

DATA TEST(KEEP=NAME AGE);/*테이블 TEST를 생성하되 칼럼 NAME과 AGE만 유지합니다.*/
SET SASHELP.CLASS;/*테이블 SASHELP.CLASS를 불러옵니다.*/
RUN;/*SAS명령어를 종료합니다.*/
```

![sas data-preprocessing command4](https://user-images.githubusercontent.com/96108301/170959528-946ec1ac-2802-4c0f-b3ba-a7f4ee21a872.PNG)


![sas data preprocessing command - formula calculation](https://user-images.githubusercontent.com/96108301/170960166-1c262f2f-9834-4a42-a10a-a1232473a94e.PNG)

![sas data preprocessing command - formula calculation2](https://user-images.githubusercontent.com/96108301/170960442-40ca03e7-8702-48af-9adb-36b42d11ae92.PNG)

```python
DATA TEST;/*테이블 TEST를 생성합니다.*/
SET SASHELP.CLASS;/*테이블 SASHELP.CLASS를 불러옵니다.*/
AGE2=AGE+1;/*칼럼 AGE2를 생성합니다. 칼럼 AGE2는 칼럼 AGE에 1을 더한 값입니다.*/
RUN;/*SAS명령어를 종료합니다.*/
```
<출력 화면>
![sas data preprocessing command - formula calculation3](https://user-images.githubusercontent.com/96108301/170961627-056969ab-0ca4-4afd-ba31-06fe159ba9e4.PNG)

SASHELP.CLASS에서 데이터를 불러오고 다음으로 칼럼 AGE2를 생성합니다. 칼럼 AGE2는 기존에 있던 칼럼 AGE의 값에 1씩을 더한 것이 됩니다.

```python
DATA TEST;/*테이블 TEST를 생성합니다.*/
SET SASHELP.CLASS;/*테이블 SASHELP.CLASS를 불러옵니다.*/
AGE+1;/*칼럼 AGE에 1을 더한 값을 저장합니다.*/
AGE2=AGE+1;/*칼럼 AGE2를 생성합니다. 칼럼 AGE2는 칼럼 AGE에 1을 더한 값입니다.*/
RUN;/*SAS명령어를 종료합니다.*/
```

<출력 화면>
![sas data preprocessing command - formula calculation4](https://user-images.githubusercontent.com/96108301/170961642-fb7dd352-1a78-4125-bdd8-ff6fcb8d25a3.PNG)

변수AGE2를 생성한 다음 칼럼 AGE를 수정합니다. AGE+1로써 칼럼 AGE에 1씩을 더한 값을 출력합니다.

![sas data preprocessing command - simple if syntax](https://user-images.githubusercontent.com/96108301/170962035-2f8caa29-a27a-4487-be57-90f93715af7c.PNG)

![sas data preprocessing command - simple if syntax2](https://user-images.githubusercontent.com/96108301/170962310-3b9ecb2a-0859-40ac-bef5-4020a08494e7.PNG)

```python
DATA TEST;/*테이블 TEST를 생성합니다.*/
SET SASHELP.CLASS;/*테이블 SASHELP.CLASS를 불러옵니다.*/
IF AGE=12;/*칼럼 AGE가 12인 행들만 선택합니다. */
RUN;/*SAS명령어를 종료합니다.*/
```

<출력 화면>
![sas data preprocessing command - simple if syntax3](https://user-images.githubusercontent.com/96108301/170962547-4066e021-3804-4e70-b9dd-422981f2b175.PNG)

예제.1에서는 IF문으로 칼럼 AGE=12를 지정합니다. 이 결과값으로 AGE값이 12인 행들이 선택되어 출력됩니다.

![sas data preprocessing command - column conversion using simple if statement](https://user-images.githubusercontent.com/96108301/170963062-5fcd7222-212b-4f22-81bc-60e4ab362a47.PNG)

![sas data preprocessing command - column conversion using simple if statement2](https://user-images.githubusercontent.com/96108301/170963104-a48be542-65e5-4ab7-ab49-c9dcb955ec6e.PNG)

```python
DATA TEST;/*테이블 TEST를 생성합니다.*/
SET SASHELP.CLASS;/*테이블 SASHELP.CLASS를 불러옵니다*/
IF AGE=12 THEN HEIGHT+300;/*칼럼 AGE가 12이면 칼럼 HEIGHT값에 300을 더합니다.*/
RUN;/*SAS명령어를 종료합니다.*/
```

<출력 화면>
![sas data preprocessing command - column conversion using simple if statement-result1](https://user-images.githubusercontent.com/96108301/170964422-2473e053-7d9d-4dab-95fc-8d96f8c5df12.PNG)

예제1은 IF와 THEN으로 이루어져 있습니다. 칼럼 AGE가 12인 행이 있다면 칼럼 HEIGHT에 각각 300씩을 더하라는 명령어입니다. 칼럼 HEIGHT 모든 값에 300을 더하는 게 아니라 칼럼 AGE가 12인 행에만 300씩을 더합니다.

```python
DATA TEST;/*테이블 TEST를 생성합니다.*/
SET SASHELP.CLASS;/*테이블 SASHELP.CLASS를 불러옵니다.*/
IF AGE=12 THEN DELETE;/*칼럼 AGE가 12이면 해당 행을 삭제합니다.*/
RUN;/*SAS명령어를 종료합니다.*/
```

<출력 화면>
![sas data preprocessing command - column conversion using simple if statement-result2](https://user-images.githubusercontent.com/96108301/170964430-9c97ad66-fd66-4d82-ab90-82cc27d5d8b9.PNG)

예제2도 동일한 방식입니다. 여기서는 칼럼 AGE가 12일 경우 해당 행을 삭제(DELETE)하도록 명령을 합니다. 그래서 출력값을 보면 칼럼 AGE가 12인 값을 찾을 수 없습니다.

```python
DATA TEST;/*테이블 TEST를 생성합니다.*/
SET SASHELP.CLASS;/*테이블 SASHELP.CLASS를 불러옵니다.*/
IF AGE=12 THEN NEW='새로운칼럼';/*칼럼 AGE가 12이면 새로운 칼럼 NEW에 ‘새로운칼럼’이라는 값을 줍니다.*/
RUN;/*SAS명령어를 종료합니다.*/
```

<출력 화면>
![sas data preprocessing command - column conversion using simple if statement-result3](https://user-images.githubusercontent.com/96108301/170964432-713c0e02-a9df-4829-96d4-a27beae3a2e2.PNG)

예제3은 새로운 칼럼을 생성하는 명령어입니다. 
칼럼 AGE가 12일 경우 새로운 칼럼 NEW를 생성하고 거기에 ‘새로운칼럼’이라는 값을 입력하는 명령어입니다. 
여기서도 예제1과 유사하게 칼럼 NEW 전체에 ‘새로운칼럼’ 값을 입력하는 게 아니라 칼럼 AGE가 12인 행에만 ‘새로운칼럼’값을 입력합니다. 
만약 칼럼 NEW 전체에 ‘새로운칼럼’이라는 값을 입력하고 싶으시다면 IF문을 사용할 필요없이 ‘NEW=‘새로운칼럼’’라는 명령어를 입력해주시면 됩니다.

```python
DATA TEST;
SET SASHELP.CLASS;
IF AGE=12 THEN NEW='새로운칼럼';
ELSE IF AGE=13 THEN NEW='새로운칼럼2';
ELSE NEW='새칼럼';
RUN;
```

<출력 화면>

![sas data preprocessing command - column conversion using simple if statement-result4](https://user-images.githubusercontent.com/96108301/170964434-454ae9d2-6e8f-44ca-b576-80e26e83a4af.PNG)

예제4처럼 IF AGE=12 THEN NEW=‘새로운칼럼’ 명령어가 종료된 다음 ELSE명령어에 의해 AGE=13 THEN NEW=‘새로운칼럼2’가 입력됐습니다. 
마지막 ELSE명령어에는 조건문이 없습니다. 그래서 이외의 값들에 대해서 NEW=‘새칼럼’를 입력하는 명령어가 실행됩니다. 
이 경우에는 AGE가 12,13이 아닌 11,14,15,16인 행에 NEW=‘새칼럼’라는 데이터가 입력됩니다. 
그 결과는 위의 표와 같습니다. ELSE명령어는 IF명령어를 마친 다음에 세트처럼 사용할 수 있는 명령어입니다. 
IF명령어를 추가하거나, IF명령어 이외의 값에 대해 데이터를 새로 생성하거나 변경하고 싶을 경우 사용하면 됩니다.

![sas data preprocessing command - column conversion using simple if statement tip](https://user-images.githubusercontent.com/96108301/170965369-bd35e93c-142c-4226-a7a7-07a98d759c38.PNG)


