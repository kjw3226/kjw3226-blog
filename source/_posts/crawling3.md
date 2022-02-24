----
title: crawling3 (크롤링3)
tag: crawling3 (크롤링3)
date: 2022-01-05
categories:	Python
----
 오늘은 [국토교통부 - KRic(철도통계)](http://www.kric.go.kr/jsp/industry/rss/cityorganpassList.jsp?q_fdate=2021)
 
 여기에 들어가서 '도시철도여객수송'의 데이터를 크롤링 해서 가져 오고 
 
 'DataFream' 형태로도 만드는 실습을 했다.
  
  아래는 코드와 실행 화면들이다.

# 1. 스크래핑 요청
```python
import requests
url = "http://www.kric.go.kr/jsp/industry/rss/citystapassList.jsp?q_org_cd=A010010021&q_fdate=2021"

html_text = requests.get(url).text
print(html_text)
```
홈페이지에 있는 내용을 그대로 가져왔다.

<실행 화면>

![crawling-train1](https://user-images.githubusercontent.com/96108301/148211224-17b39aca-623f-4b52-81ad-9f63b7f759db.PNG)
![crawling-train2](https://user-images.githubusercontent.com/96108301/148211228-41e4f8f1-171e-4c1a-9c11-1839d1166223.PNG)

# 2. Parsing

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_text, "html.parser")
soup
```
<실행 화면>

![crawling-train3](https://user-images.githubusercontent.com/96108301/148211659-d62fe60d-e8d2-4545-8058-b27c4bd6302d.PNG)
![crawling-train4](https://user-images.githubusercontent.com/96108301/148211663-2c4eafbd-fb9c-4469-a09a-7c5357456ab5.PNG)
![crawling-train5](https://user-images.githubusercontent.com/96108301/148211665-83f7f6a2-6b54-4d44-901f-e58cc261c506.PNG)

# 3. Transformation
```python
table_df = soup.find("table", class_="listtbl_c100")
print(table_df)
```
<실행 화면>

![crawling-train6](https://user-images.githubusercontent.com/96108301/148211939-1a55cc5d-2968-4bc9-ba24-1f5fd64e8eaa.PNG)

```python
trs = table_df.find("tbody").find_all("tr")
trs[2]
```
<실행 화면>

![crawling-train7](https://user-images.githubusercontent.com/96108301/148212160-2a3f5557-e0cd-467a-9d28-d5c39a023771.PNG)

```python
tdcols = trs[1].find("td", {"class" : "tdcol"}) # '{}' 는  딕셔너리로 묶는다는 의미
print(tdcols)
```
<실행 화면>

![crawling-train9](https://user-images.githubusercontent.com/96108301/148212425-137abf3c-163e-4e72-be0d-9c907f27dc1f.PNG)

```python
tds = trs[4].find_all("td")
#print(tds)

tds[0].get_text(), tds[2].get_text(),tds[3].get_text()
```
<실행 화면>

![crawling-train10](https://user-images.githubusercontent.com/96108301/148213114-d6ff599e-59ac-4cb7-bc5d-9b1b83bcdaf3.PNG)
```python
tds[0].get_text(), tds[2].get_text(),tds[3].get_text()
```
<실행 화면>

![crawling-train11](https://user-images.githubusercontent.com/96108301/148213117-0e23a0de-a97c-4082-b1d8-ff035ed7db33.PNG)
```python
trs[1:]
```
<실행 화면>

![crawling-train12](https://user-images.githubusercontent.com/96108301/148213119-e2457fec-7baa-47b2-b969-c254b964fc17.PNG)
![crawling-train13](https://user-images.githubusercontent.com/96108301/148213121-9f6f17bf-0ea0-43d8-bbf8-9e285c2486f8.PNG)

```python
stationPass = []
for tr in trs[1:]:
  dic = {}
  tbs = tr.find_all("td")
#  print("역:",tds[0].get_text())
#  print("승차인원:",tds[2].get_text())
#  print("승차인원:",tds[3].get_text())
  dic["승차역"] = tds[0].get_text()
  dic["승차인원"] = tds[2].get_text()
  dic["하차인원"] = tds[3].get_text()
  stationPass.append(dic)

print(stationPass)
```
<실행 화면>

![crawling-train14](https://user-images.githubusercontent.com/96108301/148213123-0e301b4e-751c-4a9f-9c4e-be8160a706e9.PNG)

```python
import pandas as pd
pd.DataFrame(stationPass) 
```
<실행 화면>

![crawling-train15](https://user-images.githubusercontent.com/96108301/148213124-d1faf7f3-2165-46e0-9b66-88a8cc5fc533.PNG)

아래의 코드는 실행시키면 'csv'파일 이나 'xlsx(엑셀)' 파일이
생성되어 저장되고 홈페이지에서 가져온 데이터가 데이터 프레임 형태로 
변환되는 코드이다.

```python
import pandas as pd
import requests
from bs4 import BeautifulSoup

def main():
    print("main function is executing....\n")

    # 빈 데이터 프레임 생성
    data_all = pd.DataFrame()
    for i in range(1, 20):
        url = "https://www.kric.go.kr/jsp/industry/rss/citystapassList.jsp?q_org_cd=A010010021&q_fdate=2021&pageNo=1"
        html_text = fetch(url) # <----- 크게 신경 안써도 됨.
        soup = parser(html_text) # <----- 크게 신경 안써도 됨.
        df = transforming(soup) # <---- 수정
        data_all = pd.concat([data_all, df])
         
    print(data_all.head())
    print(data_all.tail())
    print(data_all.shape)

    save_csv(data_all)
def fetch(url):
    print("fetch function is executing....\n")
    html_text = requests.get(url).text
    print("html_text")

    return html_text

def parser(text):
    print("parser function is executing....\n")
    return BeautifulSoup(text, "html.parser")

def transforming(soup):
    tab = soup.find("table", {"class": "listtbl_c100"})
    trs = tab.find("tbody").find_all("tr")
    stationpassengers = []
    if "합계" in trs[0].find("td", {"class":"tdcol"}):
        for tr in trs[1:]:
            dic = {}
            tds = tr.find_all("td")
            dic["station"] = tds[0].text
            dic["ride"] = tds[2].text
            dic["alright"] = tds[3].text
            stationpassengers.append(dic)
    # print(pd.DataFrame(stationpassengers))
        data = pd.DataFrame(stationpassengers)
    else:
        for tr in trs:
            dic = {}
            tds = tr.find_all("td")
            dic["station"] = tds[0].text
            dic["ride"] = tds[2].text
            dic["alright"] = tds[3].text
            stationpassengers.append(dic)
        # print(pd.DataFrame(stationpassengers))
        data = pd.DataFrame(stationpassengers)
    return data

def save(save_path, data):
    data.reset_index(drop=False)
    print(data.head())
    # pip install openpyxl
    data.to_excel(save_path + '/content/drive/MyDrive/crawling data/kric.csv', index = False, header=False, encoding='utf-8-sig')

def save_db(data):
  ## <-- DB 연동 예제 추가 할 코드

  pass

if __name__ == "__main__":
    main()
    # 크롤링
    # csv 파일 내보내기
    # DB 연동
```
<실행 화면>

![crawling-train16](https://user-images.githubusercontent.com/96108301/148214008-ca1215a3-d610-458e-ad74-6fc5686700f7.PNG)

