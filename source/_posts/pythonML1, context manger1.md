---
title: pythonML1, context manger1
tag: pythonML1, context manger1
date: 2021-12-06
categories:	Python Machine Learning

---
 파이썬 머신러닝에서는 함수를 거의 자신이 만들어 사용하고
 
 정규화 작업 등도 진행한다. 
  
 여기에 대해 알아보았다.
 
```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

def cnt_letter():
    """안에 있는 문자를 세는 함수입니다.""" # 함수를 설명하는 문구
    print("Hi")
    return None

if __name__ == "__main__":
    print(cnt_letter())
    print(help(cnt_letter))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\envs\Python_f\python.exe" "C:/Program Files/anaconda3/envs/Python_f/211206/step_01_1_basic.py"
Hi
None
Help on function cnt_letter in module __main__:

cnt_letter()
    안에 있는 문자를 세는 함수입니다.

None

Process finished with exit code 0
```
```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-


def cnt_letter(content, letter):
    """content 안에 있는 문자를 세는 함수입니다.
    # Google Style
    Args:
        content(str): 탐색 문자열
        letter(str): 찾을 문자열

    Returns:
        int
    """
    # code 작업
    print("함수 테스트")
    return (len([char for char in content if char == letter])) # 리스트 컴프리헨션

if __name__ == "__main__":

    docstring = cnt_letter.__doc__
    border = "*" * 20
    print('{}\n{}\n{}'.format(border, docstring, border))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\envs\Python_f\python.exe" 
"C:/Program Files/anaconda3/envs/Python_f/211206/step_01_2_basic.py"
********************
content 안에 있는 문자를 세는 함수입니다.
    # Google Style
    Args:
        content(str): 탐색 문자열
        letter(str): 찾을 문자열

    Returns:
        int
    
********************

Process finished with exit code 0
```

```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# 정규화
# Normalization (빅데이터 분석 기사, 단골!!) ~ Standardization (표준화) = Z-Score
# 데이터의 범위를 0과 1로 변환해서 데이터의 분포를 조정하는 방법
# Min_Max Normalization
#
# Y = (개별 값 - 최소값) / (최대값 - 최소값)
# pandas 데이터 프레임

import seaborn as sns

def min_max_normalize(column):
   """데이터를 정규화를 만드는 과정이다.
    Args:
        column (pandas Series): 정규화를 하기 위한 것

    Return: Series
        pandas series: min_max 정규화 공식의 답을 가져온다.
   """

   min_max_score = (column - column.min()) / (column.max() - column.min())
   return min_max_score

if __name__ == "__main__":
    iris = sns.load_dataset("iris")
    print(iris.head())

    iris['sepal_length'] = min_max_normalize(iris['sepal_length'])
    iris['sepal_width'] = min_max_normalize(iris['sepal_width'])
    iris['petal_length'] = min_max_normalize(iris['petal_length'])
    iris['petal_width'] = min_max_normalize(iris['petal_width'])

    print(iris.head())
```
<결과 화면>
```python
"C:\Program Files\anaconda3\envs\Python_f\python.exe" "C:/Program Files/anaconda3/envs/Python_f/211206/step_02_1_basic.py"
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
   sepal_length  sepal_width  petal_length  petal_width species
0      0.222222     0.625000      0.067797     0.041667  setosa
1      0.166667     0.416667      0.067797     0.041667  setosa
2      0.111111     0.500000      0.050847     0.041667  setosa
3      0.083333     0.458333      0.084746     0.041667  setosa
4      0.194444     0.666667      0.067797     0.041667  setosa

Process finished with exit code 0
```

