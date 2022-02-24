---
title: treemap graph(트리맵 그래프)
tag: treemap graph(트리맵 그래프)
date: 2021-11-19
categories:	Matplotlib

---
오늘은 트리맵을 만들어 보았다.

```python
import matplotlib.pyplot as plt #'matplotlib'의 'pyplot'모듈을 불러와서 사용.
import squarify #Squarify 패키지는 트리 맵 생성에 사용.
                #설치가 되있지 않으면 'pip install squarify'를 쳐서 설치.

plt.style.use('default')  
plt.rcParams['figure.figsize'] = (4, 4) #'rcParams'함수는 '그래프를 그리는 방식'을 설정해 줄수있다.
plt.rcParams['font.size'] = 12 

sizes = [40, 30, 5, 25]  #각 영역의 사이즈를 설정한다.
labels= ['A', 'B', 'C', 'D'] #각 영역에 '문자'를 출력해준다.

squarify.plot(sizes, 10, 10, label=labels)
#squarify.plot(sizes)와 같이 
#리스트의 형태로 값을 입력하면 값의 비율에 맞는 넓이를 갖는 사각형 영역으로 표시.
plt.show()
```

![treemap](https://user-images.githubusercontent.com/93234783/142580335-7506b307-964f-45e1-8342-596fd12395a9.PNG)

참고 : https://jrc-park.tistory.com/274
      https://data-newbie.tistory.com/731