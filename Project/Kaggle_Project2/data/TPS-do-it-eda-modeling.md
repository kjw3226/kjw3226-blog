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

    /kaggle/input/tabular-playground-series-dec-2021/sample_submission.csv
    /kaggle/input/tabular-playground-series-dec-2021/train.csv
    /kaggle/input/tabular-playground-series-dec-2021/test.csv
    

# Import Library

# T.P.S Submission File


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler , LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from scipy.stats import mode



from lightgbm import LGBMClassifier



from matplotlib import ticker
import time
import warnings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('float_format', '{:f}'.format)
warnings.filterwarnings('ignore')
```


<style type='text/css'>
.datatable table.frame { margin-bottom: 0; }
.datatable table.frame thead { border-bottom: none; }
.datatable table.frame tr.coltypes td {  color: #FFFFFF;  line-height: 6px;  padding: 0 0.5em;}
.datatable .bool    { background: #DDDD99; }
.datatable .object  { background: #565656; }
.datatable .int     { background: #5D9E5D; }
.datatable .float   { background: #4040CC; }
.datatable .str     { background: #CC4040; }
.datatable .time    { background: #40CC40; }
.datatable .row_index {  background: var(--jp-border-color3);  border-right: 1px solid var(--jp-border-color0);  color: var(--jp-ui-font-color3);  font-size: 9px;}
.datatable .frame tbody td { text-align: left; }
.datatable .frame tr.coltypes .row_index {  background: var(--jp-border-color0);}
.datatable th:nth-child(2) { padding-left: 12px; }
.datatable .hellipsis {  color: var(--jp-cell-editor-border-color);}
.datatable .vellipsis {  background: var(--jp-layout-color0);  color: var(--jp-cell-editor-border-color);}
.datatable .na {  color: var(--jp-cell-editor-border-color);  font-size: 80%;}
.datatable .sp {  opacity: 0.25;}
.datatable .footer { font-size: 9px; }
.datatable .frame_dimensions {  background: var(--jp-border-color3);  border-top: 1px solid var(--jp-border-color0);  color: var(--jp-ui-font-color3);  display: inline-block;  opacity: 0.6;  padding: 1px 10px 1px 5px;}
</style>



# Data Loading and Preperation


```python
train = pd.read_csv("../input/tabular-playground-series-dec-2021/train.csv")
test = pd.read_csv("../input/tabular-playground-series-dec-2021/test.csv")
submission = pd.read_csv("../input/tabular-playground-series-dec-2021/sample_submission.csv")


train.drop(["Id"] , axis = 1 , inplace = True)
test.drop(["Id"] , axis = 1 , inplace = True)
TARGET = 'Cover_Type'  
FEATURES = [col for col in train.columns if col not in ['id', TARGET]]
RANDOM_STATE = 12 
```

<a id="3.1"></a>
# Exploring Train Data

## Quick view of Train Data


```python
train.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Elevation</th>
      <th>Aspect</th>
      <th>Slope</th>
      <th>Horizontal_Distance_To_Hydrology</th>
      <th>Vertical_Distance_To_Hydrology</th>
      <th>Horizontal_Distance_To_Roadways</th>
      <th>Hillshade_9am</th>
      <th>Hillshade_Noon</th>
      <th>Hillshade_3pm</th>
      <th>Horizontal_Distance_To_Fire_Points</th>
      <th>Wilderness_Area1</th>
      <th>Wilderness_Area2</th>
      <th>Wilderness_Area3</th>
      <th>Wilderness_Area4</th>
      <th>Soil_Type1</th>
      <th>Soil_Type2</th>
      <th>Soil_Type3</th>
      <th>Soil_Type4</th>
      <th>Soil_Type5</th>
      <th>Soil_Type6</th>
      <th>Soil_Type7</th>
      <th>Soil_Type8</th>
      <th>Soil_Type9</th>
      <th>Soil_Type10</th>
      <th>Soil_Type11</th>
      <th>Soil_Type12</th>
      <th>Soil_Type13</th>
      <th>Soil_Type14</th>
      <th>Soil_Type15</th>
      <th>Soil_Type16</th>
      <th>Soil_Type17</th>
      <th>Soil_Type18</th>
      <th>Soil_Type19</th>
      <th>Soil_Type20</th>
      <th>Soil_Type21</th>
      <th>Soil_Type22</th>
      <th>Soil_Type23</th>
      <th>Soil_Type24</th>
      <th>Soil_Type25</th>
      <th>Soil_Type26</th>
      <th>Soil_Type27</th>
      <th>Soil_Type28</th>
      <th>Soil_Type29</th>
      <th>Soil_Type30</th>
      <th>Soil_Type31</th>
      <th>Soil_Type32</th>
      <th>Soil_Type33</th>
      <th>Soil_Type34</th>
      <th>Soil_Type35</th>
      <th>Soil_Type36</th>
      <th>Soil_Type37</th>
      <th>Soil_Type38</th>
      <th>Soil_Type39</th>
      <th>Soil_Type40</th>
      <th>Cover_Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3189</td>
      <td>40</td>
      <td>8</td>
      <td>30</td>
      <td>13</td>
      <td>3270</td>
      <td>206</td>
      <td>234</td>
      <td>193</td>
      <td>4873</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3026</td>
      <td>182</td>
      <td>5</td>
      <td>280</td>
      <td>29</td>
      <td>3270</td>
      <td>233</td>
      <td>240</td>
      <td>106</td>
      <td>5423</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3106</td>
      <td>13</td>
      <td>7</td>
      <td>351</td>
      <td>37</td>
      <td>2914</td>
      <td>208</td>
      <td>234</td>
      <td>137</td>
      <td>5269</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3022</td>
      <td>276</td>
      <td>13</td>
      <td>192</td>
      <td>16</td>
      <td>3034</td>
      <td>207</td>
      <td>238</td>
      <td>156</td>
      <td>2866</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2906</td>
      <td>186</td>
      <td>13</td>
      <td>266</td>
      <td>22</td>
      <td>2916</td>
      <td>231</td>
      <td>231</td>
      <td>154</td>
      <td>2642</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(f'Number of rows in train data: {train.shape[0]}')
print(f'Number of columns in train data: {train.shape[1]}')
print(f'No of missing values in train data: {sum(train.isna().sum())}')
```

    Number of rows in train data: 4000000
    Number of columns in train data: 55
    No of missing values in train data: 0
    

## Basic statistics of training data


```python
train.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Elevation</th>
      <th>Aspect</th>
      <th>Slope</th>
      <th>Horizontal_Distance_To_Hydrology</th>
      <th>Vertical_Distance_To_Hydrology</th>
      <th>Horizontal_Distance_To_Roadways</th>
      <th>Hillshade_9am</th>
      <th>Hillshade_Noon</th>
      <th>Hillshade_3pm</th>
      <th>Horizontal_Distance_To_Fire_Points</th>
      <th>Wilderness_Area1</th>
      <th>Wilderness_Area2</th>
      <th>Wilderness_Area3</th>
      <th>Wilderness_Area4</th>
      <th>Soil_Type1</th>
      <th>Soil_Type2</th>
      <th>Soil_Type3</th>
      <th>Soil_Type4</th>
      <th>Soil_Type5</th>
      <th>Soil_Type6</th>
      <th>Soil_Type7</th>
      <th>Soil_Type8</th>
      <th>Soil_Type9</th>
      <th>Soil_Type10</th>
      <th>Soil_Type11</th>
      <th>Soil_Type12</th>
      <th>Soil_Type13</th>
      <th>Soil_Type14</th>
      <th>Soil_Type15</th>
      <th>Soil_Type16</th>
      <th>Soil_Type17</th>
      <th>Soil_Type18</th>
      <th>Soil_Type19</th>
      <th>Soil_Type20</th>
      <th>Soil_Type21</th>
      <th>Soil_Type22</th>
      <th>Soil_Type23</th>
      <th>Soil_Type24</th>
      <th>Soil_Type25</th>
      <th>Soil_Type26</th>
      <th>Soil_Type27</th>
      <th>Soil_Type28</th>
      <th>Soil_Type29</th>
      <th>Soil_Type30</th>
      <th>Soil_Type31</th>
      <th>Soil_Type32</th>
      <th>Soil_Type33</th>
      <th>Soil_Type34</th>
      <th>Soil_Type35</th>
      <th>Soil_Type36</th>
      <th>Soil_Type37</th>
      <th>Soil_Type38</th>
      <th>Soil_Type39</th>
      <th>Soil_Type40</th>
      <th>Cover_Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
      <td>4000000.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2980.191660</td>
      <td>151.585671</td>
      <td>15.097537</td>
      <td>271.315436</td>
      <td>51.662621</td>
      <td>1766.641630</td>
      <td>211.837542</td>
      <td>221.061441</td>
      <td>140.810874</td>
      <td>1581.406810</td>
      <td>0.261193</td>
      <td>0.041661</td>
      <td>0.653573</td>
      <td>0.021819</td>
      <td>0.016841</td>
      <td>0.030896</td>
      <td>0.004275</td>
      <td>0.037913</td>
      <td>0.015715</td>
      <td>0.007973</td>
      <td>0.000000</td>
      <td>0.002900</td>
      <td>0.010893</td>
      <td>0.054541</td>
      <td>0.027985</td>
      <td>0.018290</td>
      <td>0.031295</td>
      <td>0.014977</td>
      <td>0.000000</td>
      <td>0.015888</td>
      <td>0.020672</td>
      <td>0.013436</td>
      <td>0.013811</td>
      <td>0.017368</td>
      <td>0.011539</td>
      <td>0.031346</td>
      <td>0.049171</td>
      <td>0.025022</td>
      <td>0.003258</td>
      <td>0.013527</td>
      <td>0.011766</td>
      <td>0.010708</td>
      <td>0.022274</td>
      <td>0.028867</td>
      <td>0.027493</td>
      <td>0.037462</td>
      <td>0.037821</td>
      <td>0.011995</td>
      <td>0.016053</td>
      <td>0.010713</td>
      <td>0.012207</td>
      <td>0.040752</td>
      <td>0.039239</td>
      <td>0.031619</td>
      <td>1.771335</td>
    </tr>
    <tr>
      <th>std</th>
      <td>289.048167</td>
      <td>109.961122</td>
      <td>8.546731</td>
      <td>226.549680</td>
      <td>68.215966</td>
      <td>1315.609890</td>
      <td>30.759956</td>
      <td>22.231335</td>
      <td>43.698639</td>
      <td>1127.616169</td>
      <td>0.439285</td>
      <td>0.199813</td>
      <td>0.475831</td>
      <td>0.146092</td>
      <td>0.128677</td>
      <td>0.173036</td>
      <td>0.065247</td>
      <td>0.190985</td>
      <td>0.124372</td>
      <td>0.088934</td>
      <td>0.000000</td>
      <td>0.053771</td>
      <td>0.103800</td>
      <td>0.227082</td>
      <td>0.164931</td>
      <td>0.133998</td>
      <td>0.174115</td>
      <td>0.121459</td>
      <td>0.000000</td>
      <td>0.125044</td>
      <td>0.142283</td>
      <td>0.115133</td>
      <td>0.116707</td>
      <td>0.130638</td>
      <td>0.106798</td>
      <td>0.174251</td>
      <td>0.216224</td>
      <td>0.156191</td>
      <td>0.056988</td>
      <td>0.115516</td>
      <td>0.107830</td>
      <td>0.102923</td>
      <td>0.147572</td>
      <td>0.167433</td>
      <td>0.163516</td>
      <td>0.189891</td>
      <td>0.190763</td>
      <td>0.108863</td>
      <td>0.125681</td>
      <td>0.102947</td>
      <td>0.109811</td>
      <td>0.197714</td>
      <td>0.194164</td>
      <td>0.174982</td>
      <td>0.893806</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1773.000000</td>
      <td>-33.000000</td>
      <td>-3.000000</td>
      <td>-92.000000</td>
      <td>-317.000000</td>
      <td>-287.000000</td>
      <td>-4.000000</td>
      <td>49.000000</td>
      <td>-53.000000</td>
      <td>-277.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2760.000000</td>
      <td>60.000000</td>
      <td>9.000000</td>
      <td>110.000000</td>
      <td>4.000000</td>
      <td>822.000000</td>
      <td>198.000000</td>
      <td>210.000000</td>
      <td>115.000000</td>
      <td>781.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2966.000000</td>
      <td>123.000000</td>
      <td>14.000000</td>
      <td>213.000000</td>
      <td>31.000000</td>
      <td>1436.000000</td>
      <td>218.000000</td>
      <td>224.000000</td>
      <td>142.000000</td>
      <td>1361.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3217.000000</td>
      <td>247.000000</td>
      <td>20.000000</td>
      <td>361.000000</td>
      <td>78.000000</td>
      <td>2365.000000</td>
      <td>233.000000</td>
      <td>237.000000</td>
      <td>169.000000</td>
      <td>2084.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4383.000000</td>
      <td>407.000000</td>
      <td>64.000000</td>
      <td>1602.000000</td>
      <td>647.000000</td>
      <td>7666.000000</td>
      <td>301.000000</td>
      <td>279.000000</td>
      <td>272.000000</td>
      <td>8075.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>7.000000</td>
    </tr>
  </tbody>
