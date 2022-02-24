---
title: python def, decorator
tag: python def, decorator
date: 2021-12-07
categories:	Python
---
오늘은 파이썬의 함수를 만들어서 사용하는 법(def), 자료형의 종류 등  그리고 

'docstring'의 사용법과 'Decorator'에 대해 알아보았다.

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 함수를 객체로 사용하는 방식

# function as variable
def my_fun():
    print("안녕")

if __name__ == "__main__":
    x = my_fun
    print(type(x))
    print(x())

    print_function = print
    print(print_function("파이썬 좋음"))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step06_1_basic.py"
<class 'function'>
안녕
None
파이썬 좋음
None

Process finished with exit code 0
```
```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 다양한 함수를 리스트 안에 넣기
# 딕셔너리에 추가하기

def my_fun():
    print("안녕")

if __name__ == "__main__":
    list_functions = [my_fun, open, print]
    list_functions[2]("전 리스트에 있습니다.")

    dict_functions = {
        "fun_1" : my_fun(),
        "fun_2" : open,
        "fun_3": print,
    }

    print(dict_functions["fun_3"]("전 딕셔너리에 있습니다."))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step06_2_basic.py"
전 리스트에 있습니다.
안녕
전 딕셔너리에 있습니다.
None

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

def my_fun():
    return 42

# 함수를 arguments로 사용하기도 함
def docstring_exist(func):
    """입력된 함수 내 docstring이 있는지 확인하는 함수

    Args:
        func (callable): A function

    Returns:
        bool
    """

    return func.__doc__ is not None # True or False 값 반환

def no_docstring():
    return 10

def yes_docstring():
    """value 값을 반환합니다.
    """
    return 10

if __name__ == "__main__":
    x = my_fun
    print(my_fun())
    print("-----")
    print(docstring_exist(no_docstring))
    print(docstring_exist(yes_docstring))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step06_3_basic.py"
42
-----
False
True

Process finished with exit code 0
```
```python
# Defining a function inside another function
def a():
    x = [3, 6, 9]

    def b(y):
        print(y)

    for value in x:
        b(x)

if __name__ == "__main__":
    print(a())
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step06_4_basic.py"
[3, 6, 9]
[3, 6, 9]
[3, 6, 9]
None

Process finished with exit code 0
```
```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Defining a function inside another function
def a(x, y):
    if x > 5 and x < 8 and y > 5 and y < 8:
        print(x * y)
    else:
        print("다른 값을 입력하세요!")
        # raise ValueError("X is {}, Y is {}".format(x, y))

if __name__ == "__main__":
    print(a(5, 4))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step06_5_basic.py"
다른 값을 입력하세요!
None

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

def whatsInside():
    def please_print_me(s):
        print(s)
        # return 1
    return please_print_me

if __name__ == "__main__":
    new_func = whatsInside()
    print(new_func("Hope this prints print()"))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step06_7_basic.py"
Hope this prints print()
None

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# func 이름이 들어간 덧셈 뺄셈믈 추가해본다.
# func 안에 func을 추가한다.
def math_functions(func_name):
    if func_name == "add":
        def add(a, b):
            return a + b
        return add
    elif func_name == "subtract":
        def subtract(a, b):
            return a - b
        return subtract
    elif func_name == "multiple":
        def multiple(a, b):
            return a * b
        return multiple
    elif func_name == "divide":
        def divide(a, b):
            return a // b
        return divide
    else:
        print("그 외에는 잘 모르겠습니다.")

if __name__ == "__main__":
    x = 100
    y = 2

    add = math_functions("add")
    print("100 + 2 = {}".format(add(x, y)))

    subtract = math_functions("subtract")
    print("100 - 2 = {}".format(subtract(x, y)))

    subtract = math_functions("multiple")
    print("100 * 2 = {}".format(subtract(x, y)))

    divide = math_functions("divide")
    print("100 / 2 = {}".format(divide(x, y))) # 정수 출력
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step06_8_basic.py"
100 + 2 = 102
100 - 2 = 98
100 * 2 = 200
100 / 2 = 50

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Builtin > Global > NonLocal > Local

