---
title: Feature Engineering
tag: Feature Engineering
date: 2021-11-18
categories:	Python Machine Learning

---
파이썬 머신러닝에서
Feature Engineering은 데이터 분석에 사용되는 
많은 방법 중에 하나이다.

아래의 코드는 
Feature Engineering이 어떤 작업들을 하는 것인지 
보여준다. 

<이상치 제거>

```python
train.drop(train[(train['OverallQual']<4) & (train['SalePrice']> 200000)].index, inplace=True)
train.drop(train[(train['OverallCond']<4) & (train['SalePrice']> 200000)].index, inplace=True)
train.reset_index(drop=True, inplace=True)
print(train.shape)
```
![Feature Engineering1](https://user-images.githubusercontent.com/93234783/142337957-27adf4de-5e8b-4fc3-8244-dc94504b3b2d.PNG)

종속 변수의 로그 변화

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
![Feature Engineering2](https://user-images.githubusercontent.com/93234783/142337959-af8a2387-f1d1-410b-98cc-763c77f3da80.PNG)

```python
import numpy as np 

train["SalePrice"] = np.log1p(train["SalePrice"])

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
plt.text(mu + 0.05, 0.111, 'Mean of SalePrice', rotation=0, color='r')
plt.ylim(0, 0.12)
fig.show()
```
![Feature Engineering3](https://user-images.githubusercontent.com/93234783/142337961-0de1d1d7-2c53-453a-a93b-03193a764be0.PNG)

데이터 ID값 제거
```python
train_ID = train['Id']
test_ID = test['Id']
train.drop(['Id'], axis=1, inplace=True)
test.drop(['Id'], axis=1, inplace=True)
train.shape, test.shape
```
![Feature Engineering4](https://user-images.githubusercontent.com/93234783/142337964-39016dd4-85b2-461a-bd2b-6bb76b54c9a5.PNG)

Y값 추출

```python
y = train['SalePrice'].reset_index(drop=True)
train = train.drop('SalePrice', axis = 1)
train.shape, test.shape, y.shape
```
![Feature Engineering5](https://user-images.githubusercontent.com/93234783/142337965-ff66bf6e-daf1-4294-82a3-5f3417cfd6db.PNG)

결측치 확인
```python
def check_na(data, head_num = 6):
  isnull_na = (data.isnull().sum() / len(data)) * 100
  data_na = isnull_na.drop(isnull_na[isnull_na == 0].index).sort_values(ascending=False)
  missing_data = pd.DataFrame({'Missing Ratio' :data_na, 
                               'Data Type': data.dtypes[data_na.index]})
  print("결측치 데이터 컬럼과 건수:\n", missing_data.head(head_num))

check_na(all_df, 20)
```
![Feature Engineering6](https://user-images.githubusercontent.com/93234783/142337968-71cd8a31-2810-4f2b-adcb-97ceb34fef1b.PNG)

결측치 제거

```python
all_df.drop(['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 'LotFrontage'], axis=1, inplace=True)
check_na(all_df)
```
![Feature Engineering7](https://user-images.githubusercontent.com/93234783/142337969-c27fc2dc-7336-41ea-b4b8-1949ca9b894b.PNG)

결측치 채우기

```python
print(all_df['BsmtCond'].value_counts())
print()
print(all_df['BsmtCond'].mode()[0])
```
![Feature Engineering8](https://user-images.githubusercontent.com/93234783/142337971-46696d23-0721-4c17-aaa1-a14e9fbbe1d3.PNG)

```python
import numpy as np
cat_all_vars = train.select_dtypes(exclude=[np.number])
print("The whole number of all_vars", len(list(cat_all_vars)))

final_cat_vars = []
for v in cat_all_vars:
    if v not in ['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 'LotFrontage']:
        final_cat_vars.append(v)

print("The whole number of final_cat_vars", len(final_cat_vars))
for i in final_cat_vars:
  all_df[i] = all_df[i].fillna(all_df[i].mode()[0])

check_na(all_df, 20)
```

![Feature Engineering9](https://user-images.githubusercontent.com/93234783/142337973-e569a31c-fc89-452d-a28c-cac0d5354e99.PNG)
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
![Feature Engineering10](https://user-images.githubusercontent.com/93234783/142337976-465a7b0a-5246-4696-9aed-07436d1817a6.PNG)

왜도 처리하기
```python
from scipy.stats import skew

def find_skew(x):
  return skew(x)

skewness_features = all_df[num_all_vars].apply(find_skew).sort_values(ascending=False)
skewness_features
```
![Feature Engineering11](https://user-images.githubusercontent.com/93234783/142338182-24c60259-9c3a-44f1-be86-0749bbee8030.PNG)

```python
skewnewss_index = list(skewness_features.index)
skewnewss_index.remove('LotArea')
all_numeric_df = all_df.loc[:, skewnewss_index]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, all_numeric_df.max().sort_values(ascending=False)[0])
ax = sns.boxplot(data=all_numeric_df[skewnewss_index] , orient="h", palette="Set1")
ax.xaxis.grid(False)
ax.set(ylabel="Feature names")
ax.set(xlabel="Numeric values")
ax.set(title="Numeric Distribution of Features Before Box-Cox Transformation")
sns.despine(trim=True, left=True)
```
![Feature Engineering12](https://user-images.githubusercontent.com/93234783/142338187-4d37d2bf-cc19-4ba6-9481-6305216b0805.PNG)

```python
from scipy.special import boxcox1p
from scipy.stats import boxcox_normmax

high_skew = skewness_features[skewness_features > 1]
high_skew_index = high_skew.index

print("The data before Box-Cox Transformation: \n", all_df[high_skew_index].head())

for num_var in high_skew_index:
  all_df[num_var] = boxcox1p(all_df[num_var], boxcox_normmax(all_df[num_var] + 1))

print("The data after Box-Cox Transformation: \n", all_df[high_skew_index].head())
```
![Feature Engineering13](https://user-images.githubusercontent.com/93234783/142338189-7c8d1fa5-a4a8-4acd-8309-c3d26d0d94e8.PNG)

```python
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xscale('log')
ax = sns.boxplot(data=all_df[high_skew_index] , orient="h", palette="Set1")
ax.xaxis.grid(False)
ax.set(ylabel="Feature names")
ax.set(xlabel="Numeric values")
ax.set(title="Numeric Distribution of Features Before Box-Cox Transformation")
sns.despine(trim=True, left=True)
```
![Feature Engineering14](https://user-images.githubusercontent.com/93234783/142338190-f674c240-f18a-4715-b01b-b91e3d8d3df0.PNG)

도출변수

```python
all_df['TotalSF'] = all_df['TotalBsmtSF'] + all_df['1stFlrSF'] + all_df['2ndFlrSF']
all_df = all_df.drop(['TotalBsmtSF', '1stFlrSF', '2ndFlrSF'], axis=1)
print(all_df.shape)
```
![Feature Engineering15](https://user-images.githubusercontent.com/93234783/142338193-5df93659-ee01-4b4d-90b2-78443a8970f4.PNG)

```python
all_df['Total_Bathrooms'] = (all_df['FullBath'] + (0.5 * all_df['HalfBath']) + all_df['BsmtFullBath'] + (0.5 * all_df['BsmtHalfBath']))
all_df['Total_porch_sf'] = (all_df['OpenPorchSF'] + all_df['3SsnPorch'] + all_df['EnclosedPorch'] + all_df['ScreenPorch'])
all_df = all_df.drop(['FullBath', 'HalfBath', 'BsmtFullBath', 'BsmtHalfBath', 'OpenPorchSF', '3SsnPorch', 'EnclosedPorch', 'ScreenPorch'], axis=1)
print(all_df.shape)
```
![Feature Engineering16](https://user-images.githubusercontent.com/93234783/142338196-3452936f-3947-40c4-87cd-cc3e5d516c90.PNG)

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
![Feature Engineering17](https://user-images.githubusercontent.com/93234783/142338199-f5d4295b-87d0-44c0-ad83-616755797dbf.PNG)

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
![Feature Engineering18](https://user-images.githubusercontent.com/93234783/142338202-f0473847-5ade-4719-bd9d-f4b340874ca7.PNG)

```python
all_df = all_df.drop(['YearBuilt', 'GarageYrBlt'], axis=1)
print(all_df.shape)
```
![Feature Engineering19](https://user-images.githubusercontent.com/93234783/142338203-91ce1825-1902-4261-8fca-dae913f6106b.PNG)

```python
YearsSinceRemodel = train['YrSold'].astype(int) - train['YearRemodAdd'].astype(int)

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(YearsSinceRemodel, y, alpha=0.3)
fig.show()
```
![Feature Engineering20](https://user-images.githubusercontent.com/93234783/142338204-edece57c-0c7d-4f29-9789-6960420b56a1.PNG)


```python
all_df['YearsSinceRemodel'] = all_df['YrSold'].astype(int) - all_df['YearRemodAdd'].astype(int)
all_df = all_df.drop(['YrSold', 'YearRemodAdd'], axis=1)
print(all_df.shape)
```
![Feature Engineering21](https://user-images.githubusercontent.com/93234783/142338345-b7c63ab2-7e95-467d-8a36-7fff83ba50c6.PNG)

더미변수
```python
all_df['PoolArea'].value_counts()
```
![Feature Engineering22](https://user-images.githubusercontent.com/93234783/142338348-6e1ca812-fe0d-4b6b-8a7c-00fac4029d60.PNG)

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
![Feature Engineering23](https://user-images.githubusercontent.com/93234783/142338349-5e515a14-9e14-4a4d-8853-4af1b6db9836.PNG)

위의 코드들의 결과값을 직접 프로그램을 돌려서 확인하고 싶다면
참고에 있는 주소로 들어가 'data'에 들어가서 다운을 받아
그 파일을 구글 '코랩'으로 돌려보면 된다.

참고 : https://www.kaggle.com/c/house-prices-advanced-regression-techniques



