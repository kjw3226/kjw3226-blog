```python
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
```

 #  Introduce

## 주제 
>  * 중국과 일본의 캐글러 트렌드

## 선정이유

>  * 동아시아중 가장 큰 영향력을 행사
>  * 비슷한 캐글러의 분포

## 개요
>  * 주제 중국 vs 일본 캐글러 최신 트렌드
>  * 2019년도 자료와 2021년도 자료기반 비교

#  DATA


```python
import plotly.express as px
import plotly.graph_objects as go
from warnings import filterwarnings
from plotly.subplots import make_subplots
from plotly.offline import plot, iplot, init_notebook_mode
init_notebook_mode(connected=True)
filterwarnings('ignore')

colors = ['#B1EDED','#B1B2ED','#1DE7ED','#1DA5ED','#1D50ED','#16548E']
gen_colors = ['#4169E1','#B2182B','#81007F','#D1B2FF','#EFE4E2']
JP_colors = ['#D90B0B','#F24444','#EFE4E2','#FCCE88','#64807F']
CN_colors = ['#E0201B','#FFCE3F','#A63F03','#04BF33','#F2E6D8']
coun_years_colors = ['#FDB0C0','#FFDB81','#FD4659','#FFAB0F']

coun_years = ['2019_JP','2019_CN','2021_JP','2021_CN']


df19 = pd.read_csv('../input/kaggle-survey-2019/multiple_choice_responses.csv')
df21 = pd.read_csv('../input/kaggle-survey-2021/kaggle_survey_2021_responses.csv')

df21.head()
```

* 19년도 자료와 21년도 자료를 기반으로 데이터셋 
* 2019년일본 ,2021년일본 , 2019년중국 , 2021년중국으로 분류

## DATA FRAME SET