</table>
</div>



# Exploring Test Data

## Quick view of Test Data


```python
test.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Elevation</th>
      <th>Aspect</th>
      <th>Slope</th>
      <th>Horizontal_Distance_To_Hydrology</th>
      <th>Vertical_Distance_To_Hydrology</th>
      <th>Horizontal_Distance_To_Roadways</th>
      <th>Hillshade_9am</th>
      <th>Hillshade_Noon</th>
      <th>Hillshade_3pm</th>
      <th>Horizontal_Distance_To_Fire_Points</th>
      <th>Wilderness_Area1</th>
      <th>Wilderness_Area2</th>
      <th>Wilderness_Area3</th>
      <th>Wilderness_Area4</th>
      <th>Soil_Type1</th>
      <th>Soil_Type2</th>
      <th>Soil_Type3</th>
      <th>Soil_Type4</th>
      <th>Soil_Type5</th>
      <th>Soil_Type6</th>
      <th>Soil_Type7</th>
      <th>Soil_Type8</th>
      <th>Soil_Type9</th>
      <th>Soil_Type10</th>
      <th>Soil_Type11</th>
      <th>Soil_Type12</th>
      <th>Soil_Type13</th>
      <th>Soil_Type14</th>
      <th>Soil_Type15</th>
      <th>Soil_Type16</th>
      <th>Soil_Type17</th>
      <th>Soil_Type18</th>
      <th>Soil_Type19</th>
      <th>Soil_Type20</th>
      <th>Soil_Type21</th>
      <th>Soil_Type22</th>
      <th>Soil_Type23</th>
      <th>Soil_Type24</th>
      <th>Soil_Type25</th>
      <th>Soil_Type26</th>
      <th>Soil_Type27</th>
      <th>Soil_Type28</th>
      <th>Soil_Type29</th>
      <th>Soil_Type30</th>
      <th>Soil_Type31</th>
      <th>Soil_Type32</th>
      <th>Soil_Type33</th>
      <th>Soil_Type34</th>
      <th>Soil_Type35</th>
      <th>Soil_Type36</th>
      <th>Soil_Type37</th>
      <th>Soil_Type38</th>
      <th>Soil_Type39</th>
      <th>Soil_Type40</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2763</td>
      <td>78</td>
      <td>20</td>
      <td>377</td>
      <td>88</td>
      <td>3104</td>
      <td>218</td>
      <td>213</td>
      <td>195</td>
      <td>1931</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2826</td>
      <td>153</td>
      <td>11</td>
      <td>264</td>
      <td>39</td>
      <td>295</td>
      <td>219</td>
      <td>238</td>
      <td>148</td>
      <td>2557</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2948</td>
      <td>57</td>
      <td>19</td>
      <td>56</td>
      <td>44</td>
      <td>852</td>
      <td>202</td>
      <td>217</td>
      <td>163</td>
      <td>1803</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2926</td>
      <td>119</td>
      <td>6</td>
      <td>158</td>
      <td>134</td>
      <td>2136</td>
      <td>234</td>
      <td>240</td>
      <td>142</td>
      <td>857</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2690</td>
      <td>10</td>
      <td>4</td>
      <td>38</td>
      <td>108</td>
      <td>3589</td>
      <td>213</td>
      <td>221</td>
      <td>229</td>
      <td>431</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(f'Number of rows in test data: {test.shape[0]}')
print(f'Number of columns in test data: {test.shape[1]}')
print(f'No of missing values in test data: {sum(test.isna().sum())}')
```

    Number of rows in test data: 1000000
    Number of columns in test data: 54
    No of missing values in test data: 0
    

<a id="3.3"></a>
# Submission File


```python
submission.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>Cover_Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4000000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4000001</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4000002</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4000003</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4000004</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



<a id="4"></a>
# EDA

## Overview of Data


```python
train.iloc[:, :-1].describe().T.sort_values(by='std' , ascending = False)\
                     .style.background_gradient(cmap='turbo')\
                     .bar(subset=["max"], color='#3296B1')\
                     .bar(subset=["mean"], color='#1B71B1')\
