---
title: extract kaggle questions (캐글 질문 항목 출력하기)
tag: extract kaggle questions (캐글 질문 항목 출력하기)
date: 2021-11-17
categories:	kaggle
---
오늘은 ‘kaggle-surve-2021’ 질문지에서 질문 항목을
출력하는 작업을 했다.

아래 코드는 가장 기본적인 코드이다.
```python
df['Q11'].value_counts() 
#원하는 질문값을 '[]' 안에 'Q~~'이런식으로 Q와 번호를 써주면 질문안의 데이터가 출력된다.
```

![extract kaggle questions1](https://user-images.githubusercontent.com/93234783/142092658-50d6b565-2919-44b9-8905-19f1db658c19.PNG)

```python
df_note = pd.DataFrame()    #질문 항목 중 'Part'가 붙은 질문은 이런식으로 '반복문'을 작성해서 데이터 목록을 출력한다.
df_note['std_notebook'] = [df_std[col][1:].value_counts().index[0] for col in df.columns[:]]
df_note['std_counts'] = [df_std[col][1:].value_counts().values[0] for col in df.columns[:]]
print(df_note)
```
위의 코드를 활용해서 질문 항목 중 ‘Part’로 나눠지는 ‘Q14’를
출력하는 코드가 아래의 코드이다.

```python
df_note = pd.DataFrame()
df_note['std_notebook'] = [df_std[col][1:].value_counts().index[0] for col in df.columns[59:71]] #'Q14'의 'columns'를 '59번째'에서 '71번째'까지 출력한다는 의미.
                          # '[df_std[col][1:]' 이 부분은 첫번째 열부터 한번 반복해서 출력한다는 의미이다.
df_note['std_counts'] = [df_std[col][1:].value_counts().values[0] for col in df.columns[59:71]] #'Q14'의 'columns'를 '59번째'에서 '71번째'까지 출력한다는 의미.
                        # '[df_std[col][1:]' 이 부분은 첫번째 열부터 한번 반복해서 출력한다는 의미이다.
print(df_note)
```
![extract kaggle questions2](https://user-images.githubusercontent.com/93234783/142092665-82dde5ec-4051-4aea-8511-ea5bb8c44bcd.PNG)


아래의 코드는 질문지 항목 'Q1'을 활용해서
막대그래프로 시각화 작업을 해준 것이다.

```python
q1_df = df['Q1'].value_counts()

fig = go.Figure()
fig.add_trace(go.Bar(x = q1_df.index, y = q1_df.values))

fig.show()
```
![extract kaggle questions3](https://user-images.githubusercontent.com/93234783/142092684-2a078155-a5be-4e97-a2ea-28dbc49dfe8f.PNG)


위의 코드와는 또 다른 방식으로 
좀 더 정보를 추가해서 
막대그래프로 시각화를 시켜준 것이 아래의 코드이다.
```python
q1_df = df['Q1'].value_counts()

CATEGORY_ORDER = ["18-21", "22-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-69", "70+"]

# basic graph
fig = go.Figure()
fig.add_trace(go.Bar(x = q1_df.index, y = q1_df.values))

# styling changes
fig.update_layout(plot_bgcolor = "white", 
                 font  = dict(color = "#909999"), 
                 title = dict(text = "your TITLE text"), 
                 xaxis = dict(title = "your X-AXIS TITLE", linecolor = "#21DBAA", categoryorder = "array", categoryarray = CATEGORY_ORDER), 
                 yaxis = dict(title = "your Y-AXIS TITLE", linecolor = "#DB9021"))

fig.show()
```
![extract kaggle questions4](https://user-images.githubusercontent.com/93234783/142092688-0283ee45-c16f-41dd-a7f9-9ee1a13ff224.PNG)

이번에는 'Q1'과 'Q2'를 같이 활용한 코드이다.

```python
q1_q2_df = df.loc[:, ["Q1", "Q2"]].replace({'Prefer not to say':'etc', 'Nonbinary':"etc", "Prefer to self-describe": "etc"})
q1_q2_df['Q2'].value_counts() #'Q1'과 'Q2'의 항목을 이용해서 
                               #성별에 따라서 사람들의 수를 알 수 있다.
```
![extract kaggle questions5](https://user-images.githubusercontent.com/93234783/142092696-5e736ad0-5adf-4c33-b30a-c09b458dec88.PNG)

```python
q1_q2_df = q1_q2_df.groupby(['Q2','Q1']).size().reset_index().rename(columns = {0:"Count"})
q1_q2_df.head() #'Q1'과 'Q2'의 항목을 이용해서 
                #'남자'가 '나이'에 따라서 각각 몇명씩 있는지 알 수 있다.
```
![extract kaggle questions6](https://user-images.githubusercontent.com/93234783/142092700-1ea15eca-5008-47a1-b230-97ebbb9543c6.PNG)

```python
fig = go.Figure()
for gender, group in q1_q2_df.groupby("Q2"):
   fig.add_trace(go.Bar(x = group['Q1'], y = group['Count'], name = gender))
fig.update_layout(barmode="group",        
                 plot_bgcolor = "white")  #'Q1'과 'Q2'의 항목을 이용해서 
                                          #성별 별로 막대그래프로 시각화 작업을 한 코드이다.
fig.show()
```
![extract kaggle questions7](https://user-images.githubusercontent.com/93234783/142092706-9d9648e3-40e5-4203-a24a-7ceadf9320b3.PNG)

참고 : https://www.kaggle.com/j2hoon85/plotly-tutorial-for-kaggle-survey-competitions
       https://www.kaggle.com/bhaveshkumar2806/kaggle-survey-2021-analysis-plotly

