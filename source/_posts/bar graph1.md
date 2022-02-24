---
title: bar graph1(막대그래프)
tag: bar graph1(막대그래프)
date: 2021-11-11
categories:	Matplotlib

---
  오늘은 '막대그래프'를 그리는걸 연습했다.

```python
  import matplotlib.pyplot as plt  #또는 from matplotlib import pyplot as plt 로 쓸 수도 있다.

  years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
  gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3] #1인당 국민소득
 
  plt.bar(range(len(years)), gdp)      #막대그래프 호출: bar(x, y) 
 
  plt.title("GDP per capita")          #차트 제목
  plt.ylabel('dollars')                #y축 라벨
 
  plt.xticks(range(len(years)), years) #x축에 틱을 붙임.
  plt.show()   #그래프를 보여준다.
```

![m b1](https://user-images.githubusercontent.com/96108301/146661706-39bbcf8b-938e-4b3e-ae9f-555e5f3a9d93.PNG)

  위의 코드에서 처럼 맨 처음에 'matplotlib'를 import 해줘야만 '막대그래프'를
  그릴 수 있다.
  

  또한 막대그래프의 색깔을 바꾸고 싶으면 

   https://matplotlib.org/3.1.0/gallery/color/named_colors.html
   사이트를 참고해서
   
   넣고 싶은 색을 골라서  아래의 코드 처럼 'colors' 부분에 색 이름을 넣어주면 
   막대 그래프 색이 변하게 된다.

   ```python
   import matplotlib.pyplot as plt
   #또는 from matplotlib import pyplot as plt 로 쓸 수도 있다.
   import numpy as np
   
   x = np.arange(3)  #arange 함수는 해당되는 숫자 미만의 수를 출력해준다.(예: '5'를 입력하면 '1,2,3,4'까지만 출력)
   years = ['2018', '2019', '2020'] 
   values = [100, 400, 900]
   colors = ['y', 'dodgerblue', 'C2']  #막대그래프의 색깔이 변하게 해준다.

   plt.bar(x, values, color=colors)  #막대그래프 호출: bar(x, y) 
   
   plt.xticks(x, years)    #x축에 틱을 붙임.

   plt.show()  #그래프를 보여준다.
   ```
  ![m b2](https://user-images.githubusercontent.com/96108301/146661707-c7cb7911-2445-4fbc-802d-ea04cdc5cc5a.PNG)


   또한 'import matplotlib.pyplot as plt'를 입력하지 않고
   아래의 코드처럼 입력해도 'Matplotlib'에서는 
   bar chart(막대 그래프)를 그릴 수 있도록 'plt.bar()' 메서드를 제공
   제공하기 때문에 에러를 띄우지 않고 그래프를 출력할 수 있다.
   
   ```python
   days_in_year = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
   plt.bar(range(len(days_in_year)), days_in_year)
   plt.show()  #그래프를 보여준다.
   ``` 

   아래의 코드는 'x-labels를 설정하기 전에 반드시 x-ticks를 설정해야 한다.'
   라는 것을 보여주는 코드다.

   ```python
   ax = plt.subplot()  #여러개의 그래프를 그릴수 있게 해준다.

   ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])

   ax.set_xticklabels(['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'], rotation=30) 
   #x축의 모든 막대그래프 하나 하나의 이름을 따로 설정한다.

   plt.xlabel('Planets')  #x축 전체의 이름을 설정한다.

   plt.ylabel('Days in the Year')  #y축 전체의 이름을 설정한다.

   plt.show()  #그래프를 보여준다.
   ```

   ![m b3](https://user-images.githubusercontent.com/96108301/146661708-b55f3b37-64f8-4482-8ddb-33c7595ba46e.PNG)

   ```python
   import matplotlib.pyplot as plt

   X1=[1,3,5,7]
   data1 = [1,2,3,4]
   plt.bar(X1, data1,color='r',width=0.5) #'width'를  '0.5'로 설정해서 그래프 사이 간격이 '0.5'만큼 벌어진다.

   X2=[1+0.5,3+0.5,5+0.5,7+0.5]
   data2 = [2,3,4,5]
   plt.bar(X2, data2,color='g',width=0.5) #'width'를  '0.5'로 설정해서 그래프 사이 간격이 '0.5'만큼 벌어진다.

   X3=[1+1,3+1,5+1,7+1]
   data3 = [3,4,5,6]
   plt.bar(X3, data3,color='b',width=0.5) #'width'를  '0.5'로 설정해서 그래프 사이 간격이 '0.5'만큼 벌어진다.
   ```
   ![m b4](https://user-images.githubusercontent.com/96108301/146661709-6becc7e4-07da-4122-8c2c-cd6068e64b34.PNG)
   ```python
   import matplotlib.pyplot as plt

   X=['a','b','c','d']
   height = [1,2,3,4]

   plt.barh(X, height)  #'barh'는 bar horizontal 의 약어이다. 그렇기 때문에 그래프가 '가로'방향으로 그려진다.
   plt.show()

   ```

  ![m b5](https://user-images.githubusercontent.com/96108301/146661710-9eeaae7e-052d-4a60-a4a0-b5af909e3b28.PNG)

   ```python
   import matplotlib.pyplot as plt

   X=[1,3,5,7]
   data = [1,2,3,4]
   plt.bar(X, data,width=1.5) #위의 코드에서 등장했던 'width'함수의 또 다른 기능은 그래프간 간격과 함께 두께도 설정해주는 기능이다.
   plt.show()
   ```

  ![m b6](https://user-images.githubusercontent.com/96108301/146661712-5f30b68f-697a-408e-8bee-ab6951b70ab6.PNG)

   ```python
   import matplotlib.pyplot as plt

   X=[1,3,5,7]
   data = [1,2,3,4]
   plt.bar(X, data,color='y')
   ticklabel=['a','b','c','d']
   plt.xticks(X,ticklabel,fontsize=15,rotation=-30) #'rotation'을 입력하면 그래프에 설정된 각 각의 이름이 입력한 숫자만큼 기울여서 출력된다.
   
   plt.show()
   ```

  ![m b7](https://user-images.githubusercontent.com/96108301/146661713-bc0d081c-b678-4022-982f-f7da00f65f0b.PNG)
   