```




<style type="text/css">
#T_99a36_row0_col0, #T_99a36_row1_col0, #T_99a36_row2_col0, #T_99a36_row3_col0, #T_99a36_row4_col0, #T_99a36_row5_col0, #T_99a36_row5_col3, #T_99a36_row5_col4, #T_99a36_row6_col0, #T_99a36_row7_col0, #T_99a36_row8_col0, #T_99a36_row9_col0, #T_99a36_row9_col4, #T_99a36_row10_col0, #T_99a36_row10_col2, #T_99a36_row10_col4, #T_99a36_row10_col5, #T_99a36_row10_col6, #T_99a36_row11_col0, #T_99a36_row11_col2, #T_99a36_row11_col4, #T_99a36_row11_col5, #T_99a36_row11_col6, #T_99a36_row12_col0, #T_99a36_row12_col2, #T_99a36_row12_col4, #T_99a36_row12_col5, #T_99a36_row12_col6, #T_99a36_row13_col0, #T_99a36_row13_col2, #T_99a36_row13_col4, #T_99a36_row13_col5, #T_99a36_row13_col6, #T_99a36_row14_col0, #T_99a36_row14_col2, #T_99a36_row14_col4, #T_99a36_row14_col5, #T_99a36_row14_col6, #T_99a36_row15_col0, #T_99a36_row15_col2, #T_99a36_row15_col4, #T_99a36_row15_col5, #T_99a36_row15_col6, #T_99a36_row16_col0, #T_99a36_row16_col2, #T_99a36_row16_col4, #T_99a36_row16_col5, #T_99a36_row16_col6, #T_99a36_row17_col0, #T_99a36_row17_col2, #T_99a36_row17_col4, #T_99a36_row17_col5, #T_99a36_row17_col6, #T_99a36_row18_col0, #T_99a36_row18_col2, #T_99a36_row18_col4, #T_99a36_row18_col5, #T_99a36_row18_col6, #T_99a36_row19_col0, #T_99a36_row19_col2, #T_99a36_row19_col4, #T_99a36_row19_col5, #T_99a36_row19_col6, #T_99a36_row20_col0, #T_99a36_row20_col2, #T_99a36_row20_col4, #T_99a36_row20_col5, #T_99a36_row20_col6, #T_99a36_row21_col0, #T_99a36_row21_col2, #T_99a36_row21_col4, #T_99a36_row21_col5, #T_99a36_row21_col6, #T_99a36_row22_col0, #T_99a36_row22_col2, #T_99a36_row22_col4, #T_99a36_row22_col5, #T_99a36_row22_col6, #T_99a36_row23_col0, #T_99a36_row23_col2, #T_99a36_row23_col4, #T_99a36_row23_col5, #T_99a36_row23_col6, #T_99a36_row24_col0, #T_99a36_row24_col2, #T_99a36_row24_col4, #T_99a36_row24_col5, #T_99a36_row24_col6, #T_99a36_row25_col0, #T_99a36_row25_col2, #T_99a36_row25_col4, #T_99a36_row25_col5, #T_99a36_row25_col6, #T_99a36_row26_col0, #T_99a36_row26_col2, #T_99a36_row26_col4, #T_99a36_row26_col5, #T_99a36_row26_col6, #T_99a36_row27_col0, #T_99a36_row27_col2, #T_99a36_row27_col4, #T_99a36_row27_col5, #T_99a36_row27_col6, #T_99a36_row28_col0, #T_99a36_row28_col2, #T_99a36_row28_col4, #T_99a36_row28_col5, #T_99a36_row28_col6, #T_99a36_row29_col0, #T_99a36_row29_col2, #T_99a36_row29_col4, #T_99a36_row29_col5, #T_99a36_row29_col6, #T_99a36_row30_col0, #T_99a36_row30_col2, #T_99a36_row30_col4, #T_99a36_row30_col5, #T_99a36_row30_col6, #T_99a36_row31_col0, #T_99a36_row31_col2, #T_99a36_row31_col4, #T_99a36_row31_col5, #T_99a36_row31_col6, #T_99a36_row32_col0, #T_99a36_row32_col2, #T_99a36_row32_col4, #T_99a36_row32_col5, #T_99a36_row32_col6, #T_99a36_row33_col0, #T_99a36_row33_col2, #T_99a36_row33_col4, #T_99a36_row33_col5, #T_99a36_row33_col6, #T_99a36_row34_col0, #T_99a36_row34_col2, #T_99a36_row34_col4, #T_99a36_row34_col5, #T_99a36_row34_col6, #T_99a36_row35_col0, #T_99a36_row35_col2, #T_99a36_row35_col4, #T_99a36_row35_col5, #T_99a36_row35_col6, #T_99a36_row36_col0, #T_99a36_row36_col2, #T_99a36_row36_col4, #T_99a36_row36_col5, #T_99a36_row36_col6, #T_99a36_row37_col0, #T_99a36_row37_col2, #T_99a36_row37_col4, #T_99a36_row37_col5, #T_99a36_row37_col6, #T_99a36_row38_col0, #T_99a36_row38_col2, #T_99a36_row38_col4, #T_99a36_row38_col5, #T_99a36_row38_col6, #T_99a36_row39_col0, #T_99a36_row39_col2, #T_99a36_row39_col4, #T_99a36_row39_col5, #T_99a36_row39_col6, #T_99a36_row40_col0, #T_99a36_row40_col2, #T_99a36_row40_col4, #T_99a36_row40_col5, #T_99a36_row40_col6, #T_99a36_row41_col0, #T_99a36_row41_col2, #T_99a36_row41_col4, #T_99a36_row41_col5, #T_99a36_row41_col6, #T_99a36_row42_col0, #T_99a36_row42_col2, #T_99a36_row42_col4, #T_99a36_row42_col5, #T_99a36_row42_col6, #T_99a36_row43_col0, #T_99a36_row43_col2, #T_99a36_row43_col4, #T_99a36_row43_col5, #T_99a36_row43_col6, #T_99a36_row44_col0, #T_99a36_row44_col2, #T_99a36_row44_col4, #T_99a36_row44_col5, #T_99a36_row44_col6, #T_99a36_row45_col0, #T_99a36_row45_col2, #T_99a36_row45_col4, #T_99a36_row45_col5, #T_99a36_row45_col6, #T_99a36_row46_col0, #T_99a36_row46_col2, #T_99a36_row46_col4, #T_99a36_row46_col5, #T_99a36_row46_col6, #T_99a36_row47_col0, #T_99a36_row47_col2, #T_99a36_row47_col4, #T_99a36_row47_col5, #T_99a36_row47_col6, #T_99a36_row48_col0, #T_99a36_row48_col2, #T_99a36_row48_col4, #T_99a36_row48_col5, #T_99a36_row48_col6, #T_99a36_row49_col0, #T_99a36_row49_col2, #T_99a36_row49_col4, #T_99a36_row49_col5, #T_99a36_row49_col6, #T_99a36_row50_col0, #T_99a36_row50_col2, #T_99a36_row50_col4, #T_99a36_row50_col5, #T_99a36_row50_col6, #T_99a36_row51_col0, #T_99a36_row51_col2, #T_99a36_row51_col4, #T_99a36_row51_col5, #T_99a36_row51_col6, #T_99a36_row52_col0, #T_99a36_row52_col2, #T_99a36_row52_col4, #T_99a36_row52_col5, #T_99a36_row52_col6, #T_99a36_row53_col0, #T_99a36_row53_col2, #T_99a36_row53_col4, #T_99a36_row53_col5, #T_99a36_row53_col6 {
  background-color: #30123b;
  color: #f1f1f1;
}
#T_99a36_row0_col1 {
  background-color: #dde037;
  color: #000000;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#1B71B1 59.3%, transparent 59.3%);
}
#T_99a36_row0_col2, #T_99a36_row2_col3, #T_99a36_row2_col4, #T_99a36_row2_col5, #T_99a36_row2_col6 {
  background-color: #7a0403;
  color: #f1f1f1;
}
#T_99a36_row0_col3 {
  background-color: #341b51;
  color: #f1f1f1;
}
#T_99a36_row0_col4 {
  background-color: #19d5cd;
  color: #000000;
}
#T_99a36_row0_col5 {
  background-color: #96fe44;
  color: #000000;
}
#T_99a36_row0_col6 {
  background-color: #fd8a26;
  color: #f1f1f1;
}
#T_99a36_row0_col7 {
  background-color: #a11201;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#3296B1 94.9%, transparent 94.9%);
}
#T_99a36_row1_col1 {
  background-color: #b7f735;
  color: #000000;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#1B71B1 53.1%, transparent 53.1%);
}
#T_99a36_row1_col2 {
  background-color: #da3907;
  color: #f1f1f1;
}
#T_99a36_row1_col3, #T_99a36_row8_col2 {
  background-color: #351e58;
  color: #f1f1f1;
}
#T_99a36_row1_col4 {
  background-color: #1ccdd8;
  color: #000000;
}
#T_99a36_row1_col5 {
  background-color: #80ff53;
  color: #000000;
}
#T_99a36_row1_col6 {
  background-color: #f5c53a;
  color: #000000;
}
#T_99a36_row1_col7 {
  background-color: #7a0403;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#3296B1 100.0%, transparent 100.0%);
}
#T_99a36_row2_col1 {
  background-color: #7a0403;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#1B71B1 100.0%, transparent 100.0%);
}
#T_99a36_row2_col2 {
  background-color: #37a8fa;
  color: #f1f1f1;
}
#T_99a36_row2_col7 {
  background-color: #bef434;
  color: #000000;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#3296B1 54.3%, transparent 54.3%);
}
#T_99a36_row3_col1 {
  background-color: #4454c3;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#1B71B1 9.1%, transparent 9.1%);
}
#T_99a36_row3_col2, #T_99a36_row8_col3 {
  background-color: #458afc;
  color: #f1f1f1;
}
#T_99a36_row3_col3 {
  background-color: #455ed3;
  color: #f1f1f1;
}
#T_99a36_row3_col4, #T_99a36_row4_col5, #T_99a36_row6_col4 {
  background-color: #3b2f80;
  color: #f1f1f1;
}
#T_99a36_row3_col5, #T_99a36_row7_col4, #T_99a36_row7_col5, #T_99a36_row7_col6, #T_99a36_row8_col6 {
  background-color: #4146ac;
  color: #f1f1f1;
}
#T_99a36_row3_col6 {
  background-color: #4661d6;
  color: #f1f1f1;
}
#T_99a36_row3_col7 {
  background-color: #4099ff;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#3296B1 19.8%, transparent 19.8%);
}
#T_99a36_row4_col1 {
  background-color: #3e3891;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#1B71B1 5.1%, transparent 5.1%);
}
#T_99a36_row4_col2 {
  background-color: #434eba;
  color: #f1f1f1;
}
#T_99a36_row4_col3 {
  background-color: #4771e9;
  color: #f1f1f1;
}
#T_99a36_row4_col4, #T_99a36_row7_col2 {
  background-color: #36215f;
  color: #f1f1f1;
}
#T_99a36_row4_col6, #T_99a36_row8_col4, #T_99a36_row8_col5 {
  background-color: #4249b1;
  color: #f1f1f1;
}
#T_99a36_row4_col7 {
  background-color: #3d358b;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#3296B1 5.0%, transparent 5.0%);
}
#T_99a36_row5_col1 {
  background-color: #351e58;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#1B71B1 1.7%, transparent 1.7%);
}
#T_99a36_row5_col2, #T_99a36_row6_col6 {
  background-color: #3e3891;
  color: #f1f1f1;
}
#T_99a36_row5_col5 {
  background-color: #33184a;
  color: #f1f1f1;
}
#T_99a36_row5_col6 {
  background-color: #372466;
  color: #f1f1f1;
}
#T_99a36_row5_col7 {
  background-color: #424bb5;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#3296B1 8.0%, transparent 8.0%);
}
#T_99a36_row6_col1 {
  background-color: #3d358b;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#1B71B1 4.7%, transparent 4.7%);
}
#T_99a36_row6_col2 {
  background-color: #392a73;
  color: #f1f1f1;
}
#T_99a36_row6_col3 {
  background-color: #466be3;
  color: #f1f1f1;
}
#T_99a36_row6_col5 {
  background-color: #3d358b;
  color: #f1f1f1;
}
#T_99a36_row6_col7 {
  background-color: #392a73;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#3296B1 3.4%, transparent 3.4%);
}
#T_99a36_row7_col1 {
  background-color: #4146ac;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#1B71B1 7.1%, transparent 7.1%);
}
#T_99a36_row7_col3, #T_99a36_row9_col3, #T_99a36_row10_col3, #T_99a36_row11_col3, #T_99a36_row12_col3, #T_99a36_row13_col3, #T_99a36_row14_col3, #T_99a36_row15_col3, #T_99a36_row16_col3, #T_99a36_row17_col3, #T_99a36_row18_col3, #T_99a36_row19_col3, #T_99a36_row20_col3, #T_99a36_row21_col3, #T_99a36_row22_col3, #T_99a36_row23_col3, #T_99a36_row24_col3, #T_99a36_row25_col3, #T_99a36_row26_col3, #T_99a36_row27_col3, #T_99a36_row28_col3, #T_99a36_row29_col3, #T_99a36_row30_col3, #T_99a36_row31_col3, #T_99a36_row32_col3, #T_99a36_row33_col3, #T_99a36_row34_col3, #T_99a36_row35_col3, #T_99a36_row36_col3, #T_99a36_row37_col3, #T_99a36_row38_col3, #T_99a36_row39_col3, #T_99a36_row40_col3, #T_99a36_row41_col3, #T_99a36_row42_col3, #T_99a36_row43_col3, #T_99a36_row44_col3, #T_99a36_row45_col3, #T_99a36_row46_col3, #T_99a36_row47_col3, #T_99a36_row48_col3, #T_99a36_row49_col3, #T_99a36_row50_col3, #T_99a36_row51_col3, #T_99a36_row52_col3, #T_99a36_row53_col3 {
  background-color: #477bf2;
  color: #f1f1f1;
}
#T_99a36_row7_col7 {
  background-color: #3a2d79;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#3296B1 3.7%, transparent 3.7%);
}
#T_99a36_row8_col1 {
  background-color: #4146ac;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#1B71B1 7.4%, transparent 7.4%);
}
#T_99a36_row8_col7 {
  background-color: #392a73;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#3296B1 3.5%, transparent 3.5%);
}
#T_99a36_row9_col1 {
  background-color: #321543;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#1B71B1 0.5%, transparent 0.5%);
}
#T_99a36_row9_col2, #T_99a36_row9_col5, #T_99a36_row9_col6 {
  background-color: #321543;
  color: #f1f1f1;
}
#T_99a36_row9_col7 {
  background-color: #33184a;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#3296B1 0.8%, transparent 0.8%);
}
#T_99a36_row10_col1, #T_99a36_row11_col1, #T_99a36_row12_col1, #T_99a36_row13_col1, #T_99a36_row14_col1, #T_99a36_row15_col1, #T_99a36_row16_col1, #T_99a36_row17_col1, #T_99a36_row18_col1, #T_99a36_row19_col1, #T_99a36_row20_col1, #T_99a36_row21_col1, #T_99a36_row22_col1, #T_99a36_row23_col1, #T_99a36_row24_col1, #T_99a36_row25_col1, #T_99a36_row26_col1, #T_99a36_row27_col1, #T_99a36_row28_col1, #T_99a36_row29_col1, #T_99a36_row30_col1, #T_99a36_row31_col1, #T_99a36_row32_col1, #T_99a36_row33_col1, #T_99a36_row34_col1, #T_99a36_row35_col1, #T_99a36_row36_col1, #T_99a36_row37_col1, #T_99a36_row38_col1, #T_99a36_row39_col1, #T_99a36_row40_col1, #T_99a36_row41_col1, #T_99a36_row42_col1, #T_99a36_row43_col1, #T_99a36_row44_col1, #T_99a36_row45_col1, #T_99a36_row46_col1, #T_99a36_row47_col1, #T_99a36_row48_col1, #T_99a36_row49_col1, #T_99a36_row50_col1, #T_99a36_row51_col1 {
  background-color: #30123b;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#1B71B1 0.0%, transparent 0.0%);
}
#T_99a36_row10_col7, #T_99a36_row11_col7, #T_99a36_row12_col7, #T_99a36_row13_col7, #T_99a36_row14_col7, #T_99a36_row15_col7, #T_99a36_row16_col7, #T_99a36_row17_col7, #T_99a36_row18_col7, #T_99a36_row19_col7, #T_99a36_row20_col7, #T_99a36_row21_col7, #T_99a36_row22_col7, #T_99a36_row23_col7, #T_99a36_row24_col7, #T_99a36_row25_col7, #T_99a36_row26_col7, #T_99a36_row27_col7, #T_99a36_row28_col7, #T_99a36_row29_col7, #T_99a36_row30_col7, #T_99a36_row31_col7, #T_99a36_row32_col7, #T_99a36_row33_col7, #T_99a36_row34_col7, #T_99a36_row35_col7, #T_99a36_row36_col7, #T_99a36_row37_col7, #T_99a36_row38_col7, #T_99a36_row39_col7, #T_99a36_row40_col7, #T_99a36_row41_col7, #T_99a36_row42_col7, #T_99a36_row43_col7, #T_99a36_row44_col7, #T_99a36_row45_col7, #T_99a36_row46_col7, #T_99a36_row47_col7, #T_99a36_row48_col7, #T_99a36_row49_col7, #T_99a36_row50_col7, #T_99a36_row51_col7 {
  background-color: #30123b;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#3296B1 0.0%, transparent 0.0%);
}
#T_99a36_row52_col1, #T_99a36_row52_col7, #T_99a36_row53_col1, #T_99a36_row53_col7 {
  background-color: #30123b;
  color: #f1f1f1;
  width: 10em;
  height: 80%;
}
</style>
<table id="T_99a36_">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th class="col_heading level0 col0" >count</th>
      <th class="col_heading level0 col1" >mean</th>
      <th class="col_heading level0 col2" >std</th>
      <th class="col_heading level0 col3" >min</th>
      <th class="col_heading level0 col4" >25%</th>
      <th class="col_heading level0 col5" >50%</th>
      <th class="col_heading level0 col6" >75%</th>
      <th class="col_heading level0 col7" >max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_99a36_level0_row0" class="row_heading level0 row0" >Horizontal_Distance_To_Roadways</th>
      <td id="T_99a36_row0_col0" class="data row0 col0" >4000000.000000</td>
      <td id="T_99a36_row0_col1" class="data row0 col1" >1766.641630</td>
      <td id="T_99a36_row0_col2" class="data row0 col2" >1315.609890</td>
      <td id="T_99a36_row0_col3" class="data row0 col3" >-287.000000</td>
      <td id="T_99a36_row0_col4" class="data row0 col4" >822.000000</td>
      <td id="T_99a36_row0_col5" class="data row0 col5" >1436.000000</td>
      <td id="T_99a36_row0_col6" class="data row0 col6" >2365.000000</td>
      <td id="T_99a36_row0_col7" class="data row0 col7" >7666.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row1" class="row_heading level0 row1" >Horizontal_Distance_To_Fire_Points</th>
      <td id="T_99a36_row1_col0" class="data row1 col0" >4000000.000000</td>
      <td id="T_99a36_row1_col1" class="data row1 col1" >1581.406810</td>
      <td id="T_99a36_row1_col2" class="data row1 col2" >1127.616169</td>
      <td id="T_99a36_row1_col3" class="data row1 col3" >-277.000000</td>
      <td id="T_99a36_row1_col4" class="data row1 col4" >781.000000</td>
      <td id="T_99a36_row1_col5" class="data row1 col5" >1361.000000</td>
      <td id="T_99a36_row1_col6" class="data row1 col6" >2084.000000</td>
      <td id="T_99a36_row1_col7" class="data row1 col7" >8075.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row2" class="row_heading level0 row2" >Elevation</th>
      <td id="T_99a36_row2_col0" class="data row2 col0" >4000000.000000</td>
      <td id="T_99a36_row2_col1" class="data row2 col1" >2980.191660</td>
      <td id="T_99a36_row2_col2" class="data row2 col2" >289.048167</td>
      <td id="T_99a36_row2_col3" class="data row2 col3" >1773.000000</td>
      <td id="T_99a36_row2_col4" class="data row2 col4" >2760.000000</td>
      <td id="T_99a36_row2_col5" class="data row2 col5" >2966.000000</td>
      <td id="T_99a36_row2_col6" class="data row2 col6" >3217.000000</td>
      <td id="T_99a36_row2_col7" class="data row2 col7" >4383.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row3" class="row_heading level0 row3" >Horizontal_Distance_To_Hydrology</th>
      <td id="T_99a36_row3_col0" class="data row3 col0" >4000000.000000</td>
      <td id="T_99a36_row3_col1" class="data row3 col1" >271.315436</td>
      <td id="T_99a36_row3_col2" class="data row3 col2" >226.549680</td>
      <td id="T_99a36_row3_col3" class="data row3 col3" >-92.000000</td>
      <td id="T_99a36_row3_col4" class="data row3 col4" >110.000000</td>
      <td id="T_99a36_row3_col5" class="data row3 col5" >213.000000</td>
      <td id="T_99a36_row3_col6" class="data row3 col6" >361.000000</td>
      <td id="T_99a36_row3_col7" class="data row3 col7" >1602.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row4" class="row_heading level0 row4" >Aspect</th>
      <td id="T_99a36_row4_col0" class="data row4 col0" >4000000.000000</td>
      <td id="T_99a36_row4_col1" class="data row4 col1" >151.585671</td>
      <td id="T_99a36_row4_col2" class="data row4 col2" >109.961122</td>
      <td id="T_99a36_row4_col3" class="data row4 col3" >-33.000000</td>
      <td id="T_99a36_row4_col4" class="data row4 col4" >60.000000</td>
      <td id="T_99a36_row4_col5" class="data row4 col5" >123.000000</td>
      <td id="T_99a36_row4_col6" class="data row4 col6" >247.000000</td>
      <td id="T_99a36_row4_col7" class="data row4 col7" >407.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row5" class="row_heading level0 row5" >Vertical_Distance_To_Hydrology</th>
      <td id="T_99a36_row5_col0" class="data row5 col0" >4000000.000000</td>
      <td id="T_99a36_row5_col1" class="data row5 col1" >51.662621</td>
      <td id="T_99a36_row5_col2" class="data row5 col2" >68.215966</td>
      <td id="T_99a36_row5_col3" class="data row5 col3" >-317.000000</td>
      <td id="T_99a36_row5_col4" class="data row5 col4" >4.000000</td>
      <td id="T_99a36_row5_col5" class="data row5 col5" >31.000000</td>
      <td id="T_99a36_row5_col6" class="data row5 col6" >78.000000</td>
      <td id="T_99a36_row5_col7" class="data row5 col7" >647.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row6" class="row_heading level0 row6" >Hillshade_3pm</th>
      <td id="T_99a36_row6_col0" class="data row6 col0" >4000000.000000</td>
      <td id="T_99a36_row6_col1" class="data row6 col1" >140.810874</td>
      <td id="T_99a36_row6_col2" class="data row6 col2" >43.698639</td>
      <td id="T_99a36_row6_col3" class="data row6 col3" >-53.000000</td>
      <td id="T_99a36_row6_col4" class="data row6 col4" >115.000000</td>
      <td id="T_99a36_row6_col5" class="data row6 col5" >142.000000</td>
      <td id="T_99a36_row6_col6" class="data row6 col6" >169.000000</td>
      <td id="T_99a36_row6_col7" class="data row6 col7" >272.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row7" class="row_heading level0 row7" >Hillshade_9am</th>
      <td id="T_99a36_row7_col0" class="data row7 col0" >4000000.000000</td>
      <td id="T_99a36_row7_col1" class="data row7 col1" >211.837542</td>
      <td id="T_99a36_row7_col2" class="data row7 col2" >30.759956</td>
      <td id="T_99a36_row7_col3" class="data row7 col3" >-4.000000</td>
      <td id="T_99a36_row7_col4" class="data row7 col4" >198.000000</td>
      <td id="T_99a36_row7_col5" class="data row7 col5" >218.000000</td>
      <td id="T_99a36_row7_col6" class="data row7 col6" >233.000000</td>
      <td id="T_99a36_row7_col7" class="data row7 col7" >301.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row8" class="row_heading level0 row8" >Hillshade_Noon</th>
      <td id="T_99a36_row8_col0" class="data row8 col0" >4000000.000000</td>
      <td id="T_99a36_row8_col1" class="data row8 col1" >221.061441</td>
      <td id="T_99a36_row8_col2" class="data row8 col2" >22.231335</td>
      <td id="T_99a36_row8_col3" class="data row8 col3" >49.000000</td>
      <td id="T_99a36_row8_col4" class="data row8 col4" >210.000000</td>
      <td id="T_99a36_row8_col5" class="data row8 col5" >224.000000</td>
      <td id="T_99a36_row8_col6" class="data row8 col6" >237.000000</td>
      <td id="T_99a36_row8_col7" class="data row8 col7" >279.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row9" class="row_heading level0 row9" >Slope</th>
      <td id="T_99a36_row9_col0" class="data row9 col0" >4000000.000000</td>
      <td id="T_99a36_row9_col1" class="data row9 col1" >15.097537</td>
      <td id="T_99a36_row9_col2" class="data row9 col2" >8.546731</td>
      <td id="T_99a36_row9_col3" class="data row9 col3" >-3.000000</td>
      <td id="T_99a36_row9_col4" class="data row9 col4" >9.000000</td>
      <td id="T_99a36_row9_col5" class="data row9 col5" >14.000000</td>
      <td id="T_99a36_row9_col6" class="data row9 col6" >20.000000</td>
      <td id="T_99a36_row9_col7" class="data row9 col7" >64.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row10" class="row_heading level0 row10" >Wilderness_Area3</th>
      <td id="T_99a36_row10_col0" class="data row10 col0" >4000000.000000</td>
      <td id="T_99a36_row10_col1" class="data row10 col1" >0.653573</td>
      <td id="T_99a36_row10_col2" class="data row10 col2" >0.475831</td>
      <td id="T_99a36_row10_col3" class="data row10 col3" >0.000000</td>
      <td id="T_99a36_row10_col4" class="data row10 col4" >0.000000</td>
      <td id="T_99a36_row10_col5" class="data row10 col5" >1.000000</td>
      <td id="T_99a36_row10_col6" class="data row10 col6" >1.000000</td>
      <td id="T_99a36_row10_col7" class="data row10 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row11" class="row_heading level0 row11" >Wilderness_Area1</th>
      <td id="T_99a36_row11_col0" class="data row11 col0" >4000000.000000</td>
      <td id="T_99a36_row11_col1" class="data row11 col1" >0.261193</td>
      <td id="T_99a36_row11_col2" class="data row11 col2" >0.439285</td>
      <td id="T_99a36_row11_col3" class="data row11 col3" >0.000000</td>
      <td id="T_99a36_row11_col4" class="data row11 col4" >0.000000</td>
      <td id="T_99a36_row11_col5" class="data row11 col5" >0.000000</td>
      <td id="T_99a36_row11_col6" class="data row11 col6" >1.000000</td>
      <td id="T_99a36_row11_col7" class="data row11 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row12" class="row_heading level0 row12" >Soil_Type10</th>
      <td id="T_99a36_row12_col0" class="data row12 col0" >4000000.000000</td>
      <td id="T_99a36_row12_col1" class="data row12 col1" >0.054541</td>
      <td id="T_99a36_row12_col2" class="data row12 col2" >0.227082</td>
      <td id="T_99a36_row12_col3" class="data row12 col3" >0.000000</td>
      <td id="T_99a36_row12_col4" class="data row12 col4" >0.000000</td>
      <td id="T_99a36_row12_col5" class="data row12 col5" >0.000000</td>
      <td id="T_99a36_row12_col6" class="data row12 col6" >0.000000</td>
      <td id="T_99a36_row12_col7" class="data row12 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row13" class="row_heading level0 row13" >Soil_Type23</th>
      <td id="T_99a36_row13_col0" class="data row13 col0" >4000000.000000</td>
      <td id="T_99a36_row13_col1" class="data row13 col1" >0.049171</td>
      <td id="T_99a36_row13_col2" class="data row13 col2" >0.216224</td>
      <td id="T_99a36_row13_col3" class="data row13 col3" >0.000000</td>
      <td id="T_99a36_row13_col4" class="data row13 col4" >0.000000</td>
      <td id="T_99a36_row13_col5" class="data row13 col5" >0.000000</td>
      <td id="T_99a36_row13_col6" class="data row13 col6" >0.000000</td>
      <td id="T_99a36_row13_col7" class="data row13 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row14" class="row_heading level0 row14" >Wilderness_Area2</th>
      <td id="T_99a36_row14_col0" class="data row14 col0" >4000000.000000</td>
      <td id="T_99a36_row14_col1" class="data row14 col1" >0.041661</td>
      <td id="T_99a36_row14_col2" class="data row14 col2" >0.199813</td>
      <td id="T_99a36_row14_col3" class="data row14 col3" >0.000000</td>
      <td id="T_99a36_row14_col4" class="data row14 col4" >0.000000</td>
      <td id="T_99a36_row14_col5" class="data row14 col5" >0.000000</td>
      <td id="T_99a36_row14_col6" class="data row14 col6" >0.000000</td>
      <td id="T_99a36_row14_col7" class="data row14 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row15" class="row_heading level0 row15" >Soil_Type38</th>
      <td id="T_99a36_row15_col0" class="data row15 col0" >4000000.000000</td>
      <td id="T_99a36_row15_col1" class="data row15 col1" >0.040752</td>
      <td id="T_99a36_row15_col2" class="data row15 col2" >0.197714</td>
      <td id="T_99a36_row15_col3" class="data row15 col3" >0.000000</td>
      <td id="T_99a36_row15_col4" class="data row15 col4" >0.000000</td>
      <td id="T_99a36_row15_col5" class="data row15 col5" >0.000000</td>
      <td id="T_99a36_row15_col6" class="data row15 col6" >0.000000</td>
      <td id="T_99a36_row15_col7" class="data row15 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row16" class="row_heading level0 row16" >Soil_Type39</th>
      <td id="T_99a36_row16_col0" class="data row16 col0" >4000000.000000</td>
      <td id="T_99a36_row16_col1" class="data row16 col1" >0.039239</td>
      <td id="T_99a36_row16_col2" class="data row16 col2" >0.194164</td>
      <td id="T_99a36_row16_col3" class="data row16 col3" >0.000000</td>
      <td id="T_99a36_row16_col4" class="data row16 col4" >0.000000</td>
      <td id="T_99a36_row16_col5" class="data row16 col5" >0.000000</td>
      <td id="T_99a36_row16_col6" class="data row16 col6" >0.000000</td>
      <td id="T_99a36_row16_col7" class="data row16 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row17" class="row_heading level0 row17" >Soil_Type4</th>
      <td id="T_99a36_row17_col0" class="data row17 col0" >4000000.000000</td>
      <td id="T_99a36_row17_col1" class="data row17 col1" >0.037913</td>
      <td id="T_99a36_row17_col2" class="data row17 col2" >0.190985</td>
      <td id="T_99a36_row17_col3" class="data row17 col3" >0.000000</td>
      <td id="T_99a36_row17_col4" class="data row17 col4" >0.000000</td>
      <td id="T_99a36_row17_col5" class="data row17 col5" >0.000000</td>
      <td id="T_99a36_row17_col6" class="data row17 col6" >0.000000</td>
      <td id="T_99a36_row17_col7" class="data row17 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row18" class="row_heading level0 row18" >Soil_Type33</th>
      <td id="T_99a36_row18_col0" class="data row18 col0" >4000000.000000</td>
      <td id="T_99a36_row18_col1" class="data row18 col1" >0.037821</td>
      <td id="T_99a36_row18_col2" class="data row18 col2" >0.190763</td>
      <td id="T_99a36_row18_col3" class="data row18 col3" >0.000000</td>
      <td id="T_99a36_row18_col4" class="data row18 col4" >0.000000</td>
      <td id="T_99a36_row18_col5" class="data row18 col5" >0.000000</td>
      <td id="T_99a36_row18_col6" class="data row18 col6" >0.000000</td>
      <td id="T_99a36_row18_col7" class="data row18 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row19" class="row_heading level0 row19" >Soil_Type32</th>
      <td id="T_99a36_row19_col0" class="data row19 col0" >4000000.000000</td>
      <td id="T_99a36_row19_col1" class="data row19 col1" >0.037462</td>
      <td id="T_99a36_row19_col2" class="data row19 col2" >0.189891</td>
      <td id="T_99a36_row19_col3" class="data row19 col3" >0.000000</td>
      <td id="T_99a36_row19_col4" class="data row19 col4" >0.000000</td>
      <td id="T_99a36_row19_col5" class="data row19 col5" >0.000000</td>
      <td id="T_99a36_row19_col6" class="data row19 col6" >0.000000</td>
      <td id="T_99a36_row19_col7" class="data row19 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row20" class="row_heading level0 row20" >Soil_Type40</th>
      <td id="T_99a36_row20_col0" class="data row20 col0" >4000000.000000</td>
      <td id="T_99a36_row20_col1" class="data row20 col1" >0.031619</td>
      <td id="T_99a36_row20_col2" class="data row20 col2" >0.174982</td>
      <td id="T_99a36_row20_col3" class="data row20 col3" >0.000000</td>
      <td id="T_99a36_row20_col4" class="data row20 col4" >0.000000</td>
      <td id="T_99a36_row20_col5" class="data row20 col5" >0.000000</td>
      <td id="T_99a36_row20_col6" class="data row20 col6" >0.000000</td>
      <td id="T_99a36_row20_col7" class="data row20 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row21" class="row_heading level0 row21" >Soil_Type22</th>
      <td id="T_99a36_row21_col0" class="data row21 col0" >4000000.000000</td>
      <td id="T_99a36_row21_col1" class="data row21 col1" >0.031346</td>
      <td id="T_99a36_row21_col2" class="data row21 col2" >0.174251</td>
      <td id="T_99a36_row21_col3" class="data row21 col3" >0.000000</td>
      <td id="T_99a36_row21_col4" class="data row21 col4" >0.000000</td>
      <td id="T_99a36_row21_col5" class="data row21 col5" >0.000000</td>
      <td id="T_99a36_row21_col6" class="data row21 col6" >0.000000</td>
      <td id="T_99a36_row21_col7" class="data row21 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row22" class="row_heading level0 row22" >Soil_Type13</th>
      <td id="T_99a36_row22_col0" class="data row22 col0" >4000000.000000</td>
      <td id="T_99a36_row22_col1" class="data row22 col1" >0.031295</td>
      <td id="T_99a36_row22_col2" class="data row22 col2" >0.174115</td>
      <td id="T_99a36_row22_col3" class="data row22 col3" >0.000000</td>
      <td id="T_99a36_row22_col4" class="data row22 col4" >0.000000</td>
      <td id="T_99a36_row22_col5" class="data row22 col5" >0.000000</td>
      <td id="T_99a36_row22_col6" class="data row22 col6" >0.000000</td>
      <td id="T_99a36_row22_col7" class="data row22 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row23" class="row_heading level0 row23" >Soil_Type2</th>
      <td id="T_99a36_row23_col0" class="data row23 col0" >4000000.000000</td>
      <td id="T_99a36_row23_col1" class="data row23 col1" >0.030896</td>
      <td id="T_99a36_row23_col2" class="data row23 col2" >0.173036</td>
      <td id="T_99a36_row23_col3" class="data row23 col3" >0.000000</td>
      <td id="T_99a36_row23_col4" class="data row23 col4" >0.000000</td>
      <td id="T_99a36_row23_col5" class="data row23 col5" >0.000000</td>
      <td id="T_99a36_row23_col6" class="data row23 col6" >0.000000</td>
      <td id="T_99a36_row23_col7" class="data row23 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row24" class="row_heading level0 row24" >Soil_Type30</th>
      <td id="T_99a36_row24_col0" class="data row24 col0" >4000000.000000</td>
      <td id="T_99a36_row24_col1" class="data row24 col1" >0.028867</td>
      <td id="T_99a36_row24_col2" class="data row24 col2" >0.167433</td>
      <td id="T_99a36_row24_col3" class="data row24 col3" >0.000000</td>
      <td id="T_99a36_row24_col4" class="data row24 col4" >0.000000</td>
      <td id="T_99a36_row24_col5" class="data row24 col5" >0.000000</td>
      <td id="T_99a36_row24_col6" class="data row24 col6" >0.000000</td>
      <td id="T_99a36_row24_col7" class="data row24 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row25" class="row_heading level0 row25" >Soil_Type11</th>
      <td id="T_99a36_row25_col0" class="data row25 col0" >4000000.000000</td>
      <td id="T_99a36_row25_col1" class="data row25 col1" >0.027985</td>
      <td id="T_99a36_row25_col2" class="data row25 col2" >0.164931</td>
      <td id="T_99a36_row25_col3" class="data row25 col3" >0.000000</td>
      <td id="T_99a36_row25_col4" class="data row25 col4" >0.000000</td>
      <td id="T_99a36_row25_col5" class="data row25 col5" >0.000000</td>
      <td id="T_99a36_row25_col6" class="data row25 col6" >0.000000</td>
      <td id="T_99a36_row25_col7" class="data row25 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row26" class="row_heading level0 row26" >Soil_Type31</th>
      <td id="T_99a36_row26_col0" class="data row26 col0" >4000000.000000</td>
      <td id="T_99a36_row26_col1" class="data row26 col1" >0.027493</td>
      <td id="T_99a36_row26_col2" class="data row26 col2" >0.163516</td>
      <td id="T_99a36_row26_col3" class="data row26 col3" >0.000000</td>
      <td id="T_99a36_row26_col4" class="data row26 col4" >0.000000</td>
      <td id="T_99a36_row26_col5" class="data row26 col5" >0.000000</td>
      <td id="T_99a36_row26_col6" class="data row26 col6" >0.000000</td>
      <td id="T_99a36_row26_col7" class="data row26 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row27" class="row_heading level0 row27" >Soil_Type24</th>
      <td id="T_99a36_row27_col0" class="data row27 col0" >4000000.000000</td>
      <td id="T_99a36_row27_col1" class="data row27 col1" >0.025022</td>
      <td id="T_99a36_row27_col2" class="data row27 col2" >0.156191</td>
      <td id="T_99a36_row27_col3" class="data row27 col3" >0.000000</td>
      <td id="T_99a36_row27_col4" class="data row27 col4" >0.000000</td>
      <td id="T_99a36_row27_col5" class="data row27 col5" >0.000000</td>
      <td id="T_99a36_row27_col6" class="data row27 col6" >0.000000</td>
      <td id="T_99a36_row27_col7" class="data row27 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row28" class="row_heading level0 row28" >Soil_Type29</th>
      <td id="T_99a36_row28_col0" class="data row28 col0" >4000000.000000</td>
      <td id="T_99a36_row28_col1" class="data row28 col1" >0.022274</td>
      <td id="T_99a36_row28_col2" class="data row28 col2" >0.147572</td>
      <td id="T_99a36_row28_col3" class="data row28 col3" >0.000000</td>
      <td id="T_99a36_row28_col4" class="data row28 col4" >0.000000</td>
      <td id="T_99a36_row28_col5" class="data row28 col5" >0.000000</td>
      <td id="T_99a36_row28_col6" class="data row28 col6" >0.000000</td>
      <td id="T_99a36_row28_col7" class="data row28 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row29" class="row_heading level0 row29" >Wilderness_Area4</th>
      <td id="T_99a36_row29_col0" class="data row29 col0" >4000000.000000</td>
      <td id="T_99a36_row29_col1" class="data row29 col1" >0.021819</td>
      <td id="T_99a36_row29_col2" class="data row29 col2" >0.146092</td>
      <td id="T_99a36_row29_col3" class="data row29 col3" >0.000000</td>
      <td id="T_99a36_row29_col4" class="data row29 col4" >0.000000</td>
      <td id="T_99a36_row29_col5" class="data row29 col5" >0.000000</td>
      <td id="T_99a36_row29_col6" class="data row29 col6" >0.000000</td>
      <td id="T_99a36_row29_col7" class="data row29 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row30" class="row_heading level0 row30" >Soil_Type17</th>
      <td id="T_99a36_row30_col0" class="data row30 col0" >4000000.000000</td>
      <td id="T_99a36_row30_col1" class="data row30 col1" >0.020672</td>
      <td id="T_99a36_row30_col2" class="data row30 col2" >0.142283</td>
      <td id="T_99a36_row30_col3" class="data row30 col3" >0.000000</td>
      <td id="T_99a36_row30_col4" class="data row30 col4" >0.000000</td>
      <td id="T_99a36_row30_col5" class="data row30 col5" >0.000000</td>
      <td id="T_99a36_row30_col6" class="data row30 col6" >0.000000</td>
      <td id="T_99a36_row30_col7" class="data row30 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row31" class="row_heading level0 row31" >Soil_Type12</th>
      <td id="T_99a36_row31_col0" class="data row31 col0" >4000000.000000</td>
      <td id="T_99a36_row31_col1" class="data row31 col1" >0.018290</td>
      <td id="T_99a36_row31_col2" class="data row31 col2" >0.133998</td>
      <td id="T_99a36_row31_col3" class="data row31 col3" >0.000000</td>
      <td id="T_99a36_row31_col4" class="data row31 col4" >0.000000</td>
      <td id="T_99a36_row31_col5" class="data row31 col5" >0.000000</td>
      <td id="T_99a36_row31_col6" class="data row31 col6" >0.000000</td>
      <td id="T_99a36_row31_col7" class="data row31 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row32" class="row_heading level0 row32" >Soil_Type20</th>
      <td id="T_99a36_row32_col0" class="data row32 col0" >4000000.000000</td>
      <td id="T_99a36_row32_col1" class="data row32 col1" >0.017368</td>
      <td id="T_99a36_row32_col2" class="data row32 col2" >0.130638</td>
      <td id="T_99a36_row32_col3" class="data row32 col3" >0.000000</td>
      <td id="T_99a36_row32_col4" class="data row32 col4" >0.000000</td>
      <td id="T_99a36_row32_col5" class="data row32 col5" >0.000000</td>
      <td id="T_99a36_row32_col6" class="data row32 col6" >0.000000</td>
      <td id="T_99a36_row32_col7" class="data row32 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row33" class="row_heading level0 row33" >Soil_Type1</th>
      <td id="T_99a36_row33_col0" class="data row33 col0" >4000000.000000</td>
      <td id="T_99a36_row33_col1" class="data row33 col1" >0.016841</td>
      <td id="T_99a36_row33_col2" class="data row33 col2" >0.128677</td>
      <td id="T_99a36_row33_col3" class="data row33 col3" >0.000000</td>
      <td id="T_99a36_row33_col4" class="data row33 col4" >0.000000</td>
      <td id="T_99a36_row33_col5" class="data row33 col5" >0.000000</td>
      <td id="T_99a36_row33_col6" class="data row33 col6" >0.000000</td>
      <td id="T_99a36_row33_col7" class="data row33 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row34" class="row_heading level0 row34" >Soil_Type35</th>
      <td id="T_99a36_row34_col0" class="data row34 col0" >4000000.000000</td>
      <td id="T_99a36_row34_col1" class="data row34 col1" >0.016053</td>
      <td id="T_99a36_row34_col2" class="data row34 col2" >0.125681</td>
      <td id="T_99a36_row34_col3" class="data row34 col3" >0.000000</td>
      <td id="T_99a36_row34_col4" class="data row34 col4" >0.000000</td>
      <td id="T_99a36_row34_col5" class="data row34 col5" >0.000000</td>
      <td id="T_99a36_row34_col6" class="data row34 col6" >0.000000</td>
      <td id="T_99a36_row34_col7" class="data row34 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row35" class="row_heading level0 row35" >Soil_Type16</th>
      <td id="T_99a36_row35_col0" class="data row35 col0" >4000000.000000</td>
      <td id="T_99a36_row35_col1" class="data row35 col1" >0.015888</td>
      <td id="T_99a36_row35_col2" class="data row35 col2" >0.125044</td>
      <td id="T_99a36_row35_col3" class="data row35 col3" >0.000000</td>
      <td id="T_99a36_row35_col4" class="data row35 col4" >0.000000</td>
      <td id="T_99a36_row35_col5" class="data row35 col5" >0.000000</td>
      <td id="T_99a36_row35_col6" class="data row35 col6" >0.000000</td>
      <td id="T_99a36_row35_col7" class="data row35 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row36" class="row_heading level0 row36" >Soil_Type5</th>
      <td id="T_99a36_row36_col0" class="data row36 col0" >4000000.000000</td>
      <td id="T_99a36_row36_col1" class="data row36 col1" >0.015715</td>
      <td id="T_99a36_row36_col2" class="data row36 col2" >0.124372</td>
      <td id="T_99a36_row36_col3" class="data row36 col3" >0.000000</td>
      <td id="T_99a36_row36_col4" class="data row36 col4" >0.000000</td>
      <td id="T_99a36_row36_col5" class="data row36 col5" >0.000000</td>
      <td id="T_99a36_row36_col6" class="data row36 col6" >0.000000</td>
      <td id="T_99a36_row36_col7" class="data row36 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row37" class="row_heading level0 row37" >Soil_Type14</th>
      <td id="T_99a36_row37_col0" class="data row37 col0" >4000000.000000</td>
      <td id="T_99a36_row37_col1" class="data row37 col1" >0.014977</td>
      <td id="T_99a36_row37_col2" class="data row37 col2" >0.121459</td>
      <td id="T_99a36_row37_col3" class="data row37 col3" >0.000000</td>
      <td id="T_99a36_row37_col4" class="data row37 col4" >0.000000</td>
      <td id="T_99a36_row37_col5" class="data row37 col5" >0.000000</td>
      <td id="T_99a36_row37_col6" class="data row37 col6" >0.000000</td>
      <td id="T_99a36_row37_col7" class="data row37 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row38" class="row_heading level0 row38" >Soil_Type19</th>
      <td id="T_99a36_row38_col0" class="data row38 col0" >4000000.000000</td>
      <td id="T_99a36_row38_col1" class="data row38 col1" >0.013811</td>
      <td id="T_99a36_row38_col2" class="data row38 col2" >0.116707</td>
      <td id="T_99a36_row38_col3" class="data row38 col3" >0.000000</td>
      <td id="T_99a36_row38_col4" class="data row38 col4" >0.000000</td>
      <td id="T_99a36_row38_col5" class="data row38 col5" >0.000000</td>
      <td id="T_99a36_row38_col6" class="data row38 col6" >0.000000</td>
      <td id="T_99a36_row38_col7" class="data row38 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row39" class="row_heading level0 row39" >Soil_Type26</th>
      <td id="T_99a36_row39_col0" class="data row39 col0" >4000000.000000</td>
      <td id="T_99a36_row39_col1" class="data row39 col1" >0.013527</td>
      <td id="T_99a36_row39_col2" class="data row39 col2" >0.115516</td>
      <td id="T_99a36_row39_col3" class="data row39 col3" >0.000000</td>
      <td id="T_99a36_row39_col4" class="data row39 col4" >0.000000</td>
      <td id="T_99a36_row39_col5" class="data row39 col5" >0.000000</td>
      <td id="T_99a36_row39_col6" class="data row39 col6" >0.000000</td>
      <td id="T_99a36_row39_col7" class="data row39 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row40" class="row_heading level0 row40" >Soil_Type18</th>
      <td id="T_99a36_row40_col0" class="data row40 col0" >4000000.000000</td>
      <td id="T_99a36_row40_col1" class="data row40 col1" >0.013436</td>
      <td id="T_99a36_row40_col2" class="data row40 col2" >0.115133</td>
      <td id="T_99a36_row40_col3" class="data row40 col3" >0.000000</td>
      <td id="T_99a36_row40_col4" class="data row40 col4" >0.000000</td>
      <td id="T_99a36_row40_col5" class="data row40 col5" >0.000000</td>
      <td id="T_99a36_row40_col6" class="data row40 col6" >0.000000</td>
      <td id="T_99a36_row40_col7" class="data row40 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row41" class="row_heading level0 row41" >Soil_Type37</th>
      <td id="T_99a36_row41_col0" class="data row41 col0" >4000000.000000</td>
      <td id="T_99a36_row41_col1" class="data row41 col1" >0.012207</td>
      <td id="T_99a36_row41_col2" class="data row41 col2" >0.109811</td>
      <td id="T_99a36_row41_col3" class="data row41 col3" >0.000000</td>
      <td id="T_99a36_row41_col4" class="data row41 col4" >0.000000</td>
      <td id="T_99a36_row41_col5" class="data row41 col5" >0.000000</td>
      <td id="T_99a36_row41_col6" class="data row41 col6" >0.000000</td>
      <td id="T_99a36_row41_col7" class="data row41 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row42" class="row_heading level0 row42" >Soil_Type34</th>
      <td id="T_99a36_row42_col0" class="data row42 col0" >4000000.000000</td>
      <td id="T_99a36_row42_col1" class="data row42 col1" >0.011995</td>
      <td id="T_99a36_row42_col2" class="data row42 col2" >0.108863</td>
      <td id="T_99a36_row42_col3" class="data row42 col3" >0.000000</td>
      <td id="T_99a36_row42_col4" class="data row42 col4" >0.000000</td>
      <td id="T_99a36_row42_col5" class="data row42 col5" >0.000000</td>
      <td id="T_99a36_row42_col6" class="data row42 col6" >0.000000</td>
      <td id="T_99a36_row42_col7" class="data row42 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row43" class="row_heading level0 row43" >Soil_Type27</th>
      <td id="T_99a36_row43_col0" class="data row43 col0" >4000000.000000</td>
      <td id="T_99a36_row43_col1" class="data row43 col1" >0.011766</td>
      <td id="T_99a36_row43_col2" class="data row43 col2" >0.107830</td>
      <td id="T_99a36_row43_col3" class="data row43 col3" >0.000000</td>
      <td id="T_99a36_row43_col4" class="data row43 col4" >0.000000</td>
      <td id="T_99a36_row43_col5" class="data row43 col5" >0.000000</td>
      <td id="T_99a36_row43_col6" class="data row43 col6" >0.000000</td>
      <td id="T_99a36_row43_col7" class="data row43 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row44" class="row_heading level0 row44" >Soil_Type21</th>
      <td id="T_99a36_row44_col0" class="data row44 col0" >4000000.000000</td>
      <td id="T_99a36_row44_col1" class="data row44 col1" >0.011539</td>
      <td id="T_99a36_row44_col2" class="data row44 col2" >0.106798</td>
      <td id="T_99a36_row44_col3" class="data row44 col3" >0.000000</td>
      <td id="T_99a36_row44_col4" class="data row44 col4" >0.000000</td>
      <td id="T_99a36_row44_col5" class="data row44 col5" >0.000000</td>
      <td id="T_99a36_row44_col6" class="data row44 col6" >0.000000</td>
      <td id="T_99a36_row44_col7" class="data row44 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row45" class="row_heading level0 row45" >Soil_Type9</th>
      <td id="T_99a36_row45_col0" class="data row45 col0" >4000000.000000</td>
      <td id="T_99a36_row45_col1" class="data row45 col1" >0.010893</td>
      <td id="T_99a36_row45_col2" class="data row45 col2" >0.103800</td>
      <td id="T_99a36_row45_col3" class="data row45 col3" >0.000000</td>
      <td id="T_99a36_row45_col4" class="data row45 col4" >0.000000</td>
      <td id="T_99a36_row45_col5" class="data row45 col5" >0.000000</td>
      <td id="T_99a36_row45_col6" class="data row45 col6" >0.000000</td>
      <td id="T_99a36_row45_col7" class="data row45 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row46" class="row_heading level0 row46" >Soil_Type36</th>
      <td id="T_99a36_row46_col0" class="data row46 col0" >4000000.000000</td>
      <td id="T_99a36_row46_col1" class="data row46 col1" >0.010713</td>
      <td id="T_99a36_row46_col2" class="data row46 col2" >0.102947</td>
      <td id="T_99a36_row46_col3" class="data row46 col3" >0.000000</td>
      <td id="T_99a36_row46_col4" class="data row46 col4" >0.000000</td>
      <td id="T_99a36_row46_col5" class="data row46 col5" >0.000000</td>
      <td id="T_99a36_row46_col6" class="data row46 col6" >0.000000</td>
      <td id="T_99a36_row46_col7" class="data row46 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row47" class="row_heading level0 row47" >Soil_Type28</th>
      <td id="T_99a36_row47_col0" class="data row47 col0" >4000000.000000</td>
      <td id="T_99a36_row47_col1" class="data row47 col1" >0.010708</td>
      <td id="T_99a36_row47_col2" class="data row47 col2" >0.102923</td>
      <td id="T_99a36_row47_col3" class="data row47 col3" >0.000000</td>
      <td id="T_99a36_row47_col4" class="data row47 col4" >0.000000</td>
      <td id="T_99a36_row47_col5" class="data row47 col5" >0.000000</td>
      <td id="T_99a36_row47_col6" class="data row47 col6" >0.000000</td>
      <td id="T_99a36_row47_col7" class="data row47 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row48" class="row_heading level0 row48" >Soil_Type6</th>
      <td id="T_99a36_row48_col0" class="data row48 col0" >4000000.000000</td>
      <td id="T_99a36_row48_col1" class="data row48 col1" >0.007973</td>
      <td id="T_99a36_row48_col2" class="data row48 col2" >0.088934</td>
      <td id="T_99a36_row48_col3" class="data row48 col3" >0.000000</td>
      <td id="T_99a36_row48_col4" class="data row48 col4" >0.000000</td>
      <td id="T_99a36_row48_col5" class="data row48 col5" >0.000000</td>
      <td id="T_99a36_row48_col6" class="data row48 col6" >0.000000</td>
      <td id="T_99a36_row48_col7" class="data row48 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row49" class="row_heading level0 row49" >Soil_Type3</th>
      <td id="T_99a36_row49_col0" class="data row49 col0" >4000000.000000</td>
      <td id="T_99a36_row49_col1" class="data row49 col1" >0.004275</td>
      <td id="T_99a36_row49_col2" class="data row49 col2" >0.065247</td>
      <td id="T_99a36_row49_col3" class="data row49 col3" >0.000000</td>
      <td id="T_99a36_row49_col4" class="data row49 col4" >0.000000</td>
      <td id="T_99a36_row49_col5" class="data row49 col5" >0.000000</td>
      <td id="T_99a36_row49_col6" class="data row49 col6" >0.000000</td>
      <td id="T_99a36_row49_col7" class="data row49 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row50" class="row_heading level0 row50" >Soil_Type25</th>
      <td id="T_99a36_row50_col0" class="data row50 col0" >4000000.000000</td>
      <td id="T_99a36_row50_col1" class="data row50 col1" >0.003258</td>
      <td id="T_99a36_row50_col2" class="data row50 col2" >0.056988</td>
      <td id="T_99a36_row50_col3" class="data row50 col3" >0.000000</td>
      <td id="T_99a36_row50_col4" class="data row50 col4" >0.000000</td>
      <td id="T_99a36_row50_col5" class="data row50 col5" >0.000000</td>
      <td id="T_99a36_row50_col6" class="data row50 col6" >0.000000</td>
      <td id="T_99a36_row50_col7" class="data row50 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row51" class="row_heading level0 row51" >Soil_Type8</th>
      <td id="T_99a36_row51_col0" class="data row51 col0" >4000000.000000</td>
      <td id="T_99a36_row51_col1" class="data row51 col1" >0.002900</td>
      <td id="T_99a36_row51_col2" class="data row51 col2" >0.053771</td>
      <td id="T_99a36_row51_col3" class="data row51 col3" >0.000000</td>
      <td id="T_99a36_row51_col4" class="data row51 col4" >0.000000</td>
      <td id="T_99a36_row51_col5" class="data row51 col5" >0.000000</td>
      <td id="T_99a36_row51_col6" class="data row51 col6" >0.000000</td>
      <td id="T_99a36_row51_col7" class="data row51 col7" >1.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row52" class="row_heading level0 row52" >Soil_Type15</th>
      <td id="T_99a36_row52_col0" class="data row52 col0" >4000000.000000</td>
      <td id="T_99a36_row52_col1" class="data row52 col1" >0.000000</td>
      <td id="T_99a36_row52_col2" class="data row52 col2" >0.000000</td>
      <td id="T_99a36_row52_col3" class="data row52 col3" >0.000000</td>
      <td id="T_99a36_row52_col4" class="data row52 col4" >0.000000</td>
      <td id="T_99a36_row52_col5" class="data row52 col5" >0.000000</td>
      <td id="T_99a36_row52_col6" class="data row52 col6" >0.000000</td>
      <td id="T_99a36_row52_col7" class="data row52 col7" >0.000000</td>
    </tr>
    <tr>
      <th id="T_99a36_level0_row53" class="row_heading level0 row53" >Soil_Type7</th>
      <td id="T_99a36_row53_col0" class="data row53 col0" >4000000.000000</td>
      <td id="T_99a36_row53_col1" class="data row53 col1" >0.000000</td>
      <td id="T_99a36_row53_col2" class="data row53 col2" >0.000000</td>
      <td id="T_99a36_row53_col3" class="data row53 col3" >0.000000</td>
      <td id="T_99a36_row53_col4" class="data row53 col4" >0.000000</td>
      <td id="T_99a36_row53_col5" class="data row53 col5" >0.000000</td>
      <td id="T_99a36_row53_col6" class="data row53 col6" >0.000000</td>
      <td id="T_99a36_row53_col7" class="data row53 col7" >0.000000</td>
    </tr>
  </tbody>
</table>




## Continuos and Categorical Data Distribution


```python
df = pd.concat([train[FEATURES], test[FEATURES]], axis=0)