x = 100

def a():
    x = 42
    print(x)

if __name__ == "__main__":
    print(a()) # 차이점 확인
    print(x) # 차이점 확인
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step07_1_basic.py"
42
None
100

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Builtin > Global > NonLocal > Local
# global 키워드에 배웁니다.
x = 100
def a():
    global x
    x = 10
    print(x)

if __name__ == "__main__":
    print(a())
    print(x)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step07_2_basic.py"
10
None
10

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# NonLocal Keyword
x = 1000
def a():
    x = 10

    def b():
        nonlocal x # 주석처리 할 것
        x = 100
        print(x)

    b()
    print(x)

if __name__ == "__main__":
    print(a())
    print(x)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step07_3_basic.py"
100
100
None
1000

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# global x, nonlocal x, x등 자유롭게 활용하여 다음과 같이 출력하세요.
# 단 반드시, global x 또는 nonlocal x 등은 입력되어야 함
# 변수는 x만 사용합니다.
# 100, 70, 30, 70 순서대로 출력 됨

x = 100

# 문제 낼 것

def a():
    x = 70

def b():
    global x
    x = 70

def c():
    x = 30
    print(x)

if __name__ == "__main__":
    # result = []
    for function in [a, b, c]:
        function()
        print(x)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step07_4_basic.py"
100
70
30
70

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-
# Closures

def a():
    a = 5
    def b():
        print(a)
    return b

if __name__ == "__main__":
    func = a()
    func()
    print(type(func.__closure__))
    print(len(func.__closure__))
    print(func.__closure__[0].cell_contents)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step08_1_basic.py"
5
<class 'tuple'>
1
5

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

x = 100
def a(value):
    def b():
        print(value)
    return b

if __name__ == "__main__":
    my_func = a(x)
    print(my_func())

    del(x) # x = 100을 삭제한 것
    print(my_func())

    print(len(my_func.__closure__))
    print(my_func.__closure__[0].cell_contents)


