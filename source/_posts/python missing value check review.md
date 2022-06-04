---
title: python missing value check review
tag: python missing value check review
date: 2022-06-04
categories:	Python
---

오늘은 '구글 코랩' 에서

파이썬으로 '코로나-19' 관련 자료를 

활용해서 '결측치'가 있는지 없는지 

확인하는 코드를 다시 한번 복습하고 

이해하는 시간을 가졌다.

아래는 내가 실습한 코드들이다.

```python
from google.colab import drive
drive.mount('/content/drive') # 구글 드라이브 연동 코드
```

```python
import pandas as pd
covidtotals = pd.read_csv("/content/drive/MyDrive/covid_data/covidtotals.csv")
covidtotals.head()
```

```python
covidtotals.info()
```

```python
case_vars = ["location", "total_cases", "total_deaths", "total_cases_pm", "total_deaths_pm"]
demo_vars = ["population", "pop_density", "median_age", "gdp_per_capita", "hosp_beds"]
# case -> 인구통계 관련 column
# demo -> Covid-19 관련 column
```

```python
covidtotals[demo_vars].isnull().sum(axis = 0) # column별로 결측치를 측정
# demo_vars column별로 결측치를 측정
```

```python
covidtotals[case_vars].isnull().sum(axis = 0) # column별로 결측치를 측정
# case_vars column별로 결측치를 측정
```

```python
demovars_misscnt = covidtotals[demo_vars].isnull().sum(axis = 1)
demovars_misscnt.value_counts()
# 행 방향으로 발생한 결측치 확인
```

```python
["location"] + demo_vars
covidtotals.loc[demovars_misscnt >= 3, ["location"] + demo_vars].T
# 인구 통계 관련 데이터 3가지 이상 누락된 국가 나열하기
```

```python
# case에는 누락국가가 없지만, 한번 확인
casevars_misscnt = covidtotals[case_vars].isnull().sum(axis = 1)
casevars_misscnt.value_counts()
```

```python
temp = covidtotals.copy()
temp[case_vars].isnull().sum(axis = 0)
temp.total_cases_pm.fillna(0, inplace = True)
temp.total_deaths_pm.fillna(0, inplace = True)
temp[case_vars].isnull().sum(axis = 0)
# 결측치를 모두 0으로 만드는 코드
```

이 후에 결측치가 없는지 다시 한번 확인!!

![missing value 0](https://user-images.githubusercontent.com/96108301/171993048-4b10ce2b-7fed-4e34-aa05-7a8b3d741abc.png)