```python
# define
def group(data, country, question_num):
    return data[data['Q3'] == country][question_num].value_counts()


def go_Pie(country, label_value):
    return go.Pie(title = country,
                  labels = label_value.index,
                  values = label_value.values,
                  textinfo = 'label+percent',
                  rotation=315,
                  hole = .3,)

# -----------------------------------------------------------

# Q1
JP_age_19 = group(df19,'Japan','Q1').sort_index()

JP_age_21 = group(df21,'Japan','Q1').sort_index()

CN_age_19 = group(df19,'China','Q1')
CN_age_19.loc['55-59'] = 0
CN_age_19.loc['60-69'] = 0
CN_age_19 = CN_age_19.sort_index()

CN_age_21 = group(df21,'China','Q1')
CN_age_21.loc['60-69'] = 0
CN_age_21 = CN_age_21.sort_index()

# -----------------------------------------------------------

# Q3
JP_ndarray = df19[df19['Q3'] == 'Japan']['Q2'].values
CN_ndarray = df19[df19['Q3'] == 'China']['Q2'].values
JP_age_list = [] # 'Male'을 'Man'으로 바꿔담을 빈 리스트 생성
CN_age_list = []

for item in JP_ndarray:
    if item == 'Male':
        # 문자열 치환
        item_mod = item.replace('Male','Man')
        # 새로운 리스트에 추가
        JP_age_list.append(item_mod)
    elif item == 'Female':
        item_mod2 = item.replace('Female','Woman')
        JP_age_list.append(item_mod2)
    else :
        JP_age_list.append(item)

for item in CN_ndarray:
    if item == 'Male':
        # 문자열 치환
        item_mod = item.replace('Male','Man')
        # 새로운 리스트에 추가
        CN_age_list.append(item_mod)
    elif item == 'Female':
        item_mod2 = item.replace('Female','Woman')
        CN_age_list.append(item_mod2)
    else :
        CN_age_list.append(item)

JP_age_series = pd.Series(JP_age_list)
CN_age_series = pd.Series(CN_age_list)


years = ['2019', '2021']
JP_country_count_19 = (df19[df19['Q3'] == 'Japan']['Q3']).count()
CN_country_count_19 = (df19[df19['Q3'] == 'China']['Q3']).count()
JP_country_count_21 = (df21[df21['Q3'] == 'Japan']['Q3']).count()
CN_country_count_21 = (df21[df21['Q3'] == 'China']['Q3']).count()

JP_country_count_19_21 = [JP_country_count_19, JP_country_count_21]
CN_country_count_19_21 = [CN_country_count_19, CN_country_count_21]

# -----------------------------------------------------------

# Q14
df19_JP = df19[df19.Q3.isin(['Japan'])]
df19_CN = df19[df19.Q3.isin(['China'])]
df21_JP = df21[df21.Q3.isin(['Japan'])]
df21_CN = df21[df21.Q3.isin(['China'])]
df19_JP_Q14 = pd.DataFrame()
df19_CN_Q14 = pd.DataFrame()
df21_JP_Q14 = pd.DataFrame()
df21_CN_Q14 = pd.DataFrame()
df19_JP_Q14['Q20'] = [df19_JP[col][1:].value_counts().index[0] for col in df19_JP.columns[97:109]]
df19_CN_Q14['Q20'] = [df19_CN[col][1:].value_counts().index[0] for col in df19_CN.columns[97:109]]
df21_JP_Q14['Q14'] = [df21_JP[col][1:].value_counts().index[0] for col in df21_JP.columns[59:71]]
df21_CN_Q14['Q14'] = [df21_CN[col][1:].value_counts().index[0] for col in df21_CN.columns[59:71]]
df19_JP_Q14['counts'] = [df19_JP[col][1:].value_counts().values[0] for col in df19_JP.columns[97:109]]
df19_CN_Q14['counts'] = [df19_CN[col][1:].value_counts().values[0] for col in df19_CN.columns[97:109]]
df21_JP_Q14['counts'] = [df21_JP[col][1:].value_counts().values[0] for col in df21_JP.columns[59:71]]
df21_CN_Q14['counts'] = [df21_CN[col][1:].value_counts().values[0] for col in df21_CN.columns[59:71]]


df19_JP_Q14.index = [3,0,6,4,5,2,7,1,8,9,10,11]
df19_CN_Q14.index = [3,0,6,4,5,2,7,1,8,9,10,11]
df19_JP_Q14 = df19_JP_Q14.sort_index()
df19_CN_Q14 = df19_CN_Q14.sort_index()
df21_JP_Q14['Q14'].index = [0,1,2,3,4,5,6,7,8,9,10,11]
df21_CN_Q14['Q14'].index = [0,1,2,3,4,5,6,7,8,9,10,11]
df19_JP_Q14.replace(regex = 'D3.js', value = 'D3 js', inplace = True)
df19_CN_Q14.replace(regex = 'D3.js', value = 'D3 js', inplace = True)

# Q16
df19_JP_Q16 = pd.DataFrame()
df19_CN_Q16 = pd.DataFrame()
df21_JP_Q16 = pd.DataFrame()
df21_CN_Q16 = pd.DataFrame()
df19_JP_Q16['Q28'] = [df19_JP[col][1:].value_counts().index[0] for col in df19_JP.columns[155:166]]
df19_CN_Q16['Q28'] = [df19_CN[col][1:].value_counts().index[0] for col in df19_CN.columns[155:166]]
df21_JP_Q16['Q16'] = [df21_JP[col][1:].value_counts().index[0] for col in df21_JP.columns[72:89]]
df21_CN_Q16['Q16'] = [df21_CN[col][1:].value_counts().index[0] for col in df21_CN.columns[72:89]]
df19_JP_Q16['counts'] = [df19_JP[col][1:].value_counts().values[0] for col in df19_JP.columns[155:166]]
df19_CN_Q16['counts'] = [df19_CN[col][1:].value_counts().values[0] for col in df19_CN.columns[155:166]]
df21_JP_Q16['counts'] = [df21_JP[col][1:].value_counts().values[0] for col in df21_JP.columns[72:89]]
df21_CN_Q16['counts'] = [df21_CN[col][1:].value_counts().values[0] for col in df21_CN.columns[72:89]]
df19_JP_Q16 = df19_JP_Q16.sort_index()
df19_CN_Q16 = df19_CN_Q16.sort_index()
```

> # What is your age?


