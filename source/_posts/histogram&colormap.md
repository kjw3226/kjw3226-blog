---
title: hiatogram & colormap 그리기
tag: hiatogram & colormap 그리기
date: 2021-11-24
categories:	Matplotlib
---

히스토그램 (Histogram)은 도수분포표를 그래프로 나타낸 것으로서, 가로축은 계급, 세로축은 도수 (횟수나 개수 등)를 나타냅니다.

이번에는 matplotlib.pyplot 모듈의 hist() 함수를 이용해서 다양한 히스토그램을 그려 보겠습니다.

Keyword: plt.hist(), histogram, 히스토그램

```python
import matplotlib.pyplot as plt

weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
          80, 59, 67, 81, 69, 73, 69, 74, 70, 65]

plt.hist(weight)

plt.show()
```
![histogram1](https://user-images.githubusercontent.com/93234783/143182745-a84deba0-d93e-4aa5-93f9-81f096e75ee1.png)

weight는 몸무게 값을 나타내는 리스트입니다.

hist() 함수에 리스트의 형태로 값들을 직접 입력해주면 됩니다.

결과는 위와 같다.

hist() 함수의 bins 파라미터는 히스토그램의 가로축 구간의 개수를 지정합니다.

아래 그림과 같이 구간의 개수에 따라 히스토그램 분포의 형태가 달라질 수 있기 때문에

적절한 구간의 개수를 지정해야 합니다.

```python
import matplotlib.pyplot as plt

weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
          80, 59, 67, 81, 69, 73, 69, 74, 70, 65]

plt.hist(weight, label='bins=10')
plt.hist(weight, bins=30, label='bins=30')
plt.legend()
plt.show()
```
![histogram2](https://user-images.githubusercontent.com/93234783/143182751-a06d0b40-8255-4c6f-9882-a7115e86728e.png)

첫번째 히스토그램은 bins 값을 지정하지 않아서 기본값인 10으로 지정되었습니다.

두번째 히스토그램은 bins 값을 30으로 지정했습니다.

위와 같이 다른 분포를 나타냅니다.

```python
import matplotlib.pyplot as plt

weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
          80, 59, 67, 81, 69, 73, 69, 74, 70, 65]

plt.hist(weight, cumulative=True, label='cumulative=True')
plt.hist(weight, cumulative=False, label='cumulative=False')
plt.legend(loc='upper left')
plt.show()
```
![histogram3](https://user-images.githubusercontent.com/93234783/143182756-de243cfb-cc34-4fe2-9100-0e06f91bba54.png)

cumulative 파라미터를 True로 지정하면 누적 히스토그램을 나타냅니다.

디폴트는 False로 지정됩니다.

결과는 위와 같다.

```python
import matplotlib.pyplot as plt

weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
        80, 59, 67, 81, 69, 73, 69, 74, 70, 65]
weight2 = [52, 67, 84, 66, 58, 78, 71, 57, 76, 62, 51, 79,
        69, 64, 76, 57, 63, 53, 79, 64, 50, 61]

plt.hist((weight, weight2), histtype='bar')
plt.title('histtype - bar')
plt.figure()

plt.hist((weight, weight2), histtype='barstacked')
plt.title('histtype - barstacked')
plt.figure()

plt.hist((weight, weight2), histtype='step')
plt.title('histtype - step')
plt.figure()

plt.hist((weight, weight2), histtype='stepfilled')
plt.title('histtype - stepfilled')
plt.show()
```
![histogram4](https://user-images.githubusercontent.com/93234783/143182914-b7ad42e9-f322-4bd1-b0dd-577da1c595a0.png)

![histogram5](https://user-images.githubusercontent.com/93234783/143182917-9296f425-2168-4f3f-a9fe-59a971d3a7f4.png)

![histogram6](https://user-images.githubusercontent.com/93234783/143183000-1274880e-8c42-434a-84d9-66727727f955.png)

![histogram7](https://user-images.githubusercontent.com/93234783/143183002-7855cb04-a942-4cdb-a060-0c60ef69b48c.png)


histtype은 히스토그램의 종류를 지정합니다.

{‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’} 중에서 선택할 수 있으며, 디폴트는 ‘bar’입니다.

예제에서와 같이 두 종류의 데이터를 히스토그램으로 나타냈을 때, histtype의 값에 따라 각기 다른 히스토그램이 그려집니다.

결과는 위와 같다.

```python
import matplotlib.pyplot as plt
import numpy as np


a = 2.0 * np.random.randn(10000) + 1.0
b = np.random.standard_normal(10000)
c = 20.0 * np.random.rand(5000) - 10.0

plt.hist(a, bins=100, density=True, alpha=0.7, histtype='step')
plt.hist(b, bins=50, density=True, alpha=0.5, histtype='stepfilled')
plt.hist(c, bins=100, density=True, alpha=0.9, histtype='step')

plt.show()
```
![histogram8](https://user-images.githubusercontent.com/93234783/143183066-da5f0c77-821e-44ef-9448-fc7c7c55ec6e.png)

Numpy의 np.random.randn(), np.random.standard_normal(), np.random.rand() 함수를 이용해서 임의의 값들을 만들었습니다.

어레이 a는 표준편차 2.0, 평균 1.0을 갖는 정규분포, 어레이 b는 표준정규분포를 따릅니다.

어레이 c는 -10.0에서 10.0 사이의 균일한 분포를 갖는 5000개의 임의의 값입니다.

density=True로 설정해주면, 밀도함수가 되어서 막대의 아래 면적이 1이 됩니다.

alpha는 투명도를 의미합니다. 0.0에서 1.0 사이의 값을 갖습니다.

결과는 위와 같다.



matplotlib.pyplot 모듈은 컬러맵을 간편하게 설정하기 위한 여러 함수를 제공합니다.

아래의 함수들을 사용해서 그래프의 컬러맵을 설정하는 방식에 대해 소개합니다.

autumn(), bone(), cool(), copper(), flag(), gray(), hot(), hsv(), inferno(), jet(), magma(), nipy_spectral(),

pink(), plasma(), prism(), spring(), summer(), viridis(), winter().

Keyword: colormap, 컬러맵 설정

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
arr = np.random.standard_normal((8, 100))

plt.subplot(2, 2, 1)
# plt.scatter(arr[0], arr[1], c=arr[1], cmap='spring')
plt.scatter(arr[0], arr[1], c=arr[1])
plt.spring()
plt.title('spring')

plt.subplot(2, 2, 2)
plt.scatter(arr[2], arr[3], c=arr[3])
plt.summer()
plt.title('summer')

plt.subplot(2, 2, 3)
plt.scatter(arr[4], arr[5], c=arr[5])
plt.autumn()
plt.title('autumn')

plt.subplot(2, 2, 4)
plt.scatter(arr[6], arr[7], c=arr[7])
plt.winter()
plt.title('winter')

plt.tight_layout()
plt.show()
```
![colormap_output1](https://user-images.githubusercontent.com/93234783/143183111-2347e844-7661-4ba4-b334-265cf70087b4.png)

subplot() 함수를 이용해서 네 영역에 각각의 그래프를 나타내고,

spring(), summer(), autumn(), winter() 함수를 이용해서 컬러맵을 다르게 설정했습니다.

결과는 위와 같습니다.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
arr = np.random.standard_normal((8, 100))

plt.subplot(2, 2, 1)
plt.scatter(arr[0], arr[1], c=arr[1])
plt.viridis()
plt.title('viridis')
plt.colorbar()

plt.subplot(2, 2, 2)
plt.scatter(arr[2], arr[3], c=arr[3])
plt.plasma()
plt.title('plasma')
plt.colorbar()

plt.subplot(2, 2, 3)
plt.scatter(arr[4], arr[5], c=arr[5])
plt.jet()
plt.title('jet')
plt.colorbar()

plt.subplot(2, 2, 4)
plt.scatter(arr[6], arr[7], c=arr[7])
plt.nipy_spectral()
plt.title('nipy_spectral')
plt.colorbar()

plt.tight_layout()
plt.show()
```

![colormap_output2](https://user-images.githubusercontent.com/93234783/143183148-f124f260-b9fb-43fa-8b86-7323878e2c66.png)


colorbar() 함수를 사용하면 그래프 영역에 컬러바를 포함할 수 있습니다.

결과는 위와 같다.


```python
import matplotlib.pyplot as plt
from matplotlib import cm

cmaps = plt.colormaps()
for cm in cmaps:
    print(cm)
````

pyplot 모듈의 colormaps() 함수를 사용해서 Matplotlib에서 사용할 수 있는 모든 컬러맵의 이름을 얻을 수 있습니다.

예를 들어, winter와 winter_r은 순서가 앞뒤로 뒤집어진 컬러맵입니다.

참고 : https://wikidocs.net/92112


