---
title: ml pipeline1 (머신러닝 파이프라인1)
tag: ml pipeline1 (머신러닝 파이프라인1)
date: 2021-12-23
categories:	Python Machine Learning
---
ml(머신 러닝)에서 'pipeline'라는 것을 만들어 사용 할 수 있는데

오늘은 여기에 대해 알아보고 직접 만드는 코드로 실습을 해봤다.

# ML(머신러닝) PipeLine 기본편

## 데이터 불러오기
```python
import pandas as pd 

data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data'
column_name = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 
               'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 
               'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 
               'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

df = pd.read_csv(data_url, names=column_name)
df.info()
```
<실행 화면>

![pipeline1](https://user-images.githubusercontent.com/96108301/147866580-cfb54636-10b9-4723-8b58-8e93a2c21303.PNG)

```python
df.head()
```
<실행 화면>

![pipeline2](https://user-images.githubusercontent.com/96108301/147866683-3d6754d6-4f87-4c40-8d1a-294330542f31.PNG)

```python
from sklearn.preprocessing import LabelEncoder

x = df.loc[:, "radius_mean":].values
y = df.loc[:, "diagnosis"].values

le = LabelEncoder()

#LabelEncoder변환
y = le.fit_transform(y)

le.classes_
```
<실행 화면>

![pipeline3](https://user-images.githubusercontent.com/96108301/147866684-6b7e99cf-df5b-411e-9c40-d15bb4064887.PNG)

## 훈련세트 분리
```python
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.20, stratify = y, random_state = 1)
x_train.shape, x_test.shape, y_train.shape, y_test.shape
```
<실행 화면>

![pipeline4](https://user-images.githubusercontent.com/96108301/147866685-11e00378-4baa-40c3-a8ee-ee1e969b7141.PNG)

## 파이프라인으로 변환기와 추정기 연결 (PipeLine 설계)
   ● Scale, PCA (차원축소)
     ○ 30 차원을 2차원으로 축소
   ● 로지스틱회귀모형
   ● Wrapper
   ● 훈련 세트에만 사용 (테스트에는 사용안함)
```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA 
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

pipe_lr = make_pipeline(StandardScaler(), 
                        PCA(n_components = 2), 
                        LogisticRegression(solver = "liblinear", random_state = 1))


pipe_lr.fit(x_train, y_train)
```
<실행 화면>

![pipeline5](https://user-images.githubusercontent.com/96108301/147866686-48812488-a120-4453-8f75-af0a1f78328b.PNG)

```python
y_pred = pipe_lr.predict(x_test)
print("테스트 정확도 :", pipe_lr.score(x_test, y_test))
```
<실행 화면>

![pipeline6](https://user-images.githubusercontent.com/96108301/147866687-014509c4-174d-4a1e-afaf-5f9cb969d5d9.PNG)

## 교차검증 (cross validation)
```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
import numpy as np

data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data'
column_name = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
               'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
               'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst',
               'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

df = pd.read_csv(data_url, names=column_name)
print(df.info())

X = df.loc[:, "radius_mean":].values
y = df.loc[:, "diagnosis"].values

le = LabelEncoder()
y = le.fit_transform(y)
print("종속변수 클래스:", le.classes_)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, stratify = y, random_state=1)

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

pipe_lr = make_pipeline(StandardScaler(),
                        PCA(n_components=2),
                        LogisticRegression(solver="liblinear", random_state=1))

kfold = StratifiedKFold(n_splits = 10, random_state=1, shuffle=True).split(X_train, y_train)
scores = []
for k, (train, test) in enumerate(kfold):
  pipe_lr.fit(X_train[train], y_train[train])
  score = pipe_lr.score(X_train[test], y_train[test])
  scores.append(score)
  print("폴드: %2d, 클래스 분포: %s, 정확도: %.3f" % (k+1, np.bincount(y_train[train]), score))

print("\nCV 정확도: %.3f +/- %.3f" % (np.mean(scores), np.std(scores)))

from sklearn.model_selection import cross_val_score
scores = cross_val_score(estimator=pipe_lr,
                         X = X_train,
                         y = y_train,
                         cv = 10,
                         n_jobs = 1)

print("CV 정확도 점수 : %s" % scores)
print("CV 정확도 : %.3f +/- %.3f" % (np.mean(scores), np.std(scores)))
```
<실행 화면>

![pipeline7-1](https://user-images.githubusercontent.com/96108301/147866688-d8ef427d-d43a-4f60-be91-00fb9cb4967f.PNG)
![pipeline7-2](https://user-images.githubusercontent.com/96108301/147866689-c6446c7c-eed8-4cd4-ab8b-d55611c282c2.PNG)