cat_features = [col for col in FEATURES if df[col].nunique() < 9]
cont_features = [col for col in FEATURES if df[col].nunique() >= 9]

del df
print(f'Total number of features: {len(FEATURES)}')
print(f'Number of categorical features: {len(cat_features)}')
print(f'Number of continuos features: {len(cont_features)}')

plt.pie([len(cat_features), len(cont_features)],
       labels=['Categorical', 'Continuos'],
       colors=['#B14F3A', '#07E0C5'],
       textprops={'fontsize' : 15},
       autopct='%1.1f%%')

plt.show()
```

    Total number of features: 54
    Number of categorical features: 44
    Number of continuos features: 10
    


    
![png](output_22_1.png)
    


## Feature Distribution of Continous Features


```python
ncols = 5
nrows = int(len(cont_features) / ncols + (len(FEATURES) % ncols > 0))-1

fig, axes = plt.subplots(nrows, ncols, figsize=(18, 8), facecolor='#A171E0')

for r in range(nrows) :
    for c in range(ncols) :
        col = cont_features[r*ncols+c]
        sns.kdeplot(x=train[col], ax=axes[r, c], color='#6F8CB1', label='Train data')
        sns.kdeplot(x=test[col], ax=axes[r, c], color='#4A6BB1', label='Test data')
        axes[r, c].set_ylabel('')
        axes[r, c].set_xlabel(col, fontsize=10, fontweight='bold')
        axes[r, c].tick_params(labelsize=5, width=0.5)
        axes[r, c].xaxis.offsetText.set_fontsize(4)
        axes[r, c].yaxis.offsetText.set_fontsize(4)
        