```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# 수치형 데이터 활용해서, 정규화
# 표준화 (공식) z-score
# 공식 찾으시고, 함수 작성 하시고,
# iris 데이터에서 적용
import seaborn as sns

def standardize(column):
    """데이터의 정규화를 만드는 과정이다.
    Args:
        column (pandas Series): 정규화를 하기 위한 것

    Returns: series
        pandas series: 표준화 공식을 적용한다.
    """

    # z-score 반환함
    z_score = (column - column.mean()) / column.std()
    return z_score


if __name__ == "__main__":
    iris = sns.load_dataset("iris")
    print(iris.head())

    iris['sepal_length'] = standardize(iris['sepal_length'])
    iris['sepal_width'] = standardize(iris['sepal_width'])
    iris['petal_length'] = standardize(iris['petal_length'])
    iris['petal_width'] = standardize(iris['petal_width'])

    print(iris.head())
```
<결과 화면>
```python
"C:\Program Files\anaconda3\envs\Python_f\python.exe" "C:/Program Files/anaconda3/envs/Python_f/211206/step_02_2_basic.py"
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
   sepal_length  sepal_width  petal_length  petal_width species
0     -0.897674     1.015602     -1.335752    -1.311052  setosa
1     -1.139200    -0.131539     -1.335752    -1.311052  setosa
2     -1.380727     0.327318     -1.392399    -1.311052  setosa
3     -1.501490     0.097889     -1.279104    -1.311052  setosa
4     -1.018437     1.245030     -1.335752    -1.311052  setosa

Process finished with exit code 0
```
```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-
# 함수의 규칙(Rule)

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 1. 가독성이 안 좋음
# 2. 확장성이 안 좋음
# 3. 한 함수는 무조건 하나의 기능만 하게끔 설계.

def load_and_plot(datasetname):
    """데이터를 불러오고 그래프를 작성한다.

    :param datasetname:
    :return:
    """
    # 데이터를 불러오는 코드를 작성함.
    # 작업 1. DB 연결 하는 코드 작성
    data = sns.load_dataset(datasetname)

    # 데이터 전처리 하는 코드 등등
    y = data.iloc[:, 1].values
    X = data.columns
    num_list = data.select_dtypes(include=[np.number]).columns
    print("컬럼명: ", num_list)

    # 작업 2. 시각화 코드 작성
    sns.scatterplot(x = num_list[0], y = num_list[1], data = data)
    plt.show()

    # 작업 3.
    # X, y 값 반환하기
    return X, y

if __name__ == "__main__":
    X, y = load_and_plot("tips")
    print("X is:", X)
    print("y is:", y)
```
<결과 화면>
![](../../../Figure_1.png)
```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# mutable (변경이 가능한): list, dict, set, bytearray, objects, functions
# immutable (변경이 어려운): tuple, int, float, bool, string, bytes

def list_a(var=[]): # Mutable
    var.append(1)
    return var

def list_b(var=None):
    if var is None:
        var = []
    var.append(1)
    return var

if __name__ == "__main__":
    print(list_a())
    print(list_a())
    print(list_a())
    print("------")
    print(list_b())
    print(list_b())
    print(list_b())
```
<결과 화면>
```python
"C:\Program Files\anaconda3\envs\Python_f\python.exe" "C:/Program Files/anaconda3/envs/Python_f/211206/step_04_1_basic.py"
[1]
[1, 1]
[1, 1, 1]
------
[1]
[1]
[1]

Process finished with exit code 0
```
```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# mutable (변경이 가능한): list, dict, set, bytearray, objects, functions
# immutable (변경이 어려운): tuple, int, float, bool, string, bytes

import pandas
import pandas as pd

def add_new_column(new_vals, data = pd.DataFrame()):
    """새로운 컬럼을 data에 추가. 컬럼명은 columns_<n> 형태로 저장. 이 때, 모두 numeric로 저장

    Args:
        new_vals (iterable): 함수 실행 시마다, 새로운 컬럼의 값 의미
        data (Dataframe, optional): 함수가 실행시 업데이트.
             만약에 데이터프레임으로 입력받지 못하면, 임의의 데이터프레임이 디폴트로 생성
    Returns:
        DataFrame
    """
    data['col_{}'.format(len(data.columns))] = new_vals
    return data

if __name__ == "__main__":
    print(add_new_column(new_vals=range(10)))
    print(add_new_column(new_vals=None))
    print(add_new_column(new_vals=range(10)))
    print(add_new_column(new_vals=None))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\envs\Python_f\python.exe" "C:/Program Files/anaconda3/envs/Python_f/211206/step_04_2_basic.py"
   col_0
0      0
1      1
2      2
3      3
4      4
5      5
6      6
7      7
8      8
9      9
   col_0 col_1
0      0  None
1      1  None
2      2  None
3      3  None
4      4  None
5      5  None
6      6  None
7      7  None
8      8  None
9      9  None
   col_0 col_1  col_2
0      0  None      0
1      1  None      1
2      2  None      2
3      3  None      3
4      4  None      4
5      5  None      5
6      6  None      6
7      7  None      7
8      8  None      8
9      9  None      9
   col_0 col_1  col_2 col_3
0      0  None      0  None
1      1  None      1  None
2      2  None      2  None
3      3  None      3  None
4      4  None      4  None
5      5  None      5  None
6      6  None      6  None
7      7  None      7  None
8      8  None      8  None
9      9  None      9  None

Process finished with exit code 0
```
```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# mutable (변경이 가능한): list, dict, set, bytearray, objects, functions
# immutable (변경이 어려운): tuple, int, float, bool, string, bytes

import pandas
import pandas as pd

def add_new_column(new_vals, data = None):
    """새로운 컬럼을 data에 추가. 컬럼명은 columns_<n> 형태로 저장. 이 때, 모두 numeric로 저장

    Args:
        new_vals (iterable): 함수 실행 시마다, 새로운 컬럼의 값 의미
        data (Dataframe, optional): 함수가 실행시 업데이트.
             만약에 데이터프레임으로 입력받지 못하면, 임의의 데이터프레임이 디폴트로 생성
    Returns:
        DataFrame
    """
    if data is None:
        data = pd.DataFrame()
    data['col_{}'.format(len(data.columns))] = new_vals
    return data

if __name__ == "__main__":
    print(add_new_column(new_vals=range(10)))
    print(add_new_column(new_vals=None))
    print(add_new_column(new_vals=range(10)))
    print(add_new_column(new_vals=None))
```
<결과 화면>
```python
"C:\Program Files\anaconda3\envs\Python_f\python.exe" "C:/Program Files/anaconda3/envs/Python_f/211206/step_04_3_basic.py"
   col_0
0      0
1      1
2      2
3      3
4      4
5      5
6      6
7      7
8      8
9      9
Empty DataFrame
Columns: [col_0]
Index: []
   col_0
0      0
1      1
2      2
3      3
4      4
5      5
6      6
7      7
8      8
9      9
Empty DataFrame
Columns: [col_0]
Index: []

Process finished with exit code 0
```
```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# Context Manager                         카테터 (파티준비원)
# context 세팅                             - 테이블 세팅
# 코드 실행                                 - 하객이, 스테이크 주문, 식사
# context 없앰                             - 테이블 치움

def main():

    # context manager
    with open("data/my_file.txt") as file:
        text = file.read()
        text_length = len(text)

    print("파일 글자의 총 길이는 {} 이다.".format(text_length))

if __name__ == "__main__":
    main()
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/[파이썬활용]빅데이터 전문 인재양성 과정A/빅데이터(정지훈 쌤) 비대면 수업자료/211206/step_05_1_basic.py"
파일 글자의 총 길이는 33 이다.

Process finished with exit code 0
```

