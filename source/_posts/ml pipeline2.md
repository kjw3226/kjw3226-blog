---
title: ml pipeline2 (머신러닝 파이프라인2)
tag: ml pipeline2 (머신러닝 파이프라인2)
date: 2021-12-24
categories:	Python Machine Learning
---

어제에 이어서 'pipeline 만들기' 실습을 진행하였다.

## ML Pipeline 학습 곡선 그리기

### 데이터 불러오기, 훈련세트 분리, pipeline 설계 등
```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import cross_val_score
# from sklearn.tree import DecisionTreeClassifier
# from lightgbm import LGBMClassifier

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

pipe_lr = make_pipeline(StandardScaler(), 
                        PCA(n_components=2), 
                        LogisticRegression(solver = "liblinear", random_state=0))
```
<실행 화면>

![pipeline8](https://user-images.githubusercontent.com/96108301/147866690-cbedf06d-2787-4fc4-96a7-afac595053d8.PNG)

### Learning Curve 결괏값 구하기
```python
from sklearn.model_selection import learning_curve

train_sizes, train_scores, test_scores = learning_curve(
    estimator = pipe_lr,
    X = X_train,
    y = y_train,
    train_sizes = np.linspace(0.1, 1.0, 10),
    cv =10
)

train_mean = np.mean(train_scores, axis =1)
train_std = np.std(train_scores, axis = 1)
test_mean = np.mean(test_scores, axis = 1)
test_std = np.std(test_scores, axis = 1)
```
### Learning Cruve 그래프 작성
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize = (16, 10))
ax.plot(train_sizes, 
        train_mean, 
        color = "blue", 
        marker = "o", 
        markersize = 10, 
        label = "training acc.")
ax.fill_between(train_sizes, 
                train_mean + train_std, 
                train_mean - train_std, 
                alpha = 0.15, color = "blue")
ax.plot(train_sizes, 
        test_mean, 
        color = "green", 
        marker = "s", 
        linestyle = "--", 
        markersize=10, 
        label = "testing acc.")
ax.fill_between(train_sizes, 
                test_mean + test_std, 
                test_mean - test_std, 
                alpha = 0.15, color = "yellow")
plt.grid()
plt.xlabel("Number of Training Samples")
plt.ylabel("Accuracy")
plt.legend(loc = "lower right")
plt.ylim([0.8, 1.03])
plt.tight_layout()
plt.show()
```
<실행 화면>

![pipeline9](https://user-images.githubusercontent.com/96108301/147866691-60a8df82-d806-4582-b10d-f4ee39c7d36a.PNG)

## ML PipeLine 검증 곡선 그리기
```python
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 
from sklearn.model_selection import learning_curve
from sklearn.model_selection import validation_curve
from lightgbm import LGBMClassifier

data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data'
column_name = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 
               'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 
               'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 
               'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

df = pd.read_csv(data_url, names=column_name)

X = df.loc[:, "radius_mean":].values
y = df.loc[:, "diagnosis"].values

le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, 
                                                    # stratify = y, 
                                                    random_state=1)
kfold = StratifiedKFold(n_splits = 10, random_state=1, shuffle=True)

pipe_lr = make_pipeline(StandardScaler(), 
                        PCA(n_components=2), 
                        LogisticRegression(solver = "liblinear", penalty = "l2", random_state=1))

param_range = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]
train_scores, test_scores = validation_curve(estimator=pipe_lr, 
                                                        X = X_train, 
                                                        y = y_train, 
                                                        param_name = "logisticregression__C", 
                                                        param_range = param_range, 
                                                        cv = kfold)

train_mean = np.mean(train_scores, axis = 1)
train_std = np.std(train_scores, axis = 1)
test_mean = np.mean(test_scores, axis = 1)
test_std = np.std(test_scores, axis = 1)

