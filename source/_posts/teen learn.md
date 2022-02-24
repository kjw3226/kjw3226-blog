---
title: teen learn
tag: teen learn
data: 2021-12-08
categories:	Python Machine Learning

---
 
 회귀, 지도학습, 회귀모델, 경사하강법 (비용 최소화하기), 'pycaret(파이 캐럿)', 
 
 평가지표, 'EDA'해보기, '데이터 셋 분리 -> ML 모형만들기 -> ML 모형 평가' 해보기
 
 오늘은 큰 틀에서 봤을 때 이렇게 10가지에 알아보고 직접 해보았다.

## 회귀
 ```python
- 회귀는 통계학에서 메인

- 유전적 특성

--> 부모(독립변수)의 키가 크더라도 자식(종속변수)의 키가 대를 이어서 무한정 커지지 않고,

부모의 키가 작더라도 자식의 키가 대를 이어서 무한정 작지는 않다. 
```
## 단순 선형 회귀
```python
--> 단순선형회귀 (변수, feature, 컬럼명)

f(x)(y)(종속변수, 반응변) = 기울기(독립변수, 설명변수)
```
## 회귀계수
```python
model <- lm (판매량 ~ 광고비)

summary(model)

아파트 가격 <- 학군(A, 지역, 근처 지하철역의 갯수(얼마나 관계 있느냐??), 

연도(신축, 구축), 방의 개수 (X), 아파트 단지 크기(X) ~ ~ ~ ~ 

-->  도메인 잘 활용

--> A(1), A(2), A(3), ... 독립변수의 값에 영향을 미치는 걸 

회귀 계수 (Regression Coefficients)

아파트 가격 = A1의 회귀계수 * (등급) + A2의 회귀계수 * (지역) + A3 ~~
```
## 지도학습
```python
--> 분류 (이산값) = Category (성공, 실패)

--> 수치 예측 (=회귀) / 연속값 (키, 몸무게, 판매량)
```

## 선형 회귀 모델(13-14개)
```python
--> 문제점: 오차합 (RSS) ==> 오차를 줄일수 있도록 최적화 할수 있는 규제(Regularization)

--> 전통적인 모형 

--> 릿지(Ridge) + 라쏘(Lassso) = 엘라스틱넷(ElasticNet)

-----> 

--> 로지스틱 회귀!! (비선형 문제) **** 

- 오류합 계산 방법

1. 절대값을 취해서 더하는 방식


2. 오류값의 제곱을 구해서 더하는 방식 (RSS: Residual sum of squared)

->  RSS(w0, w1) = 1/N 
```
### 비용최소화를 위해 경사하강법을 쓰는 경우
```python
 예를 들어 조선소는 1년에 수주를 

---> 많으면 1건 (몇조원),

---->    y 총 사업비용    3-4만개 

2010년 행의 개수 1            10만원, 천만원, 

2011년-1

2011년-2

2012년 

그래서 비용 최소화하기 --> 경사하강법 (Gradient Descent)
```
여기서 부터는 실습 코드들과 결과 화면이다.

- y = 4x + 6 + error 시뮬레이션 데이터 값 생성

```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

np.random.seed(123) # 실험 재현성

X = 2 * np.random.rand(100, 1) # 100개의 랩덤값 만들기
y = 4 * X + 6 + np.random.rand(100, 1)

plt.scatter(X,y)
```
<결과 화면>

