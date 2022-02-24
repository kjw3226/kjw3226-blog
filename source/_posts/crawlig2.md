---
title: crawlig2 (크롤링2)
tag: crawling2 (크롤링2)
date: 2022-01-04
categories:	Python
---

오늘은 어제에 이어서 크롤링 실습을 했다.

어제는 '직접 사이트 주소 가져오기', 'API를 사용해서 주소 가져오기'를 진행했다면

오늘은 직접 사이트의 상태를 알아보고, 주소를 가져와서 링크를 설정해주는 실습을 했다.

아래는 실습 코드와 실행화면들이다.

먼저 패키지를 설치 한다.
```python
pip install requests
```
```python
import requests

def main():
    url = "https://www.naver.com/11111"

    req = requests.get(url)

    # 상태 코드 확인
    print("현재 상태:", req.status_code)

    # text
    # print(req.text)

    print("loop")

def try_except_main():
  try:
    url = "https://www.naver.com/11111"
    req = requests.get(url)
    req.raise_for_status()
  except requests.exceptions.HTTPError as err:
    raise SystemExit(err)
  finally: 
    print("loop")


if __name__ == "__main__":
    main()
```
이렇게 url 뒤에 1이 반복되는 숫자를 넣으면 '404'에러가 떠서 
상태 코드가 '404'와 'loop' 가 출력 된다.
<실행 화면>

![requests1](https://user-images.githubusercontent.com/96108301/148006082-1b24c5f7-c5f5-46f5-8365-31e124d1fd0d.PNG)


```python
import requests

def main():
    url = "https://www.naver.com/"

    req = requests.get(url)

    # 상태 코드 확인
    print("현재 상태:", req.status_code)

    # text
    # print(req.text)

    print("loop")

def try_except_main():
  try:
    url = "https://www.naver.com/"
    req = requests.get(url)
    req.raise_for_status()
  except requests.exceptions.HTTPError as err:
    raise SystemExit(err)
  finally: 
    print("loop")


if __name__ == "__main__":
    main()
```

하지만 반대로 숫자를 빼면 이렇게 나온다.

<실행 화면>

![requests2](https://user-images.githubusercontent.com/96108301/148006293-00e814d3-1f5f-4e24-b756-6b26784020ad.PNG)

다음은 '네이버 헤드 뉴스 모으기' 코드이다.

```python
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

def main():

  custom_header = {
      "referer": "https://www.naver.com/",
      "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
  }

  url = "https://www.naver.com/"
  req = requests.get(url, headers = custom_header)

  soup = BeautifulSoup(req.text, "html.parser")

  # print("현재 상태:", req.status_code)

  # print(soup.prettify())
  titles = []
  hrefs = []
  div = soup.find("div", class_ = "issue_area")
  for a in div.find_all("a"):
      # print("url:", a)
      # print("title:", a.get_text())
      # print("HREF URL:", a["href"])
      titles.append(a.get_text())
      hrefs.append(a["href"].replace("list", "read")) # <-- list --> read

  # print(titles)
  print(hrefs)

  df = pd.DataFrame({"news": titles, "url": hrefs})
  df["datetime"] = datetime.now()
  df = df[["datetime", "news", "url"]]

  
  df.to_excel("/content/drive/MyDrive/crawling data/naver_head_news.xlsx", index=False)

  # https: // news.naver.com / main / list.naver?mode = LPOD & mid = sec & sid1 = 001 & sid2 = 140 & oid = 001 & isYeonhapFlash = Y & aid = 0012896144
  # https: // news.naver.com / main / read.naver?mode = LPOD & mid = sec & oid = 001 & aid = 0012896144 & isYeonhapFlash = Y & rc = N
  # 노가다...
  # 태그 찾고, 구조 확인하고, 전처리 하고......


if __name__ == "__main__":
  main()
```
<실행 화면>

![requests3](https://user-images.githubusercontent.com/96108301/148007711-4766cc22-d8c8-4f83-95ee-1f6f02d39a5d.PNG)
![requests4](https://user-images.githubusercontent.com/96108301/148007712-26a1e456-adee-4db0-b00b-0f7f249e9994.PNG)
![requests5](https://user-images.githubusercontent.com/96108301/148007713-0231d97c-9b80-4009-a825-09fd7837b746.PNG)
![requests6](https://user-images.githubusercontent.com/96108301/148007716-9baaa3a6-d0d5-4dd2-a263-03126def5bcb.PNG)
![requests7](https://user-images.githubusercontent.com/96108301/148007717-1199fc6a-8308-4eaf-b28a-3ab72ee5839d.PNG)
![requests8](https://user-images.githubusercontent.com/96108301/148007719-c55fe573-a2cc-44a9-91df-f8d77e6f53dc.PNG)
.

.

.

.

(출력된 주소가 더 있지만 너무 많아서 생략)

만약, 이 'url' 주소들을 엑셀 파일로 저장 하고 싶다면

```python
pip install openpyxl
```
이 패키지를 설치하고 코드를 돌리면 'url' 주소가 담긴 엑셀파일이  
'df.to_excel("/content/drive/MyDrive/crawling data/naver_head_news.xlsx", index=False)'
이 경로에 생성된다.

참고로 본인은 '구글 코랩'에서 드라이브와 연동해서 진행했기 때문에 
경로가 드라이브로 되어있다.