fig, ax = plt.subplots(figsize = (16, 10))
ax.plot(param_range, train_mean, color = "blue", marker = "o", markersize=5, label = "training accuracy")
ax.fill_between(param_range, train_mean + train_std, train_mean - train_std, alpha = 0.15, color = "blue") # 추정 분산
ax.plot(param_range, test_mean, color = "green", marker = "s", linestyle = "--", markersize=5, label = "Validation accuracy")
ax.fill_between(param_range, test_mean + test_std, test_mean - test_std, alpha = 0.15, color = "green")
plt.grid()
plt.xscale("log")
plt.xlabel("Parameter C")
plt.ylabel("Accuracy")
plt.legend(loc = "lower right")
plt.ylim([0.8, 1.03])
plt.tight_layout()
plt.show()
```
<실행 화면>

![pipeline10](https://user-images.githubusercontent.com/96108301/147866829-d9fc4b2a-51f7-4e8c-abf4-724419a77630.PNG)

## ML 그리드서치를 이용한 설계(PipeLine) 및 하이퍼파라미터(Hyper Paramiter) 튜닝

 ● 각 모델 ==> 차의 종류.
---> 차량 튜닝 4개 ---> 차량 튜닝 1개 3일 ---> 12일 뒤. (나한테 오려면)

 ● 튜닝 ==> 성능 업데이트 보정.

 ● 이론 공부 하기도 싫음. --> 그냥 쓰세요!!

  --> 남이 쓰던거 그냥 따라 같이 쓰기
 
 ● 이론 공부가 하고 싶으면 이론 공부 병행 필요.

 ● 파라미터 80개 --> 파라미터 1개 수정 2시간

  --> 80개 수정 (160시간 걸림...)

  --> 성능이 좋아진다는 보장도 없고

 ● 결국 시간낭비니 그냥 있는 그래로 써라...

  --> 이거는 진짜 우리 수준에서는 그냥 그대로 튜닝하지 말고 그대로 사용해라.
  
```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
# from sklearn.tree import DecisionTreeClassifier
# from lightgbm import LGBMClassifier

data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data'
column_name = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 
               'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 
               'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 
               'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

df = pd.read_csv(data_url, names=column_name)
#print(df.info())

X = df.loc[:, "radius_mean":].values
y = df.loc[:, "diagnosis"].values

le = LabelEncoder()
y = le.fit_transform(y)
#print("종속변수 클래스:", le.classes_)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, stratify = y, random_state=1)

pipe_svc = make_pipeline(StandardScaler(), 
                        PCA(n_components=2), 
                       SVC(random_state=0))

param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0,1000.0]
```
 ● SVM 파라미터 코드

```python
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 
from sklearn.model_selection import learning_curve
from sklearn.model_selection import validation_curve
from lightgbm import LGBMClassifier
from sklearn.model_selection import GridSearchCV 
from sklearn.svm import SVC 

data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data'
column_name = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 
               'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 
               'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 
               'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

df = pd.read_csv(data_url, names=column_name)

X = df.loc[:, "radius_mean":].values
y = df.loc[:, "diagnosis"].values

le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, 
                                                    # stratify = y, 
                                                    random_state=1)

pipe_svc = make_pipeline(StandardScaler(), 
                        PCA(n_components=2), 
                        SVC(random_state=1))

param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
param_grid = [{"svc__C": param_range, 
               "svc__gamma": param_range, 
               "svc__kernel": ["linear"]}]

gs = GridSearchCV(estimator = pipe_svc, 
                  param_grid = param_grid, 
                  scoring="accuracy", 
                  cv = 10)

gs = gs.fit(X_train, y_train)
print(gs.best_score_)
print(gs.best_params_)

clf = gs.best_estimator_
clf.fit(X_train, y_train) 
print("테스트 정확도:", clf.score(X_test, y_test))
```
<실행 화면>

![pipeline11](https://user-images.githubusercontent.com/96108301/147866831-1bb0802c-5a39-4a93-b0cf-03896edff61e.PNG)

 ● Decision Tree

```python
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 
from sklearn.model_selection import learning_curve
from sklearn.model_selection import validation_curve
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV 
from sklearn.svm import SVC 

data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data'
column_name = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 
               'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 
               'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 
               'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

df = pd.read_csv(data_url, names=column_name)

X = df.loc[:, "radius_mean":].values
y = df.loc[:, "diagnosis"].values

le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, 
                                                    # stratify = y, 
                                                    random_state=1)
kfold = StratifiedKFold(n_splits = 10, random_state=1, shuffle=True)

pipe_tree = make_pipeline(StandardScaler(), 
                          PCA(n_components=2), 
                          DecisionTreeClassifier(random_state=1))
print(pipe_tree.get_params().keys())
param_grid = [{"decisiontreeclassifier__max_depth": [1, 2, 3, 4, 5, 6, 7, None]}]

gs = GridSearchCV(estimator = pipe_tree, 
                  param_grid = param_grid, 
                  scoring="accuracy", 
                  cv = kfold)

gs = gs.fit(X_train, y_train)
print(gs.best_score_)
print(gs.best_params_)

clf = gs.best_estimator_
clf.fit(X_train, y_train) 
print("테스트 정확도:", clf.score(X_test, y_test))
```
<실행 화면>

![pipeline12](https://user-images.githubusercontent.com/96108301/147866832-73cd7a77-d4a4-4e84-8a60-848ac5a262af.PNG)