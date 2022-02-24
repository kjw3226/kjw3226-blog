---
title: kaggle-survey-2021
tag: kaggle-survey-2021
date: 2021-11-08
categories:	kaggle

---
```python
import numpy as np   
import pandas as pd
import matplotlib.pyplot as plt  # matplotlib와 그 안의 'plot(그래프)'를 import 한다는 뜻
import plotly.express as px  #Express는 plotly라이브러리 에 내장된 일부 함수이고 이 함수를 import한다는 뜻.
import plotly.graph_objects as go  #plotly.graph_objects모듈을 import한다는 뜻.
from warnings import filterwarnings #경고 메시지가 뜨지않게 예외처리 해준다는 뜻.
filterwarnings('ignore') #경고 메시지가 뜨지않게 예외처리 해준다는 뜻.
colors = ['#B1EDED','#B1B2ED','#1DE7ED','#1DA5ED','#1D50ED','#16548E'] 
df = pd.read_csv('../input/kaggle-survey-2021/kaggle_survey_2021_responses.csv') #'/'로 구분된 값(csv) 파일을 DataFrame으로 읽어온다는 뜻.
df.head()

df['Q3'] = df['Q3'].str.replace(', Islamic Republic of...', '') #.str.replace() 함수는 엑셀의 "찾기 및 바꾸기" 기능과 유사한 역할하며, .str.replace('찾을 내용`, `바꿀 내용`)과 같은 형태로 사용.
map_df = pd.DataFrame()
map_df['country'] = df['Q3'][1:].value_counts().index #value_counts() -고유한 값의 개수를 포함하는 값을 반환한다는 뜻. #.index -->모든 pandas 객체에 대한 축 레이블을 저장하는 기본 객체입니다.
map_df['count'] = df['Q3'][1:].value_counts().values #value_counts() -고유한 값의 개수를 포함하는 값을 반환한다는 뜻.   #DataFrame의 Numpy에 속하는 함수를 반환한다는 뜻.

fig = px.choropleth(map_df, locations="country", locationmode='country names', #locations->위치 ID 또는 이름을 통해 좌표를 설정합니다. #locationmode->'위치'의 항목을 지도의 지역과 일치시키는 데 사용되는 위치 집합을 결정합니다.
                     hover_name="country", color="count", color_continuous_scale=colors, #color_continuous_scale->Plotly Express 함수는 color_continuous_scale 인수를 허용하고 많은 유형에는 스키마에 colorscale 속성이 있습니다.
                    title='Country wise Distribution of Kagglers')  #Choropleth이란 색상이나 패턴을 사용하여 특정 통계에 대한 데이터를 사전 정의된 영역과 관련시켜 시각화 한 지도 유형. 