![img](https://user-images.githubusercontent.com/96108301/147241703-096f3346-ff5b-4c7a-bd6a-7e546741a5c6.png)

<데이터 확인>
```python
X_shape, y.shape
```
<결과 확인>
```python
((100, 1), (100, 1))
```

<경사하강법으로 최적의 기울기 찾기>

```python
# w1과, w0를 업데이트할 w1_update, w0_update 값 반환

def get_weight_updates(w1, w0, X, y, learning_rate=0.01):
  N = len(y)

  # w1_update, w0_update 초기화
  w1_update = np.zeros_like(w1)
  w0_update = np.zeros_like(w0)

  # 예측 배열 계산하고, 예측값과 실젯 값의 차이 계산
  y_pred = np.dot(X, w1.T) + w0
  diff = y - y_pred # 실제갓, 예측값 == 오차

  # w0_update를 dot 행렬 연산으로 구하기 위해 모두 1 값을 가진 행렬 생성
  w0_factors = np.ones((N, 1))
  
  # w1과 w0을 업데이트할 w1_update, w0_update 계산 
  w1_update = -(2/N) * learning_rate * (np.dot(X.T, diff))
  w0_update = -(2/N) * learning_rate * (np.dot(w0_factors.T, diff))

  return w1_update, w0_update
```
```python
w0 = np.zeros((1, 1))
w1 = np.zeros((1, 1))

y_pred = np.dot(X, w1.T) + w0
diff = y-y_pred
print(diff.shape)

w0_factors = np.ones((100, 1))
w1_update = -(2/100) * 0.01 * (np.dot(X.T, diff))
w0_update = -(2/100) * 0.01 * (np.dot(w0_factors.T, diff))

print(w1_update.shape, w0_update.shape)
print(w1, w0)
```
<결과 화면>
```python
(100, 1)
(1, 1) (1, 1)
[[0.]] [[0.]]
```
<입력 인자 반복문 코드>
```python
def gradient_descent_steps(X, y, iters = 100000):

  # w0와 w1을 모두 0으로 초기화
  w0 = np.zeros((1, 1))
  w1 = np.zeros((1, 1))

  # iters 만큼 반복 수행 # get_weight_updates
  for ind in range(iters):
    w1_update, w0_update = get_weight_updates(w1, w0, X, y, learning_rate=0.01)
    w1 = w1 - w1_update
    w0 = w0 - w0_update
  
  return w1, w0
```
<예측 오차 비용 계산하는 함수 생성 및 경사 하강법 수행>
```python
def get_cost(y, y_pred):
  N = len(y)

  cost = np.sum(np.square(y - y_pred)) / N 
  return cost 

w1, w0 = gradient_descent_steps(X, y, iters = 100000)
print("w1:{0:.4f}, w0:{1:.4f}".format(w1[0, 0], w0[0, 0]))

y_pred = w1[0,0] * X + w0
print("Total Cost:{0:.4f}".format(get_cost(y, y_pred)))
```
<결과 화면>
```python
w1:3.9462, w0:6.5590
Total Cost:0.0803
```
<산점도 그래프 코드>
```python
plt.scatter(X, y)
plt.plot(X, y_pred, color = "r")
```
<결과 화면>

![img_1](https://user-images.githubusercontent.com/96108301/147241763-f305acad-201e-4180-b319-ddf01a950fdb.png)

<'paycaret' 설치 코드>
```python
!pip install pycaret
```
<결과 화면>
```python
Collecting pycaret
  Downloading pycaret-2.3.5-py3-none-any.whl (288 kB)
     |████████████████████████████████| 288 kB 32.5 MB/s 
Requirement already satisfied: joblib in /usr/local/lib/python3.7/dist-packages (from pycaret) (1.1.0)
Requirement already satisfied: textblob in /usr/local/lib/python3.7/dist-packages (from pycaret) (0.15.3)
Collecting pandas-profiling>=2.8.0
  Downloading pandas_profiling-3.1.0-py2.py3-none-any.whl (261 kB)
     |████████████████████████████████| 261 kB 53.7 MB/s 
Collecting pyLDAvis
  Downloading pyLDAvis-3.3.1.tar.gz (1.7 MB)
     |████████████████████████████████| 1.7 MB 42.3 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
    Preparing wheel metadata ... done
Requirement already satisfied: spacy<2.4.0 in /usr/local/lib/python3.7/dist-packages (from pycaret) (2.2.4)
Collecting scikit-learn==0.23.2
  Downloading scikit_learn-0.23.2-cp37-cp37m-manylinux1_x86_64.whl (6.8 MB)
     |████████████████████████████████| 6.8 MB 58.0 MB/s 
Requirement already satisfied: ipywidgets in /usr/local/lib/python3.7/dist-packages (from pycaret) (7.6.5)
Requirement already satisfied: cufflinks>=0.17.0 in /usr/local/lib/python3.7/dist-packages (from pycaret) (0.17.3)
Collecting scikit-plot
  Downloading scikit_plot-0.3.7-py3-none-any.whl (33 kB)
Requirement already satisfied: yellowbrick>=1.0.1 in /usr/local/lib/python3.7/dist-packages (from pycaret) (1.3.post1)
Requirement already satisfied: nltk in /usr/local/lib/python3.7/dist-packages (from pycaret) (3.2.5)
Collecting umap-learn
  Downloading umap-learn-0.5.2.tar.gz (86 kB)
     |████████████████████████████████| 86 kB 6.0 MB/s 
Collecting Boruta
  Downloading Boruta-0.3-py3-none-any.whl (56 kB)
     |████████████████████████████████| 56 kB 4.7 MB/s 
Requirement already satisfied: wordcloud in /usr/local/lib/python3.7/dist-packages (from pycaret) (1.5.0)
Requirement already satisfied: seaborn in /usr/local/lib/python3.7/dist-packages (from pycaret) (0.11.2)
Requirement already satisfied: IPython in /usr/local/lib/python3.7/dist-packages (from pycaret) (5.5.0)
Requirement already satisfied: gensim<4.0.0 in /usr/local/lib/python3.7/dist-packages (from pycaret) (3.6.0)
Collecting lightgbm>=2.3.1
  Downloading lightgbm-3.3.1-py3-none-manylinux1_x86_64.whl (2.0 MB)
     |████████████████████████████████| 2.0 MB 47.4 MB/s 
Requirement already satisfied: pandas in /usr/local/lib/python3.7/dist-packages (from pycaret) (1.1.5)
Collecting mlxtend>=0.17.0
  Downloading mlxtend-0.19.0-py2.py3-none-any.whl (1.3 MB)
     |████████████████████████████████| 1.3 MB 60.5 MB/s 
Requirement already satisfied: matplotlib in /usr/local/lib/python3.7/dist-packages (from pycaret) (3.2.2)
Requirement already satisfied: numpy==1.19.5 in /usr/local/lib/python3.7/dist-packages (from pycaret) (1.19.5)
Collecting pyod
  Downloading pyod-0.9.5.tar.gz (113 kB)
     |████████████████████████████████| 113 kB 58.7 MB/s 
Requirement already satisfied: plotly>=4.4.1 in /usr/local/lib/python3.7/dist-packages (from pycaret) (4.4.1)
Collecting mlflow
  Downloading mlflow-1.22.0-py3-none-any.whl (15.5 MB)
     |████████████████████████████████| 15.5 MB 50.3 MB/s 
Requirement already satisfied: scipy<=1.5.4 in /usr/local/lib/python3.7/dist-packages (from pycaret) (1.4.1)
Collecting imbalanced-learn==0.7.0
  Downloading imbalanced_learn-0.7.0-py3-none-any.whl (167 kB)
     |████████████████████████████████| 167 kB 62.1 MB/s 
Collecting kmodes>=0.10.1
  Downloading kmodes-0.11.1-py2.py3-none-any.whl (19 kB)
Requirement already satisfied: threadpoolctl>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from scikit-learn==0.23.2->pycaret) (3.0.0)
Requirement already satisfied: colorlover>=0.2.1 in /usr/local/lib/python3.7/dist-packages (from cufflinks>=0.17.0->pycaret) (0.3.0)
Requirement already satisfied: setuptools>=34.4.1 in /usr/local/lib/python3.7/dist-packages (from cufflinks>=0.17.0->pycaret) (57.4.0)
Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.7/dist-packages (from cufflinks>=0.17.0->pycaret) (1.15.0)
Requirement already satisfied: smart-open>=1.2.1 in /usr/local/lib/python3.7/dist-packages (from gensim<4.0.0->pycaret) (5.2.1)
Requirement already satisfied: traitlets>=4.2 in /usr/local/lib/python3.7/dist-packages (from IPython->pycaret) (5.1.1)
Requirement already satisfied: simplegeneric>0.8 in /usr/local/lib/python3.7/dist-packages (from IPython->pycaret) (0.8.1)
Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from IPython->pycaret) (2.6.1)
Requirement already satisfied: prompt-toolkit<2.0.0,>=1.0.4 in /usr/local/lib/python3.7/dist-packages (from IPython->pycaret) (1.0.18)
Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from IPython->pycaret) (4.4.2)
Requirement already satisfied: pexpect in /usr/local/lib/python3.7/dist-packages (from IPython->pycaret) (4.8.0)
Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from IPython->pycaret) (0.7.5)
Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets->pycaret) (1.0.2)
Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets->pycaret) (3.5.2)
Requirement already satisfied: ipykernel>=4.5.1 in /usr/local/lib/python3.7/dist-packages (from ipywidgets->pycaret) (4.10.1)
Requirement already satisfied: nbformat>=4.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets->pycaret) (5.1.3)
Requirement already satisfied: ipython-genutils~=0.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets->pycaret) (0.2.0)
Requirement already satisfied: tornado>=4.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=4.5.1->ipywidgets->pycaret) (5.1.1)
Requirement already satisfied: jupyter-client in /usr/local/lib/python3.7/dist-packages (from ipykernel>=4.5.1->ipywidgets->pycaret) (5.3.5)
Requirement already satisfied: wheel in /usr/local/lib/python3.7/dist-packages (from lightgbm>=2.3.1->pycaret) (0.37.0)
Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib->pycaret) (2.8.2)
Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.7/dist-packages (from matplotlib->pycaret) (0.11.0)
Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib->pycaret) (1.3.2)
Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib->pycaret) (3.0.6)
Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in /usr/local/lib/python3.7/dist-packages (from nbformat>=4.2.0->ipywidgets->pycaret) (2.6.0)
Requirement already satisfied: jupyter-core in /usr/local/lib/python3.7/dist-packages (from nbformat>=4.2.0->ipywidgets->pycaret) (4.9.1)
Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas->pycaret) (2018.9)
Requirement already satisfied: tqdm>=4.48.2 in /usr/local/lib/python3.7/dist-packages (from pandas-profiling>=2.8.0->pycaret) (4.62.3)
Collecting tangled-up-in-unicode==0.1.0
  Downloading tangled_up_in_unicode-0.1.0-py3-none-any.whl (3.1 MB)
     |████████████████████████████████| 3.1 MB 47.3 MB/s 
Requirement already satisfied: markupsafe~=2.0.1 in /usr/local/lib/python3.7/dist-packages (from pandas-profiling>=2.8.0->pycaret) (2.0.1)
Collecting pydantic>=1.8.1
  Downloading pydantic-1.8.2-cp37-cp37m-manylinux2014_x86_64.whl (10.1 MB)
     |████████████████████████████████| 10.1 MB 37.6 MB/s 
Collecting htmlmin>=0.1.12
  Downloading htmlmin-0.1.12.tar.gz (19 kB)
Collecting multimethod>=1.4
  Downloading multimethod-1.6-py3-none-any.whl (9.4 kB)
Collecting PyYAML>=5.0.0
  Downloading PyYAML-6.0-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (596 kB)
     |████████████████████████████████| 596 kB 40.0 MB/s 
Collecting phik>=0.11.1
  Downloading phik-0.12.0-cp37-cp37m-manylinux2010_x86_64.whl (675 kB)
     |████████████████████████████████| 675 kB 62.8 MB/s 
Requirement already satisfied: jinja2>=2.11.1 in /usr/local/lib/python3.7/dist-packages (from pandas-profiling>=2.8.0->pycaret) (2.11.3)
Collecting visions[type_image_path]==0.7.4
  Downloading visions-0.7.4-py3-none-any.whl (102 kB)
     |████████████████████████████████| 102 kB 12.8 MB/s 
Collecting joblib
  Downloading joblib-1.0.1-py3-none-any.whl (303 kB)
     |████████████████████████████████| 303 kB 71.5 MB/s 
Collecting requests>=2.24.0
  Downloading requests-2.26.0-py2.py3-none-any.whl (62 kB)
     |████████████████████████████████| 62 kB 995 kB/s 
Requirement already satisfied: missingno>=0.4.2 in /usr/local/lib/python3.7/dist-packages (from pandas-profiling>=2.8.0->pycaret) (0.5.0)
Requirement already satisfied: attrs>=19.3.0 in /usr/local/lib/python3.7/dist-packages (from visions[type_image_path]==0.7.4->pandas-profiling>=2.8.0->pycaret) (21.2.0)
Requirement already satisfied: networkx>=2.4 in /usr/local/lib/python3.7/dist-packages (from visions[type_image_path]==0.7.4->pandas-profiling>=2.8.0->pycaret) (2.6.3)
Collecting imagehash
  Downloading ImageHash-4.2.1.tar.gz (812 kB)
     |████████████████████████████████| 812 kB 49.7 MB/s 
Requirement already satisfied: Pillow in /usr/local/lib/python3.7/dist-packages (from visions[type_image_path]==0.7.4->pandas-profiling>=2.8.0->pycaret) (7.1.2)
Collecting scipy<=1.5.4
  Downloading scipy-1.5.4-cp37-cp37m-manylinux1_x86_64.whl (25.9 MB)
     |████████████████████████████████| 25.9 MB 1.6 MB/s 
Requirement already satisfied: retrying>=1.3.3 in /usr/local/lib/python3.7/dist-packages (from plotly>=4.4.1->pycaret) (1.3.3)
Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit<2.0.0,>=1.0.4->IPython->pycaret) (0.2.5)
Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.7/dist-packages (from pydantic>=1.8.1->pandas-profiling>=2.8.0->pycaret) (3.10.0.2)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests>=2.24.0->pandas-profiling>=2.8.0->pycaret) (2.10)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests>=2.24.0->pandas-profiling>=2.8.0->pycaret) (2021.10.8)
Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.7/dist-packages (from requests>=2.24.0->pandas-profiling>=2.8.0->pycaret) (2.0.8)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests>=2.24.0->pandas-profiling>=2.8.0->pycaret) (1.24.3)
Requirement already satisfied: blis<0.5.0,>=0.4.0 in /usr/local/lib/python3.7/dist-packages (from spacy<2.4.0->pycaret) (0.4.1)
Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /usr/local/lib/python3.7/dist-packages (from spacy<2.4.0->pycaret) (1.0.6)
Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from spacy<2.4.0->pycaret) (3.0.6)
Requirement already satisfied: plac<1.2.0,>=0.9.6 in /usr/local/lib/python3.7/dist-packages (from spacy<2.4.0->pycaret) (1.1.3)
Requirement already satisfied: thinc==7.4.0 in /usr/local/lib/python3.7/dist-packages (from spacy<2.4.0->pycaret) (7.4.0)
Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from spacy<2.4.0->pycaret) (2.0.6)
Requirement already satisfied: wasabi<1.1.0,>=0.4.0 in /usr/local/lib/python3.7/dist-packages (from spacy<2.4.0->pycaret) (0.8.2)
Requirement already satisfied: catalogue<1.1.0,>=0.0.7 in /usr/local/lib/python3.7/dist-packages (from spacy<2.4.0->pycaret) (1.0.0)
Requirement already satisfied: srsly<1.1.0,>=1.0.2 in /usr/local/lib/python3.7/dist-packages (from spacy<2.4.0->pycaret) (1.0.5)
Requirement already satisfied: importlib-metadata>=0.20 in /usr/local/lib/python3.7/dist-packages (from catalogue<1.1.0,>=0.0.7->spacy<2.4.0->pycaret) (4.8.2)
Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata>=0.20->catalogue<1.1.0,>=0.0.7->spacy<2.4.0->pycaret) (3.6.0)
Requirement already satisfied: notebook>=4.4.1 in /usr/local/lib/python3.7/dist-packages (from widgetsnbextension~=3.5.0->ipywidgets->pycaret) (5.3.1)
Requirement already satisfied: nbconvert in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets->pycaret) (5.6.1)
Requirement already satisfied: terminado>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets->pycaret) (0.12.1)
Requirement already satisfied: Send2Trash in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets->pycaret) (1.8.0)
Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.7/dist-packages (from jupyter-client->ipykernel>=4.5.1->ipywidgets->pycaret) (22.3.0)
Requirement already satisfied: ptyprocess in /usr/local/lib/python3.7/dist-packages (from terminado>=0.8.1->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets->pycaret) (0.7.0)
Requirement already satisfied: PyWavelets in /usr/local/lib/python3.7/dist-packages (from imagehash->visions[type_image_path]==0.7.4->pandas-profiling>=2.8.0->pycaret) (1.2.0)
Collecting docker>=4.0.0
  Downloading docker-5.0.3-py2.py3-none-any.whl (146 kB)
     |████████████████████████████████| 146 kB 70.7 MB/s 
Requirement already satisfied: entrypoints in /usr/local/lib/python3.7/dist-packages (from mlflow->pycaret) (0.3)
Requirement already satisfied: protobuf>=3.7.0 in /usr/local/lib/python3.7/dist-packages (from mlflow->pycaret) (3.17.3)
Requirement already satisfied: cloudpickle in /usr/local/lib/python3.7/dist-packages (from mlflow->pycaret) (1.3.0)
Collecting databricks-cli>=0.8.7
  Downloading databricks-cli-0.16.2.tar.gz (58 kB)
     |████████████████████████████████| 58 kB 5.9 MB/s 
Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.7/dist-packages (from mlflow->pycaret) (7.1.2)
Collecting querystring-parser
  Downloading querystring_parser-1.2.4-py2.py3-none-any.whl (7.9 kB)
Collecting alembic<=1.4.1
  Downloading alembic-1.4.1.tar.gz (1.1 MB)
     |████████████████████████████████| 1.1 MB 59.1 MB/s 
Collecting prometheus-flask-exporter
  Downloading prometheus_flask_exporter-0.18.6-py3-none-any.whl (17 kB)
Requirement already satisfied: sqlalchemy in /usr/local/lib/python3.7/dist-packages (from mlflow->pycaret) (1.4.27)
Requirement already satisfied: Flask in /usr/local/lib/python3.7/dist-packages (from mlflow->pycaret) (1.1.4)
Collecting gitpython>=2.1.0
  Downloading GitPython-3.1.24-py3-none-any.whl (180 kB)
     |████████████████████████████████| 180 kB 58.3 MB/s 
Collecting gunicorn
  Downloading gunicorn-20.1.0-py3-none-any.whl (79 kB)
     |████████████████████████████████| 79 kB 8.7 MB/s 
Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from mlflow->pycaret) (21.3)
Requirement already satisfied: sqlparse>=0.3.1 in /usr/local/lib/python3.7/dist-packages (from mlflow->pycaret) (0.4.2)
Collecting Mako
  Downloading Mako-1.1.6-py2.py3-none-any.whl (75 kB)
     |████████████████████████████████| 75 kB 4.4 MB/s 
Collecting python-editor>=0.3
  Downloading python_editor-1.0.4-py3-none-any.whl (4.9 kB)
Requirement already satisfied: tabulate>=0.7.7 in /usr/local/lib/python3.7/dist-packages (from databricks-cli>=0.8.7->mlflow->pycaret) (0.8.9)
Collecting websocket-client>=0.32.0
  Downloading websocket_client-1.2.3-py3-none-any.whl (53 kB)
     |████████████████████████████████| 53 kB 2.1 MB/s 
Collecting gitdb<5,>=4.0.1
  Downloading gitdb-4.0.9-py3-none-any.whl (63 kB)
     |████████████████████████████████| 63 kB 1.9 MB/s 
Collecting smmap<6,>=3.0.1
  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)
Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.7/dist-packages (from sqlalchemy->mlflow->pycaret) (1.1.2)
Requirement already satisfied: Werkzeug<2.0,>=0.15 in /usr/local/lib/python3.7/dist-packages (from Flask->mlflow->pycaret) (1.0.1)
Requirement already satisfied: itsdangerous<2.0,>=0.24 in /usr/local/lib/python3.7/dist-packages (from Flask->mlflow->pycaret) (1.1.0)
Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets->pycaret) (0.8.4)
Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets->pycaret) (4.1.0)
Requirement already satisfied: testpath in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets->pycaret) (0.5.0)
Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets->pycaret) (0.7.1)
Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets->pycaret) (1.5.0)
Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets->pycaret) (0.5.1)
Requirement already satisfied: prometheus-client in /usr/local/lib/python3.7/dist-packages (from prometheus-flask-exporter->mlflow->pycaret) (0.12.0)
Requirement already satisfied: future in /usr/local/lib/python3.7/dist-packages (from pyLDAvis->pycaret) (0.16.0)
Collecting pyLDAvis
  Downloading pyLDAvis-3.3.0.tar.gz (1.7 MB)
     |████████████████████████████████| 1.7 MB 37.5 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
    Preparing wheel metadata ... done
  Downloading pyLDAvis-3.2.2.tar.gz (1.7 MB)
     |████████████████████████████████| 1.7 MB 45.7 MB/s 
Requirement already satisfied: numexpr in /usr/local/lib/python3.7/dist-packages (from pyLDAvis->pycaret) (2.7.3)
Collecting funcy
  Downloading funcy-1.16-py2.py3-none-any.whl (32 kB)
Requirement already satisfied: numba>=0.35 in /usr/local/lib/python3.7/dist-packages (from pyod->pycaret) (0.51.2)
Requirement already satisfied: statsmodels in /usr/local/lib/python3.7/dist-packages (from pyod->pycaret) (0.10.2)
Requirement already satisfied: llvmlite<0.35,>=0.34.0.dev0 in /usr/local/lib/python3.7/dist-packages (from numba>=0.35->pyod->pycaret) (0.34.0)
Requirement already satisfied: patsy>=0.4.0 in /usr/local/lib/python3.7/dist-packages (from statsmodels->pyod->pycaret) (0.5.2)
Collecting pynndescent>=0.5
  Downloading pynndescent-0.5.5.tar.gz (1.1 MB)
     |████████████████████████████████| 1.1 MB 49.9 MB/s 
Building wheels for collected packages: htmlmin, imagehash, alembic, databricks-cli, pyLDAvis, pyod, umap-learn, pynndescent
  Building wheel for htmlmin (setup.py) ... done
  Created wheel for htmlmin: filename=htmlmin-0.1.12-py3-none-any.whl size=27098 sha256=d7dfcc5cb8473dd5eae3fcf51c538f92f876faa04e78c8b36d9c790b9fac7e10
  Stored in directory: /root/.cache/pip/wheels/70/e1/52/5b14d250ba868768823940c3229e9950d201a26d0bd3ee8655
  Building wheel for imagehash (setup.py) ... done
  Created wheel for imagehash: filename=ImageHash-4.2.1-py2.py3-none-any.whl size=295207 sha256=8b1e1a54f9880fb8de0530e8e168811d3264000c0375d179b04677d7db738f6f
  Stored in directory: /root/.cache/pip/wheels/4c/d5/59/5e3e297533ddb09407769762985d134135064c6831e29a914e
  Building wheel for alembic (setup.py) ... done
  Created wheel for alembic: filename=alembic-1.4.1-py2.py3-none-any.whl size=158172 sha256=3a382d7a8aa3f735be58614dc83527e0801ccb0bc893eb96cc388ee8f0a5dd91
  Stored in directory: /root/.cache/pip/wheels/be/5d/0a/9e13f53f4f5dfb67cd8d245bb7cdffe12f135846f491a283e3
  Building wheel for databricks-cli (setup.py) ... done
  Created wheel for databricks-cli: filename=databricks_cli-0.16.2-py3-none-any.whl size=106811 sha256=ada21177391b9688188e6f778b0ec6b6001615c2b2f13bef53090805b2f183bf
  Stored in directory: /root/.cache/pip/wheels/f4/5c/ed/e1ce20a53095f63b27b4964abbad03e59cf3472822addf7d29
  Building wheel for pyLDAvis (setup.py) ... done
  Created wheel for pyLDAvis: filename=pyLDAvis-3.2.2-py2.py3-none-any.whl size=135618 sha256=29ef50e1603fe00d18a256b833c7feddebc16ef3ac82f37f109f991b0f95b4b0
  Stored in directory: /root/.cache/pip/wheels/f8/b1/9b/560ac1931796b7303f7b517b949d2d31a4fbc512aad3b9f284
  Building wheel for pyod (setup.py) ... done
  Created wheel for pyod: filename=pyod-0.9.5-py3-none-any.whl size=132699 sha256=851491ca675bc8eb4d9ecfb52396f362de25c1443531f442a9528c0b9b3f7b21
  Stored in directory: /root/.cache/pip/wheels/3d/bb/b7/62b60fb451b33b0df1ab8006697fba7a6a49709a629055cf77
  Building wheel for umap-learn (setup.py) ... done
  Created wheel for umap-learn: filename=umap_learn-0.5.2-py3-none-any.whl size=82709 sha256=f4bae757148b4cf4930e495a816ecb3f6fcc3a16d1014c85ce052bb2acccb378
  Stored in directory: /root/.cache/pip/wheels/84/1b/c6/aaf68a748122632967cef4dffef68224eb16798b6793257d82
  Building wheel for pynndescent (setup.py) ... done
  Created wheel for pynndescent: filename=pynndescent-0.5.5-py3-none-any.whl size=52603 sha256=e19d78d031a739792e30a3bf2d93865296b6eb66226835f66a8287b1330882f1
  Stored in directory: /root/.cache/pip/wheels/af/e9/33/04db1436df0757c42fda8ea6796d7a8586e23c85fac355f476
Successfully built htmlmin imagehash alembic databricks-cli pyLDAvis pyod umap-learn pynndescent
Installing collected packages: tangled-up-in-unicode, smmap, scipy, multimethod, joblib, websocket-client, visions, scikit-learn, requests, python-editor, Mako, imagehash, gitdb, querystring-parser, PyYAML, pynndescent, pydantic, prometheus-flask-exporter, phik, htmlmin, gunicorn, gitpython, funcy, docker, databricks-cli, alembic, umap-learn, scikit-plot, pyod, pyLDAvis, pandas-profiling, mlxtend, mlflow, lightgbm, kmodes, imbalanced-learn, Boruta, pycaret
  Attempting uninstall: scipy
    Found existing installation: scipy 1.4.1
    Uninstalling scipy-1.4.1:
      Successfully uninstalled scipy-1.4.1
  Attempting uninstall: joblib
    Found existing installation: joblib 1.1.0
    Uninstalling joblib-1.1.0:
      Successfully uninstalled joblib-1.1.0
  Attempting uninstall: scikit-learn
    Found existing installation: scikit-learn 1.0.1
    Uninstalling scikit-learn-1.0.1:
      Successfully uninstalled scikit-learn-1.0.1
  Attempting uninstall: requests
    Found existing installation: requests 2.23.0
    Uninstalling requests-2.23.0:
      Successfully uninstalled requests-2.23.0
  Attempting uninstall: PyYAML
    Found existing installation: PyYAML 3.13
    Uninstalling PyYAML-3.13:
      Successfully uninstalled PyYAML-3.13
  Attempting uninstall: pandas-profiling
    Found existing installation: pandas-profiling 1.4.1
    Uninstalling pandas-profiling-1.4.1:
      Successfully uninstalled pandas-profiling-1.4.1
  Attempting uninstall: mlxtend
    Found existing installation: mlxtend 0.14.0
    Uninstalling mlxtend-0.14.0:
      Successfully uninstalled mlxtend-0.14.0
  Attempting uninstall: lightgbm
    Found existing installation: lightgbm 2.2.3
    Uninstalling lightgbm-2.2.3:
      Successfully uninstalled lightgbm-2.2.3
  Attempting uninstall: imbalanced-learn
    Found existing installation: imbalanced-learn 0.8.1
    Uninstalling imbalanced-learn-0.8.1:
      Successfully uninstalled imbalanced-learn-0.8.1
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
google-colab 1.0.0 requires requests~=2.23.0, but you have requests 2.26.0 which is incompatible.
datascience 0.10.6 requires folium==0.2.1, but you have folium 0.8.3 which is incompatible.
albumentations 0.1.12 requires imgaug<0.2.7,>=0.2.5, but you have imgaug 0.2.9 which is incompatible.
Successfully installed Boruta-0.3 Mako-1.1.6 PyYAML-6.0 alembic-1.4.1 databricks-cli-0.16.2 docker-5.0.3 funcy-1.16 gitdb-4.0.9 gitpython-3.1.24 gunicorn-20.1.0 htmlmin-0.1.12 imagehash-4.2.1 imbalanced-learn-0.7.0 joblib-1.0.1 kmodes-0.11.1 lightgbm-3.3.1 mlflow-1.22.0 mlxtend-0.19.0 multimethod-1.6 pandas-profiling-3.1.0 phik-0.12.0 prometheus-flask-exporter-0.18.6 pyLDAvis-3.2.2 pycaret-2.3.5 pydantic-1.8.2 pynndescent-0.5.5 pyod-0.9.5 python-editor-1.0.4 querystring-parser-1.2.4 requests-2.26.0 scikit-learn-0.23.2 scikit-plot-0.3.7 scipy-1.5.4 smmap-5.0.0 tangled-up-in-unicode-0.1.0 umap-learn-0.5.2 visions-0.7.4 websocket-client-1.2.3
```
'pycaret'을 '구글코랩'에서 설치했기 때문에 이코드를 반드시 입력해서

'코랩 모드'로 바꿔줘야 된다.

<코랩 모드 코드>
```python
from pycaret.utils import enable_colab
enable_colab()
```
<결과 화면>
```python
Colab mode enabled.
```
<파이캐롯 데이터 셋 확인 코드>
```python
from pycaret.datasets import get_data
dataset = get_data('diamond')
```
<결과 화면>
![diamond](https://user-images.githubusercontent.com/96108301/147238236-9cf65900-068c-4c54-93c5-7bcf10e4e804.PNG)

아래 부터는 그냥 이어지는 '실습용 코드' 정도로 보면 된다.

```python
data = dataset.sample(frac=0.9, random_state=786)
data_unseen = dataset.drop(data.index)

data.reset_index(drop=True, inplace=True)
data_unseen.reset_index(drop=True, inplace=True)

print('Data for Modeling: ' + str(data.shape))
print('Unseen Data For Predictions: ' + str(data_unseen.shape))
```
<결과 화면>
```python
Data for Modeling: (5400, 8)
Unseen Data For Predictions: (600, 8)
```
```python
from pycaret.regression import *
exp_reg101 = setup(data = data, target = 'Price', session_id=123)
```
<결과 화면>
![r1](https://user-images.githubusercontent.com/96108301/147239115-38c941a2-9262-4fa8-a55b-77ea9ddd4846.PNG)
![r2](https://user-images.githubusercontent.com/96108301/147239120-d04a7a5c-5cff-477c-beb3-4bc638af7c08.PNG)
![r3](https://user-images.githubusercontent.com/96108301/147239123-79d7a4a5-8bbb-4f0f-b08f-51d5623ac53e.PNG)

```python
best = compare_models(exclude = ['ransac'])
```
<결과 화면>
![best](https://user-images.githubusercontent.com/96108301/147239400-8c9d9b87-4811-4b32-b206-d0271c7cc4ef.PNG)

- 사이킷런 LinearRegression 클래스

--> LinearRegression(fit_intercept = True, normalize = False) 

평가지표

- MAE(Mean Absolute Error) 오차 차이를 절댓값으로 변환해 평균한 것


- MSE(Mean Squared Error) 오차 차이를 제곱해 평균한 것


- MSLE(MSE) 로그를 적용


- RMSE 


========= 
- R^2: 분산 기반으로 예측 성능을 평가 함. R2 - 예측값(분산) / 실제값 분산

==== 
- 사이킷런 회귀 평가 모형 함수


- 기본제공: MAE, MSE, R^2


- RMSE <-- 사용자 정의 함수 구현 및 활용

```python
import pandas as pd


bostonDF = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")
bostonDF.head()
```
<결과 화면>

![crim](https://user-images.githubusercontent.com/96108301/147239869-e2817377-018a-4daa-a061-e3beda7ff0e0.PNG)

## EDA
- 종속변수가 기준, y값, medv

```python
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize = (16, 8), ncols = 4, nrows = 2)
lm_features = ["rm", "zn", "indus", "nox", "age", "ptratio", "lstat", "rad"]

for i, feature in enumerate(lm_features):
  row = int(i/4)
  col = i%4
  print("row is {}, col is {}".format(row, col))
  sns.regplot(x = feature, y = "medv", data = bostonDF, ax = ax[row][col])
```
<결과 화면>

![medv](https://user-images.githubusercontent.com/96108301/147240310-96b08251-0949-4af4-a13e-813bea576003.PNG)

- 두 연속형 변수를 활용한 산점도 그리고, 회귀식 그리고

- 박스플롯 (x: 명목형, y: medv) 

```python
rm          3.4
chas        3.0
rad         0.4
zn          0.1
b           0.0
tax        -0.0
age         0.0
indus       0.0
crim       -0.1
lstat      -0.6
ptratio    -0.9
dis        -1.7
nox       -19.8
```
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression # model

y_target = bostonDF["medv"] # 종속변수, Y
X_data = bostonDF.drop(['medv', 'rad', 'zn', 'b', 'tax', 'age', 'indus', 'crim', 'lstat'], axis = 1, inplace = False) # 독립변수

y_target.shape, X_data.shape
```
<결과 화면>
```python
((506,), (506, 5))
```
## 데이터셋 분리

- 예측, 시뮬레이션, 가상의 데이터를 가지고 예측 & 시뮬레이션

- 예측한 결괏값 vs 실젯값 비교

```python
# 임의 샘플링

X_train, X_test, y_train, y_test = train_test_split(X_data, y_target, test_size = 0.3, random_state=156)
X_train.shape, X_test.shape, y_train.shape, y_test.shape
```
<결과 화면>
```python
((354, 5), (152, 5), (354,), (152,))
```
## ML 모형 만들기
```python
lr = LinearRegression()
lr.fit(X_train, y_train)


y_preds = lr.predict(X_test)
y_preds
```
<결과 화면>
```python
array([26.78074859, 16.40377991, 34.38443472, 19.13328473, 32.89690238,
       19.25298249, 28.32071818, 22.76654888,  9.87108567, 14.66339227,
       21.55844556, 17.27788854, 28.55574467, 38.50512646, 23.60848806,
       24.03347202, 23.82317119, 15.9119451 , 28.65132167, 20.98388455,
       20.29188703, 18.37003455, 18.58675839, 14.89143225, 35.24799305,
        7.70600921, 19.39133905, 15.97963635, 16.90296718, 15.484303  ,
       29.67753869, 17.58268684, 16.91992352, 22.47407959, 16.57706526,
       18.5381101 , 13.34337954, 24.11893098, 15.48185399, 24.3234222 ,
       36.24776797, 19.60882283, 20.95016211,  6.85667164, 20.32077896,
       23.05614583, 24.65371876, 35.25609168, 22.32959594, 25.96437918,
       27.29101785, 43.32992941, 41.76994078, 19.34288261, 24.8690423 ,
       25.99270875, 20.76285715, 33.13792328, 25.00439224, 16.82906893,
       22.80895172, 23.72489982, 24.53360315, 11.82722067, 17.55728132,
       37.43371362, 33.37256916, 25.65966256, 20.90725715, 21.09529467,
       15.22097444, 30.6234335 , 37.42143489, 26.22092177, 16.71532104,
       32.62735407, 23.41004013, 23.86575538, 18.75430877, 15.9914079 ,
       30.87778491, 16.04423898, 19.01496945, 20.04269634, 28.30832805,
       15.1948795 , 30.47430322, 33.93480059, 23.87721263, 29.7167635 ,
       29.85142798, 19.10737457, 28.49523963, 27.69846662, 25.49534489,
       24.59255802, 12.34870184, 26.65951587, 31.26197918, 17.86101862,
       27.3059424 , 18.18058484, 15.67184217, 13.17304165, 17.91281425,
       23.48894551, 24.53921273, 28.14530028, 16.05340908, 24.22120622,
       21.94517346, 26.62930956, 11.39298015, 18.53099857, 22.75407122,
       33.6679728 , 23.35342973, 20.85267956, 19.69347759, 28.12264641,
       28.56541499, 17.91759633, 27.83520695, 33.8011824 , 21.75436813,
       26.6360736 , 14.70682076, 19.99114889, 21.81029849, 31.72247354,
       21.33041025, 23.52438417, 35.55842163, 20.54294729, 38.34696416,
       19.25750865, 17.07595035, 18.31764392, 17.66658651, 23.12171447,
       19.58446231, 19.90774119, 14.84809066, 19.50652744, 38.83812958,
       15.26095952, 28.56874885, 17.62298514, 22.46794555, 23.28435884,
       18.8439135 , 31.16286012])
```
## 모형 평가

```python
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_preds)

print("MSE: {0:.3f}".format(mse))
```
<결과 화면>
```python
MSE: 21.369
```
y = 상수값 + rm 기울기 x rm의 값 

```python
import numpy as np 

print("절편 값:", lr.intercept_) # 절편 값
print("회귀 계수값", np.round(lr.coef_, 1))

coeff_df = pd.Series(data=np.round(lr.coef_, 1), index = X_data.columns)
coeff_df.sort_values(ascending=False)
```
<결과 화면>
```python
절편 값: 26.830373506191982
회귀 계수값 [  4.3 -33.1   6.5  -1.1  -1.2]
rm          6.5
chas        4.3
dis        -1.1
ptratio    -1.2
nox       -33.1
dtype: float64
```
