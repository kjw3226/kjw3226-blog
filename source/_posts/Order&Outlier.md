---
title: Order & Find outliers(주문과 이상치 찾기)
tag: Order & Find outliers(주문과 이상치 찾기)
date: 2021-12-21
categories:	Python
---
python을 활용해 'restaurant,order' 와 'covid' 데이터를 이용해서

'이상치 찾기' 를 실습 해 보았다.

```python
# /c/Program Files/Anaconda3/python/envs/python-test
# -*- conding: utf-8 -*-

class Comments:
    title     = "#### %s 레스토랑에 오신걸 환영합니다. ####"

    product_description  = "%s:%s(%s원)"

    insert_price         = "\n요금을 넣어 주세요. : "

    insufficient_price    = "%s 요금이 부족합니다. 거스름돈은 %s원 입니다."

    select_menu          = "원하시는 메뉴를 선택하세요."

    select_error         = "잘못 입력하셨습니다."


    finish_sale          = "선택하신 %s 입니다. 거스름돈은 %s원 입니다.\n감사합니다."
    terminate_sale       = "주문을 종료합니다."

class Menus:
    food_names  = []
    food_prices = []
```
```python
# /c/Program Files/Anaconda3/python/envs/python-test
# -*- conding: utf-8 -*-

from restaurant import Comments, Menus

all_menus = [
            {"menu": "김밥", "price": 1500},
            {"menu": "떡볶이", "price": 1800},
            {"menu": "우동", "price": 2000},
            {"menu": "라면", "price": 2500}
        ]

class Order(Menus):
    # class attribute 
    _data = all_menus
    _name = "김밥천국"
    _status = True

    def __init__(self):
        print(Comments.title %self._name)

    def set_products(self):
        Menus.food_names  = []
        Menus.food_prices = []
        for food in self._data:
            Menus.food_names.append(food["menu"])
            Menus.food_prices.append(food["price"])

    def run(self):
        self.set_products()
        while self._status:
            try:
                inputMoney = int(input(Comments.insert_price))
            except ValueError:
                print(Comments.select_error)
            else:
                self.selectMenu(inputMoney)

    def selectMenu(self, money):
        print(Comments.select_menu)
        for idx, name in enumerate(Menus.food_names):
            price = Menus.food_prices[idx]
            print(Comments.product_description %(str(idx), name, price))
        inputFood = int(input(Comments.select_menu))
        self.payment(money, inputFood)

    def payment(self, money, idx):
        name = Menus.food_names[idx]
        price = Menus.food_prices[idx]
        if money >= price:
            balance = money - price
            print(Comments.finish_sale %(name, str(balance)))
        else:
            print(Comments.insufficient_price %(name, str(money)))

if __name__ == "__main__":
    order = Order()
    try:
        order.run()
    except KeyboardInterrupt:
        order._status = False
        print(Comments.terminate_sale)
```
<실행 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Program Files/anaconda3/envs/python-P/python-test/order.py"
#### 김밥천국 레스토랑에 오신걸 환영합니다. ####

요금을 넣어 주세요. : 1500
원하시는 메뉴를 선택하세요.
0:김밥(1500원)
1:떡볶이(1800원)
2:우동(2000원)
3:라면(2500원)
원하시는 메뉴를 선택하세요.0
선택하신 김밥 입니다. 거스름돈은 0원 입니다.
감사합니다.

