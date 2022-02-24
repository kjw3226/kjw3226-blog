---
title: craling 4 (크롤링 4)
tag: craling 4 (크롤링 4)
date: 2022-01-06
categories:	Python
---

'naver(네이버)' 에 있는 '증권' 홈페이지에서 
 특정 기업의 '주식' 데이터를 크롤링 하는 실습을 했다.
 아래는 관련 코드들이다.


맨 먼저 패키지 3개를 설치한다.
```python
pip install fake_useragent
```
```python
pip install lxml
```
```python
pip install BeautifulSoup4
```
그리고 본격적으로 코드를 입력.
```python
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import pandas as pd

if __name__ == "__main__":
    print("설치완료")
```

이건 실행시켜서 '에러'가 떠야 정상이다.

```python
import requests
url = "https://finance.naver.com/item/main.naver?code=051910&page=1"

html_text = requests.get(url).text
print(html_text)
```
'네이버'에서 '증권' 홈페이지의 데이터를 전부 '텍스트'형식으로 가져옴.

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_text, "html.parser")
soup
```
'링크' 형식으로 '네이버 증권' 홈페이지의 데이터를 가져옴.

아래는 오늘의 '핵심 코드'이다.
```python
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent # 트릭으로 api를 우회해서 가짜 정보를 주는 코드 (신기하다^^)
from datetime import datetime
import time
import pandas as pd
from numpy import random


def main():
    company_code = "005930" # 삼성전자
    url = "https://finance.naver.com/item/sise_day.nhn?code=" + company_code
    ua = UserAgent()
    headers = {"User-agent": ua.ie}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup)

    last_page = int(soup.select_one("td.pgRR").a["href"].split('=')[-1])
    # print(last_page)

    df = None
    count = 0
    for page in range(1, last_page + 1):
        req = requests.get(f'{url}&page={page}', headers=headers)
        # print(pd.read_html(req.text, encoding="euc-kr"))
        df = pd.concat([df, pd.read_html(req.text, encoding="euc-kr")[0]], ignore_index=True)
        if count > 10:
            break
        count += 1
        #time.sleep(10)
        
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    print(df.head())
    print(df.tail())

if __name__ == "__main__":
    main()
```
위의 코드에서 'from fake_useragent import UserAgent' 이 부분은 
가짜 사용자 정보로 속이고
'api'를 우회해서 가져오는 역할을 하는 코드이다.

