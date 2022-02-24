---
title: hitmap(히트맵) 그리기
tag: hitmap(히트맵) 그리기
date: 2021-11-22
categories:	Matplotlib

---
 히트맵 (Heatmap)은 다양한 값을 갖는 숫자 데이터를 열분포 형태와 같이 색상을 이용해서 시각화한 것이다.
 matplotlib.pyplot 모듈의 matshow() 함수를 이용해서 2차원 어레이 형태의 숫자 데이터를 히트맵을 그려보자.
 ```python
 import matplotlib.pyplot as plt
 import numpy as np

 arr = np.random.standard_normal((30, 40)) #np.random.standard_normal() 로 만들어진 2차원 어레이 arr는 
                                          #표준정규분포를 갖는 (30, 40) 형태의 2차원 어레이 

 plt.matshow(arr) #matshow() 함수에 어레이의 형태로 
                 #값들을 직접 입력하면 아래와 같은 그래프가 표시됩니다.

 plt.show()
 ```
![hitmap1](https://user-images.githubusercontent.com/93234783/142810226-48fa2b94-f9ad-4c67-9f15-3b6721d6f287.PNG)

```python
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.standard_normal((30, 40))

plt.matshow(arr)
plt.colorbar(shrink=0.8, aspect=10) #히트맵에 컬러바를 함께 나타내기 위해서 colorbar() 함수를 사용합니다.
                                    
plt.show()
```
![hitmap2](https://user-images.githubusercontent.com/93234783/142810572-0adaa41a-608d-4fa7-835f-a2d9ef9c797d.PNG)

colorbar() 함수의 shrink 파라미터는 컬러바의 크기를 결정합니다.
shrink 파라미터의 디폴트 값은 1.0이며, 예제에서는 0.8로 지정했습니다.
colorbar() 함수의 aspect 파라미터는 컬러바의 종횡비 (Aspect ratio)를 결정합니다.

참고 : https://codetorial.net/matplotlib/heatmap.html