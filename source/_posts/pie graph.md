---
title: Pie graph(원 그래프)
tag: Pie graph(원 그래프)
date: 2021-11-13
categories:	Matplotlib

---
오늘은 'Pie graph(원 그래프)'를 그려보았다.
```python
import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]  #'%'값을 설정 할 수 있다.
labels = ['Apple', 'Banana', 'Melon', 'Grapes'] #그래프 별 제목을 설정 할수 있다.

plt.pie(ratio, labels=labels, autopct='%.1f%%') #'pie'를 입력해줘야 원그래프를 그릴 수 있다. 
                                                #'autopct'함수는 '숫자형식'을 설정 할 때 사용된다.
plt.show()
```
![Pie1](https://user-images.githubusercontent.com/96108301/146661912-37f85de8-7e81-4f20-8172-729f4af52dcf.PNG)
```python
import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']

plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False)  
#'counterclock'함수를 'False'로 설정하면 시계 방향 순서대로 원그래프가 그려진다.
plt.show()
```
![Pie2](https://user-images.githubusercontent.com/96108301/146661913-9296915e-34af-45d4-a835-aabeaeb1c81f.PNG)
```python
import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']

plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=True) 
#'counterclock'함수를 'True'로 설정하면 시계 반대 방향 순서대로 원그래프가 그려진다.
plt.show()
```
![Pie3](https://user-images.githubusercontent.com/96108301/146661914-d0fd4c49-2c1a-424c-ab1f-34e52623244a.PNG)
```python
import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
explode = [0, 0.10, 0, 0.10]    #'explode' 함수는 그래프들을 '중심으로 부터 얼마나 떨어뜨릴것인가'를 설정할 수 있다.
                                #지금은‘Banana와‘Grapes’영역에 대해서 반지름의 10% 만큼 벗어나도록 설정했다.

plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode=explode) 
plt.show()
```
![Pie4](https://user-images.githubusercontent.com/96108301/146661916-3c1e60ca-2bbe-428a-bcba-7013c9242ba3.PNG)
```python
import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5} #'wedgeprops'는 원그래프를 '부채꼴'로 표현해 줄 때 사용된다.

plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, colors=colors, wedgeprops=wedgeprops)
#'wedgeprops'는 원그래프를 '부채꼴'로 표현해 줄 때 사용된다.
plt.show()
```
![Pie5](https://user-images.githubusercontent.com/96108301/146661917-9d77bf5f-7a79-4097-ba53-946608ee0a06.PNG)
```python
import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
explode = [0.05, 0.05, 0.05, 0.05]
colors = ['silver', 'gold', 'whitesmoke', 'lightgray']  #colors를 사용하면 각 영역의 색상을 자유롭게 지정할 수 있다.
plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode=explode, shadow=True, colors=colors)
#'shadow' 함수를 사용하면 '그림자'의 여부를 설정 가능하다.
plt.show()
```
![Pie6](https://user-images.githubusercontent.com/96108301/146661918-b53a5598-41f9-4449-b69e-3d7dc213d619.PNG)
```python
import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]                        
labels = ['Apple', 'Banana', 'Melon', 'Grapes'] 

plt.pie(ratio, labels=labels, autopct='%.1f%%',pctdistance=0.5) 
#'pctdistance'를 입력하면 '~~%'표시를 '중앙에서 부터 얼마나 떨어뜨려 표시할지 설정 할 수 있다. 
                                                
plt.show()
```
![Pie7](https://user-images.githubusercontent.com/96108301/146661919-ba3a86d9-2ec0-4b45-8385-9d51b6803681.PNG)
```python
textprops = dict(rotation=15,size=12, weight=3,color="red") 
plt.pie(incomes,explode=explodes,labels=labels,textprops=textprops) 
#'textprops' 함수를 입력하면 각 그래프의 이름이 기울어져서 출력된다.
plt.title("set textprops") 
plt.show()
```
![Pie8](https://user-images.githubusercontent.com/96108301/146661920-fc387f87-5c20-46cd-ae1b-f451eb179c99.PNG)

참고 : https://wikidocs.net/92114 
      https://mirandaherr.tistory.com/38