이 코드는 참고로 네이버 기사에서 '특정 문자가 나오는 횟수'를 카운트한 코드이다.

```python
# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Open "alice.txt" and assign the file to "file"

def main():
  with open('data/news_article.txt', encoding="utf-8") as file:
    text = file.read()

  n = 0
  for word in text.split():
    if word in ['오미크론', '코로나']:
      n += 1

  print('오미크론 및 코로나 단어가 나오는 개수는 {} 이다.'.format(n))


if __name__ == "__main__":
  main()
```
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/[파이썬활용]빅데이터 전문 인재양성 과정A/빅데이터(정지훈 쌤) 비대면 수업자료/211206/step_05_2_basic.py"
오미크론 및 코로나 단어가 나오는 개수는 5 이다.

Process finished with exit code 0
```
```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# context manager 파일을 생성

import contextlib

@contextlib.contextmanager
def my_context():
    print("안녕하세요 처음 인사드림.")
    yield 10
    print("안녕히 계세요.")
    
def main():
    with my_context() as temp:
        print("temp 인사말 {}".format(temp))

if __name__ == "__main__":
    main()
```
<결과 화면>
```python
"C:\Program Files\anaconda3\python.exe" "C:/Users/rudal/Desktop/[파이썬활용]빅데이터 전문 인재양성 과정A/빅데이터(정지훈 쌤) 비대면 수업자료/211206/step_05_3_basic.py"
안녕하세요 처음 인사드림.
temp 인사말 10
안녕히 계세요.

