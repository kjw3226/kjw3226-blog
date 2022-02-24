---
title: Missing value2 (결측치2)
tag: Missing value2 (결측치2)
date: 2021-12-22
categories:	Python
---
[data file][source/Lecture/covid_data]

# Missing Value : 결측치 확인

### data loading
```python
import pandas as pd
covidtotals = pd.read_csv("../input/covid-data/covidtotals.csv")
covidtotals.head()
```
<실행 화면>

![covid1](https://user-images.githubusercontent.com/96108301/147846380-98019f51-1219-439f-bc60-f1097f36b1b3.PNG)

### data info
```python
covidtotals.info()
```
<실행 화면>

![MissingValue_covid_info](https://user-images.githubusercontent.com/96108301/147846429-e3d9da63-8703-4e23-98dd-ce7c72452189.png)

### data division
 ● 인구통계 관련 column
 ● Covid 관련 column
 
```python
case_vars = ["location", "total_cases", "total_deaths", "total_cases_pm", "total_deaths_pm"]
demo_vars = ["population", "pop_density", "median_age", "gdp_per_capita", "hosp_beds"]
```
### demo_vars column별로 결측치를 측정
```python
covidtotals[demo_vars].isnull().sum(axis = 0) # column별로 결측치를 측정
```
<실행 화면>

![MissingValue_covid_isnullsum](https://user-images.githubusercontent.com/96108301/147846479-8761747a-383b-4917-935f-a749306c7bfd.png)

### case_vars column별로 결측치를 측정
```python
covidtotals[case_vars].isnull().sum(axis = 0) # column별로 결측치를 측정
```
<실행 화면>

![MissingValue_covid_nullSum](https://user-images.githubusercontent.com/96108301/147846480-12fd6243-cad4-4edd-8e75-1eed209ccc12.png)

● case_vars 에는 결측치가 없지만, demo_vars에는 결측치가 있는 것을 확인 할 수 있다.

![demo_bars - missing value](https://user-images.githubusercontent.com/96108301/147846501-6aa01ccf-994c-4895-add4-e1c4365fb266.PNG)

위의 column들에 각각 수만큼의 결측치를 확인 할 수 있다.

### 행 방향으로 발생한 결측치 확인
```python
demovars_misscnt = covidtotals[demo_vars].isnull().sum(axis = 1)
demovars_misscnt.value_counts()
```
<실행 화면>
```python
0 156

1 24
2 12
3 10
4 8
dtype: int64
```
```python
covidtotals[case_vars].isnull().sum(axis = 1).value_counts()
```
<실행 화면>
```python
0 210
dtype: int64
```
### 인구통계 데이터가 3가지 이상 누락된 국가를 나열하기
```python
["location"] + demo_vars
covidtotals.loc[demovars_misscnt >= 3, ["location"] + demo_vars].T
```
<실행 화면>

![MissingValue_covid_Location](https://user-images.githubusercontent.com/96108301/147846503-a04dd68d-28d6-4326-929c-4b79e2c8230a.png)

### case에는 누락국가가 없지만, 한번 확인
```python
casevars_misscnt = covidtotals[case_vars].isnull().sum(axis = 1)
casevars_misscnt.value_counts()
```
<실행 화면>
```python
0 210
dtype: int64
```
```python
covidtotals[covidtotals['location'] == "Hong Kong"]
```
```python
temp = covidtotals.copy()
temp[case_vars].isnull().sum(axis = 0)
temp.total_cases_pm.fillna(0, inplace = True)
temp.total_deaths_pm.fillna(0, inplace = True)
temp[case_vars].isnull().sum(axis = 0)
```
<실행 화면>

![MissingValue_covid_Del](https://user-images.githubusercontent.com/96108301/147846504-30b0e734-8f99-452f-85bf-2840b79f86f3.png)

위의 사진은 결측치가 있는지 없는지를 확인 시켜주는 사진이다.
