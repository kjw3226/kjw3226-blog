![](https://t4.ftcdn.net/jpg/04/60/05/05/360_F_460050532_7JjxeTTaZLyk7RTOayql8iX4O6Zlctjs.jpg)

#### This year is the year of the black tiger. happy New Year.
#### (올해는 흑호의 해입니다. 새해 복 많이 받으세요.)

#### Create a model using the following library.: (다음 라이브러리를 사용하여 모델을 생성했다.:)
#### ● Pycaret (파이캐롯)


```python
# Code Sorce : https://www.kaggle.com/bernhardklinger/tps-jan-2022
!pip install pycaret[full]
```

    Collecting pycaret[full]
      Downloading pycaret-2.3.6-py3-none-any.whl (301 kB)
         |████████████████████████████████| 301 kB 925 kB/s            
    [?25hRequirement already satisfied: scikit-learn==0.23.2 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.23.2)
    Collecting spacy<2.4.0
      Downloading spacy-2.3.7-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (10.4 MB)
         |████████████████████████████████| 10.4 MB 9.6 MB/s            
    [?25hRequirement already satisfied: lightgbm>=2.3.1 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (3.3.1)
    Requirement already satisfied: pyLDAvis in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (3.2.2)
    Requirement already satisfied: pandas in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (1.3.4)
    Requirement already satisfied: seaborn in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.11.2)
    Collecting pyod
      Downloading pyod-0.9.7.tar.gz (114 kB)
         |████████████████████████████████| 114 kB 48.0 MB/s            
    [?25h  Preparing metadata (setup.py) ... [?25l- done
    [?25hCollecting pyyaml<6.0.0
      Downloading PyYAML-5.4.1-cp37-cp37m-manylinux1_x86_64.whl (636 kB)
         |████████████████████████████████| 636 kB 52.7 MB/s            
    [?25hCollecting mlflow
      Downloading mlflow-1.23.0-py3-none-any.whl (15.6 MB)
         |████████████████████████████████| 15.6 MB 50.4 MB/s            
    [?25hCollecting imbalanced-learn==0.7.0
      Downloading imbalanced_learn-0.7.0-py3-none-any.whl (167 kB)
         |████████████████████████████████| 167 kB 60.3 MB/s            
    [?25hRequirement already satisfied: joblib in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (1.1.0)
    Requirement already satisfied: IPython in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (7.29.0)
    Requirement already satisfied: nltk in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (3.2.4)
    Requirement already satisfied: umap-learn in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.5.2)
    Requirement already satisfied: Boruta in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.3)
    Requirement already satisfied: plotly>=4.4.1 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (5.4.0)
    Requirement already satisfied: wordcloud in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (1.8.1)
    Requirement already satisfied: ipywidgets in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (7.6.5)
    Requirement already satisfied: kmodes>=0.10.1 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.11.1)
    Requirement already satisfied: matplotlib in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (3.5.0)
    Requirement already satisfied: cufflinks>=0.17.0 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.17.3)
    Requirement already satisfied: scikit-plot in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.3.7)
    Collecting scipy<=1.5.4
      Downloading scipy-1.5.4-cp37-cp37m-manylinux1_x86_64.whl (25.9 MB)
         |████████████████████████████████| 25.9 MB 58.6 MB/s            
    [?25hCollecting gensim<4.0.0
      Downloading gensim-3.8.3-cp37-cp37m-manylinux1_x86_64.whl (24.2 MB)
         |████████████████████████████████| 24.2 MB 23.1 MB/s            
    [?25hRequirement already satisfied: mlxtend>=0.17.0 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.19.0)
    Requirement already satisfied: yellowbrick>=1.0.1 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (1.3.post1)
    Requirement already satisfied: textblob in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.17.1)
    Requirement already satisfied: pandas-profiling>=2.8.0 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (3.0.0)
    Requirement already satisfied: ray[tune]>=1.0.0 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (1.8.0)
    Requirement already satisfied: hyperopt in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.2.7)
    Requirement already satisfied: uvicorn in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.15.0)
    Requirement already satisfied: fastapi in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.70.0)
    Requirement already satisfied: xgboost>=1.1.0 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (1.5.1)
    Collecting evidently
      Downloading evidently-0.1.40.dev0-py3-none-any.whl (13.3 MB)
         |████████████████████████████████| 13.3 MB 18.1 MB/s            
    [?25hCollecting gradio
      Downloading gradio-2.7.0-py3-none-any.whl (865 kB)
         |████████████████████████████████| 865 kB 42.5 MB/s            
    [?25hRequirement already satisfied: catboost>=0.23.2 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (1.0.3)
    Requirement already satisfied: shap in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.40.0)
    Requirement already satisfied: optuna>=2.2.0 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (2.10.0)
    Requirement already satisfied: google-cloud-storage in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (1.43.0)
    Requirement already satisfied: scikit-optimize>=0.8.1 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (0.9.0)
    Collecting azure-storage-blob
      Downloading azure_storage_blob-12.9.0-py2.py3-none-any.whl (356 kB)
         |████████████████████████████████| 356 kB 58.1 MB/s            
    [?25hCollecting autoviz
      Downloading autoviz-0.1.35-py3-none-any.whl (59 kB)
         |████████████████████████████████| 59 kB 4.9 MB/s             
    [?25hRequirement already satisfied: psutil in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (5.8.0)
    Collecting fairlearn
      Downloading fairlearn-0.7.0-py3-none-any.whl (177 kB)
         |████████████████████████████████| 177 kB 59.8 MB/s            
    [?25hCollecting tune-sklearn>=0.2.1
      Downloading tune_sklearn-0.4.1-py3-none-any.whl (40 kB)
         |████████████████████████████████| 40 kB 4.4 MB/s             
    [?25hCollecting interpret<=0.2.4
      Downloading interpret-0.2.4-py3-none-any.whl (1.4 kB)
    Collecting explainerdashboard
      Downloading explainerdashboard-0.3.7-py3-none-any.whl (305 kB)
         |████████████████████████████████| 305 kB 36.7 MB/s            
    [?25hRequirement already satisfied: boto3 in /opt/conda/lib/python3.7/site-packages (from pycaret[full]) (1.20.15)
    Collecting m2cgen
      Downloading m2cgen-0.9.0-py3-none-any.whl (73 kB)
         |████████████████████████████████| 73 kB 194 kB/s             
    [?25hRequirement already satisfied: numpy>=1.13.3 in /opt/conda/lib/python3.7/site-packages (from imbalanced-learn==0.7.0->pycaret[full]) (1.19.5)
    Requirement already satisfied: threadpoolctl>=2.0.0 in /opt/conda/lib/python3.7/site-packages (from scikit-learn==0.23.2->pycaret[full]) (3.0.0)
    Requirement already satisfied: six in /opt/conda/lib/python3.7/site-packages (from catboost>=0.23.2->pycaret[full]) (1.16.0)
    Requirement already satisfied: graphviz in /opt/conda/lib/python3.7/site-packages (from catboost>=0.23.2->pycaret[full]) (0.8.4)
    Requirement already satisfied: colorlover>=0.2.1 in /opt/conda/lib/python3.7/site-packages (from cufflinks>=0.17.0->pycaret[full]) (0.3.0)
    Requirement already satisfied: setuptools>=34.4.1 in /opt/conda/lib/python3.7/site-packages (from cufflinks>=0.17.0->pycaret[full]) (59.1.1)
    Requirement already satisfied: smart-open>=1.8.1 in /opt/conda/lib/python3.7/site-packages (from gensim<4.0.0->pycaret[full]) (5.2.1)
    Collecting interpret-core[dash,debug,decisiontree,ebm,lime,linear,notebook,plotly,required,sensitivity,shap,skoperules,treeinterpreter]>=0.2.4
      Downloading interpret_core-0.2.7-py3-none-any.whl (6.6 MB)
         |████████████████████████████████| 6.6 MB 16.9 MB/s            
    [?25hRequirement already satisfied: matplotlib-inline in /opt/conda/lib/python3.7/site-packages (from IPython->pycaret[full]) (0.1.3)
    Requirement already satisfied: jedi>=0.16 in /opt/conda/lib/python3.7/site-packages (from IPython->pycaret[full]) (0.18.1)
    Requirement already satisfied: decorator in /opt/conda/lib/python3.7/site-packages (from IPython->pycaret[full]) (5.1.0)
    Requirement already satisfied: pexpect>4.3 in /opt/conda/lib/python3.7/site-packages (from IPython->pycaret[full]) (4.8.0)
    Requirement already satisfied: pickleshare in /opt/conda/lib/python3.7/site-packages (from IPython->pycaret[full]) (0.7.5)
    Requirement already satisfied: pygments in /opt/conda/lib/python3.7/site-packages (from IPython->pycaret[full]) (2.10.0)
    Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /opt/conda/lib/python3.7/site-packages (from IPython->pycaret[full]) (3.0.22)
    Requirement already satisfied: backcall in /opt/conda/lib/python3.7/site-packages (from IPython->pycaret[full]) (0.2.0)
    Requirement already satisfied: traitlets>=4.2 in /opt/conda/lib/python3.7/site-packages (from IPython->pycaret[full]) (5.1.1)
    Requirement already satisfied: ipykernel>=4.5.1 in /opt/conda/lib/python3.7/site-packages (from ipywidgets->pycaret[full]) (6.5.0)
    Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /opt/conda/lib/python3.7/site-packages (from ipywidgets->pycaret[full]) (1.0.2)
    Requirement already satisfied: ipython-genutils~=0.2.0 in /opt/conda/lib/python3.7/site-packages (from ipywidgets->pycaret[full]) (0.2.0)
    Requirement already satisfied: nbformat>=4.2.0 in /opt/conda/lib/python3.7/site-packages (from ipywidgets->pycaret[full]) (5.1.3)
    Requirement already satisfied: widgetsnbextension~=3.5.0 in /opt/conda/lib/python3.7/site-packages (from ipywidgets->pycaret[full]) (3.5.2)
    Requirement already satisfied: wheel in /opt/conda/lib/python3.7/site-packages (from lightgbm>=2.3.1->pycaret[full]) (0.37.0)
    Requirement already satisfied: cycler>=0.10 in /opt/conda/lib/python3.7/site-packages (from matplotlib->pycaret[full]) (0.11.0)
    Requirement already satisfied: kiwisolver>=1.0.1 in /opt/conda/lib/python3.7/site-packages (from matplotlib->pycaret[full]) (1.3.2)
    Requirement already satisfied: pillow>=6.2.0 in /opt/conda/lib/python3.7/site-packages (from matplotlib->pycaret[full]) (8.2.0)
    Requirement already satisfied: fonttools>=4.22.0 in /opt/conda/lib/python3.7/site-packages (from matplotlib->pycaret[full]) (4.28.2)
    Requirement already satisfied: setuptools-scm>=4 in /opt/conda/lib/python3.7/site-packages (from matplotlib->pycaret[full]) (6.3.2)
    Requirement already satisfied: packaging>=20.0 in /opt/conda/lib/python3.7/site-packages (from matplotlib->pycaret[full]) (21.0)
    Requirement already satisfied: python-dateutil>=2.7 in /opt/conda/lib/python3.7/site-packages (from matplotlib->pycaret[full]) (2.8.0)
    Requirement already satisfied: pyparsing>=2.2.1 in /opt/conda/lib/python3.7/site-packages (from matplotlib->pycaret[full]) (3.0.6)
    Requirement already satisfied: cliff in /opt/conda/lib/python3.7/site-packages (from optuna>=2.2.0->pycaret[full]) (3.10.0)
    Requirement already satisfied: colorlog in /opt/conda/lib/python3.7/site-packages (from optuna>=2.2.0->pycaret[full]) (6.6.0)
    Requirement already satisfied: cmaes>=0.8.2 in /opt/conda/lib/python3.7/site-packages (from optuna>=2.2.0->pycaret[full]) (0.8.2)
    Requirement already satisfied: tqdm in /opt/conda/lib/python3.7/site-packages (from optuna>=2.2.0->pycaret[full]) (4.62.3)
    Requirement already satisfied: alembic in /opt/conda/lib/python3.7/site-packages (from optuna>=2.2.0->pycaret[full]) (1.7.5)
    Requirement already satisfied: sqlalchemy>=1.1.0 in /opt/conda/lib/python3.7/site-packages (from optuna>=2.2.0->pycaret[full]) (1.4.27)
    Requirement already satisfied: pytz>=2017.3 in /opt/conda/lib/python3.7/site-packages (from pandas->pycaret[full]) (2021.3)
    Requirement already satisfied: phik>=0.11.1 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling>=2.8.0->pycaret[full]) (0.12.0)
    Requirement already satisfied: pydantic>=1.8.1 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling>=2.8.0->pycaret[full]) (1.8.2)
    Requirement already satisfied: jinja2>=2.11.1 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling>=2.8.0->pycaret[full]) (3.0.3)
    Requirement already satisfied: tangled-up-in-unicode==0.1.0 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling>=2.8.0->pycaret[full]) (0.1.0)
    Requirement already satisfied: visions[type_image_path]==0.7.1 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling>=2.8.0->pycaret[full]) (0.7.1)
    Requirement already satisfied: missingno>=0.4.2 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling>=2.8.0->pycaret[full]) (0.4.2)
    Requirement already satisfied: requests>=2.24.0 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling>=2.8.0->pycaret[full]) (2.25.1)
    Requirement already satisfied: htmlmin>=0.1.12 in /opt/conda/lib/python3.7/site-packages (from pandas-profiling>=2.8.0->pycaret[full]) (0.1.12)
    Requirement already satisfied: networkx>=2.4 in /opt/conda/lib/python3.7/site-packages (from visions[type_image_path]==0.7.1->pandas-profiling>=2.8.0->pycaret[full]) (2.6.3)
    Requirement already satisfied: bottleneck in /opt/conda/lib/python3.7/site-packages (from visions[type_image_path]==0.7.1->pandas-profiling>=2.8.0->pycaret[full]) (1.3.2)
    Requirement already satisfied: multimethod==1.4 in /opt/conda/lib/python3.7/site-packages (from visions[type_image_path]==0.7.1->pandas-profiling>=2.8.0->pycaret[full]) (1.4)
    Requirement already satisfied: attrs>=19.3.0 in /opt/conda/lib/python3.7/site-packages (from visions[type_image_path]==0.7.1->pandas-profiling>=2.8.0->pycaret[full]) (21.2.0)
    Requirement already satisfied: imagehash in /opt/conda/lib/python3.7/site-packages (from visions[type_image_path]==0.7.1->pandas-profiling>=2.8.0->pycaret[full]) (4.2.1)
    Requirement already satisfied: tenacity>=6.2.0 in /opt/conda/lib/python3.7/site-packages (from plotly>=4.4.1->pycaret[full]) (8.0.1)
    Requirement already satisfied: msgpack<2.0.0,>=1.0.0 in /opt/conda/lib/python3.7/site-packages (from ray[tune]>=1.0.0->pycaret[full]) (1.0.3)
    Requirement already satisfied: jsonschema in /opt/conda/lib/python3.7/site-packages (from ray[tune]>=1.0.0->pycaret[full]) (3.2.0)
    Requirement already satisfied: redis>=3.5.0 in /opt/conda/lib/python3.7/site-packages (from ray[tune]>=1.0.0->pycaret[full]) (4.0.2)
    Requirement already satisfied: grpcio>=1.28.1 in /opt/conda/lib/python3.7/site-packages (from ray[tune]>=1.0.0->pycaret[full]) (1.42.0)
    Requirement already satisfied: protobuf>=3.15.3 in /opt/conda/lib/python3.7/site-packages (from ray[tune]>=1.0.0->pycaret[full]) (3.19.1)
    Requirement already satisfied: click>=7.0 in /opt/conda/lib/python3.7/site-packages (from ray[tune]>=1.0.0->pycaret[full]) (8.0.3)
    Requirement already satisfied: filelock in /opt/conda/lib/python3.7/site-packages (from ray[tune]>=1.0.0->pycaret[full]) (3.3.2)
    Requirement already satisfied: tensorboardX>=1.9 in /opt/conda/lib/python3.7/site-packages (from ray[tune]>=1.0.0->pycaret[full]) (2.2)
    Requirement already satisfied: tabulate in /opt/conda/lib/python3.7/site-packages (from ray[tune]>=1.0.0->pycaret[full]) (0.8.9)
    Requirement already satisfied: pyaml>=16.9 in /opt/conda/lib/python3.7/site-packages (from scikit-optimize>=0.8.1->pycaret[full]) (21.10.1)
    Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /opt/conda/lib/python3.7/site-packages (from spacy<2.4.0->pycaret[full]) (1.0.6)
    Requirement already satisfied: blis<0.8.0,>=0.4.0 in /opt/conda/lib/python3.7/site-packages (from spacy<2.4.0->pycaret[full]) (0.7.5)
    Collecting srsly<1.1.0,>=1.0.2
      Downloading srsly-1.0.5-cp37-cp37m-manylinux2014_x86_64.whl (184 kB)
         |████████████████████████████████| 184 kB 64.4 MB/s            
    [?25hCollecting plac<1.2.0,>=0.9.6
      Downloading plac-1.1.3-py2.py3-none-any.whl (20 kB)
    Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /opt/conda/lib/python3.7/site-packages (from spacy<2.4.0->pycaret[full]) (2.0.6)
    Collecting thinc<7.5.0,>=7.4.1
      Downloading thinc-7.4.5-cp37-cp37m-manylinux2014_x86_64.whl (1.0 MB)
         |████████████████████████████████| 1.0 MB 50.2 MB/s            
    [?25hRequirement already satisfied: preshed<3.1.0,>=3.0.2 in /opt/conda/lib/python3.7/site-packages (from spacy<2.4.0->pycaret[full]) (3.0.6)
    Collecting catalogue<1.1.0,>=0.0.7
      Downloading catalogue-1.0.0-py2.py3-none-any.whl (7.7 kB)
    Requirement already satisfied: wasabi<1.1.0,>=0.4.0 in /opt/conda/lib/python3.7/site-packages (from spacy<2.4.0->pycaret[full]) (0.8.2)
    Collecting panel==0.12.6
      Downloading panel-0.12.6-py2.py3-none-any.whl (12.9 MB)
         |████████████████████████████████| 12.9 MB 51.1 MB/s            
    [?25hRequirement already satisfied: holoviews==1.14.6 in /opt/conda/lib/python3.7/site-packages (from autoviz->pycaret[full]) (1.14.6)
    Collecting xlrd
      Downloading xlrd-2.0.1-py2.py3-none-any.whl (96 kB)
         |████████████████████████████████| 96 kB 5.5 MB/s             
    [?25hRequirement already satisfied: bokeh==2.4.2 in /opt/conda/lib/python3.7/site-packages (from autoviz->pycaret[full]) (2.4.2)
    Requirement already satisfied: jupyter in /opt/conda/lib/python3.7/site-packages (from autoviz->pycaret[full]) (1.0.0)
    Collecting hvplot==0.7.3
      Downloading hvplot-0.7.3-py2.py3-none-any.whl (3.1 MB)
         |████████████████████████████████| 3.1 MB 46.0 MB/s            
    [?25hRequirement already satisfied: emoji in /opt/conda/lib/python3.7/site-packages (from autoviz->pycaret[full]) (1.6.1)
    Requirement already satisfied: statsmodels in /opt/conda/lib/python3.7/site-packages (from autoviz->pycaret[full]) (0.12.2)
    Collecting fsspec==0.8.3
      Downloading fsspec-0.8.3-py3-none-any.whl (88 kB)
         |████████████████████████████████| 88 kB 6.8 MB/s             
    [?25hRequirement already satisfied: typing-extensions>=3.10.0 in /opt/conda/lib/python3.7/site-packages (from bokeh==2.4.2->autoviz->pycaret[full]) (3.10.0.2)
    Requirement already satisfied: tornado>=5.1 in /opt/conda/lib/python3.7/site-packages (from bokeh==2.4.2->autoviz->pycaret[full]) (6.1)
    Requirement already satisfied: pyviz-comms>=0.7.4 in /opt/conda/lib/python3.7/site-packages (from holoviews==1.14.6->autoviz->pycaret[full]) (2.1.0)
    Requirement already satisfied: colorcet in /opt/conda/lib/python3.7/site-packages (from holoviews==1.14.6->autoviz->pycaret[full]) (3.0.0)
    Requirement already satisfied: param<2.0,>=1.9.3 in /opt/conda/lib/python3.7/site-packages (from holoviews==1.14.6->autoviz->pycaret[full]) (1.12.0)
    Requirement already satisfied: pyct>=0.4.4 in /opt/conda/lib/python3.7/site-packages (from panel==0.12.6->autoviz->pycaret[full]) (0.4.8)
    Requirement already satisfied: markdown in /opt/conda/lib/python3.7/site-packages (from panel==0.12.6->autoviz->pycaret[full]) (3.3.6)
    Requirement already satisfied: bleach in /opt/conda/lib/python3.7/site-packages (from panel==0.12.6->autoviz->pycaret[full]) (4.1.0)
    Requirement already satisfied: cryptography>=2.1.4 in /opt/conda/lib/python3.7/site-packages (from azure-storage-blob->pycaret[full]) (35.0.0)
    Collecting azure-core<2.0.0,>=1.10.0
      Downloading azure_core-1.21.1-py2.py3-none-any.whl (178 kB)
         |████████████████████████████████| 178 kB 62.9 MB/s            
    [?25hCollecting msrest>=0.6.21
      Downloading msrest-0.6.21-py2.py3-none-any.whl (85 kB)
         |████████████████████████████████| 85 kB 3.6 MB/s             
    [?25hRequirement already satisfied: s3transfer<0.6.0,>=0.5.0 in /opt/conda/lib/python3.7/site-packages (from boto3->pycaret[full]) (0.5.0)
    Requirement already satisfied: botocore<1.24.0,>=1.23.15 in /opt/conda/lib/python3.7/site-packages (from boto3->pycaret[full]) (1.23.15)
    Requirement already satisfied: jmespath<1.0.0,>=0.7.1 in /opt/conda/lib/python3.7/site-packages (from boto3->pycaret[full]) (0.10.0)
    Requirement already satisfied: dataclasses>=0.6 in /opt/conda/lib/python3.7/site-packages (from evidently->pycaret[full]) (0.8)
    Collecting waitress
      Downloading waitress-2.0.0-py3-none-any.whl (56 kB)
         |████████████████████████████████| 56 kB 4.1 MB/s             
    [?25hCollecting jupyter-dash
      Downloading jupyter_dash-0.4.0-py3-none-any.whl (20 kB)
    Collecting dash-bootstrap-components<1
      Downloading dash_bootstrap_components-0.13.1-py3-none-any.whl (197 kB)
         |████████████████████████████████| 197 kB 62.6 MB/s            
    [?25hCollecting flask-simplelogin
      Downloading flask_simplelogin-0.1.1-py3-none-any.whl (7.2 kB)
    Collecting dash>=1.20
      Downloading dash-2.0.0-py3-none-any.whl (7.3 MB)
         |████████████████████████████████| 7.3 MB 28.5 MB/s            
    [?25hCollecting oyaml
      Downloading oyaml-1.0-py2.py3-none-any.whl (3.0 kB)
    Collecting dash-auth
      Downloading dash_auth-1.4.1.tar.gz (470 kB)
         |████████████████████████████████| 470 kB 57.7 MB/s            
    [?25h  Preparing metadata (setup.py) ... [?25l- done
    [?25hRequirement already satisfied: orjson in /opt/conda/lib/python3.7/site-packages (from explainerdashboard->pycaret[full]) (3.6.4)
    Collecting dtreeviz>=1.3
      Downloading dtreeviz-1.3.2.tar.gz (62 kB)
         |████████████████████████████████| 62 kB 638 kB/s             
    [?25h  Preparing metadata (setup.py) ... [?25l- done
    [?25hRequirement already satisfied: slicer==0.0.7 in /opt/conda/lib/python3.7/site-packages (from shap->pycaret[full]) (0.0.7)
    Requirement already satisfied: cloudpickle in /opt/conda/lib/python3.7/site-packages (from shap->pycaret[full]) (2.0.0)
    Requirement already satisfied: numba in /opt/conda/lib/python3.7/site-packages (from shap->pycaret[full]) (0.54.1)
    Requirement already satisfied: starlette==0.16.0 in /opt/conda/lib/python3.7/site-packages (from fastapi->pycaret[full]) (0.16.0)
    Requirement already satisfied: anyio<4,>=3.0.0 in /opt/conda/lib/python3.7/site-packages (from starlette==0.16.0->fastapi->pycaret[full]) (3.3.4)
    Requirement already satisfied: google-auth<3.0dev,>=1.25.0 in /opt/conda/lib/python3.7/site-packages (from google-cloud-storage->pycaret[full]) (1.35.0)
    Requirement already satisfied: google-resumable-media<3.0dev,>=1.3.0 in /opt/conda/lib/python3.7/site-packages (from google-cloud-storage->pycaret[full]) (1.3.3)
    Requirement already satisfied: google-api-core<3.0dev,>=1.29.0 in /opt/conda/lib/python3.7/site-packages (from google-cloud-storage->pycaret[full]) (1.31.4)
    Requirement already satisfied: google-cloud-core<3.0dev,>=1.6.0 in /opt/conda/lib/python3.7/site-packages (from google-cloud-storage->pycaret[full]) (1.7.2)
    Collecting markdown2
      Downloading markdown2-2.4.2-py2.py3-none-any.whl (34 kB)
    Collecting analytics-python
      Downloading analytics_python-1.4.0-py2.py3-none-any.whl (15 kB)
    Collecting paramiko
      Downloading paramiko-2.9.2-py2.py3-none-any.whl (210 kB)
         |████████████████████████████████| 210 kB 56.7 MB/s            
    [?25hCollecting ffmpy
      Downloading ffmpy-0.3.0.tar.gz (4.8 kB)
      Preparing metadata (setup.py) ... [?25l- done
    [?25hCollecting pycryptodome
      Downloading pycryptodome-3.12.0-cp35-abi3-manylinux2010_x86_64.whl (2.0 MB)
         |████████████████████████████████| 2.0 MB 38.7 MB/s            
    [?25hRequirement already satisfied: pydub in /opt/conda/lib/python3.7/site-packages (from gradio->pycaret[full]) (0.25.1)
    Collecting Flask-Login
      Downloading Flask_Login-0.5.0-py2.py3-none-any.whl (16 kB)
    Collecting flask-cachebuster
      Downloading Flask-CacheBuster-1.0.0.tar.gz (3.1 kB)
      Preparing metadata (setup.py) ... [?25l- done
    [?25hRequirement already satisfied: Flask>=1.1.1 in /opt/conda/lib/python3.7/site-packages (from gradio->pycaret[full]) (2.0.2)
    Requirement already satisfied: Flask-Cors>=3.0.8 in /opt/conda/lib/python3.7/site-packages (from gradio->pycaret[full]) (3.0.10)
    Requirement already satisfied: future in /opt/conda/lib/python3.7/site-packages (from hyperopt->pycaret[full]) (0.18.2)
    Requirement already satisfied: py4j in /opt/conda/lib/python3.7/site-packages (from hyperopt->pycaret[full]) (0.10.9.3)
    Requirement already satisfied: entrypoints in /opt/conda/lib/python3.7/site-packages (from mlflow->pycaret[full]) (0.3)
    Requirement already satisfied: sqlparse>=0.3.1 in /opt/conda/lib/python3.7/site-packages (from mlflow->pycaret[full]) (0.4.2)
    Collecting databricks-cli>=0.8.7
      Downloading databricks-cli-0.16.2.tar.gz (58 kB)
         |████████████████████████████████| 58 kB 4.8 MB/s             
    [?25h  Preparing metadata (setup.py) ... [?25l- done
    [?25hCollecting querystring-parser
      Downloading querystring_parser-1.2.4-py2.py3-none-any.whl (7.9 kB)
    Requirement already satisfied: docker>=4.0.0 in /opt/conda/lib/python3.7/site-packages (from mlflow->pycaret[full]) (5.0.3)
    Requirement already satisfied: gitpython>=2.1.0 in /opt/conda/lib/python3.7/site-packages (from mlflow->pycaret[full]) (3.1.24)
    Collecting gunicorn
      Downloading gunicorn-20.1.0-py3-none-any.whl (79 kB)
         |████████████████████████████████| 79 kB 7.8 MB/s             
    [?25hCollecting prometheus-flask-exporter
      Downloading prometheus_flask_exporter-0.18.7-py3-none-any.whl (17 kB)
    Requirement already satisfied: importlib-metadata!=4.7.0,>=3.7.0 in /opt/conda/lib/python3.7/site-packages (from mlflow->pycaret[full]) (4.8.2)
    Requirement already satisfied: numexpr in /opt/conda/lib/python3.7/site-packages (from pyLDAvis->pycaret[full]) (2.7.3)
    Requirement already satisfied: funcy in /opt/conda/lib/python3.7/site-packages (from pyLDAvis->pycaret[full]) (1.16)
    Requirement already satisfied: pynndescent>=0.5 in /opt/conda/lib/python3.7/site-packages (from umap-learn->pycaret[full]) (0.5.5)
    Requirement already satisfied: asgiref>=3.4.0 in /opt/conda/lib/python3.7/site-packages (from uvicorn->pycaret[full]) (3.4.1)
    Requirement already satisfied: h11>=0.8 in /opt/conda/lib/python3.7/site-packages (from uvicorn->pycaret[full]) (0.12.0)
    Requirement already satisfied: urllib3<1.27,>=1.25.4 in /opt/conda/lib/python3.7/site-packages (from botocore<1.24.0,>=1.23.15->boto3->pycaret[full]) (1.26.7)
    Requirement already satisfied: cffi>=1.12 in /opt/conda/lib/python3.7/site-packages (from cryptography>=2.1.4->azure-storage-blob->pycaret[full]) (1.15.0)
    Collecting flask-compress
      Downloading Flask_Compress-1.10.1-py3-none-any.whl (7.9 kB)
    Collecting dash-core-components==2.0.0
      Downloading dash_core_components-2.0.0.tar.gz (3.4 kB)
      Preparing metadata (setup.py) ... [?25l- done
    [?25hCollecting dash-html-components==2.0.0
      Downloading dash_html_components-2.0.0.tar.gz (3.8 kB)
      Preparing metadata (setup.py) ... [?25l- done
    [?25hCollecting dash-table==5.0.0
      Downloading dash_table-5.0.0.tar.gz (3.4 kB)
      Preparing metadata (setup.py) ... [?25l- done
    [?25hRequirement already satisfied: websocket-client>=0.32.0 in /opt/conda/lib/python3.7/site-packages (from docker>=4.0.0->mlflow->pycaret[full]) (1.2.1)
    Collecting graphviz
      Downloading graphviz-0.19.1-py3-none-any.whl (46 kB)
         |████████████████████████████████| 46 kB 3.2 MB/s             
    [?25hCollecting colour
      Downloading colour-0.1.5-py2.py3-none-any.whl (23 kB)
    Requirement already satisfied: pytest in /opt/conda/lib/python3.7/site-packages (from dtreeviz>=1.3->explainerdashboard->pycaret[full]) (6.2.5)
    Requirement already satisfied: Werkzeug>=2.0 in /opt/conda/lib/python3.7/site-packages (from Flask>=1.1.1->gradio->pycaret[full]) (2.0.2)
    Requirement already satisfied: itsdangerous>=2.0 in /opt/conda/lib/python3.7/site-packages (from Flask>=1.1.1->gradio->pycaret[full]) (2.0.1)
    Requirement already satisfied: gitdb<5,>=4.0.1 in /opt/conda/lib/python3.7/site-packages (from gitpython>=2.1.0->mlflow->pycaret[full]) (4.0.9)
    Requirement already satisfied: googleapis-common-protos<2.0dev,>=1.6.0 in /opt/conda/lib/python3.7/site-packages (from google-api-core<3.0dev,>=1.29.0->google-cloud-storage->pycaret[full]) (1.53.0)
    Requirement already satisfied: cachetools<5.0,>=2.0.0 in /opt/conda/lib/python3.7/site-packages (from google-auth<3.0dev,>=1.25.0->google-cloud-storage->pycaret[full]) (4.2.4)
    Requirement already satisfied: pyasn1-modules>=0.2.1 in /opt/conda/lib/python3.7/site-packages (from google-auth<3.0dev,>=1.25.0->google-cloud-storage->pycaret[full]) (0.2.7)
    Requirement already satisfied: rsa<5,>=3.1.4 in /opt/conda/lib/python3.7/site-packages (from google-auth<3.0dev,>=1.25.0->google-cloud-storage->pycaret[full]) (4.7.2)
    Requirement already satisfied: google-crc32c<2.0dev,>=1.0 in /opt/conda/lib/python3.7/site-packages (from google-resumable-media<3.0dev,>=1.3.0->google-cloud-storage->pycaret[full]) (1.1.2)
    Requirement already satisfied: zipp>=0.5 in /opt/conda/lib/python3.7/site-packages (from importlib-metadata!=4.7.0,>=3.7.0->mlflow->pycaret[full]) (3.6.0)
    Requirement already satisfied: dill>=0.2.5 in /opt/conda/lib/python3.7/site-packages (from interpret-core[dash,debug,decisiontree,ebm,lime,linear,notebook,plotly,required,sensitivity,shap,skoperules,treeinterpreter]>=0.2.4->interpret<=0.2.4->pycaret[full]) (0.3.4)
    Collecting skope-rules>=1.0.1
      Downloading skope_rules-1.0.1-py3-none-any.whl (14 kB)
    Collecting treeinterpreter>=0.2.2
      Downloading treeinterpreter-0.2.3-py2.py3-none-any.whl (6.0 kB)
    Collecting gevent>=1.3.6
      Downloading gevent-21.12.0-cp37-cp37m-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (5.8 MB)
         |████████████████████████████████| 5.8 MB 422 kB/s            
    [?25hCollecting dash-cytoscape>=0.1.1
      Downloading dash_cytoscape-0.3.0-py3-none-any.whl (3.6 MB)
         |████████████████████████████████| 3.6 MB 49.4 MB/s            
    [?25hRequirement already satisfied: lime>=0.1.1.33 in /opt/conda/lib/python3.7/site-packages (from interpret-core[dash,debug,decisiontree,ebm,lime,linear,notebook,plotly,required,sensitivity,shap,skoperules,treeinterpreter]>=0.2.4->interpret<=0.2.4->pycaret[full]) (0.2.0.1)
    Collecting SALib>=1.3.3
      Downloading SALib-1.4.5-py2.py3-none-any.whl (756 kB)
         |████████████████████████████████| 756 kB 28.5 MB/s            
    [?25hRequirement already satisfied: debugpy<2.0,>=1.0.0 in /opt/conda/lib/python3.7/site-packages (from ipykernel>=4.5.1->ipywidgets->pycaret[full]) (1.5.1)
    Requirement already satisfied: argcomplete>=1.12.3 in /opt/conda/lib/python3.7/site-packages (from ipykernel>=4.5.1->ipywidgets->pycaret[full]) (1.12.3)
    Requirement already satisfied: jupyter-client<8.0 in /opt/conda/lib/python3.7/site-packages (from ipykernel>=4.5.1->ipywidgets->pycaret[full]) (7.0.6)
    Requirement already satisfied: parso<0.9.0,>=0.8.0 in /opt/conda/lib/python3.7/site-packages (from jedi>=0.16->IPython->pycaret[full]) (0.8.2)
    Requirement already satisfied: MarkupSafe>=2.0 in /opt/conda/lib/python3.7/site-packages (from jinja2>=2.11.1->pandas-profiling>=2.8.0->pycaret[full]) (2.0.1)
    Requirement already satisfied: requests-oauthlib>=0.5.0 in /opt/conda/lib/python3.7/site-packages (from msrest>=0.6.21->azure-storage-blob->pycaret[full]) (1.3.0)
    Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.7/site-packages (from msrest>=0.6.21->azure-storage-blob->pycaret[full]) (2021.10.8)
    Collecting isodate>=0.6.0
      Downloading isodate-0.6.1-py2.py3-none-any.whl (41 kB)
         |████████████████████████████████| 41 kB 482 kB/s             
    [?25hRequirement already satisfied: jupyter-core in /opt/conda/lib/python3.7/site-packages (from nbformat>=4.2.0->ipywidgets->pycaret[full]) (4.9.1)
    Requirement already satisfied: pyrsistent>=0.14.0 in /opt/conda/lib/python3.7/site-packages (from jsonschema->ray[tune]>=1.0.0->pycaret[full]) (0.18.0)
    Requirement already satisfied: llvmlite<0.38,>=0.37.0rc1 in /opt/conda/lib/python3.7/site-packages (from numba->shap->pycaret[full]) (0.37.0)
    Requirement already satisfied: ptyprocess>=0.5 in /opt/conda/lib/python3.7/site-packages (from pexpect>4.3->IPython->pycaret[full]) (0.7.0)
    Requirement already satisfied: wcwidth in /opt/conda/lib/python3.7/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->IPython->pycaret[full]) (0.2.5)
    Requirement already satisfied: deprecated in /opt/conda/lib/python3.7/site-packages (from redis>=3.5.0->ray[tune]>=1.0.0->pycaret[full]) (1.2.13)
    Requirement already satisfied: chardet<5,>=3.0.2 in /opt/conda/lib/python3.7/site-packages (from requests>=2.24.0->pandas-profiling>=2.8.0->pycaret[full]) (4.0.0)
    Requirement already satisfied: idna<3,>=2.5 in /opt/conda/lib/python3.7/site-packages (from requests>=2.24.0->pandas-profiling>=2.8.0->pycaret[full]) (2.10)
    Requirement already satisfied: tomli>=1.0.0 in /opt/conda/lib/python3.7/site-packages (from setuptools-scm>=4->matplotlib->pycaret[full]) (1.2.2)
    Requirement already satisfied: greenlet!=0.4.17 in /opt/conda/lib/python3.7/site-packages (from sqlalchemy>=1.1.0->optuna>=2.2.0->pycaret[full]) (1.1.2)
    Requirement already satisfied: patsy>=0.5 in /opt/conda/lib/python3.7/site-packages (from statsmodels->autoviz->pycaret[full]) (0.5.2)
    Requirement already satisfied: notebook>=4.4.1 in /opt/conda/lib/python3.7/site-packages (from widgetsnbextension~=3.5.0->ipywidgets->pycaret[full]) (6.4.6)
    Requirement already satisfied: Mako in /opt/conda/lib/python3.7/site-packages (from alembic->optuna>=2.2.0->pycaret[full]) (1.1.6)
    Requirement already satisfied: importlib-resources in /opt/conda/lib/python3.7/site-packages (from alembic->optuna>=2.2.0->pycaret[full]) (5.4.0)
    Collecting backoff==1.10.0
      Downloading backoff-1.10.0-py2.py3-none-any.whl (31 kB)
    Collecting monotonic>=1.5
      Downloading monotonic-1.6-py2.py3-none-any.whl (8.2 kB)
    Requirement already satisfied: autopage>=0.4.0 in /opt/conda/lib/python3.7/site-packages (from cliff->optuna>=2.2.0->pycaret[full]) (0.4.0)
    Requirement already satisfied: PrettyTable>=0.7.2 in /opt/conda/lib/python3.7/site-packages (from cliff->optuna>=2.2.0->pycaret[full]) (2.4.0)
    Requirement already satisfied: cmd2>=1.0.0 in /opt/conda/lib/python3.7/site-packages (from cliff->optuna>=2.2.0->pycaret[full]) (2.3.2)
    Requirement already satisfied: stevedore>=2.0.1 in /opt/conda/lib/python3.7/site-packages (from cliff->optuna>=2.2.0->pycaret[full]) (3.5.0)
    Requirement already satisfied: pbr!=2.1.0,>=2.0.0 in /opt/conda/lib/python3.7/site-packages (from cliff->optuna>=2.2.0->pycaret[full]) (5.8.0)
    Collecting chart_studio>=1.0.0
      Downloading chart_studio-1.1.0-py3-none-any.whl (64 kB)
         |████████████████████████████████| 64 kB 2.7 MB/s             
    [?25hCollecting flask-seasurf
      Downloading Flask_SeaSurf-0.3.1-py3-none-any.whl (8.1 kB)
    Requirement already satisfied: retrying in /opt/conda/lib/python3.7/site-packages (from dash-auth->explainerdashboard->pycaret[full]) (1.3.3)
    Collecting ua_parser
      Downloading ua_parser-0.10.0-py2.py3-none-any.whl (35 kB)
    Collecting WTForms>=2.1
      Downloading WTForms-3.0.1-py3-none-any.whl (136 kB)
         |████████████████████████████████| 136 kB 61.9 MB/s            
    [?25hCollecting Flask-WTF<0.16.0,>=0.15.1
      Downloading Flask_WTF-0.15.1-py2.py3-none-any.whl (13 kB)
    Requirement already satisfied: qtconsole in /opt/conda/lib/python3.7/site-packages (from jupyter->autoviz->pycaret[full]) (5.2.0)
    Requirement already satisfied: nbconvert in /opt/conda/lib/python3.7/site-packages (from jupyter->autoviz->pycaret[full]) (6.3.0)
    Requirement already satisfied: jupyter-console in /opt/conda/lib/python3.7/site-packages (from jupyter->autoviz->pycaret[full]) (6.4.0)
    Collecting ansi2html
      Downloading ansi2html-1.6.0-py3-none-any.whl (14 kB)
    Collecting pynacl>=1.0.1
      Downloading PyNaCl-1.5.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl (856 kB)
         |████████████████████████████████| 856 kB 54.6 MB/s            
    [?25hCollecting bcrypt>=3.1.3
      Downloading bcrypt-3.2.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl (61 kB)
         |████████████████████████████████| 61 kB 362 kB/s             
    [?25hRequirement already satisfied: prometheus-client in /opt/conda/lib/python3.7/site-packages (from prometheus-flask-exporter->mlflow->pycaret[full]) (0.12.0)
    Requirement already satisfied: sniffio>=1.1 in /opt/conda/lib/python3.7/site-packages (from anyio<4,>=3.0.0->starlette==0.16.0->fastapi->pycaret[full]) (1.2.0)
    Requirement already satisfied: pycparser in /opt/conda/lib/python3.7/site-packages (from cffi>=1.12->cryptography>=2.1.4->azure-storage-blob->pycaret[full]) (2.21)
    Requirement already satisfied: pyperclip>=1.6 in /opt/conda/lib/python3.7/site-packages (from cmd2>=1.0.0->cliff->optuna>=2.2.0->pycaret[full]) (1.8.2)
    Collecting zope.event
      Downloading zope.event-4.5.0-py2.py3-none-any.whl (6.8 kB)
    Collecting zope.interface
      Downloading zope.interface-5.4.0-cp37-cp37m-manylinux2010_x86_64.whl (251 kB)
         |████████████████████████████████| 251 kB 57.4 MB/s            
    [?25hRequirement already satisfied: smmap<6,>=3.0.1 in /opt/conda/lib/python3.7/site-packages (from gitdb<5,>=4.0.1->gitpython>=2.1.0->mlflow->pycaret[full]) (3.0.5)
    Requirement already satisfied: pyzmq>=13 in /opt/conda/lib/python3.7/site-packages (from jupyter-client<8.0->ipykernel>=4.5.1->ipywidgets->pycaret[full]) (22.3.0)
    Requirement already satisfied: nest-asyncio>=1.5 in /opt/conda/lib/python3.7/site-packages (from jupyter-client<8.0->ipykernel>=4.5.1->ipywidgets->pycaret[full]) (1.5.1)
    Requirement already satisfied: scikit-image>=0.12 in /opt/conda/lib/python3.7/site-packages (from lime>=0.1.1.33->interpret-core[dash,debug,decisiontree,ebm,lime,linear,notebook,plotly,required,sensitivity,shap,skoperules,treeinterpreter]>=0.2.4->interpret<=0.2.4->pycaret[full]) (0.18.3)
    Requirement already satisfied: terminado>=0.8.3 in /opt/conda/lib/python3.7/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets->pycaret[full]) (0.12.1)
    Requirement already satisfied: argon2-cffi in /opt/conda/lib/python3.7/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets->pycaret[full]) (21.1.0)
    Requirement already satisfied: Send2Trash>=1.8.0 in /opt/conda/lib/python3.7/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets->pycaret[full]) (1.8.0)
    Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /opt/conda/lib/python3.7/site-packages (from pyasn1-modules>=0.2.1->google-auth<3.0dev,>=1.25.0->google-cloud-storage->pycaret[full]) (0.4.8)
    Requirement already satisfied: oauthlib>=3.0.0 in /opt/conda/lib/python3.7/site-packages (from requests-oauthlib>=0.5.0->msrest>=0.6.21->azure-storage-blob->pycaret[full]) (3.1.1)
    Requirement already satisfied: pathos in /opt/conda/lib/python3.7/site-packages (from SALib>=1.3.3->interpret-core[dash,debug,decisiontree,ebm,lime,linear,notebook,plotly,required,sensitivity,shap,skoperules,treeinterpreter]>=0.2.4->interpret<=0.2.4->pycaret[full]) (0.2.8)
    Requirement already satisfied: webencodings in /opt/conda/lib/python3.7/site-packages (from bleach->panel==0.12.6->autoviz->pycaret[full]) (0.5.1)
    Requirement already satisfied: wrapt<2,>=1.10 in /opt/conda/lib/python3.7/site-packages (from deprecated->redis>=3.5.0->ray[tune]>=1.0.0->pycaret[full]) (1.13.3)
    Collecting brotli
      Downloading Brotli-1.0.9-cp37-cp37m-manylinux1_x86_64.whl (357 kB)
         |████████████████████████████████| 357 kB 57.9 MB/s            
    [?25hRequirement already satisfied: PyWavelets in /opt/conda/lib/python3.7/site-packages (from imagehash->visions[type_image_path]==0.7.1->pandas-profiling>=2.8.0->pycaret[full]) (1.2.0)
    Requirement already satisfied: testpath in /opt/conda/lib/python3.7/site-packages (from nbconvert->jupyter->autoviz->pycaret[full]) (0.5.0)
    Requirement already satisfied: jupyterlab-pygments in /opt/conda/lib/python3.7/site-packages (from nbconvert->jupyter->autoviz->pycaret[full]) (0.1.2)
    Requirement already satisfied: mistune<2,>=0.8.1 in /opt/conda/lib/python3.7/site-packages (from nbconvert->jupyter->autoviz->pycaret[full]) (0.8.4)
    Requirement already satisfied: pandocfilters>=1.4.1 in /opt/conda/lib/python3.7/site-packages (from nbconvert->jupyter->autoviz->pycaret[full]) (1.5.0)
    Requirement already satisfied: nbclient<0.6.0,>=0.5.0 in /opt/conda/lib/python3.7/site-packages (from nbconvert->jupyter->autoviz->pycaret[full]) (0.5.8)
    Requirement already satisfied: defusedxml in /opt/conda/lib/python3.7/site-packages (from nbconvert->jupyter->autoviz->pycaret[full]) (0.7.1)
    Requirement already satisfied: pluggy<2.0,>=0.12 in /opt/conda/lib/python3.7/site-packages (from pytest->dtreeviz>=1.3->explainerdashboard->pycaret[full]) (1.0.0)
    Requirement already satisfied: py>=1.8.2 in /opt/conda/lib/python3.7/site-packages (from pytest->dtreeviz>=1.3->explainerdashboard->pycaret[full]) (1.11.0)
    Requirement already satisfied: toml in /opt/conda/lib/python3.7/site-packages (from pytest->dtreeviz>=1.3->explainerdashboard->pycaret[full]) (0.10.2)
    Requirement already satisfied: iniconfig in /opt/conda/lib/python3.7/site-packages (from pytest->dtreeviz>=1.3->explainerdashboard->pycaret[full]) (1.1.1)
    Requirement already satisfied: qtpy in /opt/conda/lib/python3.7/site-packages (from qtconsole->jupyter->autoviz->pycaret[full]) (1.11.2)
    Requirement already satisfied: tifffile>=2019.7.26 in /opt/conda/lib/python3.7/site-packages (from scikit-image>=0.12->lime>=0.1.1.33->interpret-core[dash,debug,decisiontree,ebm,lime,linear,notebook,plotly,required,sensitivity,shap,skoperules,treeinterpreter]>=0.2.4->interpret<=0.2.4->pycaret[full]) (2021.11.2)
    Requirement already satisfied: imageio>=2.3.0 in /opt/conda/lib/python3.7/site-packages (from scikit-image>=0.12->lime>=0.1.1.33->interpret-core[dash,debug,decisiontree,ebm,lime,linear,notebook,plotly,required,sensitivity,shap,skoperules,treeinterpreter]>=0.2.4->interpret<=0.2.4->pycaret[full]) (2.9.0)
    Requirement already satisfied: ppft>=1.6.6.4 in /opt/conda/lib/python3.7/site-packages (from pathos->SALib>=1.3.3->interpret-core[dash,debug,decisiontree,ebm,lime,linear,notebook,plotly,required,sensitivity,shap,skoperules,treeinterpreter]>=0.2.4->interpret<=0.2.4->pycaret[full]) (1.6.6.4)
    Requirement already satisfied: pox>=0.3.0 in /opt/conda/lib/python3.7/site-packages (from pathos->SALib>=1.3.3->interpret-core[dash,debug,decisiontree,ebm,lime,linear,notebook,plotly,required,sensitivity,shap,skoperules,treeinterpreter]>=0.2.4->interpret<=0.2.4->pycaret[full]) (0.3.0)
    Requirement already satisfied: multiprocess>=0.70.12 in /opt/conda/lib/python3.7/site-packages (from pathos->SALib>=1.3.3->interpret-core[dash,debug,decisiontree,ebm,lime,linear,notebook,plotly,required,sensitivity,shap,skoperules,treeinterpreter]>=0.2.4->interpret<=0.2.4->pycaret[full]) (0.70.12.2)
    Building wheels for collected packages: pyod, dash-core-components, dash-html-components, dash-table, databricks-cli, dtreeviz, dash-auth, ffmpy, flask-cachebuster
      Building wheel for pyod (setup.py) ... [?25l- \ done
    [?25h  Created wheel for pyod: filename=pyod-0.9.7-py3-none-any.whl size=136277 sha256=135dad8dd6658a060e19edf44ddaa05aaca3552013e14705bea482a578dbc9f7
      Stored in directory: /root/.cache/pip/wheels/ce/14/ae/60cbb36511e59bc12f8f0883805f586db3b315972b54865d33
      Building wheel for dash-core-components (setup.py) ... [?25l- done
    [?25h  Created wheel for dash-core-components: filename=dash_core_components-2.0.0-py3-none-any.whl size=3821 sha256=15153948e1eed9404b8f3284d94185c965b8a69282fa82eb39c5d0a1415c04ca
      Stored in directory: /root/.cache/pip/wheels/00/f9/c7/1a6437d794ed753ea9bc9079e761d4fc803a1f1f5d3697b9ec
      Building wheel for dash-html-components (setup.py) ... [?25l- done
    [?25h  Created wheel for dash-html-components: filename=dash_html_components-2.0.0-py3-none-any.whl size=4089 sha256=10d1ec0502c9ccbfaaf6a2a76e312326efa7dc6ceda9e1ffebe0ba6df5ed55ca
      Stored in directory: /root/.cache/pip/wheels/ec/6b/81/05aceabd8b27f724e2c96784016287cc1bfbc349ebfda451de
      Building wheel for dash-table (setup.py) ... [?25l- done
    [?25h  Created wheel for dash-table: filename=dash_table-5.0.0-py3-none-any.whl size=3911 sha256=ac72f4879de3ba12f5449c9a8ca3959692beb4264423dc5ed772db9f5ef05b0b
      Stored in directory: /root/.cache/pip/wheels/85/5d/4e/7c276b57992951dbe770bf5caad6448d0539c510663aefd2e2
      Building wheel for databricks-cli (setup.py) ... [?25l- \ done
    [?25h  Created wheel for databricks-cli: filename=databricks_cli-0.16.2-py3-none-any.whl size=106811 sha256=64795fc692936a6a2b56b84703c299d38f34db17d481b79a849fe21521c2e28a
      Stored in directory: /root/.cache/pip/wheels/f4/5c/ed/e1ce20a53095f63b27b4964abbad03e59cf3472822addf7d29
      Building wheel for dtreeviz (setup.py) ... [?25l- \ done
    [?25h  Created wheel for dtreeviz: filename=dtreeviz-1.3.2-py3-none-any.whl size=67936 sha256=910c21c2ea1f7dfe1a04d0ae18c26d6844d95ffa1e9ab4c8b3d996023b7210c2
      Stored in directory: /root/.cache/pip/wheels/9d/29/a1/f2ad20de79875e749330d5c6234fc5f517991fcaa23d7a3d0f
      Building wheel for dash-auth (setup.py) ... [?25l- \ done
    [?25h  Created wheel for dash-auth: filename=dash_auth-1.4.1-py3-none-any.whl size=476151 sha256=3ac7b3fa875f35655934d0ad43d3f973026b94cd1d8c413a4d4975c857cb9ea7
      Stored in directory: /root/.cache/pip/wheels/19/b2/02/3c3f05988ff92f02c52ce4e081859d423537e8e9b13f673c02
      Building wheel for ffmpy (setup.py) ... [?25l- done
    [?25h  Created wheel for ffmpy: filename=ffmpy-0.3.0-py3-none-any.whl size=4710 sha256=ce79fa89ee203799da262cff8a983fdc0fbc28d066b047f4310d89e0ed9df14f
      Stored in directory: /root/.cache/pip/wheels/13/e4/6c/e8059816e86796a597c6e6b0d4c880630f51a1fcfa0befd5e6
      Building wheel for flask-cachebuster (setup.py) ... [?25l- \ done
    [?25h  Created wheel for flask-cachebuster: filename=Flask_CacheBuster-1.0.0-py3-none-any.whl size=3371 sha256=617e815288bf87a8ad0832da08bb488e7164d6754406159280217feeeecc6489
      Stored in directory: /root/.cache/pip/wheels/28/c0/c4/44687421dab41455be93112bd1b0dee1f3c5a9aa27bee63708
    Successfully built pyod dash-core-components dash-html-components dash-table databricks-cli dtreeviz dash-auth ffmpy flask-cachebuster
    Installing collected packages: pyyaml, brotli, scipy, flask-compress, dash-table, dash-html-components, dash-core-components, zope.interface, zope.event, WTForms, srsly, plac, panel, dash, catalogue, ua-parser, treeinterpreter, thinc, skope-rules, SALib, querystring-parser, pynacl, prometheus-flask-exporter, monotonic, isodate, interpret-core, gunicorn, graphviz, gevent, Flask-WTF, flask-seasurf, databricks-cli, dash-cytoscape, colour, chart-studio, bcrypt, backoff, ansi2html, xlrd, waitress, spacy, pyod, pycryptodome, paramiko, oyaml, msrest, mlflow, markdown2, jupyter-dash, imbalanced-learn, hvplot, gensim, fsspec, flask-simplelogin, Flask-Login, flask-cachebuster, ffmpy, dtreeviz, dash-bootstrap-components, dash-auth, azure-core, analytics-python, tune-sklearn, pycaret, m2cgen, interpret, gradio, fairlearn, explainerdashboard, evidently, azure-storage-blob, autoviz
      Attempting uninstall: pyyaml
        Found existing installation: PyYAML 6.0
        Uninstalling PyYAML-6.0:
          Successfully uninstalled PyYAML-6.0
      Attempting uninstall: scipy
        Found existing installation: scipy 1.7.2
        Uninstalling scipy-1.7.2:
          Successfully uninstalled scipy-1.7.2
      Attempting uninstall: srsly
        Found existing installation: srsly 2.4.2
        Uninstalling srsly-2.4.2:
          Successfully uninstalled srsly-2.4.2
      Attempting uninstall: panel
        Found existing installation: panel 0.12.5
        Uninstalling panel-0.12.5:
          Successfully uninstalled panel-0.12.5
      Attempting uninstall: catalogue
        Found existing installation: catalogue 2.0.6
        Uninstalling catalogue-2.0.6:
          Successfully uninstalled catalogue-2.0.6
      Attempting uninstall: thinc
        Found existing installation: thinc 8.0.13
        Uninstalling thinc-8.0.13:
          Successfully uninstalled thinc-8.0.13
      Attempting uninstall: graphviz
        Found existing installation: graphviz 0.8.4
        Uninstalling graphviz-0.8.4:
          Successfully uninstalled graphviz-0.8.4
      Attempting uninstall: spacy
        Found existing installation: spacy 3.1.4
        Uninstalling spacy-3.1.4:
          Successfully uninstalled spacy-3.1.4
      Attempting uninstall: imbalanced-learn
        Found existing installation: imbalanced-learn 0.8.1
        Uninstalling imbalanced-learn-0.8.1:
          Successfully uninstalled imbalanced-learn-0.8.1
      Attempting uninstall: gensim
        Found existing installation: gensim 4.0.1
        Uninstalling gensim-4.0.1:
          Successfully uninstalled gensim-4.0.1
      Attempting uninstall: fsspec
        Found existing installation: fsspec 2021.11.1
        Uninstalling fsspec-2021.11.1:
          Successfully uninstalled fsspec-2021.11.1
    [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    dask-cudf 21.10.1 requires cupy-cuda114, which is not installed.
    cudf 21.10.1 requires cupy-cuda110, which is not installed.
    scattertext 0.1.5 requires gensim>=4.0.0, but you have gensim 3.8.3 which is incompatible.
    s3fs 2021.11.1 requires fsspec==2021.11.1, but you have fsspec 0.8.3 which is incompatible.
    pytorch-lightning 1.4.4 requires fsspec[http]!=2021.06.0,>=2021.05.0, but you have fsspec 0.8.3 which is incompatible.
    pdpbox 0.2.1 requires matplotlib==3.1.1, but you have matplotlib 3.5.0 which is incompatible.
    mxnet-cu110 1.8.0.post0 requires graphviz<0.9.0,>=0.8.1, but you have graphviz 0.19.1 which is incompatible.
    gcsfs 2021.11.0 requires fsspec==2021.11.0, but you have fsspec 0.8.3 which is incompatible.
    en-core-web-sm 3.1.0 requires spacy<3.2.0,>=3.1.0, but you have spacy 2.3.7 which is incompatible.
    en-core-web-lg 3.1.0 requires spacy<3.2.0,>=3.1.0, but you have spacy 2.3.7 which is incompatible.
    datasets 1.16.1 requires fsspec[http]>=2021.05.0, but you have fsspec 0.8.3 which is incompatible.
    dask-cudf 21.10.1 requires dask==2021.09.1, but you have dask 2021.11.2 which is incompatible.
    dask-cudf 21.10.1 requires distributed==2021.09.1, but you have distributed 2021.11.2 which is incompatible.[0m
    Successfully installed Flask-Login-0.5.0 Flask-WTF-0.15.1 SALib-1.4.5 WTForms-3.0.1 analytics-python-1.4.0 ansi2html-1.6.0 autoviz-0.1.35 azure-core-1.21.1 azure-storage-blob-12.9.0 backoff-1.10.0 bcrypt-3.2.0 brotli-1.0.9 catalogue-1.0.0 chart-studio-1.1.0 colour-0.1.5 dash-2.0.0 dash-auth-1.4.1 dash-bootstrap-components-0.13.1 dash-core-components-2.0.0 dash-cytoscape-0.3.0 dash-html-components-2.0.0 dash-table-5.0.0 databricks-cli-0.16.2 dtreeviz-1.3.2 evidently-0.1.40.dev0 explainerdashboard-0.3.7 fairlearn-0.7.0 ffmpy-0.3.0 flask-cachebuster-1.0.0 flask-compress-1.10.1 flask-seasurf-0.3.1 flask-simplelogin-0.1.1 fsspec-0.8.3 gensim-3.8.3 gevent-21.12.0 gradio-2.7.0 graphviz-0.19.1 gunicorn-20.1.0 hvplot-0.7.3 imbalanced-learn-0.7.0 interpret-0.2.4 interpret-core-0.2.7 isodate-0.6.1 jupyter-dash-0.4.0 m2cgen-0.9.0 markdown2-2.4.2 mlflow-1.23.0 monotonic-1.6 msrest-0.6.21 oyaml-1.0 panel-0.12.6 paramiko-2.9.2 plac-1.1.3 prometheus-flask-exporter-0.18.7 pycaret-2.3.6 pycryptodome-3.12.0 pynacl-1.5.0 pyod-0.9.7 pyyaml-5.4.1 querystring-parser-1.2.4 scipy-1.5.4 skope-rules-1.0.1 spacy-2.3.7 srsly-1.0.5 thinc-7.4.5 treeinterpreter-0.2.3 tune-sklearn-0.4.1 ua-parser-0.10.0 waitress-2.0.0 xlrd-2.0.1 zope.event-4.5.0 zope.interface-5.4.0
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m


# Loading Data (데이터 불러오기)


```python
# Code Sorce : https://www.kaggle.com/bernhardklinger/tps-jan-2022
import pandas as pd
import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pycaret.regression import *
from sklearn.datasets import make_classification
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv('/kaggle/input/tabular-playground-series-jan-2022/train.csv')

train = pd.read_csv('../input/tabular-playground-series-jan-2022/train.csv',index_col='row_id')
test = pd.read_csv('../input/tabular-playground-series-jan-2022/test.csv',index_col='row_id')
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



#### ▶ This is the code to check the total file size.
####   If you put 'train' and 'test' in '( )', you can check the capacity of each.
####   (전체 파일 용량을 확인하는 코드이다. '( )' 안에 'train'과 'test'를 넣으면 각각의 용량도 확인할 수 있다.)


```python
def mem_usage(pandas_obj):
    if isinstance(pandas_obj,pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else: # we assume if not a df it's a series
        usage_b = pandas_obj.memory_usage(deep=True)
    usage_mb = usage_b / 1024 ** 2 # convert bytes to megabytes
    return "{:03.2f} MB".format(usage_mb)
```


```python
mem_usage(train)
```




    '7.06 MB'




```python
mem_usage(test)
```




    '1.71 MB'




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
      <th>date</th>
      <th>country</th>
      <th>store</th>
      <th>product</th>
      <th>num_sold</th>
    </tr>
    <tr>
      <th>row_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015-01-01</td>
      <td>Finland</td>
      <td>KaggleMart</td>
      <td>Kaggle Mug</td>
      <td>329</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015-01-01</td>
      <td>Finland</td>
      <td>KaggleMart</td>
      <td>Kaggle Hat</td>
      <td>520</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015-01-01</td>
      <td>Finland</td>
      <td>KaggleMart</td>
      <td>Kaggle Sticker</td>
      <td>146</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015-01-01</td>
      <td>Finland</td>
      <td>KaggleRama</td>
      <td>Kaggle Mug</td>
      <td>572</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015-01-01</td>
      <td>Finland</td>
      <td>KaggleRama</td>
      <td>Kaggle Hat</td>
      <td>911</td>
    </tr>
  </tbody>
</table>
</div>




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
      <th>date</th>
      <th>country</th>
      <th>store</th>
      <th>product</th>
    </tr>
    <tr>
      <th>row_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>26298</th>
      <td>2019-01-01</td>
      <td>Finland</td>
      <td>KaggleMart</td>
      <td>Kaggle Mug</td>
    </tr>
    <tr>
      <th>26299</th>
      <td>2019-01-01</td>
      <td>Finland</td>
      <td>KaggleMart</td>
      <td>Kaggle Hat</td>
    </tr>
    <tr>
      <th>26300</th>
      <td>2019-01-01</td>
      <td>Finland</td>
      <td>KaggleMart</td>
      <td>Kaggle Sticker</td>
    </tr>
    <tr>
      <th>26301</th>
      <td>2019-01-01</td>
      <td>Finland</td>
      <td>KaggleRama</td>
      <td>Kaggle Mug</td>
    </tr>
    <tr>
      <th>26302</th>
      <td>2019-01-01</td>
      <td>Finland</td>
      <td>KaggleRama</td>
      <td>Kaggle Hat</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.head().style.applymap(lambda x : "background-color: #bff9ff")\
.set_table_styles([{'selector' : '', 'props' : [('border', '2px solid black')]}])
```




<style type="text/css">
#T_d674d_  {
  border: 2px solid black;
}
#T_d674d_row0_col0, #T_d674d_row0_col1, #T_d674d_row0_col2, #T_d674d_row0_col3, #T_d674d_row0_col4, #T_d674d_row0_col5, #T_d674d_row1_col0, #T_d674d_row1_col1, #T_d674d_row1_col2, #T_d674d_row1_col3, #T_d674d_row1_col4, #T_d674d_row1_col5, #T_d674d_row2_col0, #T_d674d_row2_col1, #T_d674d_row2_col2, #T_d674d_row2_col3, #T_d674d_row2_col4, #T_d674d_row2_col5, #T_d674d_row3_col0, #T_d674d_row3_col1, #T_d674d_row3_col2, #T_d674d_row3_col3, #T_d674d_row3_col4, #T_d674d_row3_col5, #T_d674d_row4_col0, #T_d674d_row4_col1, #T_d674d_row4_col2, #T_d674d_row4_col3, #T_d674d_row4_col4, #T_d674d_row4_col5 {
  background-color: #bff9ff;
}
</style>
<table id="T_d674d_">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th class="col_heading level0 col0" >row_id</th>
      <th class="col_heading level0 col1" >date</th>
      <th class="col_heading level0 col2" >country</th>
      <th class="col_heading level0 col3" >store</th>
      <th class="col_heading level0 col4" >product</th>
      <th class="col_heading level0 col5" >num_sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d674d_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_d674d_row0_col0" class="data row0 col0" >0</td>
      <td id="T_d674d_row0_col1" class="data row0 col1" >2015-01-01</td>
      <td id="T_d674d_row0_col2" class="data row0 col2" >Finland</td>
      <td id="T_d674d_row0_col3" class="data row0 col3" >KaggleMart</td>
      <td id="T_d674d_row0_col4" class="data row0 col4" >Kaggle Mug</td>
      <td id="T_d674d_row0_col5" class="data row0 col5" >329</td>
    </tr>
    <tr>
      <th id="T_d674d_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_d674d_row1_col0" class="data row1 col0" >1</td>
      <td id="T_d674d_row1_col1" class="data row1 col1" >2015-01-01</td>
      <td id="T_d674d_row1_col2" class="data row1 col2" >Finland</td>
      <td id="T_d674d_row1_col3" class="data row1 col3" >KaggleMart</td>
      <td id="T_d674d_row1_col4" class="data row1 col4" >Kaggle Hat</td>
      <td id="T_d674d_row1_col5" class="data row1 col5" >520</td>
    </tr>
    <tr>
      <th id="T_d674d_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_d674d_row2_col0" class="data row2 col0" >2</td>
      <td id="T_d674d_row2_col1" class="data row2 col1" >2015-01-01</td>
      <td id="T_d674d_row2_col2" class="data row2 col2" >Finland</td>
      <td id="T_d674d_row2_col3" class="data row2 col3" >KaggleMart</td>
      <td id="T_d674d_row2_col4" class="data row2 col4" >Kaggle Sticker</td>
      <td id="T_d674d_row2_col5" class="data row2 col5" >146</td>
    </tr>
    <tr>
      <th id="T_d674d_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_d674d_row3_col0" class="data row3 col0" >3</td>
      <td id="T_d674d_row3_col1" class="data row3 col1" >2015-01-01</td>
      <td id="T_d674d_row3_col2" class="data row3 col2" >Finland</td>
      <td id="T_d674d_row3_col3" class="data row3 col3" >KaggleRama</td>
      <td id="T_d674d_row3_col4" class="data row3 col4" >Kaggle Mug</td>
      <td id="T_d674d_row3_col5" class="data row3 col5" >572</td>
    </tr>
    <tr>
      <th id="T_d674d_level0_row4" class="row_heading level0 row4" >4</th>
      <td id="T_d674d_row4_col0" class="data row4 col0" >4</td>
      <td id="T_d674d_row4_col1" class="data row4 col1" >2015-01-01</td>
      <td id="T_d674d_row4_col2" class="data row4 col2" >Finland</td>
      <td id="T_d674d_row4_col3" class="data row4 col3" >KaggleRama</td>
      <td id="T_d674d_row4_col4" class="data row4 col4" >Kaggle Hat</td>
      <td id="T_d674d_row4_col5" class="data row4 col5" >911</td>
    </tr>
  </tbody>
</table>





```python
data = data.drop('row_id', axis=1)
data.head()

data.date = pd.to_datetime(data.date)
data.date.dtype
```




    dtype('<M8[ns]')




```python
prop = pd.DataFrame(data.groupby('product')['num_sold'].sum()).reset_index()

prop.num_sold = prop.num_sold/prop.num_sold.sum()
prop.style.applymap(lambda x : "background-color: #bff9ff")\
.set_table_styles([{'selector' : '', 'props' : [('border', '2px solid black')]}])
```




<style type="text/css">
#T_163f9_  {
  border: 2px solid black;
}
#T_163f9_row0_col0, #T_163f9_row0_col1, #T_163f9_row1_col0, #T_163f9_row1_col1, #T_163f9_row2_col0, #T_163f9_row2_col1 {
  background-color: #bff9ff;
}
</style>
<table id="T_163f9_">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th class="col_heading level0 col0" >product</th>
      <th class="col_heading level0 col1" >num_sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_163f9_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_163f9_row0_col0" class="data row0 col0" >Kaggle Hat</td>
      <td id="T_163f9_row0_col1" class="data row0 col1" >0.540896</td>
    </tr>
    <tr>
      <th id="T_163f9_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_163f9_row1_col0" class="data row1 col0" >Kaggle Mug</td>
      <td id="T_163f9_row1_col1" class="data row1 col1" >0.304796</td>
    </tr>
    <tr>
      <th id="T_163f9_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_163f9_row2_col0" class="data row2 col0" >Kaggle Sticker</td>
      <td id="T_163f9_row2_col1" class="data row2 col1" >0.154308</td>
    </tr>
  </tbody>
</table>





```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
train.describe
```




    <bound method NDFrame.describe of               date  country       store         product  num_sold
    row_id                                                           
    0       2015-01-01  Finland  KaggleMart      Kaggle Mug       329
    1       2015-01-01  Finland  KaggleMart      Kaggle Hat       520
    2       2015-01-01  Finland  KaggleMart  Kaggle Sticker       146
    3       2015-01-01  Finland  KaggleRama      Kaggle Mug       572
    4       2015-01-01  Finland  KaggleRama      Kaggle Hat       911
    ...            ...      ...         ...             ...       ...
    26293   2018-12-31   Sweden  KaggleMart      Kaggle Hat       823
    26294   2018-12-31   Sweden  KaggleMart  Kaggle Sticker       250
    26295   2018-12-31   Sweden  KaggleRama      Kaggle Mug      1004
    26296   2018-12-31   Sweden  KaggleRama      Kaggle Hat      1441
    26297   2018-12-31   Sweden  KaggleRama  Kaggle Sticker       388
    
    [26298 rows x 5 columns]>




```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
for col in ['country', 'store', 'product']:
    print(col, train[col].unique())
```

    country ['Finland' 'Norway' 'Sweden']
    store ['KaggleMart' 'KaggleRama']
    product ['Kaggle Mug' 'Kaggle Hat' 'Kaggle Sticker']
    


```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
print('train date duration : ', train['date'].min(), train['date'].max())
print('test date duration : ', test['date'].min(), test['date'].max())
```

    train date duration :  2015-01-01 2018-12-31
    test date duration :  2019-01-01 2019-12-31
    

#### Train dataset is data for 3 years from 2015 to 2018, and test dataset is data for 1 year from 2019.
#### (Train 데이터셋은 2015년부터 2018년까지 3년간의 데이터이고, 테스트 데이터셋은 2019년부터 1년간의 데이터입니다.)


```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
for col in ['country', 'store', 'product']:
    display(pd.DataFrame(train[col].value_counts()))
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
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Finland</th>
      <td>8766</td>
    </tr>
    <tr>
      <th>Norway</th>
      <td>8766</td>
    </tr>
    <tr>
      <th>Sweden</th>
      <td>8766</td>
    </tr>
  </tbody>
</table>
</div>



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
      <th>store</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>KaggleMart</th>
      <td>13149</td>
    </tr>
    <tr>
      <th>KaggleRama</th>
      <td>13149</td>
    </tr>
  </tbody>
</table>
</div>



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
      <th>product</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Kaggle Mug</th>
      <td>8766</td>
    </tr>
    <tr>
      <th>Kaggle Hat</th>
      <td>8766</td>
    </tr>
    <tr>
      <th>Kaggle Sticker</th>
      <td>8766</td>
    </tr>
  </tbody>
</table>
</div>



```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
for col in ['country', 'store', 'product']:
    display(pd.DataFrame(test[col].value_counts()))
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
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Finland</th>
      <td>2190</td>
    </tr>
    <tr>
      <th>Norway</th>
      <td>2190</td>
    </tr>
    <tr>
      <th>Sweden</th>
      <td>2190</td>
    </tr>
  </tbody>
</table>
</div>



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
      <th>store</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>KaggleMart</th>
      <td>3285</td>
    </tr>
    <tr>
      <th>KaggleRama</th>
      <td>3285</td>
    </tr>
  </tbody>
</table>
</div>



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
      <th>product</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Kaggle Mug</th>
      <td>2190</td>
    </tr>
    <tr>
      <th>Kaggle Hat</th>
      <td>2190</td>
    </tr>
    <tr>
      <th>Kaggle Sticker</th>
      <td>2190</td>
    </tr>
  </tbody>
</table>
</div>



```python
train.isnull().sum()
```




    date        0
    country     0
    store       0
    product     0
    num_sold    0
    dtype: int64




```python
test.isnull().sum()
```




    date       0
    country    0
    store      0
    product    0
    dtype: int64




```python
train.isna().sum()
```




    date        0
    country     0
    store       0
    product     0
    num_sold    0
    dtype: int64




```python
test.isna().sum()
```




    date       0
    country    0
    store      0
    product    0
    dtype: int64



# Preprocessing & Visualization (전처리와 시각화)
#### Time series data needs to be preprocessed for data analysis, feature engineering, visualization, etc.
#### (시계열 데이터는 데이터 분석, 피쳐 엔지니어링, 시각화 등을 위해 전처리해야 합니다.)

#### ▶ The date column type is text. Convert to datetime type for easy handling in pandas. 
#### (날짜 열 유형은 텍스트입니다. pandas에서 쉽게 처리할 수 있도록 datetime형으로 변환합니다.)


```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
train['date'] = pd.to_datetime(train['date'])
test['date'] = pd.to_datetime(test['date'])
```

#### Pivot Table (time) (피벗 테이블(시간))
#### ▶ by date (날짜 별)


```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
train_date = train.set_index('date').pivot(columns=['country', 'store', 'product'], values='num_sold')
train_date.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>country</th>
      <th colspan="6" halign="left">Finland</th>
      <th colspan="6" halign="left">Norway</th>
      <th colspan="6" halign="left">Sweden</th>
    </tr>
    <tr>
      <th>store</th>
      <th colspan="3" halign="left">KaggleMart</th>
      <th colspan="3" halign="left">KaggleRama</th>
      <th colspan="3" halign="left">KaggleMart</th>
      <th colspan="3" halign="left">KaggleRama</th>
      <th colspan="3" halign="left">KaggleMart</th>
      <th colspan="3" halign="left">KaggleRama</th>
    </tr>
    <tr>
      <th>product</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Sticker</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Sticker</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Sticker</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Sticker</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Sticker</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Sticker</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015-01-01</th>
      <td>329</td>
      <td>520</td>
      <td>146</td>
      <td>572</td>
      <td>911</td>
      <td>283</td>
      <td>526</td>
      <td>906</td>
      <td>250</td>
      <td>1005</td>
      <td>1461</td>
      <td>395</td>
      <td>440</td>
      <td>624</td>
      <td>175</td>
      <td>706</td>
      <td>1195</td>
      <td>324</td>
    </tr>
    <tr>
      <th>2015-01-02</th>
      <td>318</td>
      <td>493</td>
      <td>127</td>
      <td>544</td>
      <td>794</td>
      <td>249</td>
      <td>538</td>
      <td>845</td>
      <td>237</td>
      <td>949</td>
      <td>1446</td>
      <td>415</td>
      <td>384</td>
      <td>572</td>
      <td>155</td>
      <td>653</td>
      <td>986</td>
      <td>293</td>
    </tr>
    <tr>
      <th>2015-01-03</th>
      <td>360</td>
      <td>535</td>
      <td>141</td>
      <td>579</td>
      <td>843</td>
      <td>265</td>
      <td>614</td>
      <td>930</td>
      <td>254</td>
      <td>1029</td>
      <td>1631</td>
      <td>451</td>
      <td>420</td>
      <td>630</td>
      <td>173</td>
      <td>734</td>
      <td>1167</td>
      <td>319</td>
    </tr>
    <tr>
      <th>2015-01-04</th>
      <td>332</td>
      <td>544</td>
      <td>125</td>
      <td>582</td>
      <td>873</td>
      <td>245</td>
      <td>589</td>
      <td>889</td>
      <td>255</td>
      <td>957</td>
      <td>1540</td>
      <td>455</td>
      <td>406</td>
      <td>697</td>
      <td>169</td>
      <td>657</td>
      <td>1112</td>
      <td>300</td>
    </tr>
    <tr>
      <th>2015-01-05</th>
      <td>243</td>
      <td>378</td>
      <td>102</td>
      <td>423</td>
      <td>668</td>
      <td>187</td>
      <td>435</td>
      <td>671</td>
      <td>184</td>
      <td>739</td>
      <td>1126</td>
      <td>310</td>
      <td>298</td>
      <td>442</td>
      <td>127</td>
      <td>512</td>
      <td>796</td>
      <td>227</td>
    </tr>
  </tbody>
</table>
</div>



#### ▶ by month (월 별)
#### ▶ For grouping by month, I recommend using pandas' latest feature grouper.
####   (월 별 그룹화는 pandas의 최신 기능 그룹화를 사용하는 것이 좋습니다.)


```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
train_month = train.set_index('date').groupby([pd.Grouper(freq='M'), 'country', 'store', 'product'])['num_sold'].mean().unstack([1, 2, 3])
train_month_country = train.set_index('date').groupby([pd.Grouper(freq='M'), 'country'])['num_sold'].mean().unstack()
train_month.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>country</th>
      <th colspan="6" halign="left">Finland</th>
      <th colspan="6" halign="left">Norway</th>
      <th colspan="6" halign="left">Sweden</th>
    </tr>
    <tr>
      <th>store</th>
      <th colspan="3" halign="left">KaggleMart</th>
      <th colspan="3" halign="left">KaggleRama</th>
      <th colspan="3" halign="left">KaggleMart</th>
      <th colspan="3" halign="left">KaggleRama</th>
      <th colspan="3" halign="left">KaggleMart</th>
      <th colspan="3" halign="left">KaggleRama</th>
    </tr>
    <tr>
      <th>product</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Sticker</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Sticker</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Sticker</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Sticker</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Sticker</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Sticker</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015-01-31</th>
      <td>367.612903</td>
      <td>221.193548</td>
      <td>97.096774</td>
      <td>623.967742</td>
      <td>388.903226</td>
      <td>172.129032</td>
      <td>613.451613</td>
      <td>382.645161</td>
      <td>167.516129</td>
      <td>1074.225806</td>
      <td>650.419355</td>
      <td>290.419355</td>
      <td>436.290323</td>
      <td>269.516129</td>
      <td>119.032258</td>
      <td>769.387097</td>
      <td>470.096774</td>
      <td>204.064516</td>
    </tr>
    <tr>
      <th>2015-02-28</th>
      <td>362.928571</td>
      <td>193.535714</td>
      <td>88.928571</td>
      <td>632.857143</td>
      <td>341.785714</td>
      <td>154.178571</td>
      <td>623.321429</td>
      <td>338.857143</td>
      <td>154.928571</td>
      <td>1096.964286</td>
      <td>587.535714</td>
      <td>269.750000</td>
      <td>441.107143</td>
      <td>239.142857</td>
      <td>108.821429</td>
      <td>749.714286</td>
      <td>408.642857</td>
      <td>191.607143</td>
    </tr>
    <tr>
      <th>2015-03-31</th>
      <td>383.774194</td>
      <td>185.967742</td>
      <td>90.290323</td>
      <td>663.516129</td>
      <td>324.387097</td>
      <td>156.419355</td>
      <td>656.096774</td>
      <td>322.548387</td>
      <td>157.096774</td>
      <td>1165.290323</td>
      <td>555.419355</td>
      <td>272.193548</td>
      <td>455.580645</td>
      <td>224.096774</td>
      <td>107.225806</td>
      <td>800.612903</td>
      <td>397.129032</td>
      <td>189.322581</td>
    </tr>
    <tr>
      <th>2015-04-30</th>
      <td>407.800000</td>
      <td>184.633333</td>
      <td>95.666667</td>
      <td>704.733333</td>
      <td>317.800000</td>
      <td>167.466667</td>
      <td>736.266667</td>
      <td>329.000000</td>
      <td>168.333333</td>
      <td>1254.666667</td>
      <td>569.300000</td>
      <td>295.933333</td>
      <td>491.500000</td>
      <td>216.633333</td>
      <td>114.400000</td>
      <td>853.966667</td>
      <td>379.200000</td>
      <td>198.633333</td>
    </tr>
    <tr>
      <th>2015-05-31</th>
      <td>392.387097</td>
      <td>171.709677</td>
      <td>96.709677</td>
      <td>691.290323</td>
      <td>299.000000</td>
      <td>169.806452</td>
      <td>718.225806</td>
      <td>312.096774</td>
      <td>178.903226</td>
      <td>1249.000000</td>
      <td>547.903226</td>
      <td>303.548387</td>
      <td>473.838710</td>
      <td>206.451613</td>
      <td>117.838710</td>
      <td>827.709677</td>
      <td>359.354839</td>
      <td>205.387097</td>
    </tr>
  </tbody>
</table>
</div>




```python
norway  = data[data.country == 'Norway']
norway  = pd.DataFrame(norway.groupby('product')['num_sold'].sum()).reset_index()

finland = data[data.country == 'Finland']
finland = pd.DataFrame(finland.groupby('product')['num_sold'].sum()).reset_index()

sweden  = data[data.country == 'Sweden']
sweden  = pd.DataFrame(sweden.groupby('product')['num_sold'].sum()).reset_index()
```


```python
fig = make_subplots(rows=3, cols=1,
                    specs=[[{'type':'domain'}],[{'type':'domain'}],[{'type':'domain'}]],
                    vertical_spacing = 0.1)

fig.add_trace(go.Pie(
             values = norway['num_sold'],
             labels = norway['product'],
             title = dict(text = 'Distribution of<br>Kaggle Products<br>sales in Norway',
                          font = dict(size=18, family = 'monospace'),
                          ),
             hole = 0.5,
             hoverinfo='label+percent',),1,1)

fig.add_trace(go.Pie(
             values = finland['num_sold'],
             labels = finland['product'],
             title = dict(text = 'Distribution of<br>Kaggle Products<br>sales in Finland',
                          font = dict(size=18, family = 'monospace'),
                          ),
             hole = 0.5,
             hoverinfo='label+percent',),2,1)

fig.add_trace(go.Pie(
             values = sweden['num_sold'],
             labels = sweden['product'],
             title = dict(text = 'Distribution of<br>Kaggle Products<br>sales in Sweden',
                          font = dict(size=18, family = 'monospace'),
                          ),
             hole = 0.5,
             hoverinfo='label+percent',),3,1)

fig.update_traces(row=1, col=1, hoverinfo='label+percent',
                  textinfo='label+percent',
                  textfont_size=12,
                  opacity = 0.8,
                  showlegend = False,
                  marker = dict(colors = sns.color_palette('Reds').as_hex(),
                              line=dict(color='#000000', width=1)))

fig.update_traces(row=2, col=1, hoverinfo='label+percent',
                  textinfo='label+percent',
                  textfont_size=12,
                  opacity = 0.8,
                  showlegend = False,
                  marker = dict(colors = sns.color_palette('Blues').as_hex(),
                              line=dict(color='#000000', width=1)))

fig.update_traces(row=3, col=1, hoverinfo='label+percent',
                  textinfo='label+percent',
                  textfont_size=12,
                  opacity = 0.8,
                  showlegend = False,
                  marker = dict(colors = sns.color_palette('Wistia').as_hex(),
                              line=dict(color='#000000', width=1)))

fig.add_layout_image(
    dict(
        source="https://i.postimg.cc/mZ8B9tGT/image.png",
        xref="paper", yref="paper",
        x=0.05, y=0.92, opacity = 0.8,
        sizex=0.2, sizey=0.2,
        xanchor="left", yanchor="top"
    )
)

fig.add_layout_image(
    dict(
        source="https://i.postimg.cc/wv9Yydft/image.png",
        xref="paper", yref="paper",
        x=0.05, y=0.55, opacity = 0.8,
        sizex=0.2, sizey=0.2,
        xanchor="left", yanchor="top"
    )
)

fig.add_layout_image(
    dict(
        source="https://i.postimg.cc/T27vwFrw/image.png",
        xref="paper", yref="paper",
        x=0.05, y=0.18, opacity = 0.8,
        sizex=0.2, sizey=0.2,
        xanchor="left", yanchor="top"
    )
)

fig.update_layout(margin=dict(t=0, b=0, l=0, r=0),
                  paper_bgcolor = '#d5eff0',
                  height = 1200,
                  font_family   = 'monospace',)
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




<div>                            <div id="8cca672b-42bf-4151-8480-ca85273a76dc" class="plotly-graph-div" style="height:1200px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("8cca672b-42bf-4151-8480-ca85273a76dc")) {                    Plotly.newPlot(                        "8cca672b-42bf-4151-8480-ca85273a76dc",                        [{"hole":0.5,"hoverinfo":"label+percent","labels":["Kaggle Hat","Kaggle Mug","Kaggle Sticker"],"title":{"font":{"family":"monospace","size":18},"text":"Distribution of<br>Kaggle Products<br>sales in Norway"},"values":[2382896,1342174,679636],"type":"pie","domain":{"x":[0.0,1.0],"y":[0.7333333333333334,1.0]},"textfont":{"size":12},"marker":{"line":{"color":"#000000","width":1},"colors":["#fedbcc","#fcaf93","#fc8161","#f44f39","#d52221","#aa1016"]},"opacity":0.8,"showlegend":false,"textinfo":"label+percent"},{"hole":0.5,"hoverinfo":"label+percent","labels":["Kaggle Hat","Kaggle Mug","Kaggle Sticker"],"title":{"font":{"family":"monospace","size":18},"text":"Distribution of<br>Kaggle Products<br>sales in Finland"},"values":[1448445,818615,413867],"type":"pie","domain":{"x":[0.0,1.0],"y":[0.3666666666666667,0.6333333333333333]},"textfont":{"size":12},"marker":{"line":{"color":"#000000","width":1},"colors":["#dbe9f6","#bad6eb","#89bedc","#539ecd","#2b7bba","#0b559f"]},"opacity":0.8,"showlegend":false,"textinfo":"label+percent"},{"hole":0.5,"hoverinfo":"label+percent","labels":["Kaggle Hat","Kaggle Mug","Kaggle Sticker"],"title":{"font":{"family":"monospace","size":18},"text":"Distribution of<br>Kaggle Products<br>sales in Sweden"},"values":[1681124,945498,479103],"type":"pie","domain":{"x":[0.0,1.0],"y":[0.0,0.26666666666666666]},"textfont":{"size":12},"marker":{"line":{"color":"#000000","width":1},"colors":["#f3f244","#ffe216","#ffc908","#ffb500","#ffa400","#fe9200"]},"opacity":0.8,"showlegend":false,"textinfo":"label+percent"}],                        {"template":{"data":{"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmap"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmapgl"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"geo":{"bgcolor":"white","lakecolor":"white","landcolor":"#E5ECF6","showlakes":true,"showland":true,"subunitcolor":"white"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"light"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"ternary":{"aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"title":{"x":0.05},"xaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2}}},"images":[{"opacity":0.8,"sizex":0.2,"sizey":0.2,"source":"https://i.postimg.cc/mZ8B9tGT/image.png","x":0.05,"xanchor":"left","xref":"paper","y":0.92,"yanchor":"top","yref":"paper"},{"opacity":0.8,"sizex":0.2,"sizey":0.2,"source":"https://i.postimg.cc/wv9Yydft/image.png","x":0.05,"xanchor":"left","xref":"paper","y":0.55,"yanchor":"top","yref":"paper"},{"opacity":0.8,"sizex":0.2,"sizey":0.2,"source":"https://i.postimg.cc/T27vwFrw/image.png","x":0.05,"xanchor":"left","xref":"paper","y":0.18,"yanchor":"top","yref":"paper"}],"margin":{"t":0,"b":0,"l":0,"r":0},"font":{"family":"monospace"},"paper_bgcolor":"#d5eff0","height":1200},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('8cca672b-42bf-4151-8480-ca85273a76dc');
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



```python
plt.figure(figsize=(8, 4))
sns.countplot(x='country', data=train, order=train["country"].value_counts().index[:3],palette = "turbo")
plt.title("Total counts of country ", size=15)
plt.show()
```


    
![png](output_34_0.png)
    



```python
plt.figure(figsize=(8, 4))
sns.countplot(x='store', data=train, order=train["store"].value_counts().index[:2],palette = "turbo")
plt.title("Total counts of stores ", size=15)
plt.show()
```


    
![png](output_35_0.png)
    



```python
plt.figure(figsize=(7,2))
sns.countplot(x='product', data=train, order=train["product"].value_counts().index[:3],palette = "flag")
plt.title("Total count kaggle products ", size=13)
plt.show()
```


    
![png](output_36_0.png)
    



```python
train['date'] = pd.to_datetime(train['date'], format='%Y/%m/%d')
plt.figure(figsize=(15,7))
sld_time = train.groupby(['date']).sum().reset_index()
sns.lineplot(x=sld_time.date, y=sld_time.num_sold,)
plt.title('number sold over time ', fontsize=14)
plt.show()
```


    
![png](output_37_0.png)
    



```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
country_daily = train.groupby(['date','country'])[['num_sold']].sum().reset_index(level=[0,1])
for country in train['country'].unique():
    display(country_daily[country_daily['country']==country].sort_values(by=['num_sold'], ascending=False).head(30))
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
      <th>date</th>
      <th>country</th>
      <th>num_sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4374</th>
      <td>2018-12-29</td>
      <td>Finland</td>
      <td>6029</td>
    </tr>
    <tr>
      <th>4377</th>
      <td>2018-12-30</td>
      <td>Finland</td>
      <td>5869</td>
    </tr>
    <tr>
      <th>3282</th>
      <td>2017-12-30</td>
      <td>Finland</td>
      <td>5611</td>
    </tr>
    <tr>
      <th>3285</th>
      <td>2017-12-31</td>
      <td>Finland</td>
      <td>4683</td>
    </tr>
    <tr>
      <th>3279</th>
      <td>2017-12-29</td>
      <td>Finland</td>
      <td>4650</td>
    </tr>
    <tr>
      <th>2190</th>
      <td>2016-12-31</td>
      <td>Finland</td>
      <td>4414</td>
    </tr>
    <tr>
      <th>4371</th>
      <td>2018-12-28</td>
      <td>Finland</td>
      <td>4287</td>
    </tr>
    <tr>
      <th>2187</th>
      <td>2016-12-30</td>
      <td>Finland</td>
      <td>4251</td>
    </tr>
    <tr>
      <th>2184</th>
      <td>2016-12-29</td>
      <td>Finland</td>
      <td>3953</td>
    </tr>
    <tr>
      <th>4380</th>
      <td>2018-12-31</td>
      <td>Finland</td>
      <td>3951</td>
    </tr>
    <tr>
      <th>1086</th>
      <td>2015-12-29</td>
      <td>Finland</td>
      <td>3824</td>
    </tr>
    <tr>
      <th>1089</th>
      <td>2015-12-30</td>
      <td>Finland</td>
      <td>3800</td>
    </tr>
    <tr>
      <th>3276</th>
      <td>2017-12-28</td>
      <td>Finland</td>
      <td>3796</td>
    </tr>
    <tr>
      <th>2193</th>
      <td>2017-01-01</td>
      <td>Finland</td>
      <td>3614</td>
    </tr>
    <tr>
      <th>2181</th>
      <td>2016-12-28</td>
      <td>Finland</td>
      <td>3427</td>
    </tr>
    <tr>
      <th>1080</th>
      <td>2015-12-27</td>
      <td>Finland</td>
      <td>3387</td>
    </tr>
    <tr>
      <th>1083</th>
      <td>2015-12-28</td>
      <td>Finland</td>
      <td>3331</td>
    </tr>
    <tr>
      <th>3576</th>
      <td>2018-04-07</td>
      <td>Finland</td>
      <td>3318</td>
    </tr>
    <tr>
      <th>3288</th>
      <td>2018-01-01</td>
      <td>Finland</td>
      <td>3274</td>
    </tr>
    <tr>
      <th>1092</th>
      <td>2015-12-31</td>
      <td>Finland</td>
      <td>3205</td>
    </tr>
    <tr>
      <th>4368</th>
      <td>2018-12-27</td>
      <td>Finland</td>
      <td>3192</td>
    </tr>
    <tr>
      <th>3579</th>
      <td>2018-04-08</td>
      <td>Finland</td>
      <td>3068</td>
    </tr>
    <tr>
      <th>3273</th>
      <td>2017-12-27</td>
      <td>Finland</td>
      <td>3052</td>
    </tr>
    <tr>
      <th>3573</th>
      <td>2018-04-06</td>
      <td>Finland</td>
      <td>3038</td>
    </tr>
    <tr>
      <th>2526</th>
      <td>2017-04-22</td>
      <td>Finland</td>
      <td>2965</td>
    </tr>
    <tr>
      <th>1095</th>
      <td>2016-01-01</td>
      <td>Finland</td>
      <td>2927</td>
    </tr>
    <tr>
      <th>1371</th>
      <td>2016-04-02</td>
      <td>Finland</td>
      <td>2924</td>
    </tr>
    <tr>
      <th>1098</th>
      <td>2016-01-02</td>
      <td>Finland</td>
      <td>2908</td>
    </tr>
    <tr>
      <th>3570</th>
      <td>2018-04-05</td>
      <td>Finland</td>
      <td>2869</td>
    </tr>
    <tr>
      <th>3660</th>
      <td>2018-05-05</td>
      <td>Finland</td>
      <td>2822</td>
    </tr>
  </tbody>
</table>
</div>



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
      <th>date</th>
      <th>country</th>
      <th>num_sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4378</th>
      <td>2018-12-30</td>
      <td>Norway</td>
      <td>8980</td>
    </tr>
    <tr>
      <th>4375</th>
      <td>2018-12-29</td>
      <td>Norway</td>
      <td>8855</td>
    </tr>
    <tr>
      <th>3283</th>
      <td>2017-12-30</td>
      <td>Norway</td>
      <td>8388</td>
    </tr>
    <tr>
      <th>3286</th>
      <td>2017-12-31</td>
      <td>Norway</td>
      <td>7433</td>
    </tr>
    <tr>
      <th>3280</th>
      <td>2017-12-29</td>
      <td>Norway</td>
      <td>7018</td>
    </tr>
    <tr>
      <th>2191</th>
      <td>2016-12-31</td>
      <td>Norway</td>
      <td>6854</td>
    </tr>
    <tr>
      <th>4372</th>
      <td>2018-12-28</td>
      <td>Norway</td>
      <td>6427</td>
    </tr>
    <tr>
      <th>1090</th>
      <td>2015-12-30</td>
      <td>Norway</td>
      <td>6381</td>
    </tr>
    <tr>
      <th>2188</th>
      <td>2016-12-30</td>
      <td>Norway</td>
      <td>6380</td>
    </tr>
    <tr>
      <th>4381</th>
      <td>2018-12-31</td>
      <td>Norway</td>
      <td>6275</td>
    </tr>
    <tr>
      <th>1087</th>
      <td>2015-12-29</td>
      <td>Norway</td>
      <td>6038</td>
    </tr>
    <tr>
      <th>2185</th>
      <td>2016-12-29</td>
      <td>Norway</td>
      <td>5919</td>
    </tr>
    <tr>
      <th>3277</th>
      <td>2017-12-28</td>
      <td>Norway</td>
      <td>5839</td>
    </tr>
    <tr>
      <th>2194</th>
      <td>2017-01-01</td>
      <td>Norway</td>
      <td>5756</td>
    </tr>
    <tr>
      <th>3577</th>
      <td>2018-04-07</td>
      <td>Norway</td>
      <td>5631</td>
    </tr>
    <tr>
      <th>1093</th>
      <td>2015-12-31</td>
      <td>Norway</td>
      <td>5360</td>
    </tr>
    <tr>
      <th>1081</th>
      <td>2015-12-27</td>
      <td>Norway</td>
      <td>5347</td>
    </tr>
    <tr>
      <th>3289</th>
      <td>2018-01-01</td>
      <td>Norway</td>
      <td>5310</td>
    </tr>
    <tr>
      <th>3559</th>
      <td>2018-04-01</td>
      <td>Norway</td>
      <td>5254</td>
    </tr>
    <tr>
      <th>1084</th>
      <td>2015-12-28</td>
      <td>Norway</td>
      <td>5243</td>
    </tr>
    <tr>
      <th>2182</th>
      <td>2016-12-28</td>
      <td>Norway</td>
      <td>5044</td>
    </tr>
    <tr>
      <th>3724</th>
      <td>2018-05-26</td>
      <td>Norway</td>
      <td>4953</td>
    </tr>
    <tr>
      <th>3571</th>
      <td>2018-04-05</td>
      <td>Norway</td>
      <td>4933</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2015-01-03</td>
      <td>Norway</td>
      <td>4909</td>
    </tr>
    <tr>
      <th>4369</th>
      <td>2018-12-27</td>
      <td>Norway</td>
      <td>4884</td>
    </tr>
    <tr>
      <th>3556</th>
      <td>2018-03-31</td>
      <td>Norway</td>
      <td>4858</td>
    </tr>
    <tr>
      <th>3580</th>
      <td>2018-04-08</td>
      <td>Norway</td>
      <td>4840</td>
    </tr>
    <tr>
      <th>3574</th>
      <td>2018-04-06</td>
      <td>Norway</td>
      <td>4823</td>
    </tr>
    <tr>
      <th>2527</th>
      <td>2017-04-22</td>
      <td>Norway</td>
      <td>4732</td>
    </tr>
    <tr>
      <th>3565</th>
      <td>2018-04-03</td>
      <td>Norway</td>
      <td>4720</td>
    </tr>
  </tbody>
</table>
</div>



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
      <th>date</th>
      <th>country</th>
      <th>num_sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4376</th>
      <td>2018-12-29</td>
      <td>Sweden</td>
      <td>6377</td>
    </tr>
    <tr>
      <th>3284</th>
      <td>2017-12-30</td>
      <td>Sweden</td>
      <td>6248</td>
    </tr>
    <tr>
      <th>4379</th>
      <td>2018-12-30</td>
      <td>Sweden</td>
      <td>6227</td>
    </tr>
    <tr>
      <th>3287</th>
      <td>2017-12-31</td>
      <td>Sweden</td>
      <td>5488</td>
    </tr>
    <tr>
      <th>3281</th>
      <td>2017-12-29</td>
      <td>Sweden</td>
      <td>5205</td>
    </tr>
    <tr>
      <th>2192</th>
      <td>2016-12-31</td>
      <td>Sweden</td>
      <td>5173</td>
    </tr>
    <tr>
      <th>2189</th>
      <td>2016-12-30</td>
      <td>Sweden</td>
      <td>4945</td>
    </tr>
    <tr>
      <th>2186</th>
      <td>2016-12-29</td>
      <td>Sweden</td>
      <td>4734</td>
    </tr>
    <tr>
      <th>4373</th>
      <td>2018-12-28</td>
      <td>Sweden</td>
      <td>4660</td>
    </tr>
    <tr>
      <th>1088</th>
      <td>2015-12-29</td>
      <td>Sweden</td>
      <td>4603</td>
    </tr>
    <tr>
      <th>1091</th>
      <td>2015-12-30</td>
      <td>Sweden</td>
      <td>4500</td>
    </tr>
    <tr>
      <th>3278</th>
      <td>2017-12-28</td>
      <td>Sweden</td>
      <td>4496</td>
    </tr>
    <tr>
      <th>4382</th>
      <td>2018-12-31</td>
      <td>Sweden</td>
      <td>4476</td>
    </tr>
    <tr>
      <th>2195</th>
      <td>2017-01-01</td>
      <td>Sweden</td>
      <td>4306</td>
    </tr>
    <tr>
      <th>2183</th>
      <td>2016-12-28</td>
      <td>Sweden</td>
      <td>4178</td>
    </tr>
    <tr>
      <th>1094</th>
      <td>2015-12-31</td>
      <td>Sweden</td>
      <td>3995</td>
    </tr>
    <tr>
      <th>1085</th>
      <td>2015-12-28</td>
      <td>Sweden</td>
      <td>3979</td>
    </tr>
    <tr>
      <th>1082</th>
      <td>2015-12-27</td>
      <td>Sweden</td>
      <td>3843</td>
    </tr>
    <tr>
      <th>3578</th>
      <td>2018-04-07</td>
      <td>Sweden</td>
      <td>3777</td>
    </tr>
    <tr>
      <th>3290</th>
      <td>2018-01-01</td>
      <td>Sweden</td>
      <td>3671</td>
    </tr>
    <tr>
      <th>1100</th>
      <td>2016-01-02</td>
      <td>Sweden</td>
      <td>3557</td>
    </tr>
    <tr>
      <th>4370</th>
      <td>2018-12-27</td>
      <td>Sweden</td>
      <td>3479</td>
    </tr>
    <tr>
      <th>3581</th>
      <td>2018-04-08</td>
      <td>Sweden</td>
      <td>3476</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015-01-01</td>
      <td>Sweden</td>
      <td>3464</td>
    </tr>
    <tr>
      <th>1097</th>
      <td>2016-01-01</td>
      <td>Sweden</td>
      <td>3461</td>
    </tr>
    <tr>
      <th>3275</th>
      <td>2017-12-27</td>
      <td>Sweden</td>
      <td>3457</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2015-01-03</td>
      <td>Sweden</td>
      <td>3443</td>
    </tr>
    <tr>
      <th>3305</th>
      <td>2018-01-06</td>
      <td>Sweden</td>
      <td>3363</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2015-01-04</td>
      <td>Sweden</td>
      <td>3341</td>
    </tr>
    <tr>
      <th>2528</th>
      <td>2017-04-22</td>
      <td>Sweden</td>
      <td>3320</td>
    </tr>
  </tbody>
</table>
</div>


#### Grouping by month makes it easier to see overall trends. You can see the trend of peaking at the beginning and end of the year and decreasing before and after.
#### (월별로 그룹화하면 전반적인 추세를 더 쉽게 볼 수 있습니다. 
####  연초와 연말에 정점을 찍고 전후로 감소하는 추세를 볼 수 있습니다.)


```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
fig, ax = plt.subplots(1, 1, figsize=(12, 7))
train_monthly_country = train.set_index('date').groupby([pd.Grouper(freq='M'),'country'])[['num_sold']].mean()
sns.lineplot(x="date", y='num_sold', hue='country', data=train_monthly_country, ax=ax)

ax.set_ylabel('num_sold')
ax.set_title('Monthly Trend by Country', fontsize=15, fontweight='bold', loc='left')
ax.grid(alpha=0.5)
plt.show()
```


    
![png](output_40_0.png)
    


#### Day of Week (요일)
#### Time-series data, such as product sales, often have different distributions on weekends and weekdays. Using the day of the week as a feature is often very effective.
#### (제품 판매와 같은 시계열 데이터는 종종 주말과 주중의 분포가 다릅니다. 요일을 기능으로 사용하면 종종 매우 효과적입니다.)


```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
train['dayofweek'] = train['date'].dt.dayofweek
test['dayofweek'] = test['date'].dt.dayofweek
```


```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
fig, ax = plt.subplots(1, 1, figsize=(12, 7))
train_dayofweek = train.set_index('date').groupby([pd.Grouper(freq='M'), 'dayofweek'])[['num_sold']].mean()

sns.lineplot(x="date", y='num_sold', hue='dayofweek', data=train_dayofweek, ax=ax)
ax.set_title('Trend by day of the week', fontsize=15, fontweight='bold', loc='left')
ax.grid(alpha=0.5)
plt.show()
```


    
![png](output_43_0.png)
    


#### The following is a comparison by creating a weekend column in more detail.
#### (다음은 주말 칼럼을 보다 구체적으로 생성하여 비교한 것이다.)


```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
train['weekend'] = train['dayofweek'].apply(lambda x : x >= 5)
fig, ax = plt.subplots(1, 1, figsize=(12, 7))
train_weekend = train.set_index('date').groupby([pd.Grouper(freq='M'), 'weekend'])[['num_sold']].mean()
sns.lineplot(x="date", y="num_sold", hue='weekend', data=train_weekend, ax=ax)
ax.set_title('Weekend vs. Weekday Trend Comparison', fontsize=15, fontweight='bold', loc='left')
ax.grid(alpha=0.5)
plt.show()
```


    
![png](output_45_0.png)
    



```python
country_dayofweek = pd.pivot_table(train, index='country', columns='dayofweek', values='num_sold', aggfunc=np.mean)
country_dayofweek = pd.DataFrame(country_dayofweek.divide(country_dayofweek.sum(axis=1), axis=0).unstack()).reset_index(level=[0,1])
country_dayofweek.rename(columns={0:'num_sold'}, inplace=True)
country_dayofweek
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
      <th>dayofweek</th>
      <th>country</th>
      <th>num_sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Finland</td>
      <td>0.131726</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>Norway</td>
      <td>0.132270</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>Sweden</td>
      <td>0.131658</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>Finland</td>
      <td>0.131869</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>Norway</td>
      <td>0.131490</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1</td>
      <td>Sweden</td>
      <td>0.131453</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2</td>
      <td>Finland</td>
      <td>0.132289</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2</td>
      <td>Norway</td>
      <td>0.131899</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2</td>
      <td>Sweden</td>
      <td>0.132017</td>
    </tr>
    <tr>
      <th>9</th>
      <td>3</td>
      <td>Finland</td>
      <td>0.132997</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3</td>
      <td>Norway</td>
      <td>0.133000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>3</td>
      <td>Sweden</td>
      <td>0.133482</td>
    </tr>
    <tr>
      <th>12</th>
      <td>4</td>
      <td>Finland</td>
      <td>0.139886</td>
    </tr>
    <tr>
      <th>13</th>
      <td>4</td>
      <td>Norway</td>
      <td>0.139745</td>
    </tr>
    <tr>
      <th>14</th>
      <td>4</td>
      <td>Sweden</td>
      <td>0.140047</td>
    </tr>
    <tr>
      <th>15</th>
      <td>5</td>
      <td>Finland</td>
      <td>0.165803</td>
    </tr>
    <tr>
      <th>16</th>
      <td>5</td>
      <td>Norway</td>
      <td>0.166186</td>
    </tr>
    <tr>
      <th>17</th>
      <td>5</td>
      <td>Sweden</td>
      <td>0.165944</td>
    </tr>
    <tr>
      <th>18</th>
      <td>6</td>
      <td>Finland</td>
      <td>0.165430</td>
    </tr>
    <tr>
      <th>19</th>
      <td>6</td>
      <td>Norway</td>
      <td>0.165410</td>
    </tr>
    <tr>
      <th>20</th>
      <td>6</td>
      <td>Sweden</td>
      <td>0.165399</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
fig, ax = plt.subplots(figsize=(12, 9))
country_dayofweek = pd.pivot_table(train, index='country', columns='dayofweek', values='num_sold', aggfunc=np.mean)
country_dayofweek = pd.DataFrame(country_dayofweek.divide(country_dayofweek.sum(axis=1), axis=0).unstack()).reset_index(level=[0,1])
country_dayofweek.rename(columns={0:'num_sold'}, inplace=True)
# country_dayofweek.reset_index(level=[0,1])
sns.barplot(x='dayofweek', y='num_sold', hue='country',data=country_dayofweek, ax=ax)
ax.grid(axis='y',alpha=0.5, )
ax.set_xticklabels(['MON', 'TUE', 'WED','THU','FRI','SAT','SUN'])
ax.set_title('Percentage by day of the week by country', fontsize=15, fontweight='bold', loc='left')
plt.show()
```


    
![png](output_47_0.png)
    


#### You can see that Friday has a higher percentage compared to other days of the week.
#### (금요일에는 다른 요일에 비해 비율이 높은 것을 알 수 있습니다.)

#### Pivot (etc) (피벗(기타))
####  ▶ product ratio by country  (국가별 제품 비율)
#### You can check the following to see if there is a preference for each country, and there does not seem to be a significant difference.
#### (국가별 선호도가 있는지는 다음과 같이 확인할 수 있으며, 큰 차이는 없어 보입니다.)


```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
country_product = pd.pivot_table(train, index='country', columns='product', values='num_sold', aggfunc=np.mean)
country_product.divide(country_product.sum(axis=1), axis=0)
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
      <th>product</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Sticker</th>
    </tr>
    <tr>
      <th>country</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Finland</th>
      <td>0.540278</td>
      <td>0.305348</td>
      <td>0.154375</td>
    </tr>
    <tr>
      <th>Norway</th>
      <td>0.540989</td>
      <td>0.304714</td>
      <td>0.154298</td>
    </tr>
    <tr>
      <th>Sweden</th>
      <td>0.541298</td>
      <td>0.304437</td>
      <td>0.154264</td>
    </tr>
  </tbody>
</table>
</div>



#### You can check the following to see if there is a preference for each day of week, and there does not seem to be a significant difference.
#### (요일별 선호도가 있는지 다음과 같이 확인할 수 있으며, 큰 차이는 없어 보입니다.)


```python
# Code Source : https://www.kaggle.com/subinium/tps-jan-happy-new-year
country_product_dayofweek = pd.pivot_table(train, index='dayofweek', columns='product', values='num_sold', aggfunc=np.mean)
country_product_dayofweek.divide(country_product_dayofweek.sum(axis=1), axis=0)
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
      <th>product</th>
      <th>Kaggle Hat</th>
      <th>Kaggle Mug</th>
      <th>Kaggle Sticker</th>
    </tr>
    <tr>
      <th>dayofweek</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.540618</td>
      <td>0.305092</td>
      <td>0.154290</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.540861</td>
      <td>0.304648</td>
      <td>0.154491</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.541073</td>
      <td>0.304628</td>
      <td>0.154299</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.541214</td>
      <td>0.304677</td>
      <td>0.154108</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.540796</td>
      <td>0.304549</td>
      <td>0.154655</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.540148</td>
      <td>0.305577</td>
      <td>0.154275</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.541584</td>
      <td>0.304332</td>
      <td>0.154083</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Code Sorce : https://www.kaggle.com/bernhardklinger/tps-jan-2022
def pre_process(df):
    
    df['date'] = pd.to_datetime(df['date'])
    df['week']= df['date'].dt.week
    df['year'] = 'Y'+df['date'].dt.year.astype(str)
    df['quarter'] = 'Q'+df['date'].dt.quarter.astype(str)
    df['day'] = df['date'].dt.day
    df['dayofyear'] = df['date'].dt.dayofyear
    df.loc[(df.date.dt.is_leap_year) & (df.dayofyear >= 60),'dayofyear'] -= 1
    df['weekend'] = df['date'].dt.weekday >=5
    df['weekday'] = 'WD' + df['date'].dt.weekday.astype(str)
    df.drop(columns=['date'],inplace=True)   

pre_process(train)
pre_process(test)
```


```python
# Code Sorce : https://www.kaggle.com/bernhardklinger/tps-jan-2022
train.info(), test.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 26298 entries, 0 to 26297
    Data columns (total 12 columns):
     #   Column     Non-Null Count  Dtype 
    ---  ------     --------------  ----- 
     0   country    26298 non-null  object
     1   store      26298 non-null  object
     2   product    26298 non-null  object
     3   num_sold   26298 non-null  int64 
     4   dayofweek  26298 non-null  int64 
     5   weekend    26298 non-null  bool  
     6   week       26298 non-null  int64 
     7   year       26298 non-null  object
     8   quarter    26298 non-null  object
     9   day        26298 non-null  int64 
     10  dayofyear  26298 non-null  int64 
     11  weekday    26298 non-null  object
    dtypes: bool(1), int64(5), object(6)
    memory usage: 3.4+ MB
    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 6570 entries, 26298 to 32867
    Data columns (total 11 columns):
     #   Column     Non-Null Count  Dtype 
    ---  ------     --------------  ----- 
     0   country    6570 non-null   object
     1   store      6570 non-null   object
     2   product    6570 non-null   object
     3   dayofweek  6570 non-null   int64 
     4   week       6570 non-null   int64 
     5   year       6570 non-null   object
     6   quarter    6570 non-null   object
     7   day        6570 non-null   int64 
     8   dayofyear  6570 non-null   int64 
     9   weekend    6570 non-null   bool  
     10  weekday    6570 non-null   object
    dtypes: bool(1), int64(4), object(6)
    memory usage: 571.0+ KB
    




    (None, None)



# Modeling (모델링)

#### Code to calculate the 'time series data' of the second place in the 'Web Traffic Time Series Prediction' contest held in Kaggle 4 years ago
#### (4년전 캐글에서 열린 '웹 트래픽 시계열 예측' 대회에서 2등을 한 사람의 '시계열 데이터'를 계산하는 코드)


```python
# Code sorce : https://www.kaggle.com/c/web-traffic-time-series-forecasting/discussion/36414
def SMAPE(y_true, y_pred):
    denominator = (y_true + np.abs(y_pred)) / 200.0
    diff = np.abs(y_true - y_pred) / denominator
    diff[denominator == 0] = 0.0
    return np.mean(diff)
```


```python
reg = setup(data = train,
            target = 'num_sold',
            normalize=True,
            normalize_method='robust',
            transform_target = True,
            data_split_shuffle = False, 
            create_clusters = False,
            use_gpu = True,
            silent = True,
            fold=10,
            n_jobs = -1)
```


<style type="text/css">
#T_d6bbc_row16_col1, #T_d6bbc_row27_col1, #T_d6bbc_row42_col1, #T_d6bbc_row56_col1 {
  background-color: lightgreen;
}
</style>
<table id="T_d6bbc_">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th class="col_heading level0 col0" >Description</th>
      <th class="col_heading level0 col1" >Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d6bbc_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_d6bbc_row0_col0" class="data row0 col0" >session_id</td>
      <td id="T_d6bbc_row0_col1" class="data row0 col1" >1256</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_d6bbc_row1_col0" class="data row1 col0" >Target</td>
      <td id="T_d6bbc_row1_col1" class="data row1 col1" >num_sold</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_d6bbc_row2_col0" class="data row2 col0" >Original Data</td>
      <td id="T_d6bbc_row2_col1" class="data row2 col1" >(26298, 12)</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_d6bbc_row3_col0" class="data row3 col0" >Missing Values</td>
      <td id="T_d6bbc_row3_col1" class="data row3 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row4" class="row_heading level0 row4" >4</th>
      <td id="T_d6bbc_row4_col0" class="data row4 col0" >Numeric Features</td>
      <td id="T_d6bbc_row4_col1" class="data row4 col1" >3</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row5" class="row_heading level0 row5" >5</th>
      <td id="T_d6bbc_row5_col0" class="data row5 col0" >Categorical Features</td>
      <td id="T_d6bbc_row5_col1" class="data row5 col1" >8</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row6" class="row_heading level0 row6" >6</th>
      <td id="T_d6bbc_row6_col0" class="data row6 col0" >Ordinal Features</td>
      <td id="T_d6bbc_row6_col1" class="data row6 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row7" class="row_heading level0 row7" >7</th>
      <td id="T_d6bbc_row7_col0" class="data row7 col0" >High Cardinality Features</td>
      <td id="T_d6bbc_row7_col1" class="data row7 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row8" class="row_heading level0 row8" >8</th>
      <td id="T_d6bbc_row8_col0" class="data row8 col0" >High Cardinality Method</td>
      <td id="T_d6bbc_row8_col1" class="data row8 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row9" class="row_heading level0 row9" >9</th>
      <td id="T_d6bbc_row9_col0" class="data row9 col0" >Transformed Train Set</td>
      <td id="T_d6bbc_row9_col1" class="data row9 col1" >(18408, 25)</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row10" class="row_heading level0 row10" >10</th>
      <td id="T_d6bbc_row10_col0" class="data row10 col0" >Transformed Test Set</td>
      <td id="T_d6bbc_row10_col1" class="data row10 col1" >(7890, 25)</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row11" class="row_heading level0 row11" >11</th>
      <td id="T_d6bbc_row11_col0" class="data row11 col0" >Shuffle Train-Test</td>
      <td id="T_d6bbc_row11_col1" class="data row11 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row12" class="row_heading level0 row12" >12</th>
      <td id="T_d6bbc_row12_col0" class="data row12 col0" >Stratify Train-Test</td>
      <td id="T_d6bbc_row12_col1" class="data row12 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row13" class="row_heading level0 row13" >13</th>
      <td id="T_d6bbc_row13_col0" class="data row13 col0" >Fold Generator</td>
      <td id="T_d6bbc_row13_col1" class="data row13 col1" >KFold</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row14" class="row_heading level0 row14" >14</th>
      <td id="T_d6bbc_row14_col0" class="data row14 col0" >Fold Number</td>
      <td id="T_d6bbc_row14_col1" class="data row14 col1" >10</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row15" class="row_heading level0 row15" >15</th>
      <td id="T_d6bbc_row15_col0" class="data row15 col0" >CPU Jobs</td>
      <td id="T_d6bbc_row15_col1" class="data row15 col1" >-1</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row16" class="row_heading level0 row16" >16</th>
      <td id="T_d6bbc_row16_col0" class="data row16 col0" >Use GPU</td>
      <td id="T_d6bbc_row16_col1" class="data row16 col1" >True</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row17" class="row_heading level0 row17" >17</th>
      <td id="T_d6bbc_row17_col0" class="data row17 col0" >Log Experiment</td>
      <td id="T_d6bbc_row17_col1" class="data row17 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row18" class="row_heading level0 row18" >18</th>
      <td id="T_d6bbc_row18_col0" class="data row18 col0" >Experiment Name</td>
      <td id="T_d6bbc_row18_col1" class="data row18 col1" >reg-default-name</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row19" class="row_heading level0 row19" >19</th>
      <td id="T_d6bbc_row19_col0" class="data row19 col0" >USI</td>
      <td id="T_d6bbc_row19_col1" class="data row19 col1" >6fb2</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row20" class="row_heading level0 row20" >20</th>
      <td id="T_d6bbc_row20_col0" class="data row20 col0" >Imputation Type</td>
      <td id="T_d6bbc_row20_col1" class="data row20 col1" >simple</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row21" class="row_heading level0 row21" >21</th>
      <td id="T_d6bbc_row21_col0" class="data row21 col0" >Iterative Imputation Iteration</td>
      <td id="T_d6bbc_row21_col1" class="data row21 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row22" class="row_heading level0 row22" >22</th>
      <td id="T_d6bbc_row22_col0" class="data row22 col0" >Numeric Imputer</td>
      <td id="T_d6bbc_row22_col1" class="data row22 col1" >mean</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row23" class="row_heading level0 row23" >23</th>
      <td id="T_d6bbc_row23_col0" class="data row23 col0" >Iterative Imputation Numeric Model</td>
      <td id="T_d6bbc_row23_col1" class="data row23 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row24" class="row_heading level0 row24" >24</th>
      <td id="T_d6bbc_row24_col0" class="data row24 col0" >Categorical Imputer</td>
      <td id="T_d6bbc_row24_col1" class="data row24 col1" >constant</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row25" class="row_heading level0 row25" >25</th>
      <td id="T_d6bbc_row25_col0" class="data row25 col0" >Iterative Imputation Categorical Model</td>
      <td id="T_d6bbc_row25_col1" class="data row25 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row26" class="row_heading level0 row26" >26</th>
      <td id="T_d6bbc_row26_col0" class="data row26 col0" >Unknown Categoricals Handling</td>
      <td id="T_d6bbc_row26_col1" class="data row26 col1" >least_frequent</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row27" class="row_heading level0 row27" >27</th>
      <td id="T_d6bbc_row27_col0" class="data row27 col0" >Normalize</td>
      <td id="T_d6bbc_row27_col1" class="data row27 col1" >True</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row28" class="row_heading level0 row28" >28</th>
      <td id="T_d6bbc_row28_col0" class="data row28 col0" >Normalize Method</td>
      <td id="T_d6bbc_row28_col1" class="data row28 col1" >robust</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row29" class="row_heading level0 row29" >29</th>
      <td id="T_d6bbc_row29_col0" class="data row29 col0" >Transformation</td>
      <td id="T_d6bbc_row29_col1" class="data row29 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row30" class="row_heading level0 row30" >30</th>
      <td id="T_d6bbc_row30_col0" class="data row30 col0" >Transformation Method</td>
      <td id="T_d6bbc_row30_col1" class="data row30 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row31" class="row_heading level0 row31" >31</th>
      <td id="T_d6bbc_row31_col0" class="data row31 col0" >PCA</td>
      <td id="T_d6bbc_row31_col1" class="data row31 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row32" class="row_heading level0 row32" >32</th>
      <td id="T_d6bbc_row32_col0" class="data row32 col0" >PCA Method</td>
      <td id="T_d6bbc_row32_col1" class="data row32 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row33" class="row_heading level0 row33" >33</th>
      <td id="T_d6bbc_row33_col0" class="data row33 col0" >PCA Components</td>
      <td id="T_d6bbc_row33_col1" class="data row33 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row34" class="row_heading level0 row34" >34</th>
      <td id="T_d6bbc_row34_col0" class="data row34 col0" >Ignore Low Variance</td>
      <td id="T_d6bbc_row34_col1" class="data row34 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row35" class="row_heading level0 row35" >35</th>
      <td id="T_d6bbc_row35_col0" class="data row35 col0" >Combine Rare Levels</td>
      <td id="T_d6bbc_row35_col1" class="data row35 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row36" class="row_heading level0 row36" >36</th>
      <td id="T_d6bbc_row36_col0" class="data row36 col0" >Rare Level Threshold</td>
      <td id="T_d6bbc_row36_col1" class="data row36 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row37" class="row_heading level0 row37" >37</th>
      <td id="T_d6bbc_row37_col0" class="data row37 col0" >Numeric Binning</td>
      <td id="T_d6bbc_row37_col1" class="data row37 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row38" class="row_heading level0 row38" >38</th>
      <td id="T_d6bbc_row38_col0" class="data row38 col0" >Remove Outliers</td>
      <td id="T_d6bbc_row38_col1" class="data row38 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row39" class="row_heading level0 row39" >39</th>
      <td id="T_d6bbc_row39_col0" class="data row39 col0" >Outliers Threshold</td>
      <td id="T_d6bbc_row39_col1" class="data row39 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row40" class="row_heading level0 row40" >40</th>
      <td id="T_d6bbc_row40_col0" class="data row40 col0" >Remove Multicollinearity</td>
      <td id="T_d6bbc_row40_col1" class="data row40 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row41" class="row_heading level0 row41" >41</th>
      <td id="T_d6bbc_row41_col0" class="data row41 col0" >Multicollinearity Threshold</td>
      <td id="T_d6bbc_row41_col1" class="data row41 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row42" class="row_heading level0 row42" >42</th>
      <td id="T_d6bbc_row42_col0" class="data row42 col0" >Remove Perfect Collinearity</td>
      <td id="T_d6bbc_row42_col1" class="data row42 col1" >True</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row43" class="row_heading level0 row43" >43</th>
      <td id="T_d6bbc_row43_col0" class="data row43 col0" >Clustering</td>
      <td id="T_d6bbc_row43_col1" class="data row43 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row44" class="row_heading level0 row44" >44</th>
      <td id="T_d6bbc_row44_col0" class="data row44 col0" >Clustering Iteration</td>
      <td id="T_d6bbc_row44_col1" class="data row44 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row45" class="row_heading level0 row45" >45</th>
      <td id="T_d6bbc_row45_col0" class="data row45 col0" >Polynomial Features</td>
      <td id="T_d6bbc_row45_col1" class="data row45 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row46" class="row_heading level0 row46" >46</th>
      <td id="T_d6bbc_row46_col0" class="data row46 col0" >Polynomial Degree</td>
      <td id="T_d6bbc_row46_col1" class="data row46 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row47" class="row_heading level0 row47" >47</th>
      <td id="T_d6bbc_row47_col0" class="data row47 col0" >Trignometry Features</td>
      <td id="T_d6bbc_row47_col1" class="data row47 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row48" class="row_heading level0 row48" >48</th>
      <td id="T_d6bbc_row48_col0" class="data row48 col0" >Polynomial Threshold</td>
      <td id="T_d6bbc_row48_col1" class="data row48 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row49" class="row_heading level0 row49" >49</th>
      <td id="T_d6bbc_row49_col0" class="data row49 col0" >Group Features</td>
      <td id="T_d6bbc_row49_col1" class="data row49 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row50" class="row_heading level0 row50" >50</th>
      <td id="T_d6bbc_row50_col0" class="data row50 col0" >Feature Selection</td>
      <td id="T_d6bbc_row50_col1" class="data row50 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row51" class="row_heading level0 row51" >51</th>
      <td id="T_d6bbc_row51_col0" class="data row51 col0" >Feature Selection Method</td>
      <td id="T_d6bbc_row51_col1" class="data row51 col1" >classic</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row52" class="row_heading level0 row52" >52</th>
      <td id="T_d6bbc_row52_col0" class="data row52 col0" >Features Selection Threshold</td>
      <td id="T_d6bbc_row52_col1" class="data row52 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row53" class="row_heading level0 row53" >53</th>
      <td id="T_d6bbc_row53_col0" class="data row53 col0" >Feature Interaction</td>
      <td id="T_d6bbc_row53_col1" class="data row53 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row54" class="row_heading level0 row54" >54</th>
      <td id="T_d6bbc_row54_col0" class="data row54 col0" >Feature Ratio</td>
      <td id="T_d6bbc_row54_col1" class="data row54 col1" >False</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row55" class="row_heading level0 row55" >55</th>
      <td id="T_d6bbc_row55_col0" class="data row55 col0" >Interaction Threshold</td>
      <td id="T_d6bbc_row55_col1" class="data row55 col1" >None</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row56" class="row_heading level0 row56" >56</th>
      <td id="T_d6bbc_row56_col0" class="data row56 col0" >Transform Target</td>
      <td id="T_d6bbc_row56_col1" class="data row56 col1" >True</td>
    </tr>
    <tr>
      <th id="T_d6bbc_level0_row57" class="row_heading level0 row57" >57</th>
      <td id="T_d6bbc_row57_col0" class="data row57 col0" >Transform Target Method</td>
      <td id="T_d6bbc_row57_col1" class="data row57 col1" >box-cox</td>
    </tr>
  </tbody>
</table>




```python
# Code Sorce : https://www.kaggle.com/bernhardklinger/tps-jan-2022
add_metric('SMAPE', 'SMAPE', SMAPE, greater_is_better = False)
top =compare_models(sort = 'SMAPE',n_select = 3, include = ['catboost','lightgbm','xgboost']) 
```


<style type="text/css">
#T_3345f_ th {
  text-align: left;
}
#T_3345f_row0_col0, #T_3345f_row1_col0, #T_3345f_row1_col1, #T_3345f_row1_col2, #T_3345f_row1_col3, #T_3345f_row1_col4, #T_3345f_row1_col5, #T_3345f_row1_col6, #T_3345f_row1_col7, #T_3345f_row2_col0, #T_3345f_row2_col1, #T_3345f_row2_col2, #T_3345f_row2_col3, #T_3345f_row2_col4, #T_3345f_row2_col5, #T_3345f_row2_col6, #T_3345f_row2_col7 {
  text-align: left;
}
#T_3345f_row0_col1, #T_3345f_row0_col2, #T_3345f_row0_col3, #T_3345f_row0_col4, #T_3345f_row0_col5, #T_3345f_row0_col6, #T_3345f_row0_col7 {
  text-align: left;
  background-color: yellow;
}
#T_3345f_row0_col8, #T_3345f_row1_col8 {
  text-align: left;
  background-color: lightgrey;
}
#T_3345f_row2_col8 {
  text-align: left;
  background-color: yellow;
  background-color: lightgrey;
}
</style>
<table id="T_3345f_">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th class="col_heading level0 col0" >Model</th>
      <th class="col_heading level0 col1" >MAE</th>
      <th class="col_heading level0 col2" >MSE</th>
      <th class="col_heading level0 col3" >RMSE</th>
      <th class="col_heading level0 col4" >R2</th>
      <th class="col_heading level0 col5" >RMSLE</th>
      <th class="col_heading level0 col6" >MAPE</th>
      <th class="col_heading level0 col7" >SMAPE</th>
      <th class="col_heading level0 col8" >TT (Sec)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_3345f_level0_row0" class="row_heading level0 row0" >lightgbm</th>
      <td id="T_3345f_row0_col0" class="data row0 col0" >Light Gradient Boosting Machine</td>
      <td id="T_3345f_row0_col1" class="data row0 col1" >26.4778</td>
      <td id="T_3345f_row0_col2" class="data row0 col2" >2476.0365</td>
      <td id="T_3345f_row0_col3" class="data row0 col3" >46.4348</td>
      <td id="T_3345f_row0_col4" class="data row0 col4" >0.9653</td>
      <td id="T_3345f_row0_col5" class="data row0 col5" >0.0912</td>
      <td id="T_3345f_row0_col6" class="data row0 col6" >0.0670</td>
      <td id="T_3345f_row0_col7" class="data row0 col7" >6.6983</td>
      <td id="T_3345f_row0_col8" class="data row0 col8" >1.0440</td>
    </tr>
    <tr>
      <th id="T_3345f_level0_row1" class="row_heading level0 row1" >catboost</th>
      <td id="T_3345f_row1_col0" class="data row1 col0" >CatBoost Regressor</td>
      <td id="T_3345f_row1_col1" class="data row1 col1" >27.4563</td>
      <td id="T_3345f_row1_col2" class="data row1 col2" >3036.9175</td>
      <td id="T_3345f_row1_col3" class="data row1 col3" >49.7696</td>
      <td id="T_3345f_row1_col4" class="data row1 col4" >0.9589</td>
      <td id="T_3345f_row1_col5" class="data row1 col5" >0.0947</td>
      <td id="T_3345f_row1_col6" class="data row1 col6" >0.0679</td>
      <td id="T_3345f_row1_col7" class="data row1 col7" >6.7530</td>
      <td id="T_3345f_row1_col8" class="data row1 col8" >2.8350</td>
    </tr>
    <tr>
      <th id="T_3345f_level0_row2" class="row_heading level0 row2" >xgboost</th>
      <td id="T_3345f_row2_col0" class="data row2 col0" >Extreme Gradient Boosting</td>
      <td id="T_3345f_row2_col1" class="data row2 col1" >27.0547</td>
      <td id="T_3345f_row2_col2" class="data row2 col2" >2557.9026</td>
      <td id="T_3345f_row2_col3" class="data row2 col3" >47.0485</td>
      <td id="T_3345f_row2_col4" class="data row2 col4" >0.9643</td>
      <td id="T_3345f_row2_col5" class="data row2 col5" >0.0942</td>
      <td id="T_3345f_row2_col6" class="data row2 col6" >0.0682</td>
      <td id="T_3345f_row2_col7" class="data row2 col7" >6.8439</td>
      <td id="T_3345f_row2_col8" class="data row2 col8" >0.4410</td>
    </tr>
  </tbody>
</table>




```python
best_models = compare_models(top)
```


<style type="text/css">
#T_d1a67_ th {
  text-align: left;
}
#T_d1a67_row0_col0, #T_d1a67_row1_col0, #T_d1a67_row1_col1, #T_d1a67_row1_col2, #T_d1a67_row1_col3, #T_d1a67_row1_col4, #T_d1a67_row1_col5, #T_d1a67_row1_col6, #T_d1a67_row1_col7, #T_d1a67_row2_col0, #T_d1a67_row2_col1, #T_d1a67_row2_col2, #T_d1a67_row2_col3, #T_d1a67_row2_col4, #T_d1a67_row2_col5, #T_d1a67_row2_col6, #T_d1a67_row2_col7 {
  text-align: left;
}
#T_d1a67_row0_col1, #T_d1a67_row0_col2, #T_d1a67_row0_col3, #T_d1a67_row0_col4, #T_d1a67_row0_col5, #T_d1a67_row0_col6, #T_d1a67_row0_col7 {
  text-align: left;
  background-color: yellow;
}
#T_d1a67_row0_col8, #T_d1a67_row2_col8 {
  text-align: left;
  background-color: lightgrey;
}
#T_d1a67_row1_col8 {
  text-align: left;
  background-color: yellow;
  background-color: lightgrey;
}
</style>
<table id="T_d1a67_">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th class="col_heading level0 col0" >Model</th>
      <th class="col_heading level0 col1" >MAE</th>
      <th class="col_heading level0 col2" >MSE</th>
      <th class="col_heading level0 col3" >RMSE</th>
      <th class="col_heading level0 col4" >R2</th>
      <th class="col_heading level0 col5" >RMSLE</th>
      <th class="col_heading level0 col6" >MAPE</th>
      <th class="col_heading level0 col7" >SMAPE</th>
      <th class="col_heading level0 col8" >TT (Sec)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d1a67_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_d1a67_row0_col0" class="data row0 col0" >Light Gradient Boosting Machine</td>
      <td id="T_d1a67_row0_col1" class="data row0 col1" >26.5439</td>
      <td id="T_d1a67_row0_col2" class="data row0 col2" >2487.1471</td>
      <td id="T_d1a67_row0_col3" class="data row0 col3" >46.5142</td>
      <td id="T_d1a67_row0_col4" class="data row0 col4" >0.9652</td>
      <td id="T_d1a67_row0_col5" class="data row0 col5" >0.0915</td>
      <td id="T_d1a67_row0_col6" class="data row0 col6" >0.0671</td>
      <td id="T_d1a67_row0_col7" class="data row0 col7" >6.7180</td>
      <td id="T_d1a67_row0_col8" class="data row0 col8" >0.4970</td>
    </tr>
    <tr>
      <th id="T_d1a67_level0_row1" class="row_heading level0 row1" >2</th>
      <td id="T_d1a67_row1_col0" class="data row1 col0" >Extreme Gradient Boosting</td>
      <td id="T_d1a67_row1_col1" class="data row1 col1" >27.0547</td>
      <td id="T_d1a67_row1_col2" class="data row1 col2" >2557.9026</td>
      <td id="T_d1a67_row1_col3" class="data row1 col3" >47.0485</td>
      <td id="T_d1a67_row1_col4" class="data row1 col4" >0.9643</td>
      <td id="T_d1a67_row1_col5" class="data row1 col5" >0.0942</td>
      <td id="T_d1a67_row1_col6" class="data row1 col6" >0.0682</td>
      <td id="T_d1a67_row1_col7" class="data row1 col7" >6.8439</td>
      <td id="T_d1a67_row1_col8" class="data row1 col8" >0.3730</td>
    </tr>
    <tr>
      <th id="T_d1a67_level0_row2" class="row_heading level0 row2" >1</th>
      <td id="T_d1a67_row2_col0" class="data row2 col0" >CatBoost Regressor</td>
      <td id="T_d1a67_row2_col1" class="data row2 col1" >27.4563</td>
      <td id="T_d1a67_row2_col2" class="data row2 col2" >3036.9175</td>
      <td id="T_d1a67_row2_col3" class="data row2 col3" >49.7696</td>
      <td id="T_d1a67_row2_col4" class="data row2 col4" >0.9589</td>
      <td id="T_d1a67_row2_col5" class="data row2 col5" >0.0947</td>
      <td id="T_d1a67_row2_col6" class="data row2 col6" >0.0679</td>
      <td id="T_d1a67_row2_col7" class="data row2 col7" >6.7530</td>
      <td id="T_d1a67_row2_col8" class="data row2 col8" >2.8350</td>
    </tr>
  </tbody>
</table>




```python
# Code Sorce : https://www.kaggle.com/bernhardklinger/tps-jan-2022
blend = blend_models(top)
predict_model(blend)
```


<style type="text/css">
#T_6c319_row10_col0, #T_6c319_row10_col1, #T_6c319_row10_col2, #T_6c319_row10_col3, #T_6c319_row10_col4, #T_6c319_row10_col5, #T_6c319_row10_col6 {
  background: yellow;
}
</style>
<table id="T_6c319_">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th class="col_heading level0 col0" >MAE</th>
      <th class="col_heading level0 col1" >MSE</th>
      <th class="col_heading level0 col2" >RMSE</th>
      <th class="col_heading level0 col3" >R2</th>
      <th class="col_heading level0 col4" >RMSLE</th>
      <th class="col_heading level0 col5" >MAPE</th>
      <th class="col_heading level0 col6" >SMAPE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_6c319_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_6c319_row0_col0" class="data row0 col0" >30.0974</td>
      <td id="T_6c319_row0_col1" class="data row0 col1" >3187.3524</td>
      <td id="T_6c319_row0_col2" class="data row0 col2" >56.4566</td>
      <td id="T_6c319_row0_col3" class="data row0 col3" >0.9601</td>
      <td id="T_6c319_row0_col4" class="data row0 col4" >0.1014</td>
      <td id="T_6c319_row0_col5" class="data row0 col5" >0.0690</td>
      <td id="T_6c319_row0_col6" class="data row0 col6" >7.0693</td>
    </tr>
    <tr>
      <th id="T_6c319_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_6c319_row1_col0" class="data row1 col0" >35.4112</td>
      <td id="T_6c319_row1_col1" class="data row1 col1" >2911.4366</td>
      <td id="T_6c319_row1_col2" class="data row1 col2" >53.9577</td>
      <td id="T_6c319_row1_col3" class="data row1 col3" >0.9579</td>
      <td id="T_6c319_row1_col4" class="data row1 col4" >0.1162</td>
      <td id="T_6c319_row1_col5" class="data row1 col5" >0.1002</td>
      <td id="T_6c319_row1_col6" class="data row1 col6" >9.3873</td>
    </tr>
    <tr>
      <th id="T_6c319_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_6c319_row2_col0" class="data row2 col0" >13.9867</td>
      <td id="T_6c319_row2_col1" class="data row2 col1" >413.6943</td>
      <td id="T_6c319_row2_col2" class="data row2 col2" >20.3395</td>
      <td id="T_6c319_row2_col3" class="data row2 col3" >0.9870</td>
      <td id="T_6c319_row2_col4" class="data row2 col4" >0.0558</td>
      <td id="T_6c319_row2_col5" class="data row2 col5" >0.0453</td>
      <td id="T_6c319_row2_col6" class="data row2 col6" >4.4456</td>
    </tr>
    <tr>
      <th id="T_6c319_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_6c319_row3_col0" class="data row3 col0" >27.8423</td>
      <td id="T_6c319_row3_col1" class="data row3 col1" >2582.1833</td>
      <td id="T_6c319_row3_col2" class="data row3 col2" >50.8152</td>
      <td id="T_6c319_row3_col3" class="data row3 col3" >0.9619</td>
      <td id="T_6c319_row3_col4" class="data row3 col4" >0.1019</td>
      <td id="T_6c319_row3_col5" class="data row3 col5" >0.0708</td>
      <td id="T_6c319_row3_col6" class="data row3 col6" >6.6853</td>
    </tr>
    <tr>
      <th id="T_6c319_level0_row4" class="row_heading level0 row4" >4</th>
      <td id="T_6c319_row4_col0" class="data row4 col0" >34.4194</td>
      <td id="T_6c319_row4_col1" class="data row4 col1" >4221.2063</td>
      <td id="T_6c319_row4_col2" class="data row4 col2" >64.9708</td>
      <td id="T_6c319_row4_col3" class="data row4 col3" >0.9491</td>
      <td id="T_6c319_row4_col4" class="data row4 col4" >0.1145</td>
      <td id="T_6c319_row4_col5" class="data row4 col5" >0.0777</td>
      <td id="T_6c319_row4_col6" class="data row4 col6" >8.0964</td>
    </tr>
    <tr>
      <th id="T_6c319_level0_row5" class="row_heading level0 row5" >5</th>
      <td id="T_6c319_row5_col0" class="data row5 col0" >19.8335</td>
      <td id="T_6c319_row5_col1" class="data row5 col1" >1007.8525</td>
      <td id="T_6c319_row5_col2" class="data row5 col2" >31.7467</td>
      <td id="T_6c319_row5_col3" class="data row5 col3" >0.9770</td>
      <td id="T_6c319_row5_col4" class="data row5 col4" >0.0737</td>
      <td id="T_6c319_row5_col5" class="data row5 col5" >0.0598</td>
      <td id="T_6c319_row5_col6" class="data row5 col6" >5.7670</td>
    </tr>
    <tr>
      <th id="T_6c319_level0_row6" class="row_heading level0 row6" >6</th>
      <td id="T_6c319_row6_col0" class="data row6 col0" >14.5810</td>
      <td id="T_6c319_row6_col1" class="data row6 col1" >444.0523</td>
      <td id="T_6c319_row6_col2" class="data row6 col2" >21.0725</td>
      <td id="T_6c319_row6_col3" class="data row6 col3" >0.9860</td>
      <td id="T_6c319_row6_col4" class="data row6 col4" >0.0581</td>
      <td id="T_6c319_row6_col5" class="data row6 col5" >0.0453</td>
      <td id="T_6c319_row6_col6" class="data row6 col6" >4.5424</td>
    </tr>
    <tr>
      <th id="T_6c319_level0_row7" class="row_heading level0 row7" >7</th>
      <td id="T_6c319_row7_col0" class="data row7 col0" >33.7929</td>
      <td id="T_6c319_row7_col1" class="data row7 col1" >5585.3312</td>
      <td id="T_6c319_row7_col2" class="data row7 col2" >74.7351</td>
      <td id="T_6c319_row7_col3" class="data row7 col3" >0.9371</td>
      <td id="T_6c319_row7_col4" class="data row7 col4" >0.1127</td>
      <td id="T_6c319_row7_col5" class="data row7 col5" >0.0650</td>
      <td id="T_6c319_row7_col6" class="data row7 col6" >6.9509</td>
    </tr>
    <tr>
      <th id="T_6c319_level0_row8" class="row_heading level0 row8" >8</th>
      <td id="T_6c319_row8_col0" class="data row8 col0" >34.4807</td>
      <td id="T_6c319_row8_col1" class="data row8 col1" >4201.7844</td>
      <td id="T_6c319_row8_col2" class="data row8 col2" >64.8212</td>
      <td id="T_6c319_row8_col3" class="data row8 col3" >0.9525</td>
      <td id="T_6c319_row8_col4" class="data row8 col4" >0.1139</td>
      <td id="T_6c319_row8_col5" class="data row8 col5" >0.0753</td>
      <td id="T_6c319_row8_col6" class="data row8 col6" >7.9423</td>
    </tr>
    <tr>
      <th id="T_6c319_level0_row9" class="row_heading level0 row9" >9</th>
      <td id="T_6c319_row9_col0" class="data row9 col0" >15.3415</td>
      <td id="T_6c319_row9_col1" class="data row9 col1" >486.8727</td>
      <td id="T_6c319_row9_col2" class="data row9 col2" >22.0652</td>
      <td id="T_6c319_row9_col3" class="data row9 col3" >0.9873</td>
      <td id="T_6c319_row9_col4" class="data row9 col4" >0.0550</td>
      <td id="T_6c319_row9_col5" class="data row9 col5" >0.0442</td>
      <td id="T_6c319_row9_col6" class="data row9 col6" >4.4627</td>
    </tr>
    <tr>
      <th id="T_6c319_level0_row10" class="row_heading level0 row10" >Mean</th>
      <td id="T_6c319_row10_col0" class="data row10 col0" >25.9786</td>
      <td id="T_6c319_row10_col1" class="data row10 col1" >2504.1766</td>
      <td id="T_6c319_row10_col2" class="data row10 col2" >46.0981</td>
      <td id="T_6c319_row10_col3" class="data row10 col3" >0.9656</td>
      <td id="T_6c319_row10_col4" class="data row10 col4" >0.0903</td>
      <td id="T_6c319_row10_col5" class="data row10 col5" >0.0653</td>
      <td id="T_6c319_row10_col6" class="data row10 col6" >6.5349</td>
    </tr>
    <tr>
      <th id="T_6c319_level0_row11" class="row_heading level0 row11" >SD</th>
      <td id="T_6c319_row11_col0" class="data row11 col0" >8.5943</td>
      <td id="T_6c319_row11_col1" class="data row11 col1" >1757.4123</td>
      <td id="T_6c319_row11_col2" class="data row11 col2" >19.4717</td>
      <td id="T_6c319_row11_col3" class="data row11 col3" >0.0168</td>
      <td id="T_6c319_row11_col4" class="data row11 col4" >0.0252</td>
      <td id="T_6c319_row11_col5" class="data row11 col5" >0.0167</td>
      <td id="T_6c319_row11_col6" class="data row11 col6" >1.6203</td>
    </tr>
  </tbody>
</table>




<style type="text/css">
</style>
<table id="T_14321_">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th class="col_heading level0 col0" >Model</th>
      <th class="col_heading level0 col1" >MAE</th>
      <th class="col_heading level0 col2" >MSE</th>
      <th class="col_heading level0 col3" >RMSE</th>
      <th class="col_heading level0 col4" >R2</th>
      <th class="col_heading level0 col5" >RMSLE</th>
      <th class="col_heading level0 col6" >MAPE</th>
      <th class="col_heading level0 col7" >SMAPE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_14321_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_14321_row0_col0" class="data row0 col0" >Voting Regressor</td>
      <td id="T_14321_row0_col1" class="data row0 col1" >42.5749</td>
      <td id="T_14321_row0_col2" class="data row0 col2" >5527.1179</td>
      <td id="T_14321_row0_col3" class="data row0 col3" >74.3446</td>
      <td id="T_14321_row0_col4" class="data row0 col4" >0.9348</td>
      <td id="T_14321_row0_col5" class="data row0 col5" >0.1192</td>
      <td id="T_14321_row0_col6" class="data row0 col6" >0.0881</td>
      <td id="T_14321_row0_col7" class="data row0 col7" >9.3742</td>
    </tr>
  </tbody>
</table>






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
      <th>week</th>
      <th>day</th>
      <th>dayofyear</th>
      <th>country_Finland</th>
      <th>country_Norway</th>
      <th>country_Sweden</th>
      <th>store_KaggleRama</th>
      <th>product_Kaggle Hat</th>
      <th>product_Kaggle Mug</th>
      <th>product_Kaggle Sticker</th>
      <th>...</th>
      <th>quarter_Q1</th>
      <th>quarter_Q2</th>
      <th>quarter_Q3</th>
      <th>quarter_Q4</th>
      <th>weekday_WD0</th>
      <th>weekday_WD1</th>
      <th>weekday_WD3</th>
      <th>weekday_WD6</th>
      <th>num_sold</th>
      <th>Label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.708333</td>
      <td>0.2</td>
      <td>0.707602</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>223</td>
      <td>223.599741</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.708333</td>
      <td>0.2</td>
      <td>0.707602</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>303</td>
      <td>301.143469</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.708333</td>
      <td>0.2</td>
      <td>0.707602</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>112</td>
      <td>109.308410</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.708333</td>
      <td>0.2</td>
      <td>0.707602</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>419</td>
      <td>385.684089</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.708333</td>
      <td>0.2</td>
      <td>0.707602</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>550</td>
      <td>524.650568</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7885</th>
      <td>-1.000000</td>
      <td>1.0</td>
      <td>1.134503</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>823</td>
      <td>648.333201</td>
    </tr>
    <tr>
      <th>7886</th>
      <td>-1.000000</td>
      <td>1.0</td>
      <td>1.134503</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>250</td>
      <td>219.045871</td>
    </tr>
    <tr>
      <th>7887</th>
      <td>-1.000000</td>
      <td>1.0</td>
      <td>1.134503</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1004</td>
      <td>753.086341</td>
    </tr>
    <tr>
      <th>7888</th>
      <td>-1.000000</td>
      <td>1.0</td>
      <td>1.134503</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1441</td>
      <td>1189.189096</td>
    </tr>
    <tr>
      <th>7889</th>
      <td>-1.000000</td>
      <td>1.0</td>
      <td>1.134503</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>388</td>
      <td>381.601778</td>
    </tr>
  </tbody>
</table>
<p>7890 rows × 27 columns</p>
</div>




```python
# Code Sorce : https://www.kaggle.com/bernhardklinger/tps-jan-2022
final_blend = finalize_model(blend)  
predict_model(final_blend)
```


<style type="text/css">
</style>
<table id="T_d6dcd_">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th class="col_heading level0 col0" >Model</th>
      <th class="col_heading level0 col1" >MAE</th>
      <th class="col_heading level0 col2" >MSE</th>
      <th class="col_heading level0 col3" >RMSE</th>
      <th class="col_heading level0 col4" >R2</th>
      <th class="col_heading level0 col5" >RMSLE</th>
      <th class="col_heading level0 col6" >MAPE</th>
      <th class="col_heading level0 col7" >SMAPE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d6dcd_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_d6dcd_row0_col0" class="data row0 col0" >Voting Regressor</td>
      <td id="T_d6dcd_row0_col1" class="data row0 col1" >20.7013</td>
      <td id="T_d6dcd_row0_col2" class="data row0 col2" >1067.2105</td>
      <td id="T_d6dcd_row0_col3" class="data row0 col3" >32.6682</td>
      <td id="T_d6dcd_row0_col4" class="data row0 col4" >0.9874</td>
      <td id="T_d6dcd_row0_col5" class="data row0 col5" >0.0605</td>
      <td id="T_d6dcd_row0_col6" class="data row0 col6" >0.0475</td>
      <td id="T_d6dcd_row0_col7" class="data row0 col7" >4.8403</td>
    </tr>
  </tbody>
</table>






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
      <th>week</th>
      <th>day</th>
      <th>dayofyear</th>
      <th>country_Finland</th>
      <th>country_Norway</th>
      <th>country_Sweden</th>
      <th>store_KaggleRama</th>
      <th>product_Kaggle Hat</th>
      <th>product_Kaggle Mug</th>
      <th>product_Kaggle Sticker</th>
      <th>...</th>
      <th>quarter_Q1</th>
      <th>quarter_Q2</th>
      <th>quarter_Q3</th>
      <th>quarter_Q4</th>
      <th>weekday_WD0</th>
      <th>weekday_WD1</th>
      <th>weekday_WD3</th>
      <th>weekday_WD6</th>
      <th>num_sold</th>
      <th>Label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.708333</td>
      <td>0.2</td>
      <td>0.707602</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>223</td>
      <td>225.670747</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.708333</td>
      <td>0.2</td>
      <td>0.707602</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>303</td>
      <td>304.633516</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.708333</td>
      <td>0.2</td>
      <td>0.707602</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>112</td>
      <td>110.237661</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.708333</td>
      <td>0.2</td>
      <td>0.707602</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>419</td>
      <td>392.953237</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.708333</td>
      <td>0.2</td>
      <td>0.707602</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>550</td>
      <td>531.769134</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7885</th>
      <td>-1.000000</td>
      <td>1.0</td>
      <td>1.134503</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>823</td>
      <td>842.107813</td>
    </tr>
    <tr>
      <th>7886</th>
      <td>-1.000000</td>
      <td>1.0</td>
      <td>1.134503</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>250</td>
      <td>254.266953</td>
    </tr>
    <tr>
      <th>7887</th>
      <td>-1.000000</td>
      <td>1.0</td>
      <td>1.134503</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1004</td>
      <td>957.357321</td>
    </tr>
    <tr>
      <th>7888</th>
      <td>-1.000000</td>
      <td>1.0</td>
      <td>1.134503</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1441</td>
      <td>1422.996849</td>
    </tr>
    <tr>
      <th>7889</th>
      <td>-1.000000</td>
      <td>1.0</td>
      <td>1.134503</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>388</td>
      <td>416.196506</td>
    </tr>
  </tbody>
</table>
<p>7890 rows × 27 columns</p>
</div>




```python
# Code Sorce : https://www.kaggle.com/bernhardklinger/tps-jan-2022
preds = predict_model(final_blend, data=test) 
sub = pd.DataFrame(list(zip(test.index,preds.Label)),columns = ['row_id', 'num_sold']) 
sub.to_csv('submission.csv', index = False) 
print(sub.head(),sub.describe())
```

       row_id    num_sold
    0   26298  385.076906
    1   26299  586.455865
    2   26300  165.921560
    3   26301  656.086402
    4   26302  996.272651              row_id     num_sold
    count   6570.000000  6570.000000
    mean   29582.500000   410.390106
    std     1896.739966   277.224519
    min    26298.000000    96.117375
    25%    27940.250000   201.661353
    50%    29582.500000   339.755171
    75%    31224.750000   536.487421
    max    32867.000000  2822.059314
    


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
      <th>country</th>
      <th>store</th>
      <th>product</th>
      <th>dayofweek</th>
      <th>week</th>
      <th>year</th>
      <th>quarter</th>
      <th>day</th>
      <th>dayofyear</th>
      <th>weekend</th>
      <th>weekday</th>
    </tr>
    <tr>
      <th>row_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>26298</th>
      <td>Finland</td>
      <td>KaggleMart</td>
      <td>Kaggle Mug</td>
      <td>1</td>
      <td>1</td>
      <td>Y2019</td>
      <td>Q1</td>
      <td>1</td>
      <td>1</td>
      <td>False</td>
      <td>WD1</td>
    </tr>
    <tr>
      <th>26299</th>
      <td>Finland</td>
      <td>KaggleMart</td>
      <td>Kaggle Hat</td>
      <td>1</td>
      <td>1</td>
      <td>Y2019</td>
      <td>Q1</td>
      <td>1</td>
      <td>1</td>
      <td>False</td>
      <td>WD1</td>
    </tr>
    <tr>
      <th>26300</th>
      <td>Finland</td>
      <td>KaggleMart</td>
      <td>Kaggle Sticker</td>
      <td>1</td>
      <td>1</td>
      <td>Y2019</td>
      <td>Q1</td>
      <td>1</td>
      <td>1</td>
      <td>False</td>
      <td>WD1</td>
    </tr>
    <tr>
      <th>26301</th>
      <td>Finland</td>
      <td>KaggleRama</td>
      <td>Kaggle Mug</td>
      <td>1</td>
      <td>1</td>
      <td>Y2019</td>
      <td>Q1</td>
      <td>1</td>
      <td>1</td>
      <td>False</td>
      <td>WD1</td>
    </tr>
    <tr>
      <th>26302</th>
      <td>Finland</td>
      <td>KaggleRama</td>
      <td>Kaggle Hat</td>
      <td>1</td>
      <td>1</td>
      <td>Y2019</td>
      <td>Q1</td>
      <td>1</td>
      <td>1</td>
      <td>False</td>
      <td>WD1</td>
    </tr>
  </tbody>
</table>
</div>




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
      <th>country</th>
      <th>store</th>
      <th>product</th>
      <th>num_sold</th>
      <th>dayofweek</th>
      <th>weekend</th>
      <th>week</th>
      <th>year</th>
      <th>quarter</th>
      <th>day</th>
      <th>dayofyear</th>
      <th>weekday</th>
    </tr>
    <tr>
      <th>row_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Finland</td>
      <td>KaggleMart</td>
      <td>Kaggle Mug</td>
      <td>329</td>
      <td>3</td>
      <td>False</td>
      <td>1</td>
      <td>Y2015</td>
      <td>Q1</td>
      <td>1</td>
      <td>1</td>
      <td>WD3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Finland</td>
      <td>KaggleMart</td>
      <td>Kaggle Hat</td>
      <td>520</td>
      <td>3</td>
      <td>False</td>
      <td>1</td>
      <td>Y2015</td>
      <td>Q1</td>
      <td>1</td>
      <td>1</td>
      <td>WD3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Finland</td>
      <td>KaggleMart</td>
      <td>Kaggle Sticker</td>
      <td>146</td>
      <td>3</td>
      <td>False</td>
      <td>1</td>
      <td>Y2015</td>
      <td>Q1</td>
      <td>1</td>
      <td>1</td>
      <td>WD3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Finland</td>
      <td>KaggleRama</td>
      <td>Kaggle Mug</td>
      <td>572</td>
      <td>3</td>
      <td>False</td>
      <td>1</td>
      <td>Y2015</td>
      <td>Q1</td>
      <td>1</td>
      <td>1</td>
      <td>WD3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Finland</td>
      <td>KaggleRama</td>
      <td>Kaggle Hat</td>
      <td>911</td>
      <td>3</td>
      <td>False</td>
      <td>1</td>
      <td>Y2015</td>
      <td>Q1</td>
      <td>1</td>
      <td>1</td>
      <td>WD3</td>
    </tr>
  </tbody>
</table>
</div>