Process finished with exit code 0
```
```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

# DB 연동

import sqlite3

def db_create():
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    
    # Create table
    cur.execute('''CREATE TABLE stocks
                   (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    con.commit()
    con.close()

if __name__ == "__main__":
    db_create()
```
<결과 화면>
```python
"C:\Program Files\anaconda3\envs\Python_f\python.exe" "C:/Program Files/anaconda3/envs/Python_f/211206/step_05_4_basic.py"
Process finished with exit code 0
```

```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

import contextlib
import sqlite3

@contextlib.contextmanager
def db_connect(url):

    # example.db 주소 입력
    db = sqlite3.connect(url)

    yield db

    # db 연결 종료
    db.close()

def main(url):
    with db_connect(url) as con:
        cur = con.cursor()
        for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
            print(row)

if __name__ == "__main__":
    url = "example.db"
    main(url)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\envs\Python_f\python.exe" "C:/Program Files/anaconda3/envs/Python_f/211206/step_05_5_basic.py"
('2006-01-05', 'BUY', 'RHAT', 100.0, 35.14)

Process finished with exit code 0
```

```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

import contextlib
import time

@contextlib.contextmanager
def timer():
    """시간 측정하는 context manager 관리 함수

    Yields:
        None
    """

    start = time.time()
    yield
    end = time.time()

    print("시간측정(Elapsed): {:.2f} 초".format(end - start))

def main():
    with timer():
        print("얼마 걸릴까요?")
        time.sleep(0.25) # 크롤링 할 때, 종종 사용

if __name__ == "__main__":
    main()
```
<결과 화면>
```python
"C:\Program Files\anaconda3\envs\Python_f\python.exe" "C:/Program Files/anaconda3/envs/Python_f/211206/step_05_6_basic.py"
얼마 걸릴까요?
시간측정(Elapsed): 0.25 초

Process finished with exit code 0
```
아래의 코드는 인터넷 기사의 반복 되는 단어 수와 그걸 찾아 내는 시간을 카운터
해주는 코드다.
```python
# /c/Users/GREEN/Desktop/python_fun/venv/Scripts/python
# -*- coding: utf-8 -*-

import contextlib
import step_05_6_basic # <---- utils
import time

@contextlib.contextmanager
def openReadOnly(fileName):
    """

    :param fileName:
    :return:
    """

    read_file = open(fileName, mode = "r", encoding="utf-8")
    yield read_file
    read_file.close()

def main(fileName):
    with openReadOnly(fileName) as file:
        text = file.read() # 파일 전체 읽어오기 (한줄씩 읽어오기 아님...)

    n=0
    for word in text.split():
        if word in ["오미크론", "코로나"]:
            n += 1
    print("오미크론 및 코로나 단어의 갯수는 {} 이다.".format(n))

if __name__ == "__main__":
    fileName = "data/news_article.txt"
    with step_05_6_basic.timer():
        main(fileName)
        time.sleep(0.25)
```
<결과 화면>
```python
"C:\Program Files\anaconda3\envs\Python_f\python.exe" "C:/Program Files/anaconda3/envs/Python_f/211206/step_05_7_basic.py"
오미크론 및 코로나 단어의 갯수는 5 이다.
시간측정(Elapsed): 0.27 초

Process finished with exit code 0
```