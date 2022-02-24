---
title: 넘파이 기본함수와 사용법
tag: 넘파이 기본함수와 사용법
date: 2021-11-05
categories:	Numpy
---
-넘파이 불러오기
```python
import numpy as np
print(np.__version__)
```

    1.19.5
    

-넘파이 기본함수 zeros()
```python
zeros_array = np.zeros((3,2))
print(zeros_array)
print("Data Type is:", zeros_array.dtype)
print("Data Shape is:", zeros_array.shape)
```

    [[0. 0.]
     [0. 0.]
     [0. 0.]]
    Data Type is: float64
    Data Shape is: (3, 2)
    

-넘파이 기본함수 ones()
```python
ones_array = np.ones((3,4), dtype='int32')
print(ones_array)
print("Data Type is:", ones_array.dtype)
print("Data Shape is:", ones_array.shape)
```

    [[1 1 1 1]
     [1 1 1 1]
     [1 1 1 1]]
    Data Type is: int32
    Data Shape is: (3, 4)
    

-넘파이 기본함수 reshape()
```python
# 3 X 4 배열을 Reshape --> 6 x 2
after_reshape = ones_array.reshape(6,2)
print(after_reshape)
print("Data Shape is:", after_reshape.shape)
```

    [[1 1]
     [1 1]
     [1 1]
     [1 1]
     [1 1]
     [1 1]]
    Data Shape is: (6, 2)
    


```python
after_reshape = ones_array.reshape(3,4)
```


```python
# 3 x 4 12 --> 2 x 3 x 2 = 12
after_reshape = ones_array.reshape(2,3,2)
print(after_reshape)
print("Data Shape is:", after_reshape.shape)
```

    [[[1 1]
      [1 1]
      [1 1]]
    
     [[1 1]
      [1 1]
      [1 1]]]
    Data Shape is: (2, 3, 2)
    


```python
after_reshape2= ones_array.reshape(2, -1, 2)
print("reshape(-1,2)?", after_reshape2.shape)
print(after_reshape2)
```

    reshape(-1,2)? (2, 3, 2)
    [[[1 1]
      [1 1]
      [1 1]]
    
     [[1 1]
      [1 1]
      [1 1]]]
    


```python
after_reshape3= ones_array.reshape(3,-1)
print("reshape(3, -1)? \n")
print(after_reshape3)
print("Data Shape is:", after_reshape3.shape)
```

    reshape(3, -1)? 
    
    [[1 1 1 1]
     [1 1 1 1]
     [1 1 1 1]]
    Data Shape is: (3, 4)
    
