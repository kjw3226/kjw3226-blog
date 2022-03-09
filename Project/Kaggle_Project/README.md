# 2021 Kaggle Machine Learning & Data Science Survey

![img1](https://user-images.githubusercontent.com/93234783/144552544-98653e94-a356-41ce-b63b-761482754bae.PNG)

-----

## Outline of the contest (대회개요)

#### 1.대회 설명

연례 데이터 과학 설문 조사에서 의미 있는 콘텐츠를 발견하십시오.

#### 2.도전 목표

내러티브 텍스트와 데이터 탐색의 조합을 통해 이 설문조사에 포함된 데이터 과학 커뮤니티의 하위 집합에 대한 데이터 스토리를 전달합니다. 
"스토리"는 여러 가지 방법으로 정의할 수 있으며 이는 의도적입니다. 
과제는 데이터 과학 및 기계 학습 실무자의 특정 그룹의 영향, 우선 순위 또는 우려 사항을 (데이터를 통해) 깊이 탐구하는 것입니다. 
해당 그룹은 매크로(예: Python 에서 대부분의 코딩을 수행하는 모든 사람) 또는 마이크로(예: 석사 프로그램에서 기계 학습을 공부하는 여성 데이터 과학 학생)로 정의할 수 있습니다. 
이것은 당신이 동일시하거나 열정을 갖고 있는 커뮤니티의 이야기를 창의적으로 말할 수 있는 기회입니다!

#### 3.참여 방법

제출하려면 제출양식을 작성하십시오.
참가자당 하나의 제출만 심사되므로 여러 번 제출하는 경우 마지막(가장 최근) 항목을 검토합니다.

노트북 어워드는 제출할 필요가 없습니다. 
자격을 얻으려면 노트북이 공개되어 있어야 하며 2021 데이터 과학 설문조사를 데이터 원본으로 사용해야 합니다.

#### 4.제출 기한

● 제출 마감: 2021년 11월 28일

● 당첨자 발표: 2021년 12월 16일

Kaggle 은 또한 11월 7일 이전에 출판된 우리가 가장 좋아하는 노트북에 수여하는 노트북 상을 수여합니다. 

모든 노트북은 마감일 이후에 평가됩니다.

모든 마감일은 달리 명시되지 않는 한 해당 날짜의 오후 11:59 UTC 입니다. 

대회 주최자는 필요하다고 판단되는 경우 대회 일정을 업데이트할 권리가 있습니다.

제출하려면 제출양식을 작성하십시오.

#### 5. 상금

최고의 데이터 스토리텔링 제출물에는 5개의 상품이 있습니다.

● 1등: $10,000

● 2등: $5,000

● 3등: $5,000

● 4등: $5,000

● 5등 상금: $5,000 

Kaggle 은 또한 11월 7일 일요일 오후 11:59:00 UTC 이전에 게시된 우리가 가장 좋아하는 노트북을 인정하기 위해 

1,000달러 의 노트북 상을 수여 합니다.


#### 제출 프로젝트 코드


[the-latest-trends-in-east-asia-japan-and-china](https://www.kaggle.com/kwdoku145/the-latest-trends-in-east-asia-japan-and-china)

## the-latest-trends-in-east-asia-japan-and-china

### Introduce

● 주제

 중국과 일본의 캐글러 트렌드

● 선정이유

 동아시아중 가장 큰 영향력을 행사

 비슷한 캐글러의 분포 

● 개요

 주제 중국 vs 일본 캐글러 최신 트렌드

 2019년도 자료와 2021년도 자료기반 비교
 

## DATA
```python
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
## DATA FRAME SET

### define
```python
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

###Q1
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

###Q3
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

###Q14
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

###Q16
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
## What is your age?
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
## Gender Distribution
### What is your gender?
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
## 2019 vs 2021 (Japan , China)

### In which country do you currently reside?
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
## visualization libraries or tools
### What data visualization libraries or tools do you use on a regular basis? (Select all that apply)
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
## Japan & China programming languages
### What data visualization libraries or tools do you use on a regular basis? (Select all that apply)

### 2021 Japan & China total Dataframe SET

#### 2021년 Q3(Country) 일본 중국 추출 dataframe
```python
df21_ChJp = df21[df21.Q3.isin(["Japan","China"])]

df21_ChJp_total_PL = pd.DataFrame()
df21_ChJp_total_PL['Program_Language'] = [df21_ChJp[col][1:].value_counts().index[0] for col in df21_ChJp.columns[7:20]]
df21_ChJp_total_PL['counts'] = [df21_ChJp[col][1:].value_counts().values[0] for col in df21_ChJp.columns[7:20]]
```
### 2019 Japan & China total

#### 2019년 Q3(Country) 일본 중국 추출 dataframe
```python
df19_ChJp = df19[df19.Q3.isin(["Japan","China"])]

df19_ChJp_total_PL = pd.DataFrame()
df19_ChJp_total_PL['Program_Language'] = [df19_ChJp[col][1:].value_counts().index[0] for col in df19_ChJp.columns[82:94]]
df19_ChJp_total_PL['counts'] = [df19_ChJp[col][1:].value_counts().values[0] for col in df19_ChJp.columns[82:94]]
```
## Split Country
### 나라별 value_counts를 위해 각 나라로 dataframe 분리
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
## Split year{Country}

#### 다른 csv인 2019자료와 2021자료 통합
```python
df21_PL_JnC.insert(0, 'year',  '2021')
df19_PL_JnC.insert(0, 'year',  '2019')

df_PL_JnC_21n19 = pd.concat([df21_PL_JnC,df19_PL_JnC], ignore_index=True)
```
```python
fig = px.treemap(df_PL_JnC_21n19, path=[px.Constant("2019n2021"),'year','Program_Language','Country'],
                values='counts', color='Country',
                  color_discrete_map={'(?)':'lightgrey', 'China':'gold', 'Japan':'darkblue'})

fig.data[0].textinfo = 'label+percent parent+value'

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

fig.show()
```
## Japan & China: IDE's
#### Which of the following integrated development environments (IDE's) do you use on a regular basis? (Select all that apply)

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
## Frameworks
### Which of the following machine learning frameworks do you use on a regular basis? (Select all that apply)
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

