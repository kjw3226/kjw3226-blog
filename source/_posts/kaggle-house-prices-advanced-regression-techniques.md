---
title: kaggle-house-prices-advanced-regression-techniques
tag: kaggle-house-prices-advanced-regression-techniques
date: 2021-12-10
categories:	kaggle
---
오늘은 'kaggle' 대회 사이트에서

'house-prices-advanced-regression-techniques' 데이터를 

가져와서 '데이터 전처리' ~ 'ML 모형 평가' 까지 한번 해 보았다.

# 데이터 불러오기
- 변수를 줄여야겠다! 
- 어떤 변수를 줄여야할까? 

```python
import pandas as pd 
train = pd.read_csv("/kaggle/input/house-prices-advanced-regression-techniques/train.csv")
test = pd.read_csv("/kaggle/input/house-prices-advanced-regression-techniques/test.csv")

train.shape, test.shape
```
<결과 화면>
```python
((1460, 81), (1459, 80))
```
## EDA
- 이상치 제거, 중복값 제거
- overallQual 변수, 판매가 상승 
- 평점 1, 판매가 엄청 비쌈 <-- 이상치
```python
train.info() # 'train' 데이터 확인하기
```
<결과 화면>
```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1460 entries, 0 to 1459
Data columns (total 81 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Id             1460 non-null   int64  
 1   MSSubClass     1460 non-null   int64  
 2   MSZoning       1460 non-null   object 
 3   LotFrontage    1201 non-null   float64
 4   LotArea        1460 non-null   int64  
 5   Street         1460 non-null   object 
 6   Alley          91 non-null     object 
 7   LotShape       1460 non-null   object 
 8   LandContour    1460 non-null   object 
 9   Utilities      1460 non-null   object 
 10  LotConfig      1460 non-null   object 
 11  LandSlope      1460 non-null   object 
 12  Neighborhood   1460 non-null   object 
 13  Condition1     1460 non-null   object 
 14  Condition2     1460 non-null   object 
 15  BldgType       1460 non-null   object 
 16  HouseStyle     1460 non-null   object 
 17  OverallQual    1460 non-null   int64  
 18  OverallCond    1460 non-null   int64  
 19  YearBuilt      1460 non-null   int64  
 20  YearRemodAdd   1460 non-null   int64  
 21  RoofStyle      1460 non-null   object 
 22  RoofMatl       1460 non-null   object 
 23  Exterior1st    1460 non-null   object 
 24  Exterior2nd    1460 non-null   object 
 25  MasVnrType     1452 non-null   object 
 26  MasVnrArea     1452 non-null   float64
 27  ExterQual      1460 non-null   object 
 28  ExterCond      1460 non-null   object 
 29  Foundation     1460 non-null   object 
 30  BsmtQual       1423 non-null   object 
 31  BsmtCond       1423 non-null   object 
 32  BsmtExposure   1422 non-null   object 
 33  BsmtFinType1   1423 non-null   object 
 34  BsmtFinSF1     1460 non-null   int64  
 35  BsmtFinType2   1422 non-null   object 
 36  BsmtFinSF2     1460 non-null   int64  
 37  BsmtUnfSF      1460 non-null   int64  
 38  TotalBsmtSF    1460 non-null   int64  
 39  Heating        1460 non-null   object 
 40  HeatingQC      1460 non-null   object 
 41  CentralAir     1460 non-null   object 
 42  Electrical     1459 non-null   object 
 43  1stFlrSF       1460 non-null   int64  
 44  2ndFlrSF       1460 non-null   int64  
 45  LowQualFinSF   1460 non-null   int64  
 46  GrLivArea      1460 non-null   int64  
 47  BsmtFullBath   1460 non-null   int64  
 48  BsmtHalfBath   1460 non-null   int64  
 49  FullBath       1460 non-null   int64  
 50  HalfBath       1460 non-null   int64  
 51  BedroomAbvGr   1460 non-null   int64  
 52  KitchenAbvGr   1460 non-null   int64  
 53  KitchenQual    1460 non-null   object 
 54  TotRmsAbvGrd   1460 non-null   int64  
 55  Functional     1460 non-null   object 
 56  Fireplaces     1460 non-null   int64  
 57  FireplaceQu    770 non-null    object 
 58  GarageType     1379 non-null   object 
 59  GarageYrBlt    1379 non-null   float64
 60  GarageFinish   1379 non-null   object 
 61  GarageCars     1460 non-null   int64  
 62  GarageArea     1460 non-null   int64  
 63  GarageQual     1379 non-null   object 
 64  GarageCond     1379 non-null   object 
 65  PavedDrive     1460 non-null   object 
 66  WoodDeckSF     1460 non-null   int64  
 67  OpenPorchSF    1460 non-null   int64  
 68  EnclosedPorch  1460 non-null   int64  
 69  3SsnPorch      1460 non-null   int64  
 70  ScreenPorch    1460 non-null   int64  
 71  PoolArea       1460 non-null   int64  
 72  PoolQC         7 non-null      object 
 73  Fence          281 non-null    object 
 74  MiscFeature    54 non-null     object 
 75  MiscVal        1460 non-null   int64  
 76  MoSold         1460 non-null   int64  
 77  YrSold         1460 non-null   int64  
 78  SaleType       1460 non-null   object 
 79  SaleCondition  1460 non-null   object 
 80  SalePrice      1460 non-null   int64  
dtypes: float64(3), int64(35), object(43)
memory usage: 924.0+ KB
```