fig.show()
```
![kaggle1](https://user-images.githubusercontent.com/93234783/140717495-23a75a77-f7f9-4ac8-a078-2f56f6082179.PNG)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_object go
from warnings import filterwarnings
filterwarnings('ignore')

colors = ['#B1EDED', '#B1B2ED', '#1DE7ED', '#1D50ED','#16548E']

df = pd.read_csv('../input/kaggle-survey-2021/kaggle_survey_2021_responses.csv')
df.head()
x=df['Q5'][1:].value_counts().values[::-1]
y=df['Q5'][1:].value_counts().index[::-1]
percent = [round(((i/sum(x)) * 100), 1) for i in x]
fig = go.Figure(data=[go.Bar( #go.Figure->plotly.graph_objects 모듈 에서 Figure(그래프의 외형)를 사용한다는 뜻 
            x=x,              #go.Bar -> plotly.graph_objects 모듈 에서 Bar를 사용한다는 뜻.
            y=y,
            text=percent,
            textposition='inside',     #textposition->'텍스트'의 위치를 지정합니다. "내부" 위치 `텍스트`내부, 막대 끝 옆(필요한 경우 회전 및 크기 조정).
            texttemplate='%{text:.3s}%', #texttemplate->차트에 임의의 텍스트를 표시하려고 texttemplate 을 사용한다는 뜻.
            orientation='h',              #orientation-> 방향(str, 가로의 경우 'h' 또는 세로의 경우 'v' 중 하나)
            marker_color=colors[2]        
        )])


fig.update_layout(title='Current role of kagglers', xaxis_title='counts', yaxis_title='Current role')#update_layout->update_layout을 이용하면 타이틀과 X축, Y축을 변경할 수 있다. 
fig.show()
```
![kaggle2](https://user-images.githubusercontent.com/93234783/140717501-6f81444d-8495-4829-9f7c-d2e7a13bbb10.PNG)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from warnings import filterwarnings
filterwarnings('ignore')

colors = ['#B1EDED','#B1B2ED','#1DE7ED','#1DA5ED','#1D50ED','#16548E']

df = pd.read_csv('../input/kaggle-survey-2021/kaggle_survey_2021_responses.csv')
df.head()

fig = go.Figure(data=[go.Pie(labels=df['Q4'][1:].value_counts().index, values=df['Q4'][1:].value_counts().values,
                             textinfo='label+percent')])# textinfo = 'label+percent'-->그래프 항목당 나타낼 텍스트 (여기서는 항목명, 비율)
fig.update_traces(marker=dict(colors=colors[2:])) #update_traces ->지정된 기준을 충족하는 모든 값에 대해 속성 업데이트 작업을 수행합니다.
                                                  #'marker=dict' --> # 그래프를 어떤 색으로 표현할 것인가를 설정
fig.update_layout(title_text='Formal Education attained or plan to attain in next 2 year', showlegend=False)
#showlegend --> 범롈를 표시 할지의 여부를 설정하는 함수
fig.show()
```
![kaggle3](https://user-images.githubusercontent.com/93234783/140717502-a50203d3-d746-4cb9-a449-64e76daae845.PNG)
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from warnings import filterwarnings
filterwarnings('ignore')

colors = ['#B1EDED','#B1B2ED','#1DE7ED','#1DA5ED','#1D50ED','#16548E']

df = pd.read_csv('../input/kaggle-survey-2021/kaggle_survey_2021_responses.csv')
df.head()

man = df[df['Q2'] == 'Man']['Q1'].value_counts()
woman = df[df['Q2'] == 'Woman']['Q1'].value_counts()
textonbar_man = [round((m/(m+w))*100, 1) for m, w in zip(man.values, woman.values)]# list comprehension = [(변수를 활용한 값) for (사용할 변수 이름) in (순회 할 수 있는 값)]
                                                                                    # for문을 사용하여 round함수의 계산을 하고 textonbar_man에 저장
textonbar_woman = [round((w/(m+w))*100, 1) for m, w in zip(man.values, woman.values)]# for문을 사용하여 round함수의 계산을 하고 textonbar_woman에 저장

fig = go.Figure(data=[
    go.Bar(name='Man', x=man.index, y=man.values, text=textonbar_man, marker_color=colors[2]),
    go.Bar(name='Woman', x=woman.index, y=woman.values, text=textonbar_woman, marker_color=colors[3]) 
])
fig.update_traces(texttemplate='%{text:.3s}%', textposition='inside')
fig.update_layout(barmode='stack', title_text='Age distribution by gender', xaxis_title='Age', yaxis_title='Counts')
#barmode --> 막대그래프의 형태를 나타낸다. 
fig.show()
```
![kaggle4](https://user-images.githubusercontent.com/93234783/140845962-ea37dcc0-461d-4c5b-8cd6-7053a6bb91d6.PNG)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from warnings import filterwarnings
filterwarnings('ignore')

colors = ['#B1EDED','#B1B2ED','#1DE7ED','#1DA5ED','#1D50ED','#16548E']

df = pd.read_csv('../input/kaggle-survey-2021/kaggle_survey_2021_responses.csv')
df.head()

fig = px.funnel_area(names=df['Q6'][1:].value_counts().index, values=df['Q6'][1:].value_counts().values,#funnel_area-> 역삼각형 형태로 그래프를 그리는데 사용되는 함수.
                    title='Coding Experince')
fig.update_traces(marker=dict(colors=colors[::-1]))
fig.show()
```
![kaggle5](https://user-images.githubusercontent.com/93234783/140845983-b574be8d-9ddd-4ba7-9d11-566abc1705e2.PNG)
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from warnings import filterwarnings
filterwarnings('ignore')

colors = ['#B1EDED','#B1B2ED','#1DE7ED','#1DA5ED','#1D50ED','#16548E']
df = pd.read_csv('../input/kaggle-survey-2021/kaggle_survey_2021_responses.csv')
df.head()

df_py = df[(df['Q7_Part_1'] == 'Python')]
df_r = df[(df['Q7_Part_2'] == 'R')]

fig = go.Figure(data=[
    go.Bar(name='Python', x=df_py['Q1'].value_counts().index, y=df_r['Q1'].value_counts().values,
          marker_color=colors[2]),
    go.Bar(name='R', x=df_r['Q1'].value_counts().index, y=df_r['Q1'].value_counts().values,
          marker_color=colors[3])
])

fig.update_layout(barmode='group', title='Kagglers using Python and R on regular basis by Age',
                 xaxis_title='Age', yaxis_title='Counts')
fig.show()
```
![kaggle6](https://user-images.githubusercontent.com/93234783/140846010-dd22400f-fa0f-436c-aeb3-61c0eb6273b0.PNG)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from warnings import filterwarnings
filterwarnings('ignore')

colors = ['#B1EDED','#B1B2ED','#1DE7ED','#1DA5ED','#1D50ED','#16548E']
df = pd.read_csv('../input/kaggle-survey-2021/kaggle_survey_2021_responses.csv')
df.head()

df_env = pd.DataFrame()
df_env['dev_env'] = [df[col][1:].value_counts().index[0] for col in df.columns[21:34]] # list comprehension = [(변수를 활용한 값) for (사용할 변수 이름) in (순회 할 수 있는 값)]
df_env['counts'] = [df[col][1:].value_counts().values[0] for col in df.columns[21:34]]
df_env.sort_values(by='counts', ascending=False, inplace=True)
#sort_values->두 축 중 하나를 따라 값을 기준으로 정렬하는 함수.
fig = px.treemap(df_env, path=[px.Constant("all"),'dev_env'], values='counts', color='counts', color_continuous_scale=colors)
#treemap-> 출력되는 그래프의 형태를 나타내기 위해 사용되는 함수.
fig.update_traces(root_color="lightgrey")
fig.update_layout(title='Development environment used by kagglers')
fig.show()
```
![kaggle7](https://user-images.githubusercontent.com/93234783/140846033-e3479b68-c1ed-4cfd-a702-b129624674a9.PNG)
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from warnings import filterwarnings
filterwarnings('ignore')

colors = ['#B1EDED','#B1B2ED','#1DE7ED','#1DA5ED','#1D50ED','#16548E']
df = pd.read_csv('../input/kaggle-survey-2021/kaggle_survey_2021_responses.csv')
df.head()

df_std = df[df['Q5'] == 'Student']
df_ds = df[df['Q5'] == 'Data Scientist']

df_note = pd.DataFrame()
df_note['std_notebook'] = [df_std[col][1:].value_counts().index[0] for col in df.columns[34:51]]
df_note['std_counts'] = [df_std[col][1:].value_counts().values[0] for col in df.columns[34:51]]

df_note['ds_notebook'] = [df_ds[col][1:].value_counts().index[0] for col in df.columns[34:51]]
df_note['ds_counts'] = [df_ds[col][1:].value_counts().values[0] for col in df.columns[34:51]]
df_note.sort_values(by=['std_counts', 'ds_counts'], ascending=False, inplace=True 
fig = go.Figure(data=[
    go.Bar(name='Student', x=df_note['std_notebook'], y=df_note['std_counts'], marker_color=colors[2]),
    go.Bar(name='Data Scientist', x=df_note['ds_notebook'], y=df_note['ds_counts'], marker_color=colors[3])
])


fig.update_layout(barmode='group', title='Cloud notebooks used by kagglers', xaxis_title='Notebook', yaxis_title='Counts',
                 height=600, width=900) #barmode -> 기본 누적 막대 차트 동작은 barmode 인수를 사용하여 그룹화(클러스터라고도 함)로 변경할 수 있다.
fig.show()

```
![kaggle8](https://user-images.githubusercontent.com/93234783/140846076-241a285f-f6f8-42aa-86ed-852d55660668.PNG)

<소스별 참고 주소>

-import matplotlib.pyplot as plt -->https://ordo.tistory.com/68

-import plotly.express as px --->https://plotly.com/python/plotly-express/

-import plotly.graph_objects as go --->https://plotly.com/python/graph-objects/

-from warnings import filterwarnings --> https://docs.python.org/ko/dev/library/warnings.html

-filterwarnings('ignore') --->https://docs.python.org/ko/dev/library/warnings.html

-colors = ['#B1EDED', '#B1B2ED', '#1DE7ED', '#1DA5ED', '#1D50ED', '#16548E']-->https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors

-df = pd.read_csv ---->https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

-choropleth --> https://anweh.tistory.com/55

-locations -->https://plotly.com/python/reference/choropleth/#choropleth

-locationmode-->https://plotly.com/python/reference/choropleth/#choropleth-locationmode

-hover_name-->https://plotly.com/python-api-reference/generated/plotly.express.bar.html

-color_continuous_scale --->https://plotly.com/python/builtin-colorscales/

-.values --->https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.values.html?highlight=values#pandas.DataFrame.values

-.index-->https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.html?highlight=index#pandas.Index

-value_counts()--->https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html

-str.replace -->https://hogni.tistory.com/14

-pd.DataFrame() -->https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html


[1:]-->처음부터 끝까지 슬라이싱 한다는 의미

[::-1]-->처음부터 -1번째 까지 슬라이싱한다는 의미

-go.Figure--->https://steminher.tistory.com/13

-textposition-->https://www.kite.com/python/docs/plotly.graph_objs.Bar.textposition

-texttemplate--> https://plotly.com/python/text-and-annotations/

-orientation-->https://plotly.com/python-api-reference/generated/plotly.express.bar.html

-marker_color-->https://www.kite.com/python/docs/plotly.graph_objs.Scatter.marker

-update_layout-->https://tariat.tistory.com/928

-go.Pie-->https://plotly.com/python/pie-charts/

-textinfo-->https://plotly.com/python/reference/

-fig.update_traces-->https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html

-showlegend -->https://plotly.com/python/legend/

-funnel_area-->https://plotly.com/python/funnel-charts/

-barmode -->https://plotly.com/python/bar-charts/

-sort_values-->https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html

-ascending -->https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html

-inplace -->https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html

-treemaps -->https://plotly.com/python/treemaps/

-path --> https://www.kite.com/python/docs/plotly.graph_objs.layout.Shape.path

-root_color --->https://plotly.com/python/reference/treemap/
