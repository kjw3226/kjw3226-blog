---
title: bar graph2(막대그래프)
tag: bar graph2(막대그래프)
date: 2021-11-12
categories:	Pandas

---

오늘은 'pandas'를 이용해서 '막대그래프'를 그려보았다.
```python
import pandas as pd    #DataFrame 객체의 plot()메서드를 사용해서 막대그래프를 출력했다.

data=[["Rudra",23,156,70],  #DataFrame 객체에 값을 넣어준다.
      ["Nayan",20,136,60],
      ["Alok",15,100,35],
      ["Prince",30,150,85]
     ]

df=pd.DataFrame(data,columns=["Name","Age","Height(cm)","Weight(kg)"])
print(df)
```
![pandas1](https://user-images.githubusercontent.com/96108301/146661780-01da5825-6924-4991-9ad6-f913888dbfa7.PNG)

```python
import pandas as pd          #DataFrame 객체의 plot()메서드를 사용해서 막대그래프를 출력했다.
import matplotlib.pyplot as plt 

data=[["Rudra",23,156,70],
      ["Nayan",20,136,60],
      ["Alok",15,100,35],
      ["Prince",30,150,85]
     ]

df=pd.DataFrame(data,columns=["Name","Age","Height(cm)","Weight(kg)"])
df.plot(x="Name", y=["Age", "Height(cm)", "Weight(kg)"], kind="bar",figsize=(9,8))
plt.show()
```
![pandas2](https://user-images.githubusercontent.com/96108301/146661786-4badc0b5-7662-4e63-a18c-c35fa8ac8b2d.PNG)
```python
import pandas as pd           #DataFrame 객체의 plot()메서드를 사용해서 막대그래프를 출력했다.
import matplotlib.pyplot as plt

employees=["Rudra","Alok","Prince","Nayan","Reman"]
earnings={
    "January":[10,20,15,18,14],
    "February":[20,13,10,18,15],
    "March":[20,20,10,15,18],
}

df=pd.DataFrame(earnings,index=employees)

df.plot(kind="bar",stacked=True,figsize=(10,8))
plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
plt.show()
```
![pandas3](https://user-images.githubusercontent.com/96108301/146661789-4ba43638-4d18-4c23-84a1-b578716bb239.PNG)
