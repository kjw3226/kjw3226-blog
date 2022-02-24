---
title: decision tree(결정 나무)에 대해
date: 2021-11-04
categories:	Python Machine Learning

---

<decision tree(결정 나무)에 대해>

결정 나무는 머신러닝에서 중요한 개념 중 하나이다.
핵심 컨셉은 아래와 같다.

![decision_tree concept](https://user-images.githubusercontent.com/96108301/146630620-04de6f9f-041f-4748-80de-99e994a8b839.PNG)

위 사진을 보면 단계 별로 나눠져 있는데

첫 번째 단계는 우리가 문제가 무엇인지 머신에게 알려주는

‘Define Problem’과 data를 모아서 주든 어떤 형태로든 머신에게 주는
‘Collect training data’가 있고

두 번째 단계는 데이터를 만드는 ‘Extract Data’와 결정 나무를 만드는 ‘Build a tree’가 있다.

세 번째는 머신이 작동하는 ‘Deploy machine’이 있다.

마지막 단계는 학습을 통해서 똑똑해진 머신이 우리가 데이터를 제시하면 그걸 구분하는 단계이다.

그리고 장점도 존재한다. 장점은 다음과 같다.

1.결과를 해석하고 이해하기 쉽다.

간략한 설명만으로 결정 트리를 이해하는 것이 가능.

2.자료를 가공할 필요가 거의 없다.다른 기법들의 경우 자료를 정규화하거나 임의의 변수를 생성하거나 값이 없는 변수를 제거해야 하는 경우있음.

3.수치 자료와 범주 자료 모두에 적용할 수 있다.다른 기법들은 일반적으로 오직 한 종류의 변수를 갖는 데이터 셋을 분석하는 것에 특화.

4.안정적이다. 해당 모델 추리의 기반이 되는 명제가 다소 손상되었더라도 잘 동작.

대규모의 데이터 셋에서도 잘 동작함. 방대한 분량의 데이터를 일반적인 컴퓨터 환경에서 비교적 짧은 시간에 분석가능.

참고 영상: https://www.youtube.com/watch?v=n0p0120Gxqk
```python
from sklearn import tree 
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
```
```python
clf.predict([[2., 2.]])
```
<결과 화면>
```python
array([1])
```

```python
clf.predict_proba([[2., 2.]])
```

<결과 화면>
```python
array([[0., 1.]])
```

```python
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
X, y = iris.data, iris.target
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
tree.plot_tree(clf)
```
<결과 화면>

[Text(167.4, 199.32, 'X[3] <= 0.8\ngini = 0.667\nsamples = 150\nvalue = [50, 50, 50]'),
 Text(141.64615384615385, 163.07999999999998, 'gini = 0.0\nsamples = 50\nvalue = [50, 0, 0]'),
 Text(193.15384615384616, 163.07999999999998, 'X[3] <= 1.75\ngini = 0.5\nsamples = 100\nvalue = [0, 50, 50]'),
 Text(103.01538461538462, 126.83999999999999, 'X[2] <= 4.95\ngini = 0.168\nsamples = 54\nvalue = [0, 49, 5]'),
 Text(51.50769230769231, 90.6, 'X[3] <= 1.65\ngini = 0.041\nsamples = 48\nvalue = [0, 47, 1]'),
 Text(25.753846153846155, 54.359999999999985, 'gini = 0.0\nsamples = 47\nvalue = [0, 47, 0]'),
 Text(77.26153846153846, 54.359999999999985, 'gini = 0.0\nsamples = 1\nvalue = [0, 0, 1]'),
 Text(154.52307692307693, 90.6, 'X[3] <= 1.55\ngini = 0.444\nsamples = 6\nvalue = [0, 2, 4]'),
 Text(128.76923076923077, 54.359999999999985, 'gini = 0.0\nsamples = 3\nvalue = [0, 0, 3]'),
 Text(180.27692307692308, 54.359999999999985, 'X[0] <= 6.95\ngini = 0.444\nsamples = 3\nvalue = [0, 2, 1]'),
 Text(154.52307692307693, 18.119999999999976, 'gini = 0.0\nsamples = 2\nvalue = [0, 2, 0]'),
 Text(206.03076923076924, 18.119999999999976, 'gini = 0.0\nsamples = 1\nvalue = [0, 0, 1]'),
 Text(283.2923076923077, 126.83999999999999, 'X[2] <= 4.85\ngini = 0.043\nsamples = 46\nvalue = [0, 1, 45]'),
 Text(257.53846153846155, 90.6, 'X[0] <= 5.95\ngini = 0.444\nsamples = 3\nvalue = [0, 1, 2]'),
 Text(231.7846153846154, 54.359999999999985, 'gini = 0.0\nsamples = 1\nvalue = [0, 1, 0]'),
 Text(283.2923076923077, 54.359999999999985, 'gini = 0.0\nsamples = 2\nvalue = [0, 0, 2]'),
 Text(309.04615384615386, 90.6, 'gini = 0.0\nsamples = 43\nvalue = [0, 0, 43]')]

![output_4_1](https://user-images.githubusercontent.com/96108301/146630771-683ed2b7-ce9b-4fe0-92ae-3cbebdf2be55.png)

```python
import graphviz  
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris")
```
<결과 화면>
```python
'iris.pdf'
```
```python
dot_data = tree.export_graphviz(clf, out_file=None, 
...                      feature_names=iris.feature_names,  
...                      class_names=iris.target_names,  
...                      filled=True, rounded=True,  
...                      special_characters=True)  
graph = graphviz.Source(dot_data)  
graph 
```

<결과 화면>

![output_6_01](https://user-images.githubusercontent.com/96108301/146630790-9e57b480-8ee3-411b-9103-4193aa545dc4.png)

![output_6_02](https://user-images.githubusercontent.com/96108301/146630803-b0bf304b-0d36-42f1-96d0-697e87589789.png)

![output_6_03](https://user-images.githubusercontent.com/96108301/146630804-d8566074-f72a-41c1-b0f7-37720d33c516.PNG)


```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
iris = load_iris()
decision_tree = DecisionTreeClassifier(random_state=0, max_depth=2)
decision_tree = decision_tree.fit(iris.data, iris.target)
r = export_text(decision_tree, feature_names=iris['feature_names'])
print(r)
```
<결과 화면>
```python
|--- petal width (cm) <= 0.80
|   |--- class: 0
|--- petal width (cm) >  0.80
|   |--- petal width (cm) <= 1.75
|   |   |--- class: 1
|   |--- petal width (cm) >  1.75
|   |   |--- class: 2
```