"""
개념정리: Nested Functions
- 하나의 function 안에 또다른 function이 있는 것. 

# outer function
def parent():
    # nested function
    def child():
        pass 
    return child
    
개념정리: Definitions - Nonlocal Variables
- Nonlocal Variables: Variables defined in the parent function that are used by the child function

def parent(arg_1, arg_2)
    # child() 함수 관점에서는 value & my_dict은 nonlocal variables
    value = 22
    my_dict = {"A": 100}
    
    def child()
        print(2 * value)
        print(my_dict["A"])
        print(arg_1 + arg_2)
    return child
"""
```

<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step08_2_basic.py"
100
None
100
None
1
100

Process finished with exit code 0
```
```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Closure: Nonlocal Variables은 반환되는 함수에 붙여서 나오게 됨
def parent(arg_1, arg_2):
    nonlocal_value = 100
    nonlocal_my_dict = {"A": 0}

    def child():
        print(2 * nonlocal_value)
        print(nonlocal_my_dict["A"])
        print(arg_1 + arg_2)

    return child

if __name__ == "__main__":
    new_function = parent(100, 200)
    print([cell.cell_contents for cell in new_function.__closure__]) # 리스트로 반환
    for cell in new_function.__closure__:                            # 단일 객체로 반환
        print(cell.cell_contents)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step08_3_basic.py"
[100, 200, {'A': 0}, 100]
100
200
{'A': 0}
100

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

def check_closure(arg1, arg2):
    def inside_func():
        print("arg1 was {}".format(arg1))
        print("arg1 was {}".format(arg2))
    return inside_func

if __name__ == "__main__":
    my_func = check_closure(10, 100)

    # Closure 에 결측치 있는지 확인
    print(my_func.__closure__ is not None)

    # 2개의 변수가 존재하는지 확인
    print(len(my_func.__closure__) == 2)

    # closure value 확인
    closure_values = [
        my_func.__closure__[i].cell_contents for i in range(2)
    ]

    print(closure_values == [2, 10])
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step08_4_basic.py"
True
True
False

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

def print_msg():
    print('print_msg 함수입니다. ')

def new_func(func):
    def call_func():
        func()
    return call_func


new_func = new_func(print_msg)

# 삭제
del(print_msg)

if __name__ == "__main__":
    print(new_func())
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step08_5_basic.py"
print_msg 함수입니다. 
None

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 과제, 함수를 활용하여 제곱 곱셈 함수 만들기
def multiple_a(a):
    def multiple_b(b):
        return a * b
    return multiple_b

if __name__ == "__main__":
    m1 = multiple_a(1)
    m2 = multiple_a(2)
    m3 = multiple_a(3)

    print(m1(3))
    print(m1(5))
    print(m1(7))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step08_6_basic.py"
3
5
7

Process finished with exit code 0
```
```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Decorator를 이해하기 위해서는 앞에서 계속 설명해왔던 4가지 개념을 이해해야 함
"""
1. 객체로서의 함수
2. Nested 함수
3. Nonlocal Variable
4. Closures
"""

"""
@two_args
def add(a, b):
    return a + b

if __name__ == "__main__":
    multiply(1, 5)
"""

def add(a, b):
    return a + b

"""
def two_args(func): # 그저 함수
    return func
"""

"""
def two_args(func):
    # 새로운 함수
    def wrapper(a, b):

        # 수정전의 함수 반환
        return func(a, b)

    # 새로운 함수 반환
    return wrapper
"""

def two_args(func):
    # 새로운 함수
    def wrapper(a, b):

        # 수정전의 함수 반환
        return func(a * 2, b * 2)

    # 새로운 함수 반환
    return wrapper

if __name__ == "__main__":
    new_add = two_args(add)
    print(new_add(1, 2))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step09_1_basic.py"
6

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 기존 문법
def two_args(func):
    def wrapper(a, b):
        return func(a * 3, b * 3)

    return wrapper

def multiple(a, b):
    return a * b

if __name__ == "__main__":
    new_multiple = two_args(multiple)
    print(new_multiple(2, 3))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step09_2_basic.py"
54

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Decorator 문법
def two_args(func):
    def wrapper(a, b):
        return func(a * 3, b * 3)

    return wrapper

@two_args
def multiple(a, b):
    return a * b

if __name__ == "__main__":
    print(multiple(2, 3))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step09_3_basic.py"
54

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

import inspect

def print_args(func):
    sig = inspect.signature(func) # 객체는 콜러블 객체의 호출 서명과 반환 값 어노테이션을 나타냅니다.
    print(sig)

    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs).arguments # 반복문 돌리기 위해 딕셔너리 형태로 묶어줌
        str_args = ', '.join(['{}={}'.format(k, v) for k, v in bound.items()])
        print('{} was called with {}'.format(func.__name__, str_args))
        return func(*args, **kwargs)
    return wrapper

@print_args
def my_function(a, b, c):
  print(a + b + c)


if __name__ == "__main__":
    # my_function = print_args(my_function) # 데코레이터 안할 시
    print(my_function(1, 2, 3))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step09_4_basic.py"
(a, b, c)
my_function was called with a=1, b=2, c=3
6
None

Process finished with exit code 0
```
아래의 코드는 시간이 얼마나 걸리는지 체크해 주는 함수를 직접 만든 것이다.
```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 시간 측정 함수 만들기
# time Decorator 만들기

import time

def timer(func):
    """함수 실행 시 얼마나 오래 걸리는지 확인"""

    def wrapper(*args, **kwargs):
        # 현재시간
        time_start = time.time()
        # decorated 함수 불러오기
        result = func(*args, **kwargs)
        time_total = time.time() - time_start
        print("{} took {}s".format(func.__name__, time_total))
        return result
    return wrapper

@timer
def check_time(num):
    time.sleep(num)

if __name__ == "__main__":
    check_time(3)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step09_5_basic.py"
check_time took 3.0077176094055176s

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# 데코레이터 함수 만들기
def return_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(func.__name__, type(result)))

        return result

    return wrapper

@return_type
def a(value):
    return value

if __name__ == "__main__":
    print(a(123))
    print(a([1, 2, 3]))
    print(a({"a": 42}))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/python_f/step09_6_basic.py"
a() returned type <class 'int'>
123
a() returned type <class 'list'>
[1, 2, 3]
a() returned type <class 'dict'>
{'a': 42}

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Counter
# 특정 함수가 몇번 불러왔는지 확인하는 함수
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1

        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper

@counter
def a():
    print("임의의 함수 호출")

if __name__ == "__main__":

    a()
    a()
    a()
    print("a() 함수는 현재 {} 번 호출됨".format(a.count))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/python_f/step09_7_basic.py"
임의의 함수 호출
임의의 함수 호출
임의의 함수 호출
a() 함수는 현재 3 번 호출됨

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# (2) 추가
from functools import wraps

# 메타데이터
def print_hello(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        """안녕을 출력하는 데커레이션 함수입니다.""" # (1) 추가
        print('안녕')
        return func(*args, **kwargs)
    return wrapper


# Decorate print_sum() with the add_hello() decorator
@print_hello
def print_add(a, b):
    """덧셈을 출력하는 함수입니다. """
    print(a + b)

if __name__ == "__main__":
    print_add(10, 20)
    print_sum_docstring = print_add.__doc__
    print(print_sum_docstring)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/[파이썬활용]빅데이터 전문 인재양성 과정A/빅데이터(정지훈 쌤) 비대면 수업자료/211207/step09_8_basic.py"
안녕
30
덧셈을 출력하는 함수입니다. 

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

import inspect
import step01_3_basic

def check_tooltip(funct):
    """기본함수의 문서를 보여주는 함수를 만든다.

    Args:
        function (callable): 문서를 보여주고자 하는 임의의 함수

    Returns:
        str
    """
    docstring = inspect.getdoc(funct)
    borderline = '#' * 10
    return '{}\n{}\n{}'.format(borderline, docstring, borderline)

if __name__ == "__main__":
    print(check_tooltip(step01_3_basic.cnt_letter))
    print(check_tooltip(list))
    print(check_tooltip(range))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/[파이썬활용]빅데이터 전문 인재양성 과정A/빅데이터(정지훈 쌤) 비대면 수업자료/211207/check_tooltip.py"
##########
content 안에 있는 문자를 세는 함수입니다.
# Google Style
Args:
    content(str): 탐색 문자열
    letter(str): 찾을 문자열

Returns:
    int

Raises:
    ValueError: 만약 Return 값이 문자가 아니라면 에러를 발생시킨다.
##########
##########
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
##########
##########
range(stop) -> range object
range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
##########

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-
# https://www.programiz.com/python-programming/list-comprehension

def lc_main():
    my_list = [[10], [20, 30]]
    flattend_list = [value for value_list in my_list for value in value_list]
    print(flattend_list)

def for_main():
    my_list = [[10], [20, 30]]
    flattend_list = []
    for value_list in my_list:
        for value in value_list:
            flattend_list.append(value)
    print(flattend_list)

if __name__ == "__main__":
    lc_main()
    for_main()
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/[파이썬활용]빅데이터 전문 인재양성 과정A/빅데이터(정지훈 쌤) 비대면 수업자료/211207/list_comprehension.py"
[10, 20, 30]
[10, 20, 30]

Process finished with exit code 0
```

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

import step01_3_basic
import inspect

docstring = inspect.getdoc(step01_3_basic.cnt_letter)

if __name__ == "__main__":
    border = '#' * 28
    print('{}\n{}\n{}'.format(border, docstring, border))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/[파이썬활용]빅데이터 전문 인재양성 과정A/빅데이터(정지훈 쌤) 비대면 수업자료/211207/retrive.py"
############################
content 안에 있는 문자를 세는 함수입니다.
# Google Style
Args:
    content(str): 탐색 문자열
    letter(str): 찾을 문자열

Returns:
    int

Raises:
    ValueError: 만약 Return 값이 문자가 아니라면 에러를 발생시킨다.
############################

Process finished with exit code 0
```