```python
fig_age = make_subplots(rows=1, cols=2, specs=[[{'type':'xy'}, {'type':'xy'}]])

fig_age.add_trace(go.Bar(name=coun_years[0], x=JP_age_19.index, y=JP_age_19.values, marker_color='#FDB0C0'),1,1)
fig_age.add_trace(go.Bar(name=coun_years[2], x=JP_age_21.index, y=JP_age_21.values, marker_color='#FD4659'),1,1)
fig_age.add_trace(go.Bar(name=coun_years[1], x=CN_age_19.index, y=CN_age_19.values, marker_color='#FFDB81'),1,2)
fig_age.add_trace(go.Bar(name=coun_years[3], x=CN_age_21.index, y=CN_age_21.values, marker_color='#FFAB0F'),1,2)

fig_age.update_layout(barmode='group', title_text='2019 & 2021, Japan and China age distribution', showlegend=True)

fig_age.update_xaxes(title_text='Japan Age distribution', row=1, col=1)
fig_age.update_yaxes(title_text='Counts', row=1, col=1)
fig_age.update_xaxes(title_text='China Age distribution', row=1, col=2)
fig_age.update_yaxes(title_text='Counts', row=1, col=2)

fig_age.show()
```

# 나이 분포도
#### 일본
> * 2019년도에 25-29세의 분포가 가장 크게 나타났으며, 다음으로는 30-34 , 35-39 비율이 가장 높다.
> * 2021년도에 25-29세의 비율이 가장 높았으며, 2019년도 자료와 점유율은 비슷하지만 모든 연령층이 증가한것을 볼 수 있다.
> * 가장 눈에 띄는것은 18-21세의 비율이 급격하게 높아진것과 35-49세 이상의 나이 분포도가 모두 급격하게 증가한것이 눈에 띈다.

#### 중국
> * 2019년도에 22-24 , 25-29 , 18-21 순서대로 높았으며 젊은층의 비율이 압도적으로 높은것을 볼수 있다.
> * 2019년도에 비해 2021년에 전 연령대비 비율이 증가했지만, 18-21, 22-24, 30-34의 분포도가 압도적으로 높아진것을 볼 수 있다.
> * 가장 눈에 띄는것은 젊은층의 비율 18-21, 22-24의 분포가 급격하게 높아졌으며 30-34 분포 또한 소폭 상승했으며 그 외에는 미미하거나 조금 높아 졌다.


### 중국은 22-24세의 비율이 가장 높으며, 일본은 25-29세의 비율이 가장 높다.
### 두 나라 모두 젊은층의 점유율이 가장 높은 것을 알 수 있다. 

# Gender Distribution
> ## What is your gender?


```python
fig = make_subplots(rows=2, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}],
                                           [{'type':'domain'}, {'type':'domain'}]])

fig.add_trace(go_Pie('2019_Japan', JP_age_series.value_counts()),1,1)
fig.add_trace(go_Pie('2019_China', CN_age_series.value_counts()),1,2)
fig.add_trace(go_Pie('2021_Japan', group(df21,'Japan','Q2')),2,1)
fig.add_trace(go_Pie('2021_China', group(df21,'China','Q2')),2,2)

fig.update_traces(marker=dict(colors=gen_colors[0:]))
fig.update_layout(title_text='Gender Distribution',
                  showlegend=True,
                  autosize=True,
                  height=700)
fig.show()
```

# 성비율

#### 일본
> * 2019년도와 2021년도 모두 남성의 비율이 높으며 여성의 비율은 미미하게 감소했다.

#### 중국
> * 2019년도와 2021년도 모두 남성의 비율이 높으며 여성의 비율은 미미하게 감소했다.


### 일본과 중국 모두 남성의 비율이 압도적으로 높다
### 증가한 캐글러들의 성비가 남성의 유입이 많은걸 알 수 있다.


# 2019 vs 2021 (Japan , China)
> ##  In which country do you currently reside?


```python
fig_country = go.Figure(data=[
    go.Bar(name='Japan', x=years, y=JP_country_count_19_21, marker_color=JP_colors[0]),
    go.Bar(name='China', x=years, y=CN_country_count_19_21, marker_color=CN_colors[1])
])

fig_country.update_layout(
                    barmode='group',
                    title_text='2019 & 2021, the number of Kaggler living in Japan and China',
                    xaxis_title='Years',
                    yaxis_title='Counts')
fig_country.show()

```

 # 인원의 증감

#### 일본
> * 2019년 673명, 2021년에는 921명으로 약 248명정도 증가 했다.

#### 중국
> * 2019년 574명, 2021년에는 814명으로 약 240명정도 증가 했다.

### 일본이 중국보다 약 90명정도 캐글러가 많으며, 
### 2019년대비 2021년 현재 두 나라 모두 증가했음을 알 수 있다.

# visualization libraries or tools
>  ## What data visualization libraries or tools do you use on a regular basis? (Select all that apply)