plt.show()
```


    
![png](output_24_0.png)
    


## Feature Distribution of Categorical Features


```python
if len(cat_features) == 0 :
    print("No Categorical features")
else:
    ncols = 5
    nrows = int(len(cat_features) / ncols + (len(FEATURES) % ncols > 0))
    
    fig, axes = plt.subplots(nrows, ncols, figsize=(18, 45), facecolor='#DB92DB')
    
    for r in range(nrows):
        for c in range(ncols):
            if r*ncols+c >= len(cat_features):
                break
            col = cat_features[r*ncols+c]
            sns.countplot(x=train[col], ax=axes[r, c], color='#97A0DB', label='Train Data')
            sns.countplot(x=train[col], ax=axes[r, c], color='#DB48A1', label='Test Data')
            axes[r, c].set_ylabel('')
            axes[r, c].set_xlabel(col, fontsize=10, fontweight='bold')
            axes[r, c].tick_params(labelsize=5, width=0.6)
            axes[r, c].xaxis.offsetText.set_fontsize(4)
            axes[r, c].yaxis.offsetText.set_fontsize(4)
            
plt.show()
```


    
![png](output_26_0.png)
    


## Target Distribution


```python
target_df = pd.DataFrame(train[TARGET].value_counts()).reset_index()
target_df.columns = [TARGET, 'count']
fig = px.bar(data_frame = target_df,
            x = 'Cover_Type',
            y = 'count',
            color = "count",
            color_continuous_scale="Emrld")

