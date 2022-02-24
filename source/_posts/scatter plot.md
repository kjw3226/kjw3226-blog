---
title: Scatter plot(산점도) 그리기
tag: Scatter plot(산점도) 그리기
date: 2021-11-23
categories:	Matplotlib

---
산점도 (Scatter plot)는 두 변수의 상관 관계를 직교 좌표계의 평면에 점으로 표현하는 그래프다.

matplotlib.pyplot 모듈의 scatter() 함수를 이용하면 산점도를 그릴 수 있다.

Keyword: plt.scatter(), scatter plot, 산점도

코드는 아래와 같다.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n = 50
x = np.random.rand(n) #NumPy의 random 모듈에 포함된 rand() 함수를 사용해서 
                      # (0, 1) 범위의 난수를 각각 50개씩 생성했다.
y = np.random.rand(n)
plt.scatter(x, y) #x, y 데이터를 순서대로 scatter() 함수에 입력하면 
                  # x, y 값에 해당하는 위치에 기본 마커가 표시됩니다.
plt.show()
```
![scatter plot](https://user-images.githubusercontent.com/93234783/142975965-381ca8a4-d8a1-45c4-9948-cc8ba0922315.PNG)

다음은 색과 크기를 결정하는 코드이다.

예를 들어 plot() 함수에 markersize=20으로 지정하는 것과

scatter() 함수에 s=20**2으로 지정하는 것은 같은 크기의 마커를 표시하도록 합니다.

마커의 색상은 데이터의 길이와 같은 크기의 숫자 시퀀스 또는 rgb, 

그리고 Hex code 색상을 입력해서 지정합니다.

마커에 임의의 크기와 색상을 지정했습니다. 결과는 아래와 같습니다.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n = 50
x = np.random.rand(n)
y = np.random.rand(n)
area = (30 * np.random.rand(n))**2 #마커의 크기는 size**2 의 형태로 지정.
colors = np.random.rand(n)

plt.scatter(x, y, s=area, c=colors) #scatter() 함수의 s, c 파라미터는 각각 마커의 크기와 색상을 지정.
plt.show()
```
![scatter plot2](https://user-images.githubusercontent.com/93234783/142976759-92e8b4bf-2dfb-4728-a969-845facd8d32a.PNG)