```python
fig_T = make_subplots(rows=1, cols=2, specs=[[{'type':'xy'}, {'type':'xy'}]])

fig_T.add_trace(go.Bar(name=coun_years[0], x=df19_JP_Q14['Q20'].values, y=df19_JP_Q14['counts'].values, marker_color=coun_years_colors[0]),1,1)
fig_T.add_trace(go.Bar(name=coun_years[1], x=df19_CN_Q14['Q20'].values, y=df19_CN_Q14['counts'].values, marker_color=coun_years_colors[1]),1,1)
fig_T.add_trace(go.Bar(name=coun_years[2], x=df21_JP_Q14['Q14'].values, y=df21_JP_Q14['counts'].values, marker_color=coun_years_colors[2]),1,2)
fig_T.add_trace(go.Bar(name=coun_years[3], x=df21_CN_Q14['Q14'].values, y=df21_CN_Q14['counts'].values, marker_color=coun_years_colors[3]),1,2)

fig_T.update_layout(title_text='2019 & 2021, Visualization Library and Tools in Use',
                    showlegend=True,
                    autosize=True)

fig_T.update_xaxes(title_text='2019 Library and Tools', row=1, col=1)
fig_T.update_yaxes(title_text='Counts', row=1, col=1)
fig_T.update_xaxes(title_text='2021 Library and Tools', row=1, col=2)
fig_T.update_yaxes(title_text='Counts', row=1, col=2)

fig_T.show()
```

# 라이브러리와 툴 프로그램
#### 일본
> * 2019년 일본은 Matplotlib수치가 367로 가장 높은 비율이며, 두번째로는 seaborn(247) 세번째로는 Ggplot/ggplot2(79) 네번째로는 Plotly(61)이다.
> * 2021년 일본은 Matplotlib수치가 660로 가장 높은 비율이며, 두번째로는 seaborn(412) 세번째로는 None(137) 네번째는 Plotly(115) 다섯번째가 Ggplot/gglot2(74)이다.
> * 2019년 대비 Matplotlib가 2배에 가까운 수치로 증가했으며, seaborn이 뒤를 따르고 있다. None의 응답수도 많아졌으며, 2019년에 세번째로 비율이 높았던 Ggplot/ggplot2의 인원과 비율이 줄었다.
> * Plotly는 2019년 대비 인원과 비율이 증가했으며 None의 응답을 제외하면 3번째의 비율을 차지하고 있다.

#### 중국
> * 2019년 중국은 Matplotlib수치가 321로 가장 높은 비율이며, 두번째로는 seaborn(160) 세번째로는 Ggplot/gglot2(54) 네번째로는 Plotly(50)이다.
> * 2021년 중국은 Matplotlib수치가 491로 가장 높은 비율이며, 두번째로는 Seaborn(215) 세번째로는 None(155) 네번째는 Plotly(75) 다섯번째로 Ggplot/ggplot2(72)이다.
> * 2019년 대비 Matplotlib의 수치가 약 170명 정도 늘어 났고 seaborn 또한 약 50명정도 늘어났으며 세번째로 높았던 Ggplot/ggplot2의 시용은 소폭 증가했지만 Plotly의 증가에 뒤쳐졌다. None의 응답수가 눈에 띄게 증가했다.

### 2019년과 대비해 기존에 높았던 Matplotlib와 Seaborn 차지 비율은 더 높아졌고 Plotly/Plotly Express이 Ggplot/ggplot2를 제치고 증가했다.

# Japan & China programming languages
> ## What data visualization libraries or tools do you use on a regular basis? (Select all that apply)

### 2021 Japan & China total Dataframe SET
2021년 Q3(Country) 일본 중국 추출 dataframe


```python
df21_ChJp = df21[df21.Q3.isin(["Japan","China"])]

df21_ChJp_total_PL = pd.DataFrame()
df21_ChJp_total_PL['Program_Language'] = [df21_ChJp[col][1:].value_counts().index[0] for col in df21_ChJp.columns[7:20]]
df21_ChJp_total_PL['counts'] = [df21_ChJp[col][1:].value_counts().values[0] for col in df21_ChJp.columns[7:20]]
```

### 2019 Japan & China total
2019년 Q3(Country) 일본 중국 추출 dataframe


```python
df19_ChJp = df19[df19.Q3.isin(["Japan","China"])]

df19_ChJp_total_PL = pd.DataFrame()
df19_ChJp_total_PL['Program_Language'] = [df19_ChJp[col][1:].value_counts().index[0] for col in df19_ChJp.columns[82:94]]
df19_ChJp_total_PL['counts'] = [df19_ChJp[col][1:].value_counts().values[0] for col in df19_ChJp.columns[82:94]]
```

