---
title: plotly.express에 있는 choropleth maps 이용해서 지도 그리기
tag: plotly.express에 있는 choropleth maps 이용해서 지도 그리기
date: 2021-11-25
categories:	Plotly
 
---
plotly.express 에 있는 'choropleth' 함수를 이용하면 지도를 
그리는 것이 가능하다.

그리고 아래의 코드를 실행하기전 반드시
아래의 코드를 입력해 줘야지 에러가 발생하지 않는다.
```python
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
```

코드는 아래와 같다.

```python
import plotly.express as px

df = px.data.election()
geojson = px.data.election_geojson()

fig = px.choropleth(df, geojson=geojson, color="winner",
                    locations="district", featureidkey="properties.district",
                    projection="mercator", hover_data=["Bergeron", "Coderre", "Joly"]
                   )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```
참고로 위코드는 미국 선거 관련 데이터를 지도에 색상을 바꿔 시각화 한것이다.

![choropleth1](https://user-images.githubusercontent.com/93234783/143378402-e6822863-963a-4069-b1cd-83477e4b7f31.PNG)




참고: https://plotly.com/python/choropleth-maps/