---
title: separating data(데이터 분리하기)
tag: separating data(데이터 분리하기)
date: 2021-11-15
categories:	Pandas
 
---
오늘은 '데이터 분리하기'를 해보았다.
```python
import pandas as pd

df = pd.DataFrame([{"country":"한국","population":500},{"country":"미국","population":450},{"country":"싱가폴","population":705},
                   {"country":"호주","population":878},{"country":"베트남","population":660},{"country":"대만","population":808}])
```
위 코드는 'DataFrame'에 값을 넣어서 
'DataFrame'을 객체로 다룰 수 있게 미리 만들어주는 코드이다.

이렇게 'DataFrame'을 출력해서 값이 잘 드러갔는지 확인한다.
```python
print(df)
```
![separating data1](https://user-images.githubusercontent.com/93234783/141740601-57459904-4287-4bc4-bde2-9ccbff1429be.PNG)

이렇게 준비가 끝나면 

이제 코딩만 하면된다.

```python
df[df['country'] == '한국'] #여기서 만일 country가 한국일 때를 선택하고 싶다면 아래와 같이 코드를 작성하면 된다.
```
![separating data2](https://user-images.githubusercontent.com/93234783/141740608-05b43971-f466-4097-96b1-1ec7316e37eb.PNG)

```python
#country가 한국이거나 호주일때의 데이터를 추출하고 싶다면 아래와 같이 코드를 작성하면 된다.
df[(df['country']=='한국') | (df['country']=='호주')]
```
![separating data3](https://user-images.githubusercontent.com/93234783/141740609-1516f2bc-c340-472b-b7f3-b8838219372b.PNG)

```python
#country가 한국이 아닌 것 중 population이 800이상인 것을 추출하는 것이다.
df[(df['country']!='한국') & (df['population']>=800)]
```
![separating data4](https://user-images.githubusercontent.com/93234783/141740614-664a1bd7-f7f4-49f4-85a8-ad5255cc2989.PNG)

### 조건을 둘다 만족해야 할때
df[(조건1) & (조건2)]

### 조건 중 하나라도 만족하면 될때
df[(조건1) | (조건2)]

```python
#country가 한국이 아닌 것 중 population이 800이상인 것을 추출하는 것이다.
df[(df['country']!='한국') & (df['population']>=800)]
```
![separating data5](https://user-images.githubusercontent.com/93234783/141740616-3246d27c-a560-4820-9b43-6f80ba4f6091.PNG)

```python
#만일 리스트 조건 안에 포함되는 데이터를 추출하고 싶다면 isin()함수를 사용해주면 된다. 
#만일, country가 [한국, 일본, 대만, 영국, 호주] 리스트에 포함되는 것을 추출하고 싶다면 기존에 
#조건을 여러개 열거했던 것처럼 사용하지 않고 아래 코드와 같은 형태를 사용함으로써 데이터를 추출할 수 있다.
country_list = ['한국', '일본', '대만', '영국', '호주']
df[df['country'].isin(country_list)]
```
![separating data6](https://user-images.githubusercontent.com/93234783/141740618-7998e0d6-c422-4393-8d7d-c74a3fc3abfb.PNG)

```python
#반대로 country 열에 country_list에 포함되지 않는 데이터를 추출하고 싶다면 아래 코드 처럼 위의 코드에서 ~를 붙여 사용하면 된다.
country_list = ['한국', '일본', '대만', '영국', '호주']
df[~df['country'].isin(country_list)]
```
![separating data6](https://user-images.githubusercontent.com/93234783/141740618-7998e0d6-c422-4393-8d7d-c74a3fc3abfb.PNG)

```python
#위처럼 리스트 조건에 포함되는 혹은 포함되지 않는 데이터를 추출할 때, 
#in 혹은 not in 키워드를 사용해도 될 수 있겠다고 하지만, 불가능하다. 
#만일 in 키워드를 사용해 아래 코드와 같이 작성하면 아래 첨부한 사진 같은 오류가 발생할 것이다.
# 잘못된 방식
country_list = ['한국', '일본', '대만', '영국', '호주']
df[df['country'] in country_list]
```
![separating data7](https://user-images.githubusercontent.com/93234783/141741456-6dc41b0f-211e-45db-b974-31217ddcddb8.PNG)

참고 : https://computer-science-student.tistory.com/m/375