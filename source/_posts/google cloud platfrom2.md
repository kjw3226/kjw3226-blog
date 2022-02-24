---
title: Google Cloud Platfrom2(구글 클라우드 플랫폼2)
tag: Google Cloud Platfrom2(구글 클라우드 플랫폼2)
date: 2022-01-21
categories:	SQL
----

어제에 이어 오늘도 'Google'에 있는 'Big Query'를 이용해 실습을 하였다.

크게 2가지를 알아보기 위해 실습했는데 

1. 구글 코랩과 연동시키기

2. 'Big Query'에서 'ML'(Machine Learning) 코드 만들고 실행 시켜보기

3. 'data studio'에서 '차트' 추가해보기

먼저 '구글 클라우드 플랫폼' 사이트에 들어간다.

그리고 '구글 코랩'도 실행시켜 놓는다.

그 다음 어제 만들어 놓은 '데이터 베이스'에 새로운 '테이블'을 하나 만들어준다.

그리고 '쿼리툴'을 열어 아래의 쿼리문을 순서대로 입력하고 실행시킨다.

여기서 부터는 '구글 코랩'에서 입력해야 된다.
```python
# 인증하기
from google.colab import auth
auth.authenticate_user()
print('Authenticated')
```
```python
# 데이터 불러오기
from google.cloud import bigquery

client = bigquery.Client(project=project_id)

df = client.query('''
  SELECT * FROM `basketball.mascots`
''').to_dataframe()

df
```
```python
#서브 쿼리 테스트
df = client.query('''
  WITH matchups AS (
  SELECT g.win_team_id
  , g.lose_team_id
  , (SELECT win_masc.tax_family FROM `basketball.mascots` win_masc WHERE win_masc.id = g.win_team_id) AS tax_family_winner
  , (SELECT win_masc.tax_genus FROM `basketball.mascots` win_masc WHERE win_masc.id = g.win_team_id) AS tax_genus_winner
  , (SELECT lose_masc.tax_family FROM `basketball.mascots` lose_masc WHERE lose_masc.id = g.lose_team_id) AS tax_family_loser
  , (SELECT lose_masc.tax_genus FROM `basketball.mascots` lose_masc WHERE lose_masc.id = g.lose_team_id) AS tax_genus_loser
  FROM `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games` g
  )
  SELECT
    SUM(IF(tax_family_winner = "Felidae" AND tax_genus_loser = "Canis", 1, 0)) AS num_cat_wins,
    SUM(IF(tax_genus_winner = "Canis" AND tax_family_loser = "Felidae", 1, 0)) AS num_dog_wins
  FROM matchups
''').to_dataframe()

df
```
```python
# Sample 데이터 가져오기
import pandas as pd 
df = pd.read_csv("/content/sample_data/california_housing_train.csv")
df.head()
```
여기까지가 구글 코랩에서 입력해야 되는 부분.

여기는 다시 'Big Query' '쿼리툴'에서 입력한다.
```python
# Dataset Project Name
TABLE_NAME = 'basketball.housting_train'
project_id = 'your_project_id' # 생성한 프로젝트 이름 입력

df.to_gbq(TABLE_NAME, project_id, if_exists='append')
```
이제 마지막으로 'google data studio'에 들어가서 

결과 값을 추가 하고 '차트'를 추가해보면 끝이다.


이제 'Big Query'에서 'Machine Learning(ML - 머신러닝)' 코드를 작성하고 

실행시켜 보자.

1단계: 모델 만들기 SQL 코드
```python
CREATE OR REPLACE MODEL `bigpractice.penguins_model`
OPTIONS
  (model_type='linear_reg',
  input_label_cols=['body_mass_g']) AS
SELECT
  *
FROM
  `bigquery-public-data.ml_datasets.penguins`
WHERE
  body_mass_g IS NOT NULL
```
▶ 학습한 모델의 정보를 확인.
```python
SELECT
  *
FROM
  ML.TRAINING_INFO(MODEL `bigPractice.penguins_model`)
```
2단계: 모델 평가
```python
SELECT
  *
FROM
  ML.EVALUATE(MODEL `bigPractice.penguins_model`,
    (
    SELECT
      *
    FROM
      `bigquery-public-data.ml_datasets.penguins`
    WHERE
      body_mass_g IS NOT NULL))
```
3단계: 모델 사용하여 결과 예측
```python
SELECT
  *
FROM
  ML.PREDICT(MODEL `bigPractice.penguins_model`,
    (
    SELECT
      *
    FROM
      `bigquery-public-data.ml_datasets.penguins`
    WHERE
      body_mass_g IS NOT NULL
      AND island = "Biscoe"))
```
이제 마지막으로 'google data studio'에 들어가서 

예측값을 넣고 '차트'를 추가해주면 끝이다.

아래는 실습 화면을 캡쳐한 것들이다.

![BigQuery-query tool](https://user-images.githubusercontent.com/96108301/150477627-7f31189a-8ca3-47b2-8c29-7ec0777013e6.PNG)

![data studio - 01 21](https://user-images.githubusercontent.com/96108301/150477636-ab4b2ae4-46a1-4c92-9073-301fc761c18e.PNG)

![data studio - 01 21 -2](https://user-images.githubusercontent.com/96108301/150477639-14744395-f151-49c6-9f88-60de1d6a45bc.PNG)