### Split Country
나라별 value_counts를 위해 각 나라로 dataframe 분리

#### 2021


```python
df21_Ch = df21_ChJp[df21_ChJp.Q3.isin(["China"])]
df21_Jp = df21_ChJp[df21_ChJp.Q3.isin(["Japan"])]


## Q7(Program_Language): 칼럼번호 8~20 - others
df21_Jp_PL = pd.DataFrame()
df21_Jp_PL['Program_Language'] = [df21_Jp[col][1:].value_counts().index[0] for col in df21_Jp.columns[7:19]]
df21_Jp_PL['counts'] = [df21_Jp[col][1:].value_counts().values[0] for col in df21_Jp.columns[7:19]]


## 2021 China: Q7_Part12(None) value == 0이므로 결측값 제거
df21_Ch_rmQ07P12 = df21_Ch.drop(['Q7_Part_12'], axis='columns')

## Q7(Program_Language): 칼럼번호 8~20 - others - Q7_Part12(None)
df21_Ch_PL = pd.DataFrame()
df21_Ch_PL['Program_Language'] = [df21_Ch_rmQ07P12[col][1:].value_counts() .index[0] for col in df21_Ch_rmQ07P12.columns[7:18]]
df21_Ch_PL['counts'] = [df21_Ch_rmQ07P12[col][1:].value_counts() .values[0] for col in df21_Ch_rmQ07P12.columns[7:18]]


## 제거된 나라 칼럼과 value를 각각 삽입 및 통합
df21_Jp_PL.insert(0, 'Country',  'Japan')
df21_Ch_PL.insert(0, 'Country',  'China')

df21_PL_JnC = pd.concat([df21_Jp_PL,df21_Ch_PL], ignore_index=True)
```

#### 2019


```python
df19_Ch = df19_ChJp[df19_ChJp.Q3.isin(["China"])]
df19_Jp = df19_ChJp[df19_ChJp.Q3.isin(["Japan"])]


## Q18(Program_Language): 칼럼번호 83~95 - others
df19_Jp_PL = pd.DataFrame()
df19_Jp_PL['Program_Language'] = [df19_Jp[col][1:].value_counts().index[0] for col in df19_Jp.columns[82:94]]
df19_Jp_PL['counts'] = [df19_Jp[col][1:].value_counts().values[0] for col in df19_Jp.columns[82:94]]


## 2019 China Q18_Part11(None) 결측값 제거
df19_Ch_rmQ18P11 = df19_Ch.drop(['Q18_Part_11'], axis='columns')

## Q18(Program_Language): 칼럼번호 83~95 - others - Q18_Part11(None)
df19_Ch_PL = pd.DataFrame()
df19_Ch_PL['Program_Language'] = [df19_Ch_rmQ18P11[col][1:].value_counts() .index[0] for col in df19_Ch_rmQ18P11.columns[82:93]]
df19_Ch_PL['counts'] = [df19_Ch_rmQ18P11[col][1:].value_counts() .values[0] for col in df19_Ch_rmQ18P11.columns[82:93]]



df19_Jp_PL.insert(0, 'Country',  'Japan')
df19_Ch_PL.insert(0, 'Country',  'China')

df19_PL_JnC = pd.concat([df19_Jp_PL,df19_Ch_PL], ignore_index=True)
```

### Split year{Country}
다른 csv인 2019자료와 2021자료 통합


```python
df21_PL_JnC.insert(0, 'year',  '2021')
df19_PL_JnC.insert(0, 'year',  '2019')

df_PL_JnC_21n19 = pd.concat([df21_PL_JnC,df19_PL_JnC], ignore_index=True)
```

* Program_Language의 19년도 21년도 통합 value_counts의 정렬(연도 - 언어 - 나라)

* values는 Program_Language의 value_counts

* color 기준: country


```python
fig = px.treemap(df_PL_JnC_21n19, path=[px.Constant("2019n2021"),'year','Program_Language','Country'],
                values='counts', color='Country',
                  color_discrete_map={'(?)':'lightgrey', 'China':'gold', 'Japan':'darkblue'})

fig.data[0].textinfo = 'label+percent parent+value'

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

fig.show()
```


 # 프로그램 언어
