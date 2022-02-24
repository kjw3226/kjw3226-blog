---
title: 구글 코랩과 드라이브 연동하고 파일 불러오기
tag: 구글 코랩과 드라이브 연동하고 파일 불러오기
date: 2021-11-06
categories: google colab
---

-구글 드라이브와 연동하기
```python
from google.colab import drive
drive.mount('/content/drive')
```
<결과 화면>
```python
Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).
```

-파일 불러오기
```python
#DATA_PATH = "경로를 입력하시기를 바랍니다."

# 필자의 경로는 다음과 같았습니다. 
DATA_PATH = '/content/drive/MyDrive/Colab Notebooks/lectures_210923/PART_I_Intro/data/Lemonade2016.csv'
lemonade = pd.read_csv(DATA_PATH)
lemonade.info()
```
<결과 화면>

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 32 entries, 0 to 31
    Data columns (total 7 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   Date         31 non-null     object 
     1   Location     32 non-null     object 
     2   Lemon        32 non-null     int64  
     3   Orange       32 non-null     int64  
     4   Temperature  32 non-null     int64  
     5   Leaflets     31 non-null     float64
     6   Price        32 non-null     float64
    dtypes: float64(2), int64(3), object(2)
    memory usage: 1.9+ KB
    