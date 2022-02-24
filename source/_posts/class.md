---
title: class2
tag: class2
date: 2021-12-14
categories:	Python
---
 오늘은 직접 클래스와 함수를 하나 하나 만들어보고 
 연결해서 다양한 기초문법을 실습을 통해 알아보았다.

 아래의 코드는 직접 실습한 코드들이다.

```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step03
# -*- coding: utf-8 -*-

class Human:

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    human01 = Human(name="A")
    human02 = Human(name="A")

    print(human01 == human02)
    print("human01: ", human01)
    print("human02: ", human02)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Program Files/anaconda3/envs/step03_04(12.14)/step03/bank00.py"
Setter method is called
3000
Setter method is called
1000

Process finished with exit code 0
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step03
# -*- coding: utf-8 -*-
# != __ne__()
# >= __ge__()
# <= __le__()
# > __gt__()
# < __lt__()

class Bank:

    # instance attribute
    def __init__(self, cust_id, balance=0):
        self.balance = balance
        self.cust_id = cust_id

    # instance method
    def withdraw(self, amount):
        self.balance -= amount

    def __eq__(self, other):
        print("__eq()__ is called")
        return self.cust_id == other.cust_id

    def __ne__(self, other):
        print("__eq()__ is called")
        return self.cust_id != other.cust_id
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step03
# -*- coding: utf-8 -*-

class Bank:

    # cust_id, balance = 0
    def __init__(self, cust_id, balance = 0):
        self.cust_id, self.balance = cust_id, balance


    # withdraw method
    def withdraw(self, amount):
        self.balance -= amount

    # eq
    def __eq__(self, other):
        print("__eq()__ is called")
        return (self.cust_id == other.cust_id) and (type(self) == type(other))

class Phone:

    def __init__(self, cust_id):
        self.cust_id = cust_id

    def __eq__(self, other):
        return self.cust_id == other.cust_id

if __name__ == "__main__":
    account01 = Bank(1234)
    phone01 = Phone(1234)

    print(account01 == phone01)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Program Files/anaconda3/envs/step03_04(12.14)/step03/bank02.py"
__eq()__ is called
False

Process finished with exit code 0
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step03
# -*- coding: utf-8 -*-

# 프로젝트 4개월
# 1개월 환경세팅, 미팅, 요구 사항 미팅
# 2개월 날코딩 (프레임워크 위주로 코드 짬) / 자동화 (x)
# 1개월 문서 작업, 코드 리팩토링 (기초문법*****)

class Bank:

    def __init__(self, cust_id, name, balance = 0):
        self.cust_id, self.name, self.balance = cust_id, name, balance

    def __str__(self):
        cust_str = """
        Customer:
            cust_id : {cust_id}
            name : {name}
            balance : {balance}
        """.format(cust_id = self.cust_id, name = self.name, balance = self.balance)

        return cust_str

if __name__ == "__main__":
    bank_cust = Bank(123, "Kim")
    print(bank_cust)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Program Files/anaconda3/envs/step03_04(12.14)/step03/bank03.py"

        Customer:
            cust_id : 123
            name : Kim
            balance : 0
        

Process finished with exit code 0
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step03
# -*- coding: utf-8 -*-
# 프로젝트 4개월
# 1개월 환경세팅, 미팅, 요구 사항 미팅
# 2개월 날코딩 (프레임워크 위주로 코드 짬) / 자동화 (x)
# 1개월 문서 작업, 코드 리팩토링 (기초문법*****)

class Bank:

    def __init__(self, cust_id, name, balance = 0):
        self.cust_id, self.name, self.balance = cust_id, name, balance

    def __str__(self):
        cust_str = """
        Customer:
            cust_id : {cust_id}
            name : {name}
            balance : {balance}
        """.format(cust_id = self.cust_id, name = self.name, balance = self.balance)

        return cust_str

    def __repr__(self):
        cust_str = "Bank({cust_id}, '{name}', {balance})".format(cust_id = self.cust_id, name = self.name, balance = self.balance)
        return cust_str

if __name__ == "__main__":
    bank_cust = Bank(123, "Kim")
    print(str(bank_cust))
    print(repr(bank_cust))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step03/bank04.py"

        Customer:
            cust_id : 123
            name : Kim
            balance : 0
        
Bank(123, 'Kim', 0)

Process finished with exit code 0
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step03
# -*- coding: utf-8 -*-
def error01():
    a = 10
    a / 0
    # ZeroDivisionError: division by zero

def error02():
    a = [1, 2, 3, 4, 5]
    a[10]
    # IndexError: list index out of range

def error03():
    a = 1000
    a + "안녕"
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'

def error04():
    a = 1000
    a + b
    # NameError: name 'b' is not defined

if __name__ == "__main__":
    error01()
    error02()
    error03()
    error04()

    print("Program is done")

# 크롤링 코드 작성
# "https://sports.news.naver.com/news?oid=109&aid=00045260" + "83" # 페이지 없음

# 크롤링 코드 멈춤

# URL: https://sports.news.naver.com/news?oid=109&aid=0004526080
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step03
# -*- coding: utf-8 -*-

def try_func(x, idx):
    try:
        return 100/x[idx]
    except ZeroDivisionError:
        print("Zero로 나눌 수 없음")
    except IndexError:
        print("Index 범위 밖에 있음")
    except TypeError:
        print("Type Error가 존재")
    except NameError:
        print("변수 정의 안한 것이 있음")
    finally:
        print("무조건 실행됨")

def main():
    a = [50, 60, 0, 70]
    print(try_func(a, 1))

    # zero Division Error
    print(try_func(a, 0))

    # Index Error
    print(try_func(a, 5))

    # type Error
    print(try_func(a, "안녕"))

if __name__ == "__main__":
    main()
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step03/exceptions02.py"
무조건 실행됨
1.6666666666666667
무조건 실행됨
2.0
Index 범위 밖에 있음
무조건 실행됨
None
Type Error가 존재
무조건 실행됨
None

Process finished with exit code 0
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step03
# -*- coding: utf-8 -*-
# 클래스
# __init__ <--- set_name, set_balanace
# __eq__, __ne__, etc
# 상속, 다형성


class SalaryExcept(ValueError): pass # 상속
class TipExcept(SalaryExcept): pass # 상속

class Employee:

    # class attribute
    MIN_SALARY = 20000
    MAX_BONUS = 10000

    # instance attribute
    def __init__(self, name, salary = 30000):
        self.name = name
        if salary < Employee.MIN_SALARY:
            raise SalaryExcept("급여가 너무 낮아요!")
        self.salary = salary

    # instance method
    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            print("보너스가 너무 많습니다!")
        elif self.salary + amount < Employee.MIN_SALARY:
            print("보너스 지급 후의 급여도 매우 낮아요!")
        else:
            self.salary += amount

if __name__ == "__main__":
    emp = Employee("Evan", salary=20000)
    try:
        emp.give_bonus(70000)
    except SalaryExcept:
        print("Salary 오류가 감지됨")
    try:
        emp.give_bonus(-100000)
    except TipExcept:
        print("Tip 오류 감지됨")
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step03/exceptions03.py"
보너스가 너무 많습니다!
보너스 지급 후의 급여도 매우 낮아요!

Process finished with exit code 0
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step04
# -*- coding: utf-8 -*-
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError("Invalid Balance")
        self._balance = new_bal

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_bal):
        if new_bal < 0:
            raise ValueError("Invalid balance!")
        self._balance = new_bal
        print("Setter method is called")
```
```python
from customer05 import Customer

if __name__ == "__main__":
    cust = Customer("Belinda Lutz", 2000)
    cust.balance = 3000
    print(cust.balance)
    cust.balance = -1000
    print(cust.balance)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step04/customer_test.py"
Traceback (most recent call last):
  File "C:\Users\rudal\Desktop\[파이썬활용]빅데이터 전문 인재양성 과정A\빅데이터(정지훈 쌤) 비대면 수업자료\step03_04(12.14)\step04\customer_test.py", line 10, in <module>
    cust.balance = -1000
  File "C:\Users\rudal\Desktop\[파이썬활용]빅데이터 전문 인재양성 과정A\빅데이터(정지훈 쌤) 비대면 수업자료\step03_04(12.14)\step04\customer05.py", line 18, in balance
    raise ValueError("Invalid balance!")
ValueError: Invalid balance!
Setter method is called
3000

Process finished with exit code 1
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step04
# -*- coding: utf-8 -*-

class BetterDate:
    _MAX_DAYS = 30
    _MAX_MONTHS = 12

    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day


    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    def _is_valid(self):
        return (self.day <= BetterDate._MAX_DAYS) and \
               (self.month <= BetterDate._MAX_MONTHS)
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step04
# -*- coding: utf-8 -*-

from internal_attributes03 import BetterDate

if __name__ == "__main__":
    bd1 = BetterDate(2021, 4, 30)
    print(bd1._is_valid())
    bd2 = BetterDate(2021, 6, 45)
    print(bd2._is_valid())
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step04/internal_attributes_test.py"
True
False

Process finished with exit code 0
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step04
# -*- coding: utf-8 -*-
class Parent:
    def talk(self):
        print("Parent talking!")

class Son(Parent):
    def talk(self):
        print("Son talking!")

class Daughter(Parent):
    def talk(self):
        print("Daughter talking!")
        Parent.talk(self)

if __name__ == "__main__":
    pat, son, daughter = Parent(), Son(), Daughter()
    for obj in (pat, son, daughter):
        obj.talk()
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step04/parent01.py"
Parent talking!
Son talking!
Daughter talking!
Parent talking!

Process finished with exit code 0
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step04
# -*- coding: utf-8 -*-

class Employee:
    def __init__(self, name, new_salary):
        self._salary = new_salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Invalid salary")
        self._salary = new_salary
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step04
# -*- coding: utf-8 -*-

from properties04 import Employee

if __name__ == "__main__":

    emp = Employee("Miriam Azari", 3000)
    print(emp.salary)

    emp.salary = 6000 # <= @salary.setter
    print(emp.salary)
    emp.salary = -1000
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step04/properties_test.py"
3000
6000

Process finished with exit code 0
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step04
# -*- coding: utf-8 -*-

class Rectangle:
    def __init__(self, h, w):
        self.h, self.w = h, w

# Define a Square class
class Square(Rectangle):
    def __init__(self, w):
        self.h, self.w = w, w
```
```python
lass Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h

    # Define set_h to set h
    def set_h(self, h):
        self.h = h

    # Define set_w to set w
    def set_w(self, w):
        self.w = w

class Square(Rectangle):
    def __init__(self, w):
        self.w, self.h = w, w

    # Define set_h to set w and h
    def set_h(self, h):
        self.h = h
        self.w = h

    # Define set_w to set w and h
    def set_w(self, w):
        self.w = w
        self.h = w
```
```python
# /c/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step04
# -*- coding: utf-8 -*-

from rectangle01 import Rectangle, Square

if __name__ == "__main__":
    rec = Rectangle(4, 7)
    sq = Square(4)
    print(rec.h)
    print(rec.w)
    print(sq.h)
    print(sq.w)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Program Files/anaconda3/envs/python-P/step03_04(12.14)/step04/rectangle_test.py"
4
7
4
4

Process finished with exit code 0
```