#### 일본
> * 2019년도엔 Python(442)이 가장 높았으며 SQL(150) , R(121) , C++(79) ,Javascript(73), C(70) , Bash(64) , Java(56) 순으로 높았다.
> * 2021년도엔 Python(786)이 가장 높았으며 SQL(232) , C++(164) , C(163) , Javascript(147) , Java(137) , R(122) , Bash(81) 순으로 높았다.
> * Python과 SQL의 언어 비중이 대부분을 차지 하고 있으며 2019년도에 비해 R의 비중이 크게 감소했다.

#### 중국
> * 2019년도엔 Python(375)이 가장 높았으며 SQL(117) , C++(98) , Java(73) , Matlab(67) , C(66) , R(60) , Javascript(38) , Bash(36)순으로 높았다.
> * 2021년도엔 Python(737)이 가장 높았으며 C++(267) , C(225) , SQL(215) , Java(212) , Matlab(169) , Javascript(86) , R(85) , Bash(31)순으로 높았다. 
> * Python의 차지 비율이 대부분을 차지 하고 있으며 2019년도 대비 C++과 C이 급증 했고 R과 Bash는 미미하며 낮은 비중을 차지한다.

### 2019년도 대비 2021년에는 여전히 Python의 자리는 굳건해졌고 Python을 제외하면 대부분 고른 분포를 보이지만 R과 Bash의 사용률은 굉장히 낮다.

# Japan & China: IDE's
> ##  Which of the following integrated development environments (IDE's) do you use on a regular basis? (Select all that apply)

## DataFrame Set

### Split Country

#### 2021


```python
## 앞선 Program_Language에서 선언된 객체로 주석처리
#df21_Ch = df21_ChJp[df21_ChJp.Q3.isin(["China"])]
#df21_Jp = df21_ChJp[df21_ChJp.Q3.isin(["Japan"])]


## Q9(IDE's): 칼럼번호 22~34 - others
df21_Jp_IDEs = pd.DataFrame()
df21_Jp_IDEs['IDE\'s'] = [df21_Jp[col][1:].value_counts().index[0] for col in df21_Jp.columns[21:33]]
df21_Jp_IDEs['counts'] = [df21_Jp[col][1:].value_counts().values[0] for col in df21_Jp.columns[21:33]]


df21_Ch_IDEs = pd.DataFrame()
df21_Ch_IDEs['IDE\'s'] = [df21_Ch[col][1:].value_counts().index[0] for col in df21_Ch.columns[21:33]]
df21_Ch_IDEs['counts'] = [df21_Ch[col][1:].value_counts().values[0] for col in df21_Ch.columns[21:33]]



df21_Ch_IDEs.insert(0, 'Country',  'China')
df21_Jp_IDEs.insert(0, 'Country',  'Japan')

df21_IDEs_JnC = pd.concat([df21_Jp_IDEs,df21_Ch_IDEs], ignore_index=True)
```

#### 2019


```python
#df19_Ch = df19_ChJp[df19.Q3.isin(["China"])]
#df19_Jp = df19_ChJp[df19.Q3.isin(["Japan"])]


## Q16(IDE's): 칼럼번호 57~69 - others
df19_Jp_IDEs = pd.DataFrame()
df19_Jp_IDEs['IDE\'s'] = [df19_Jp[col][1:].value_counts().index[0] for col in df19_Jp.columns[56:68]]
df19_Jp_IDEs['counts'] = [df19_Jp[col][1:].value_counts().values[0] for col in df19_Jp.columns[56:68]]


df19_Ch_IDEs = pd.DataFrame()
df19_Ch_IDEs['IDE\'s'] = [df19_Ch[col][1:].value_counts().index[0] for col in df19_Ch.columns[56:68]]
df19_Ch_IDEs['counts'] = [df19_Ch[col][1:].value_counts().values[0] for col in df19_Ch.columns[56:68]]



df19_Jp_IDEs.insert(0, 'Country',  'China')
df19_Ch_IDEs.insert(0, 'Country',  'Japan')

df19_IDEs_JnC = pd.concat([df19_Jp_IDEs,df19_Ch_IDEs], ignore_index=True)
```

### Split year{Country}


```python
df21_IDEs_JnC.insert(0, 'year',  '2021')
#df21_JCQ9.rename(columns={'Q9':'IDE'}, inplace = True)
df19_IDEs_JnC.insert(0, 'year',  '2019')
#df19_JCQ9.rename(columns={'Q16':'IDE'}, inplace = True)

df_IDEs_JnC_21n19 = pd.concat([df21_IDEs_JnC,df19_IDEs_JnC], ignore_index=True)
```


