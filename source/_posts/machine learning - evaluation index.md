---
title: machine learning evaluation index(머신러닝 평가지표)
tag: machine learning evaluation index(머신러닝 평가지표)
date: 2021-11-18
categories:	Python Machine Learning

---
파이썬 머신러닝의 평가지표에는 
'MAE', 'MSE', 'RMSE' 이렇게 크게 3가지 종류가 있다.

오늘은 이 3가지에 대해 알아보았다.

1.MAE
-'Mean Absolute Error'의 줄임말이다.
 실제 값과 예측값의 차이를 절댓값으로 변환해 평균한 것을 말한다.
 코드는 아래와 같다.
```python
  import numpy as np

  def mean_absolute_error(y_true, y_pred):

  error = 0
  for yt, yp in zip(y_true, y_pred):
    error = error + np.abs(yt-yp)
  
  mae = error / len(y_true)
  return mae
```
2.MSE
-'Mean Squared Log Error'의 줄임말이다.
 실제 값과 예측값의 차이를 제곱해 평균한 것을 말한다.
 코드는 아래와 같다.
```python
  import numpy as np

  def mean_squared_error(y_true, y_pred):
   
  error = 0 
  for yt, yp in zip(y_true, y_pred):
    error = error + (yt - yp) ** 2
  
  mse = error / len(y_true)
  return mse
```
3.RMSE
-'Root Mean Squared Eerror'의 줄임말이다.
 MSE 같은 오류의 제곱을 구할때 
 실제 오류 평균보다 더 커지는 특성이 있으므로 
 MSE에 루트를 씌운 것   
 수식은 이렇게 생겼다.

 ![RMSE](https://user-images.githubusercontent.com/93234783/142362702-5fc45960-47de-432e-908a-4acbb2d88fc1.png)
 
 코드는 아래와 같다.

```python
import numpy as np

def root_rmse_squared_error(y_true, ypred):
  error = 0
  
  for yt, yp in zip(y_true, y_pred):
    error = error + (yt - yp) ** 2
  
  mse = error / len(y_true)
  rmse = np.round(np.sqrt(mse), 3)
  return rmse
```
참고 : https://libertegrace.tistory.com/entry/Evaluation2?category=864460