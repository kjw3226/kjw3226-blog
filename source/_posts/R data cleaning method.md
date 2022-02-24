---
title: R data cleaning method('R' 데이터 정제 방법)
tag: R data cleaning method('R' 데이터 정제 방법)
date: 2021-12-05
categories:	
 
---
##1 .결측치 정제하기
결측치 (Missing Value)는 누락된 값, 비어 있는 값을 의미한다.

실제로도 수집과정에서 발생한 오류로 인해 결측치를 포함하고 있는 경우가 많아 

그것을 확인하고 제거하는 정제과정을 거친 후에 분석을 해야 한다.

그럼 확인하고 제거하는 방법 등 을 알아보자.

### 결측치 확인
```python
table(is.na(df$score))
```
### 여러 변수 동시에 결측치 제거
```python
df_nomiss<-df %>% filter(!is.na(score) & !is.na(sex)) 

▲ score, sex 결측치 제거
```
### 함수의 결측치 제외 기능 이용하기
```python
mean(df$score, na.rm = T)
▲ mean 에 'na.rm = T' 를 적용해서 결측치 제외하고 평균 산출.

exam %>% summarise(mean_math = mean(math, na.rm = T))
▲ mean 에 'na.rm = T' 를 적용해서 math의 결측치 제외하고 평균 산출. 
```


## 2 .이상치 정제하기
정상 범주에서 크게 벗어난 값을 이상치 (Outlier)라고 한다.

이상치가 포함되어 있으면 분석 결과가 왜곡되기 때문에 

반드시 분석하기 전 이상치 제거 작업을 먼저 해야 한다.

그럼 그 방법을 알아보자.

### 이상치 확인
```python
table(outlier$sex)
▲ table() 을 이용해 이상치의 빈도표를 생성해 'sex'의 이상치를 확인한다.
```
### 결측 처리하기
```python
outlier$sex <- lfelse(outlier$sex == 3, NA, outlier$sex)
▲ 이상치를 확인했으니 이상치를 결측치로 변환한다.  
  'ifelse()'를 이용해서 'sex'에 '3'이 있으면 'NA'(결측치) 로 변환한다.
```
### 극단치?
극단치란 존재는 하지만 극단적으로 크거나 작은 값을 '극단치' 라고 한다.

이 값도 분석 결과를 왜곡시킬 수 있기 때문에 분석 전에 제거해야 한다.

그 방법을 알아보자.

### 극단치 'boxplot'으로 확인하기 
```python
boxplot(mpg$hwy)$stats
▲ 상자 그림 통계치 출력
```

### 12-37 벗어나면 'NA(결측치)' 처리 하기
```python
mpg$hwy <- ifelse(mpg$hwy < 12 | mpg$hwy > 37, NA, mpg$hwy)

▲ 'ifelse'를 이용해 12-37을 벗어나면 'NA(결측치)'를 할당시킨다.
```
### 결측치 제외하고 최종 분석 하기
```python
mpg %>% group_by(drv) %>% summarise(mean_hwy = mean(hwy, na.rm = T))

▲ summarise를 이용해 '요약 통계량'을 출력할 때 'mean'에 'na.rm'을 이용해

  결측치를 제외하고 평균을 출력.
```
참고 : 'Do it! 쉽게배우는 R 데이터분석'