```python
# 요소명 간략화
df_IDEs_JnC_21n19.replace(to_replace = 'Jupyter (JupyterLab, Jupyter Notebooks, etc) ', value = 'Jupyter', inplace = True)
df_IDEs_JnC_21n19.replace(to_replace = 'Visual Studio / Visual Studio Code', value = 'VS / VSCode', inplace = True, regex = True)
```


```python
fig = px.treemap(df_IDEs_JnC_21n19, path=[px.Constant("2019n2021"),'year','IDE\'s','Country'],
                values='counts', color='Country',
                  color_discrete_map={'(?)':'lightgrey', 'China':'gold', 'Japan':'darkblue'})

fig.data[0].textinfo = 'label+percent parent+value'

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

fig.show()
```

# Frameworks
> ##  Which of the following machine learning frameworks do you use on a regular basis? (Select all that apply)



 # 통합 개발 환경(IDE's) 
 - *2021년도 자료에는 문항이 나누어져 있어 Jupyter와 visual이 세부적으로 나뉘져 있다.(편의상 Jupter와 visual로 호칭)*
 
#### 일본
> * 2019년도엔 Jupyter(293)과 Pycharm(240)이 주를 이르고 있으며 Visual(137)이 세번째의 비중을 차지하고 있으며 뒤따르고 있는 개발 환경들은 비슷비슷한 수치를 보이고 있다.
> * 2021년도엔 Jupyter과 Visual 대부분을 차지 하며 Pycharm과 나머지 항목들이 뒤를 잇고 있다.
> * Visual의 사용률이 급증했으며 Jupyter와 Visual 이 양대산맥을 이룰정도로 압도적인 수치를 보이고 Pycharm의 증가는 미미하고 Visual에 밀린 모습이다.

#### 중국
> * 2019년도엔 Jupyter과 Visual이 주를 이루고 있으며 Vim / Emacs가 세번째로 비중이 컸다 pycharm과 Rstudio가 그 뒤를 따르고 있다.
> * 2021년도엔 Pycharm의 비중이 크게 증가했으며 Jupter와 Visual은 여전히 높은 수치를 보여 주고 있고 Python도 어깨를 나란히 하고 있다.
> * 기존에 높았던 Jupter와 Visual은 더 많은 사람들이 사용을 하고 점유율이 크지 않던 Pycharm이 2021년도가 됨에따라 많은 비중을 차지 한다.

### 두 나라 모두 Jupyter, Visual 굉장히 큰 비중을 차지하고 있다


```python
fig_F = make_subplots(rows=1, cols=2, specs=[[{'type':'xy'}, {'type':'xy'}]])
 
fig_F.add_trace(go.Bar(name=coun_years[0], x=df19_JP_Q16['Q28'].values, y=df19_JP_Q16['counts'].sort_values(ascending=False).values, marker_color=coun_years_colors[0]),1,1)
fig_F.add_trace(go.Bar(name=coun_years[1], x=df19_CN_Q16['Q28'].values, y=df19_CN_Q16['counts'].sort_values(ascending=False).values, marker_color=coun_years_colors[1]),1,1)
fig_F.add_trace(go.Bar(name=coun_years[2], x=df21_JP_Q16['Q16'].values, y=df21_JP_Q16['counts'].sort_values(ascending=False).values, marker_color=coun_years_colors[2]),1,2)
fig_F.add_trace(go.Bar(name=coun_years[3], x=df21_CN_Q16['Q16'].values, y=df21_CN_Q16['counts'].sort_values(ascending=False).values, marker_color=coun_years_colors[3]),1,2)
 
fig_F.update_layout(title_text='2019 & 2021, Machine Learning Frameworks in Use',
                    showlegend=True,
                    autosize=True)

fig_F.update_xaxes(title_text='2019 Machine Learning Frameworks', row=1, col=1)
fig_F.update_yaxes(title_text='Counts', row=1, col=1)
fig_F.update_xaxes(title_text='2021 Machine Learning Frameworks', row=1, col=2)
fig_F.update_yaxes(title_text='Counts', row=1, col=2)

fig_F.show()
```

 # 머신러닝 프레임워크
 
