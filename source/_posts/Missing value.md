---
title: Missing value (결측치)
tag: Missing value (결측치)
date: 2021-12-21
categories:	Python
---
# -Missing Value : 결측치
```python
1. 정의 : 
1. Missing Feature(누락 data) 를 처리 해주어야 ML이 잘 돌아 간다.
2. Na, Nan 과 같은 값
```
```python
2. 종류 : 
1. Random : 패턴이 없는 무작위 값
2. No Random : 패턴을 가진 결측치
```
# Deletion
```python
● deletion해서 특성이 바뀌지 않는다면, 가장 좋은 방법 
  ○ dropna()
  ○ axis = (0 : 행 제거, default),(1: 열제거)
  ○ subset = (특정 feature을 지정하여 해당 누락 data 제거)
```
```python
● Listwist(목록삭제)
  ○ 결측치가 있는 행 전부 삭제
```
```python
● pairwise(단일 값 삭제)
```
```python
df = df.dropna() # 결측치 있는 행 전부 삭제
df = df.dropna(axis = 1) # 결측치 있는 열 전부 삭제

df = df.dropna(how = 'all') # 전체가 결측인 행 삭제
df = df.dropna(thresh = 2) # threshold 2, 결측치 2초과 삭제 
```
```python
df = df.dropna(subset=['col1', 'col2', 'col3'])

# 특정열 모두가 결측치일 경우 해당 행 삭제
df = df.dropna(subset=['col1', 'col2', 'col3'], how = 'all')

# 특정열에 1개 초과의 결측치가 있을 경우 해당 행 삭제
df = df.dropna(subset=['col1', 'col2', 'col3'], thresh = 1 )

#바로 적용
df.dropna(inplace = True)
```              

<br><br>

---

### Imputation
1. 결측치를 특정 값으로 대치 
  - mode : 최빈값
    + 번주형, 빈도가 제일 높은값으로 대치 
  - median : 중앙값
    + 연속형, 결측값을 제외한 중앙값으로 대치 
  - mean : 평균
    + 연속형, 결측값을 제외한 평균으로 대치 
  - similar case imputation : 조건부 대치 
  - Generalized imputation : 회귀분석을 이용한 대치 
2. 사용함수
   - fillna(), replace(), interpolate()

##### fillna() : 0 처리

```python
df.fillna(0)
```
● df[].fillna() : 특정 column만 대치
```python
# 0으로 대체하기
df['col'] = df['col'].fillna(0)

# 컬럼의 평균으로 대체하기
df['col'] = df['col'].fillna(df['col'].mean())
```
```python
# 바로 위의 값으로 채우기
df.fillna(method = 'pad')

#바로 아래 값으로 채우기 
df.fillna(method='bfill')
```
● replace()
```python
#  대체, 결측치가 있으면, -50으로 채운다.
df.replace(to_replace = np.nan, value = -50)
```
● interpolate()
  ○ 만약, 값들이 선형적이라추정 후 간격으로 처리
```python
df.interpolate(method = 'linear' , limit_direction = 'forward')
```
5. prediction Model (예측모델)

  ● 결측치가 pattern을 가진다고 가정하고 진행.

  ● 결측값이 없는 컬럼들로 구성된 dataset으로 예측

  ● 회기분석기술 혹은 SVM과같은 ML 통계기법이 있다.

6. guid Line (Missiong Value : MV)

  ● MV < 10% : 삭제 or 대치

  ● 10% < MV < 50% : regression or model based imputation

  ● 50%< MV : 해당 column 제거