---
title: Trees - Decision Tree about(결정 트리에 대해)
tag: Trees - Decision Tree about(결정 트리에 대해)
date: 2021-12-10
categories:	Python
---
 결정 트리에 대해 알아보고,
 직접 코딩 실습도 해 보았다.
 
- 결정 트리(Decision Tree) 는 머신러닝 알고리즘 중 직관적이고 
  이해하기 쉬운 알고리즘이다. 쉽게 생각하면 '스무 고개'이다.
  
![Decision Tree about](https://user-images.githubusercontent.com/96108301/147845340-ed67fb14-0886-4bb5-a1db-0db03734b813.jpg)
  위 사진을 보면 강조된 부분이 보인다. 저 부분이 계속 반복 되어 만들어지면
  질 수록 정확도는 떨어지게 된다. 그래서 '높은 예측 정확도'를 가지려면
  최대한 많은 데이터 세트가 해당 분류에 속할 수 있도록 결정 노드의 규칙이
  정해져야 한다. 이를 위해서는 '어떻게 트리를 분할 할 것인가'를 생각해야 한다.
  
- 아래는 오늘 '구글 코랩'에서 실습한 내용들이다.
 
● 정보 이득이 높은 속성을 기준으로 분할.
● -> 분류 오차, 지니 불순도, 엔트로피 3가지 분류 방법이 있음.

```python
from sklearn import datasets 
import numpy as np 

iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target 

print("클래스 레이블:", np.unique(y))
```
<실행 화면>
![Decision Tree - about1](https://user-images.githubusercontent.com/96108301/147845438-e50ee961-e1b4-49bf-836d-50410692051f.PNG)

● 훈련 데이터 / 테스트 분리

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.3, random_state = 1
)

print("y 레이블 갯수:", np.bincount(y))
```
![Decision Tree - about2](https://user-images.githubusercontent.com/96108301/147845466-aa4494e7-3700-4e79-91d4-824bb7f0129e.PNG)

● 시각화

```python
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):

    # 마커와 컬러맵을 설정합니다.
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # 결정 경계를 그립니다.
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], 
                    y=X[y == cl, 1],
                    alpha=0.8, 
                    c=colors[idx],
                    marker=markers[idx], 
                    label=cl, 
                    edgecolor='black')

    # 테스트 샘플을 부각하여 그립니다.
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]

        plt.scatter(X_test[:, 0],
                    X_test[:, 1],
                    c='',
                    edgecolor='black',
                    alpha=1.0,
                    linewidth=1,
                    marker='o',
                    s=100, 
                    label='test set')
```
●이진 결정 트리에서 널리 사용되는 세 개의 불순도 지표
  ○ 지니 불순도
  ○ 엔트로피
  ○ 분류오차

```python
import matplotlib.pyplot as plt
import numpy as np

# 지니 불순도 함수
def gini(p):
    return p * (1 - p) + (1 - p) * (1 - (1 - p))


# 엔트로피 함수 
def entropy(p):
    return - p * np.log2(p) - (1 - p) * np.log2((1 - p))

# 분류 오차
def error(p):
    return 1 - np.max([p, 1 - p])

x = np.arange(0.0, 1.0, 0.01)

ent = [entropy(p) if p != 0 else None for p in x]
sc_ent = [e * 0.5 if e else None for e in ent]
err = [error(i) for i in x]

fig = plt.figure()
ax = plt.subplot(111)
for i, lab, ls, c, in zip([ent, sc_ent, gini(x), err], 
                          ['Entropy', 'Entropy (scaled)', 
                           'Gini Impurity', 'Misclassification Error'],
                          ['-', '-', '--', '-.'],
                          ['black', 'lightgray', 'red', 'green', 'cyan']):
    line = ax.plot(x, i, label=lab, linestyle=ls, lw=2, color=c)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
          ncol=5, fancybox=True, shadow=False)

ax.axhline(y=0.5, linewidth=1, color='k', linestyle='--')
ax.axhline(y=1.0, linewidth=1, color='k', linestyle='--')
plt.ylim([0, 1.1])
plt.xlabel('p(i=1)')
plt.ylabel('Impurity Index')
plt.show()
```
<실행 화면>

![Decision Tree - about3](https://user-images.githubusercontent.com/96108301/147845543-3fe33ebf-bb59-487f-9a3e-1c3dafd06669.PNG)

● 정보이득을 최대로 하는 옵션

```python
from sklearn.tree import DecisionTreeClassifier

tree_entropy = DecisionTreeClassifier(criterion="gini", max_depth=3)
tree_entropy.fit(X_train, y_train)
```
<실행 화면>

![Decision Tree - about4](https://user-images.githubusercontent.com/96108301/147845556-e4fd24a1-27c7-4cdd-a1bd-5fa2c95ea1dd.PNG)

```python
X_combined = np.vstack((X_train, X_test))
y_combined = np.hstack((y_train, y_test))

plot_decision_regions(X_combined, y_combined, classifier=tree_entropy, test_idx = range(105, 150))
plt.xlabel("petal length")
plt.ylabel("petal width")
plt.legend(loc = "upper left")
plt.tight_layout()
plt.show()
```
<실행 화면>

![Decision Tree - about5](https://user-images.githubusercontent.com/96108301/147845595-79e059dd-ce71-46e2-8766-ccf5e42444bb.PNG)

```python
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz

dot_data = export_graphviz(tree_entropy,
                           filled=True, 
                           rounded=True,
                           class_names=['Setosa', 
                                        'Versicolor',
                                        'Virginica'],
                           feature_names=['petal length', 
                                          'petal width'],
                           out_file=None) 
graph = graph_from_dot_data(dot_data) 
graph.write_png('gini_tree.png') 
```
<실행 화면>

![Decision Tree - about6](https://user-images.githubusercontent.com/96108301/147845619-83b458cc-0e10-42b6-979c-9f21ec582b40.PNG)