#### 일본
> * 2019년도엔 Scikit-learn이 가장 높은 비율을 차지한다.
> * 2021년도엔 Scikit-learn이 가장 높은 비율을 차지한다.
> * Scikit-learn이 높은 비율을 차지하는것은 여전하다.

#### 중국
> * 2019년도엔 Scikit-learn이 가장 높은 비율을 차지한다.
> * 2021년도엔 Scikit-learn이 가장 높은 비율을 차지한다.
> * Scikit-learn이 높은 비율을 차지하지만 압도적인 사용률을 자랑하진 않는다.

### 일본은 Scikit-learn이 압도적으로 높은 인기를 자랑하지만 중국은 크게 차이나는 수치는 아니다.
### 두 나라 모두 Xgboost 와 Caret 인기가 식었다. 반면 PyTorch와 Fast.ai ,MXNET 항목들이 성장하여 현재 순위권에 이름을 올렸다.


# Conclusion !
## 지표로 보는 2019년과 2021년의 차이
* 막대그래프와 트리맵으로 보는 2019년과 2021년의 차이
  > * 2019년에 비해 2021년도에 크게 캐글러들이 많이 유입된 걸 알 수 있다. 중국은 인구비율에 비해 적은 캐글러의 숫자가 눈에 띈다. 두 나라 모두 젊은층의 인원들이 급격하게 증가했다. 
  > * 두 나라 모두 대개 남성의 인원이 많다. 
* 동아시아에서 캐글러들의 크게 나타나는 특징
  > * 툴과 언어에 대해서 비슷하지만 다른 양상을 보이고 있다.
  > * Matplotlib,Seaborn,Plotly의 비중이 높아졌다.
  > * 프로그래밍 언어는 조금 다른 특징이 있다. 먼저 일본같은 경우 Phython과 SQL의 비중이 가장 높은 반면 중국은 Python의 비중이 크지만 다른 언어들의 비중 차지는 비슷하다. 공통점으로는 R의 언어비중이 크게 감소한게 눈에 띈다. 두 나라 모두 2019년도 대비 2021년도에는 R의 사용량이 많이 낮아졌다. 
  > * IDE's 개발 환경은 두 나라의 경우 쥬피터와 비쥬얼 모두 많은 점유율을 보이고 있으나 다른 프로그램들은 두 프로그램에 비해 낮은 점유율을 보이고 있으며 일본은 파이썬의 비중이 적은 반면 중국은 파이썬의 비중이 커졌다.
  > * 머신 러닝 프레임워크같은경우 두 나라가 Scikit-learn이 높은 비율을 차지하는건 동일하지만 나머지 항목들은 비슷하며 Xgboost와 Caret의 점유율이 떨어졌다. 그리고 Pytorch와 Fast.ai,MXNET이 새롭게 이름을 올린 모습을 보인다.
* 향후 동아시아 미래의 캐글러들의 비전과 트렌드 예측 
 > * 캐글러들의 성장이 기대된다 앞으로 캐글러들의 성장은 계속 될 걸로 보인다.
 > * 앞서 봤던 나이 분포도를 보면 젊은 인원들의 유입에 의해 캐글시장이 확대 될 걸로 보여진다.
 > * IT산업의 증진에 따라 더욱 많은 인원들이 유입될걸로 보이며 압도적인 수치를 보였던 툴과 언어 머신러닝 프레임워크는 더욱 더 많은 사람들이 사용될 걸로 보인다.
 > * 동아시아의 인접한 국가지만 가장 높은 비율이 차지하는것들은 일치하며 동아시아에 많은 영향이 미칠것으로 기대되고 앞으로 주목해야할 포인트라고 보인다.

### REFERENCE
 - plotly bar chart tutorial(https://plotly.com/python/bar-charts/)
 - plotly bar chart properties (bar traces)(https://plotly.com/python/reference/bar/)
 - plotly pie chart tutorial(https://plotly.com/python/pie-charts/)
 - plotly pie chart properties (pie traces)(https://plotly.com/python/reference/pie/)
 - [데이터프레임 합치기](https://yganalyst.github.io/data_handling/Pd_12/)
 - [행열 이름 변경](https://mizykk.tistory.com/131)
 - [pd insert](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html)
     - [Ex1](https://www.delftstack.com/ko/howto/python-pandas/how-to-add-new-column-to-existing-dataframe-in-python-pandas/)
     - [Ex2](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=rising_n_falling&logNo=221631637822)
