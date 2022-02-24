---
title: pyplot API+object oriented API (Pyplot API+객체지향 API)
tag: pyplot API+object oriented API (Pyplot API+객체지향 API)
date: 2021-11-22
categories:	Plotly

---
'kaggle' 대회나 'Dacon' 대회를 나가게 된다면 
 위 처럼의 형식으로 되어 있는 코드를 '지향'하고 
 다른 형식으로 짜여진 코드는 '지양' 하는 것이 본인이나 팀에 매우 
 도움이 될 것이다.
 그 이유는 이런 형식으로 코드가 짜여져 있으면 
 객체지향이든 'pyplot'이든 어떤 형식이든 
 활용이 가능해 지기 때문이다.
 코드는 아래와 같다.

```python
import yfinance as yf # yfinance 모듈의 yf 함수를 가져와 사용하겠다는 뜻.
import matplotlib.pyplot as plt #matplotlib.pyplot 모듈에 plt함수를 가져와 사용하겠다는 뜻.

data = yf.download('AAPL', '2019-08-01', '2020-08-01') 
ts = data['Open']

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(ts)
ax.set_title('Stock Market fluctuation of AAPL')
ax.legend(labels=['Price'], loc='best')
ax.set_xlabel('Date') 
ax.set_ylabel('Stock Market Open Price')
plt.show() #plt.show()를 사용하기 전까지는 제목이라든지 시각 요소들을 바꾸거나 설정할 수 있다.
           #현재의 컨텍스트가 flush()되는 구조인 듯 하다. 다시 차트를 생성하고 타이틀을 붙인 후에 렌더링할 수 있다.
           #matplotlib.pyplot 모듈의 show() 함수는 그래프를 화면에 나타나도록 합니다.
```

![plotly api+object oriented api 1](https://user-images.githubusercontent.com/93234783/142788856-5bc06975-c1e5-45cc-a22c-8c798b68564e.PNG)