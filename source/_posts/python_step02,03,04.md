---
title: python_step02,03,04
tag: python_step02,03,04
date: 2021-12-14
categories:	Python
---
파이썬에 있는 'inheritance' 대해 실습 해 보았다.

참고로 아래의 코드들 외의 실습한 자료는 맨 밑의 링크를
클릭하면 볼 수 있다.

```python
#/c/Program Files/anaconda3/envs/Python_f/python
# -*- conding: utf-8 -*-

class Employee:
    def __init__(self, name, tip):
        self.name = name
        self.tip = tip



if __name__=="__main__":
    emp1 = Employee("kim", 10000)
    emp2 = Employee("Lee", 10000)



# 100명을 고용
```
```python
#/c/Program Files/anaconda3/envs/Python_f/python
# -*- conding: utf-8 -*-
# Class Attribute


class Employee:

    #Class Attribute
    MAX_TIP = 10000
    DEFAULT_TIP = 20000

    def __init__(self, name, tip = 0):
        self.name = name
        if tip >= Employee.MAX_TIP:
            self.tip = Employee.MAX_TIP
        else:
            self.tip = Employee.DEFAULT_TIP



if __name__ == "__main__":
    emp1 = Employee("kim")
    print(emp1.tip)
    emp2 = Employee("Lee", 10000)
    print(emp2.tip)
```
<실행 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:c/Program Files/anaconda3/envs/Python_f/python/inheritance02.py"
20000
10000
```
```python
"C:\Program Files\anaconda3\python.exe" "C:c/Program Files/anaconda3/envs/Python_f/python/inheritance03.py"
name
kim
evan
A
B
C
D
F

Process finished with exit code 0
```
```python
#/c/Program Files/anaconda3/envs/Python_f/python
# -*- coding: utf-8 -*-

"""
- 클래스 메서드 사용
- 정적 메서드 사용
- 날짜 입력 예제
- "2021-12-13"
"""

from datetime import datetime

class BetterDate:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_str(cls, date_str):
        parts = date_str.split("-") # 2021-12-17
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        return cls(year, month, day)

    @staticmethod
    def from_str2(date_str):
        parts = date_str.split("-")  # 2021-12-17
        BetterDate.year, BetterDate.month, BetterDate.day = int(parts[0]), int(parts[1]), int(parts[2])
        return BetterDate.year, BetterDate.month, BetterDate.day

    @classmethod
    def from_datetime(cls, dateobj):
        year, month, day = dateobj.year, dateobj.month, dateobj.day
        return cls(year, month, day)

if __name__ == "__main__":

    bd_str = BetterDate.from_str("2021-12-13")
    print("---- Date String----")
    # print("연도는 {}")
    print(bd_str.year)
    print(bd_str.month)
    print(bd_str.day)

    bd_str2 = BetterDate.from_str2("2021-12-13")
    print("---- Date String----")
    # print("연도는 {}")
    print(bd_str2[0])
    print(bd_str2[1])
    print(bd_str2[2])

    today = datetime.today()
    print("Today", today)
    print("Type", type(today))
    bd_str3 = BetterDate.from_datetime(today)
    print("---- Date Datetime----")
    # print("연도는 {}")
    print(bd_str3.year)
    print(bd_str3.month)
    print(bd_str3.day)
```
<실행 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:c/Program Files/anaconda3/envs/Python_f/python/inheritance04.py"
name
kim
evan
A
B
C
D
F

Process finished with exit code 0
```
```python
#/c/Program Files/anaconda3/envs/Python_f/python
# -*- coding: utf-8 -*-

"""
모방 (부모 클래스를 모방)
모방 한 뒤, 자식이 창조
"""

import pandas as pd

class newDataFrame(pd.DataFrame):
    pass



if __name__=="__main__":
    temp_dict = {"A": [1, 2, 3], "B": [4, 5, 6]}
    temp = pd.DataFrame(temp_dict, columns=["B", "A"])
    #print(temp)
    print("---------")
    temp2 = newDataFrame(temp_dict, columns=["B", "A"])
    print(temp2)
```
<실행 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:c/Program Files/anaconda3/envs/Python_f/python/inheritance05.py"
---------
   B  A
0  4  1
1  5  2
2  6  3

Process finished with exit code 0
```

```python
#/c/Program Files/anaconda3/envs/Python_f/python
# -*- coding: utf-8 -*-

class Employee:
    MIN_TIP =3000

    def __init__(self, name, tip = MIN_TIP):
        self.name = name
        if tip >= Employee.MIN_TIP:
            self.tip = tip
        else:
            self.tip  =Employee.MIN_TIP

    def give_raise(self, amount):
        self.tip += amount

class Manager(Employee):
    pass


if __name__=="__main__":
    mng = Manager("Evan", 5000)
    print(mng.name)
    print(mng.tip)
```
<실행 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:c/Program Files/anaconda3/envs/Python_f/python/inheritance06.py"
Kim
5000

Process finished with exit code 0
```

```python
#/c/Program Files/anaconda3/envs/Python_f/python
# -*- coding: utf-8 -*-

class Employee:

    def __init__(self, name, tip = 30000):
        self.name = name
        self.tip = tip

    def give_raise(self, amount):
        self.tip += amount
        return self.tip

class Manager(Employee):
    def disaply(self):
        print("Manager: ", self.name)

    def __init__(self, name, tip = 50000, project=None):
        Employee.__init__(self, name, tip)
        self.project = project


    # give_raise
    def give_raise(self, amount = 0, bouns = 2):
        if amount > 0:
           Employee.give_raise(self, amount * bouns)
        else:
            Employee.give_raise(self, amount)

if __name__=="__main__":
    mng = Manager("Kim")
    print(mng.name)
    print(mng.tip)
    mng.give_raise(2000, bouns=3)
    print(mng.tip)
```
<실행 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:c/Program Files/anaconda3/envs/Python_f/python/inheritance07.py"
Kim
50000
56000

Process finished with exit code 0
```

여기 들어가면 더 많은 실습 자료를 볼수 있다.
[URL][source/python 12.14]