```python
train.drop(train[(train['OverallQual'] < 6) & (train['SalePrice'] > 200000)].index, inplace = True)
train.reset_index(drop = True, inplace = True)
train.shape
```
<결과 화면>
```python
(1452, 81)
```
- 종속변수 시각화 (변환 전)
```python
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

(mu, sigma) = norm.fit(train['SalePrice'])
print("The value of mu before log transformation is:", mu)
print("The value of sigma before log transformation is:", sigma)

fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(train['SalePrice'], color="b", stat="probability")
ax.xaxis.grid(False)
ax.set(ylabel="Frequency")
ax.set(xlabel="SalePrice")
ax.set(title="SalePrice distribution")

plt.axvline(mu, color='r', linestyle='--')
plt.text(mu + 10000, 0.11, 'Mean of SalePrice', rotation=0, color='r')
fig.show()
```
<결과 화면>

The value of mu before log transformation is: 180694.21212121213
The value of sigma before log transformation is: 79566.38005194599
![kaggle-house-price1](https://user-images.githubusercontent.com/96108301/147399787-51345c9b-6240-4e94-bdec-bbf26ef8f21b.png)

- 로그변환 후 종속변수 시각화
```python
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

# 로그변환 코드
train['SalePrice'] = np.log1p(train['SalePrice'])

(mu, sigma) = norm.fit(train['SalePrice'])
print("The value of mu before log transformation is:", mu)
print("The value of sigma before log transformation is:", sigma)

fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(train['SalePrice'], color="b", stat="probability")
ax.xaxis.grid(False)
ax.set(ylabel="Frequency")
ax.set(xlabel="SalePrice")
ax.set(title="SalePrice distribution")

plt.axvline(mu, color='r', linestyle='--')
plt.text(mu + 0.05, 0.105, 'Mean of SalePrice', rotation=0, color='r')
fig.show()
```
<결과 화면>

The value of mu before log transformation is: 12.022489590747329
The value of sigma before log transformation is: 0.3998184355740231
![kaggle-house-price2](https://user-images.githubusercontent.com/96108301/147399819-00cd84c4-b4f9-4162-bf1c-77a89407027a.png)

## 데이터 Feature 제거

- 첫번째. 모형 학습 시간 감소

- 두번째. 연산 시, 노이즈 (Noise, 쓰레기)

```python
train_ID = train["Id"]
test_ID = test["Id"]

train.drop(['Id'], axis = 1, inplace = True)
test.drop(['Id'], axis = 1, inplace = True)
```
```python
train.shape, test.shape
```
<결과 화면>
```python
((1452, 80), (1459, 79))
```
- y값 추출

- 데이터셋 분리, 독립변수 ~ 종속변수

```python
y = train['SalePrice'].reset_index(drop = True)
y.shape

train = train.drop('SalePrice', axis = 1)
train.shape
```
<결과 화면>
```python
(1452, 79)
```
```python
train.shape, test.shape
```
<결과 화면>
```python
((1452, 79), (1459, 79))
```
## 데이터 합치기

- train, test 같이 전처리 

```python
all_df = pd.concat([train, test]).reset_index(drop = True)
all_df.shape
```
<결과 화면>
```python
(2911, 79)
```
# 결측치 확인 / 비율로 구하기

- 빅분기 작업 1유형, 

- 결측치 처리 할 때, 

  - 사전작업: 반드시 유관부서와 확인 (왜 생길까?)
  
  - (1) 제거하기 (Column 제거) / 행만 제거하기 
  
  - (2) 채우기
  
        - numeric, 평균 또는 중간값으로 채우기 / 문자열 최대빈도수로 채우기 (쉬워)
  
  - (3) 채우기 (데이터 보간) ** (실무에서 배우기)
  
        - 통계기법을 활용해서 채우기 / 시계열자료
  
```python
temp = all_df.isnull().sum()
print(temp)

isnull_na = (all_df.isnull().sum() / len(all_df)) * 100
print(isnull_na)
```
<결과 화면>
```python
MSSubClass         0
MSZoning           4
LotFrontage      484
LotArea            0
Street             0
                ... 
MiscVal            0
MoSold             0
YrSold             0
SaleType           1
SaleCondition      0
Length: 79, dtype: int64
MSSubClass        0.000000
MSZoning          0.137410
LotFrontage      16.626589
LotArea           0.000000
Street            0.000000
                   ...    
MiscVal           0.000000
MoSold            0.000000
YrSold            0.000000
SaleType          0.034352
SaleCondition     0.000000
Length: 79, dtype: float64
```

```python
data_na = isnull_na.drop(isnull_na[isnull_na == 0].index).sort_values(ascending=False)
print(data_na)
```
<결과 화면>
```python
PoolQC          99.656475
MiscFeature     96.427345
Alley           93.198214
Fence           80.419100
FireplaceQu     48.746135
LotFrontage     16.626589
GarageFinish     5.427688
GarageQual       5.427688
GarageCond       5.427688
GarageYrBlt      5.427688
GarageType       5.358983
BsmtExposure     2.816901
BsmtCond         2.816901
BsmtQual         2.782549
BsmtFinType2     2.748196
BsmtFinType1     2.713844
MasVnrType       0.824459
MasVnrArea       0.790106
MSZoning         0.137410
BsmtFullBath     0.068705
BsmtHalfBath     0.068705
Functional       0.068705
Utilities        0.068705
GarageArea       0.034352
GarageCars       0.034352
Electrical       0.034352
KitchenQual      0.034352
TotalBsmtSF      0.034352
BsmtUnfSF        0.034352
BsmtFinSF2       0.034352
BsmtFinSF1       0.034352
Exterior2nd      0.034352
Exterior1st      0.034352
SaleType         0.034352
dtype: float64
```

```python
def check_na(data, head_num = 6):
  isnull_na = (data.isnull().sum() / len(data)) * 100
  data_na = isnull_na.drop(isnull_na[isnull_na == 0].index).sort_values(ascending=False)
  missing_data = pd.DataFrame({'Missing Ratio' :data_na, 
                               'Data Type': data.dtypes[data_na.index]})
  print("결측치 데이터 컬럼과 건수:\n", missing_data.head(head_num))

check_na(all_df, 40)
```
<결과 화면>
```python
결측치 데이터 컬럼과 건수:
               Missing Ratio Data Type
PoolQC            99.656475    object
MiscFeature       96.427345    object
Alley             93.198214    object
Fence             80.419100    object
FireplaceQu       48.746135    object
LotFrontage       16.626589   float64
GarageFinish       5.427688    object
GarageQual         5.427688    object
GarageCond         5.427688    object
GarageYrBlt        5.427688   float64
GarageType         5.358983    object
BsmtExposure       2.816901    object
BsmtCond           2.816901    object
BsmtQual           2.782549    object
BsmtFinType2       2.748196    object
BsmtFinType1       2.713844    object
MasVnrType         0.824459    object
MasVnrArea         0.790106   float64
MSZoning           0.137410    object
BsmtFullBath       0.068705   float64
BsmtHalfBath       0.068705   float64
Functional         0.068705    object
Utilities          0.068705    object
GarageArea         0.034352   float64
GarageCars         0.034352   float64
Electrical         0.034352    object
KitchenQual        0.034352    object
TotalBsmtSF        0.034352   float64
BsmtUnfSF          0.034352   float64
BsmtFinSF2         0.034352   float64
BsmtFinSF1         0.034352   float64
Exterior2nd        0.034352    object
Exterior1st        0.034352    object
SaleType           0.034352    object
```
## 결측치 제거

```python
all_df.drop(['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 'LotFrontage'], axis=1, inplace=True)
```
```python
check_na(all_df, 30)
```
<결과 화면>
```python
결측치 데이터 컬럼과 건수:
               Missing Ratio Data Type
GarageCond         5.427688    object
GarageQual         5.427688    object
GarageYrBlt        5.427688   float64
GarageFinish       5.427688    object
GarageType         5.358983    object
BsmtCond           2.816901    object
BsmtExposure       2.816901    object
BsmtQual           2.782549    object
BsmtFinType2       2.748196    object
BsmtFinType1       2.713844    object
MasVnrType         0.824459    object
MasVnrArea         0.790106   float64
MSZoning           0.137410    object
Functional         0.068705    object
Utilities          0.068705    object
BsmtFullBath       0.068705   float64
BsmtHalfBath       0.068705   float64
GarageArea         0.034352   float64
GarageCars         0.034352   float64
TotalBsmtSF        0.034352   float64
KitchenQual        0.034352    object
Electrical         0.034352    object
BsmtUnfSF          0.034352   float64
BsmtFinSF2         0.034352   float64
BsmtFinSF1         0.034352   float64
Exterior2nd        0.034352    object
Exterior1st        0.034352    object
SaleType           0.034352    object
```
- 문자열 채워넣기
```python
print(all_df['BsmtQual'].value_counts())
print(all_df['BsmtQual'].mode()[0])
# all_df['BsmtQual'](결측치가 존재하면) = all_df['BsmtQual'].mode()[0]
```
<결과 화면>
```python
TA    1278
Gd    1206
Ex     258
Fa      88
Name: BsmtQual, dtype: int64
TA
```

```python
# 1. object 컬럼명 추출

import numpy as np 
cat_all_vars = train.select_dtypes(exclude=[np.number])
print("cat vars", len(list(cat_all_vars)))
# cat_all_vars.info()

final_cat_vars = []
for var in cat_all_vars:
    if var not in ['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 'LotFrontage']:
        final_cat_vars.append(var)
        
print("cat vars", len(list(final_cat_vars)))

for i in final_cat_vars:
    all_df[i] = all_df[i].fillna(all_df[i].mode()[0])
    
check_na(all_df, 20)
```
<결과 화면>
```python
cat vars 43
cat vars 38
결측치 데이터 컬럼과 건수:
               Missing Ratio Data Type
GarageYrBlt        5.427688   float64
MasVnrArea         0.790106   float64
BsmtFullBath       0.068705   float64
BsmtHalfBath       0.068705   float64
BsmtFinSF1         0.034352   float64
BsmtFinSF2         0.034352   float64
BsmtUnfSF          0.034352   float64
TotalBsmtSF        0.034352   float64
GarageCars         0.034352   float64
GarageArea         0.034352   float64
```

```python
print(all_df['BsmtQual'].value_counts())
```
<결과 화면>
```python
TA    1359
Gd    1206
Ex     258
Fa      88
Name: BsmtQual, dtype: int64
```
- 수치형 데이터셋 적용

```python
import numpy as np
num_all_vars = list(train.select_dtypes(include=[np.number]))
print("The whole number of all_vars", len(num_all_vars))

num_all_vars.remove('LotFrontage')

print("The whole number of final_cat_vars", len(num_all_vars))
for i in num_all_vars:
  all_df[i].fillna(value=all_df[i].median(), inplace=True)

check_na(all_df, 20)
```
<결과 화면>
```python
The whole number of all_vars 36
The whole number of final_cat_vars 35
결측치 데이터 컬럼과 건수:
 Empty DataFrame
Columns: [Missing Ratio, Data Type]
Index: []
```

```python
all_df.info()
```
<결과 화면>
```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2911 entries, 0 to 2910
Data columns (total 73 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   MSSubClass     2911 non-null   int64  
 1   MSZoning       2911 non-null   object 
 2   LotArea        2911 non-null   int64  
 3   Street         2911 non-null   object 
 4   LotShape       2911 non-null   object 
 5   LandContour    2911 non-null   object 
 6   Utilities      2911 non-null   object 
 7   LotConfig      2911 non-null   object 
 8   LandSlope      2911 non-null   object 
 9   Neighborhood   2911 non-null   object 
 10  Condition1     2911 non-null   object 
 11  Condition2     2911 non-null   object 
 12  BldgType       2911 non-null   object 
 13  HouseStyle     2911 non-null   object 
 14  OverallQual    2911 non-null   int64  
 15  OverallCond    2911 non-null   int64  
 16  YearBuilt      2911 non-null   int64  
 17  YearRemodAdd   2911 non-null   int64  
 18  RoofStyle      2911 non-null   object 
 19  RoofMatl       2911 non-null   object 
 20  Exterior1st    2911 non-null   object 
 21  Exterior2nd    2911 non-null   object 
 22  MasVnrType     2911 non-null   object 
 23  MasVnrArea     2911 non-null   float64
 24  ExterQual      2911 non-null   object 
 25  ExterCond      2911 non-null   object 
 26  Foundation     2911 non-null   object 
 27  BsmtQual       2911 non-null   object 
 28  BsmtCond       2911 non-null   object 
 29  BsmtExposure   2911 non-null   object 
 30  BsmtFinType1   2911 non-null   object 
 31  BsmtFinSF1     2911 non-null   float64
 32  BsmtFinType2   2911 non-null   object 
 33  BsmtFinSF2     2911 non-null   float64
 34  BsmtUnfSF      2911 non-null   float64
 35  TotalBsmtSF    2911 non-null   float64
 36  Heating        2911 non-null   object 
 37  HeatingQC      2911 non-null   object 
 38  CentralAir     2911 non-null   object 
 39  Electrical     2911 non-null   object 
 40  1stFlrSF       2911 non-null   int64  
 41  2ndFlrSF       2911 non-null   int64  
 42  LowQualFinSF   2911 non-null   int64  
 43  GrLivArea      2911 non-null   int64  
 44  BsmtFullBath   2911 non-null   float64
 45  BsmtHalfBath   2911 non-null   float64
 46  FullBath       2911 non-null   int64  
 47  HalfBath       2911 non-null   int64  
 48  BedroomAbvGr   2911 non-null   int64  
 49  KitchenAbvGr   2911 non-null   int64  
 50  KitchenQual    2911 non-null   object 
 51  TotRmsAbvGrd   2911 non-null   int64  
 52  Functional     2911 non-null   object 
 53  Fireplaces     2911 non-null   int64  
 54  GarageType     2911 non-null   object 
 55  GarageYrBlt    2911 non-null   float64
 56  GarageFinish   2911 non-null   object 
 57  GarageCars     2911 non-null   float64
 58  GarageArea     2911 non-null   float64
 59  GarageQual     2911 non-null   object 
 60  GarageCond     2911 non-null   object 
 61  PavedDrive     2911 non-null   object 
 62  WoodDeckSF     2911 non-null   int64  
 63  OpenPorchSF    2911 non-null   int64  
 64  EnclosedPorch  2911 non-null   int64  
 65  3SsnPorch      2911 non-null   int64  
 66  ScreenPorch    2911 non-null   int64  
 67  PoolArea       2911 non-null   int64  
 68  MiscVal        2911 non-null   int64  
 69  MoSold         2911 non-null   int64  
 70  YrSold         2911 non-null   int64  
 71  SaleType       2911 non-null   object 
 72  SaleCondition  2911 non-null   object 
dtypes: float64(10), int64(25), object(38)
memory usage: 1.6+ MB
```
# 왜도 처리하는 방법

```python
from scipy.stats import skew
def find_skew(x):
    return skew(x)

skew_vars = all_df[num_all_vars].apply(find_skew).sort_values(ascending=False)
skew_vars
```
<결과 화면>
```python
MiscVal          21.932511
PoolArea         16.874914
LotArea          12.859498
LowQualFinSF     12.375424
3SsnPorch        11.360117
KitchenAbvGr      4.295433
BsmtFinSF2        4.152826
EnclosedPorch     3.997699
ScreenPorch       3.952221
BsmtHalfBath      3.925199
MasVnrArea        2.614079
OpenPorchSF       2.543427
WoodDeckSF        1.836030
1stFlrSF          1.476986
BsmtFinSF1        1.436719
MSSubClass        1.372781
GrLivArea         1.269773
TotalBsmtSF       1.168795
BsmtUnfSF         0.918196
2ndFlrSF          0.861869
TotRmsAbvGrd      0.751467
Fireplaces        0.736456
HalfBath          0.691802
BsmtFullBath      0.622262
OverallCond       0.572220
BedroomAbvGr      0.325942
GarageArea        0.243497
MoSold            0.194552
OverallQual       0.192615
FullBath          0.162186
YrSold            0.131015
GarageCars       -0.217124
GarageYrBlt      -0.400867
YearRemodAdd     -0.448947
YearBuilt        -0.602755
dtype: float64
```
-- 왜도가 뭐지? --> 수치형 데이터는 정규분포를 이루지 못하는 변수

--> 정규분포로 변환을

-- 설문조사 논문통계 : ~1 ~ 1 

방법론 2가지 있음

- 박스콕스변환 --> ML --> RMSE (2.5)

  -- ~1 ~ 1 사이에 있는 변수들만 가지고 테스트

  -- 모두 포함 테스트

- 로그변환    --> ML --> RMSE (2.1)

  -- ~1 ~ 1 사이에 있는 변수들만 가지고 테스트

  -- 모두 포함 테스트

```python
from scipy.special import boxcox1p
from scipy.stats import boxcox_normmax

high_skew = skew_vars[skew_vars > 1]
high_skew_index = high_skew.index

print("The data before Box-Cox Transformation: \n", all_df[high_skew_index].head())

for num_var in high_skew_index:
  all_df[num_var] = boxcox1p(all_df[num_var], boxcox_normmax(all_df[num_var] + 1))

print("The data after Box-Cox Transformation: \n", all_df[high_skew_index].head())
```
<결과 화면>
```python
The data before Box-Cox Transformation: 
    MiscVal  PoolArea  LotArea  LowQualFinSF  3SsnPorch  KitchenAbvGr  \
0        0         0     8450             0          0             1   
1        0         0     9600             0          0             1   
2        0         0    11250             0          0             1   
3        0         0     9550             0          0             1   
4        0         0    14260             0          0             1   

   BsmtFinSF2  EnclosedPorch  ScreenPorch  BsmtHalfBath  MasVnrArea  \
0         0.0              0            0           0.0       196.0   
1         0.0              0            0           1.0         0.0   
2         0.0              0            0           0.0       162.0   
3         0.0            272            0           0.0         0.0   
4         0.0              0            0           0.0       350.0   

   OpenPorchSF  WoodDeckSF  1stFlrSF  BsmtFinSF1  MSSubClass  GrLivArea  \
0           61           0       856       706.0          60       1710   
1            0         298      1262       978.0          20       1262   
2           42           0       920       486.0          60       1786   
3           35           0       961       216.0          70       1717   
4           84         192      1145       655.0          60       2198   

   TotalBsmtSF  
0        856.0  
1       1262.0  
2        920.0  
3        756.0  
4       1145.0  
The data after Box-Cox Transformation: 
    MiscVal  PoolArea    LotArea  LowQualFinSF  3SsnPorch  KitchenAbvGr  \
0      0.0       0.0  15.495582           0.0        0.0      0.750946   
1      0.0       0.0  15.843244           0.0        0.0      0.750946   
2      0.0       0.0  16.282264           0.0        0.0      0.750946   
3      0.0       0.0  15.828920           0.0        0.0      0.750946   
4      0.0       0.0  16.953004           0.0        0.0      0.750946   

   BsmtFinSF2  EnclosedPorch  ScreenPorch  BsmtHalfBath  MasVnrArea  \
0         0.0       0.000000          0.0      0.000000   19.391616   
1         0.0       0.000000          0.0      0.711151    0.000000   
2         0.0       0.000000          0.0      0.000000   17.732491   
3         0.0      16.046854          0.0      0.000000    0.000000   
4         0.0       0.000000          0.0      0.000000   25.342500   

   OpenPorchSF  WoodDeckSF  1stFlrSF  BsmtFinSF1  MSSubClass  GrLivArea  \
0    12.045934    0.000000  5.265270  117.394542    6.525091   7.214050   
1     0.000000   56.760518  5.492339  146.196345    4.261606   6.928720   
2     9.875871    0.000000  5.307955   91.241513    6.525091   7.254837   
3     8.944564    0.000000  5.333653   52.614353    6.890496   7.217883   
4    14.227188   42.638190  5.436054  111.607853    6.525091   7.449330   

   TotalBsmtSF  
0   293.068021  
1   401.784662  
2   310.762298  
3   264.906745  
4   371.243881  
```

```python
skew_vars = all_df[num_all_vars].apply(find_skew).sort_values(ascending=False)
skew_vars
```
<결과 화면>
```python
PoolArea         14.965284
3SsnPorch         8.852740
LowQualFinSF      8.596740
MiscVal           5.259376
BsmtHalfBath      3.774855
KitchenAbvGr      3.773653
ScreenPorch       3.156089
BsmtFinSF2        2.588861
EnclosedPorch     2.146056
MasVnrArea        0.974333
BsmtUnfSF         0.918196
2ndFlrSF          0.861869
WoodDeckSF        0.785362
TotRmsAbvGrd      0.751467
Fireplaces        0.736456
HalfBath          0.691802
BsmtFullBath      0.622262
OpenPorchSF       0.620990
OverallCond       0.572220
MSSubClass        0.436372
BsmtFinSF1        0.376542
TotalBsmtSF       0.371431
BedroomAbvGr      0.325942
GarageArea        0.243497
MoSold            0.194552
OverallQual       0.192615
FullBath          0.162186
YrSold            0.131015
GrLivArea         0.004768
1stFlrSF         -0.011197
LotArea          -0.116936
GarageCars       -0.217124
GarageYrBlt      -0.400867
YearRemodAdd     -0.448947
YearBuilt        -0.602755
dtype: float64
```
# 도출변수

- 판매량 * 단가 = new_var 

- 매출액 도출변수

- 매출액이 함의하는 것 (판매량 * 단가)

- ML 수식: 도출변수가 생겼다? --> 수식을 할게 더 생겼다 --> 연산할게 많아졌다 --> 시간이 오래 걸린다 --> 성능 향상에 도움이 될까? 

- 판매량이 늘어나면 매출액도 당연히 늘어날 것

--> 상관관계 분석 0.99

```python
all_df['TotalSF'] = all_df['TotalBsmtSF'] + all_df['1stFlrSF'] + all_df['2ndFlrSF']
all_df = all_df.drop(['TotalBsmtSF', '1stFlrSF', '2ndFlrSF'], axis=1)
print(all_df.shape)
```
<결과 화면>
```python
(2911, 71)
```

```python
all_df['Total_Bathrooms'] = (all_df['FullBath'] + (0.5 * all_df['HalfBath']) + all_df['BsmtFullBath'] + (0.5 * all_df['BsmtHalfBath']))
all_df['Total_porch_sf'] = (all_df['OpenPorchSF'] + all_df['3SsnPorch'] + all_df['EnclosedPorch'] + all_df['ScreenPorch'])
all_df = all_df.drop(['FullBath', 'HalfBath', 'BsmtFullBath', 'BsmtHalfBath', 'OpenPorchSF', '3SsnPorch', 'EnclosedPorch', 'ScreenPorch'], axis=1)
print(all_df.shape)
```
<결과 화면>
```python
(2911, 65)
```
- 1차적으로 데이터 정의서부터 찾기

---> 없음

- 시각화 무한 작업 ~ 도메인 공부

```python
num_all_vars = list(train.select_dtypes(include=[np.number]))
year_feature = []
for var in num_all_vars:
  if 'Yr' in var:
    year_feature.append(var)
  elif 'Year' in var:
    year_feature.append(var)
  else:  
    print(var, "is not related with Year")
print(year_feature)
```
<결과 화면>
```python
MSSubClass is not related with Year
LotFrontage is not related with Year
LotArea is not related with Year
OverallQual is not related with Year
OverallCond is not related with Year
MasVnrArea is not related with Year
BsmtFinSF1 is not related with Year
BsmtFinSF2 is not related with Year
BsmtUnfSF is not related with Year
TotalBsmtSF is not related with Year
1stFlrSF is not related with Year
2ndFlrSF is not related with Year
LowQualFinSF is not related with Year
GrLivArea is not related with Year
BsmtFullBath is not related with Year
BsmtHalfBath is not related with Year
FullBath is not related with Year
HalfBath is not related with Year
BedroomAbvGr is not related with Year
KitchenAbvGr is not related with Year
TotRmsAbvGrd is not related with Year
Fireplaces is not related with Year
GarageCars is not related with Year
GarageArea is not related with Year
WoodDeckSF is not related with Year
OpenPorchSF is not related with Year
EnclosedPorch is not related with Year
3SsnPorch is not related with Year
ScreenPorch is not related with Year
PoolArea is not related with Year
MiscVal is not related with Year
MoSold is not related with Year
['YearBuilt', 'YearRemodAdd', 'GarageYrBlt', 'YrSold']
```

```python
fig, ax = plt.subplots(3, 1, figsize=(10, 6), sharex=True, sharey=True)
for i, var in enumerate(year_feature):
  if var != 'YrSold':
    ax[i].scatter(train[var], y, alpha=0.3)
    ax[i].set_title('{}'.format(var), size=15)
    ax[i].set_ylabel('SalePrice', size=15, labelpad=12.5)
plt.tight_layout()
plt.show()
```
<결과 화면>
![kaggle-house-price3](https://user-images.githubusercontent.com/96108301/147400069-6a8b91f0-f3fa-44f9-adc7-fa027fa5d9d3.png)

```python
all_df = all_df.drop(['YearBuilt', 'GarageYrBlt'], axis=1)
print(all_df.shape)
```
<결과 화면>
```python
(2911, 63)
```
```python
YearsSinceRemodel = train['YrSold'].astype(int) - train['YearRemodAdd'].astype(int)

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(YearsSinceRemodel, y, alpha=0.3)
fig.show()
```
<결과 화면>
![kaggle-house-price4](https://user-images.githubusercontent.com/96108301/147400082-521d2e95-049f-4435-a3a7-514690606158.png)

```python
all_df['YearsSinceRemodel'] = all_df['YrSold'].astype(int) - all_df['YearRemodAdd'].astype(int)
all_df = all_df.drop(['YrSold', 'YearRemodAdd'], axis=1)
print(all_df.shape)
```
<결과 화면>
```python
(2911, 62)
```
# 더미 변수

```python
all_df['PoolArea'].value_counts()
```
<결과 화면>
```python
0.000000    2898
5.845773       1
6.051326       1
5.948667       1
5.916247       1
5.789294       1
5.857648       1
6.164404       1
4.723614       1
5.556047       1
5.720976       1
5.132936       1
5.925636       1
6.234397       1
Name: PoolArea, dtype: int64
```
```python
def count_dummy(x):
  if x > 0:
    return 1
  else:
    return 0
```
```python
all_df['PoolArea'] = all_df['PoolArea'].apply(count_dummy)
all_df['PoolArea'].value_counts()
```
<결과 화면>
```python
0    2898
1      13
Name: PoolArea, dtype: int64
```

```python
all_df['GarageArea'] = all_df['GarageArea'].apply(count_dummy)
all_df['GarageArea'].value_counts()
```
<결과 화면>
```python
1    2755
0     156
Name: GarageArea, dtype: int64
```

```python
all_df['Fireplaces'] = all_df['Fireplaces'].apply(count_dummy)
all_df['Fireplaces'].value_counts()
```
<결과 화면>
```python
1    1492
0    1419
Name: Fireplaces, dtype: int64
```
- Label Encoding, Ordinal Encoding (서열, 순서)

--> (종속변수에만 쓰세요!), Ordinal --> (독립변수에만 쓰세요)

```python
from sklearn.preprocessing import LabelEncoder
import pandas as pd

temp = pd.DataFrame({'Food_Name': ['Apple', 'Chicken', 'Broccoli'], 
                     'Calories': [95, 231, 50]})

encoder = LabelEncoder()
encoder.fit(temp['Food_Name'])
labels = encoder.transform(temp['Food_Name'])
print(list(temp['Food_Name']), "==>", labels)
```
<결과 화면>
```python
['Apple', 'Chicken', 'Broccoli'] ==> [0 2 1]
```
```python
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

temp = pd.DataFrame({'Food_Name': ['Apple', 'Chicken', 'Broccoli'], 
                     'Calories': [95, 231, 50]})

encoder = OrdinalEncoder()
labels = encoder.fit_transform(temp[['Food_Name']])
print(list(temp['Food_Name']), "==>", labels.tolist())
```
<결과 화면>
```python
['Apple', 'Chicken', 'Broccoli'] ==> [[0.0], [2.0], [1.0]]
```
```python
import pandas as pd

temp = pd.DataFrame({'Food_Name': ['Apple', 'Chicken', 'Broccoli'], 
                     'Calories': [95, 231, 50]})

temp = pd.get_dummies(temp) ## one hot encoding <--- 명목형 데이터를 0과 1
print(temp)
print(temp.shape)
```
<결과 화면>
```python
 Calories  Food_Name_Apple  Food_Name_Broccoli  Food_Name_Chicken
0        95                1                   0                  0
1       231                0                   0                  1
2        50                0                   1                  0
(3, 4)
```

```python
all_df.shape
```
<결과 화면>
```python
(2911, 62)
```
- 원 핫 코딩

```python
all_df = pd.get_dummies(all_df).reset_index(drop=True)
all_df.shape
```
<결과 화면>
```python
(2911, 258)
```

```python
all_df
```
<결과 화면>
![kaggle-house-price5](https://user-images.githubusercontent.com/96108301/147400206-22609e73-955d-4ec2-9d21-2db209a0ea14.PNG)

머신러닝 가장 성능 좋게 하는 방법

---> 노가다!! 시간 들이면 성능은 좋아집니다! 

# 머신러닝 모형 학습

- 데이터셋 분리

- 훈련데이터와 테스트데이터로 재 분리

- X_train, X_test

```python
X = all_df.iloc[:len(y), :]
X_test = all_df.iloc[len(y):, :]
X.shape, y.shape, X_test.shape
```
<결과 화면>
```python
((1452, 258), (1452,), (1459, 258))
```

```python
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=2) # 실험 재현성 위해서 고정
X_train.shape, X_test.shape, y_train.shape, y_test.shape
```
<결과 화면>
```python
((1089, 258), (363, 258), (1089,), (363,))
```
- RMSE

```python
from sklearn.metrics import mean_squared_error

def rmse(y_true, y_pred):
    """RMSE 함수
    
    Args:
        y_true (list): 테스트 데이터의 실젯값
        y_pred (list): 모형을 통해 얻어진 예측값
    
    Returns
        rmse_val
    """
    rmse_val = np.sqrt(mean_squared_error(y_true, y_pred))
    return rmse_val
```
```python
y_true = [400, 300, 800, 900]
y_pred = [380, 320, 777, 600]
rmse(y_true, y_pred)
```
<결과 화면>
```python
151.10344139032705
```

```python
import numpy as np

def root_rmse_squared_error(y_true, ypred):
  error = 0
  
  for yt, yp in zip(y_true, y_pred):
    error = error + (yt - yp) ** 2
  
  mse = error / len(y_true)
  rmse = np.round(np.sqrt(mse), 3)
  return rmse

root_rmse_squared_error(y_true, y_pred)
```
<결과 화면>
```python
151.103
```
## 모형 정의 및 검증 평가

- cv_rmse() 함수

```python
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold, cross_val_score # 교차검증 시 평가 메트릭 함수

def cv_rmse(model, n_folds = 5):
    cv = KFold(n_splits = n_folds, random_state=42, shuffle=True)
    rmse_list = np.sqrt(-cross_val_score(model, X, y, scoring = "neg_mean_squared_error", cv=cv))
    print("CV RMSE value list:", np.round(rmse_list, 4))
    print("CV RMSE mean value:", np.round(np.mean(rmse_list), 4))
    return (rmse_list)
```
```python
from sklearn.linear_model import LinearRegression
n_folds = 10
rmse_scores = {}
lr_model = LinearRegression()

score = cv_rmse(lr_model, n_folds)
```

<결과 화면>
```python
CV RMSE value list: [0.1499 0.1016 0.1089 0.105  0.1553 0.1262 0.186  0.1154 0.121  0.1728]
CV RMSE mean value: 0.1342
```

```python
from sklearn.model_selection import cross_val_predict

X = all_df.iloc[:len(y), :]
X_test = all_df.iloc[len(y):, :]
X.shape, y.shape, X_test.shape

lr_model_fit = lr_model.fit(X, y)
# y 로그변환, y값 로그값 --> 원래값
final_preds = np.floor(np.expm1(lr_model_fit.predict(X_test)))
print(final_preds)
```
<결과 화면>
```python
[117094. 158154. 187402. ... 173323. 115909. 219598.]
```

```python
submission = pd.read_csv("/kaggle/input/house-prices-advanced-regression-techniques/sample_submission.csv")
submission.head()
```
<결과 화면>

![kaggle-house-price6](https://user-images.githubusercontent.com/96108301/147400290-72ab0862-6088-4588-a782-e2d6aece6e1c.PNG)

```python
submission.iloc[:,1] = final_preds
print(submission.head())
```
<결과 화면>
```python
   Id  SalePrice
0  1461   117094.0
1  1462   158154.0
2  1463   187402.0
3  1464   197038.0
4  1465   200628.0
```

```python
submission.to_csv("submission.csv", index=False)
```