요금을 넣어 주세요. : 
```
이런 식으로 가격을 입력하고 메뉴를 번호로 선택하면 

해당 메뉴를 선택했다는 것과 거스름돈을 계산해서 출력해 주는 

코드이다.

다음은 '결측치 찾기' 코드이다.

<결측치 확인>
```python
import pandas as pd
covidtotals = pd.read_csv("data/covidtotalswithmissings.csv")
covidtotals.head()
```
<실행 화면>

![missing value1](https://user-images.githubusercontent.com/96108301/147823771-ad4a3313-0020-49cc-9fd7-de0c57b3c9f0.PNG)

- 일부 feature 에서 Missing Values 확인

```python
covidtotals.info()
```
<실행 화면>

![missing value2](https://user-images.githubusercontent.com/96108301/147823857-579ca682-2662-46dc-9e12-89546a4903d1.PNG)

- 리스트 작성
    ● 인구통계 관련 column
    ● Covid 관련 column
```python
case_vars = ["location", "total_cases", "total_deaths", "total_cases_pm", "total_deaths_pm"]
demo_vars = ["population", "pop_density", "median_age", "gdp_per_capita", "hosp_beds"]
```
```python
["location"] + demo_vars
```
```python
covidtotals[demo_vars].isnull().sum(axis = 0) # column별로 결측치를 측정
```
<실행 화면>

![missing value3](https://user-images.githubusercontent.com/96108301/147824020-a2625700-fa4f-4516-91b2-317e74dfb8a0.PNG)

```python
covidtotals[case_vars].isnull().sum(axis = 0) # column별로 결측치를 측정
```
![missing value4](https://user-images.githubusercontent.com/96108301/147824021-1c260158-4bfb-4e11-b6a0-ed59074f674c.PNG)

- 행 방향으로 발생한 결측치 확인
```python
demovars_misscnt = covidtotals[demo_vars].isnull().sum(axis = 1)
demovars_misscnt.value_counts()
```
<실행 화면>

![missing value5](https://user-images.githubusercontent.com/96108301/147824254-aad35518-414d-4e4d-83f2-e7abbc7f85b0.PNG)

```python
covidtotals[case_vars].isnull().sum(axis = 1).value_counts()
```
<실행 화면>

![missing value6](https://user-images.githubusercontent.com/96108301/147824256-57514c98-b19d-4549-a22d-77c08ede446e.PNG)

- 인구통계 데이터가 3가지 이상 누락된 국가를 나열하기
```python
["location"] + demo_vars
```
<실행 화면>

![missing value7](https://user-images.githubusercontent.com/96108301/147824257-01333101-4abe-4da8-b476-0aed7d407c66.PNG)

```python
covidtotals.loc[demovars_misscnt >= 3, ["location"] + demo_vars].T
```
<실행 화면>

![missing value8](https://user-images.githubusercontent.com/96108301/147824258-ecc13cec-ac22-4a19-a76a-d47340a74f14.PNG)

- case 누락 국가 확인
```python
casevars_misscnt = covidtotals[case_vars].isnull().sum(axis = 1)
casevars_misscnt.value_counts()
```
<실행 화면>

![missing value9](https://user-images.githubusercontent.com/96108301/147824259-9b6b10d8-119b-4c4c-8e43-6a80cf9cf7be.PNG)

```python
covidtotals.loc[casevars_misscnt == 2, ["location"] + case_vars].T
```
<실행 화면>

![missing value10](https://user-images.githubusercontent.com/96108301/147824260-ceb6c475-3b70-4f38-8550-afa2231422a8.PNG)

```python
covidtotals[covidtotals['location'] == "Hong Kong"]
```
<실행 화면>

![missing value11](https://user-images.githubusercontent.com/96108301/147824262-f5148fc5-c093-4e91-b9e4-ca2f83091907.PNG)

```python
temp = covidtotals.copy()
temp
```
<실행 화면>

![missing value12](https://user-images.githubusercontent.com/96108301/147824565-da290110-eb96-4c3f-b734-4d3a19ef2a8f.PNG)

```python
temp[case_vars].isnull().sum(axis = 0)
```
<실행 화면>

![missing value13](https://user-images.githubusercontent.com/96108301/147824566-c115bd84-46bd-45e6-a5ab-4e64ce8e2004.PNG)

```python
temp.total_cases_pm.fillna(0, inplace = True)
temp.total_deaths_pm.fillna(0, inplace = True)
```
```python
temp[case_vars].isnull().sum(axis = 0)
```
<실행 화면>

![missing value14](https://user-images.githubusercontent.com/96108301/147824568-cd281e21-b379-4ebd-9b34-9ab0bab28291.PNG)
