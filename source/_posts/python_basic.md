---
title: 파이썬 기초문법
tag: 파이썬 기초문법
date: 2021-11-04
categories:	Python

---
```python
-딕셔너리
dic = {'teacher':'alice', 'class': 5, 'studentid': '15', 'list':[1,2,3]}

print(dic['teacher'])
print(dic['class'])
print(dic['list'])
```

    alice
    5
    [1, 2, 3]
    


```python
-if 조건문
a = -5

if a>5:
    print('a is bigger than 5')

elif a > 0:
    print("a is bigger than 0 but a is smaller than 5 ")

else:
    print("a is negative")
```


```python
- 반복문
for i in range(100):
  print("Hello World")
```

    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    


```python
a = "Kaggle"

for x in a:
    print(x)

    if x == 'g':
        break
```

    K
    a
    g
    


```python
alphabets = ['A', 'B', 'C']
for index, value in enumerate(alphabets):
    print(index, value)
```

    0 A
    1 B
    2 C
    