fig.show()
target_df.sort_values(by =TARGET , ignore_index = True)
```


<script type="text/javascript">
window.PlotlyConfig = {MathJaxConfig: 'local'};
if (window.MathJax) {MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}
if (typeof require !== 'undefined') {
require.undef("plotly");
requirejs.config({
    paths: {
        'plotly': ['https://cdn.plot.ly/plotly-2.6.3.min']
    }
});
require(['plotly'], function(Plotly) {
    window._Plotly = Plotly;
});
}
</script>




<div>                            <div id="c3b4143e-edfe-40d1-a1f8-1e4d38fc1ef0" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("c3b4143e-edfe-40d1-a1f8-1e4d38fc1ef0")) {                    Plotly.newPlot(                        "c3b4143e-edfe-40d1-a1f8-1e4d38fc1ef0",                        [{"alignmentgroup":"True","hovertemplate":"Cover_Type=%{x}<br>count=%{marker.color}<extra></extra>","legendgroup":"","marker":{"color":[2262087,1468136,195712,62261,11426,377,1],"coloraxis":"coloraxis","pattern":{"shape":""}},"name":"","offsetgroup":"","orientation":"v","showlegend":false,"textposition":"auto","x":[2,1,3,7,6,4,5],"xaxis":"x","y":[2262087,1468136,195712,62261,11426,377,1],"yaxis":"y","type":"bar"}],                        {"template":{"data":{"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmap"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmapgl"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"geo":{"bgcolor":"white","lakecolor":"white","landcolor":"#E5ECF6","showlakes":true,"showland":true,"subunitcolor":"white"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"light"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"ternary":{"aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"title":{"x":0.05},"xaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Cover_Type"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"count"}},"coloraxis":{"colorbar":{"title":{"text":"count"}},"colorscale":[[0.0,"rgb(211, 242, 163)"],[0.16666666666666666,"rgb(151, 225, 150)"],[0.3333333333333333,"rgb(108, 192, 139)"],[0.5,"rgb(76, 155, 130)"],[0.6666666666666666,"rgb(33, 122, 121)"],[0.8333333333333334,"rgb(16, 89, 101)"],[1.0,"rgb(7, 64, 80)"]]},"legend":{"tracegroupgap":0},"margin":{"t":60},"barmode":"relative"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('c3b4143e-edfe-40d1-a1f8-1e4d38fc1ef0');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cover_Type</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1468136</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2262087</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>195712</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>377</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>11426</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>62261</td>
    </tr>
  </tbody>
</table>
</div>



### Removing Unwanted Rows and columns


```python
train = train.drop(index = int(np.where(train["Cover_Type"] == 5 )[0]))
train = train.drop(labels = ["Soil_Type7" , "Soil_Type15"] ,axis = 1)
FEATURES.remove('Soil_Type7')
FEATURES.remove('Soil_Type15')
```

# Feature Engineering


```python
train["mean"] = train[FEATURES].mean(axis=1)
train["std"] = train[FEATURES].std(axis=1)
train["min"] = train[FEATURES].min(axis=1)
train["max"] = train[FEATURES].max(axis=1)

test["mean"] = test[FEATURES].mean(axis=1)
test["std"] = test[FEATURES].std(axis=1)
test["min"] = test[FEATURES].min(axis=1)
test["max"] = test[FEATURES].max(axis=1)

FEATURES.extend(['mean', 'std', 'min', 'max'])
```

# Modeling


```python
scaler = StandardScaler()
for col in FEATURES:
    train[col] = scaler.fit_transform(train[col].to_numpy().reshape(-1,1))
    test[col] = scaler.transform(test[col].to_numpy().reshape(-1,1))
    
X = train[FEATURES].to_numpy().astype(np.float32)
y = train[TARGET].to_numpy().astype(np.float32)
X_test = test[FEATURES].to_numpy().astype(np.float32)
```

# LGBM Classifier


```python
lgb_params = {
    'objective' : 'multiclass',
    'metric' : 'multi_logloss',
    'device' : 'gpu',
}


lgb_predictions = []
lgb_scores = []

kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
for fold, (train_idx, valid_idx) in enumerate(kf.split(X = X, y = y)):

    print(10*"=", f"Fold={fold+1}", 10*"=")
    start_time = time.time()
    x_train = X[train_idx, :]
    x_valid = X[valid_idx, :]
    y_train = y[train_idx]
    y_valid = y[valid_idx]
    
    model = LGBMClassifier(**lgb_params)
    model.fit(x_train, y_train,
          early_stopping_rounds=200,
          eval_set=[(x_valid, y_valid)],
          verbose=0)
    
    preds_valid = model.predict(x_valid)
    acc = accuracy_score(y_valid,  preds_valid)
    lgb_scores.append(acc)
    run_time = time.time() - start_time
    print(f"Fold={fold+1}, acc: {acc:.8f}, Run Time: {run_time:.2f}")
    test_preds = model.predict(X_test)
    lgb_predictions.append(test_preds)
    
print("Mean Accuracy :", np.mean(lgb_scores))
```

    ========== Fold=1 ==========
    Fold=1, acc: 0.94587375, Run Time: 149.55
    ========== Fold=2 ==========
    Fold=2, acc: 0.95172000, Run Time: 150.94
    ========== Fold=3 ==========
    Fold=3, acc: 0.94838625, Run Time: 145.89
    ========== Fold=4 ==========
    Fold=4, acc: 0.94935625, Run Time: 156.39
    ========== Fold=5 ==========
    Fold=5, acc: 0.94886244, Run Time: 146.27
    Mean Accuracy : 0.948839737215609
    

# Submission 

### LGBM Classifier Submission


```python
lgb_submission = submission.copy()
lgb_submission['Cover_Type'] = np.squeeze(mode(np.column_stack(lgb_predictions),axis = 1)[0]).astype('int')
lgb_submission.to_csv("lgb-subs.csv",index=None)
lgb_submission.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>Cover_Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4000000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4000001</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4000002</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4000003</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4000004</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>


