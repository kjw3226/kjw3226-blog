---
title: crawling basic (크롤링 기본)
tag: crawling basic (크롤링 기본)
date: 2022-01-03
categories:	Python
---

# 크롤링

## 1. file 준비

file -> [crawling data](source/Lecture/crawling data)

## 2.크롤링 : BeautifulSoup 설치

beautifulsoup 설치는 --> [여기](https://pypi.org/project/beautifulsoup4/)에서 시작

![Crawling_beautifulsoup](https://user-images.githubusercontent.com/96108301/147913919-2ebf5707-1d2f-43c3-a203-5cb697bce955.png)

terminal에 위의 명령어 입력

BeautifulSoup 설치 되었는지 한번 더 확인

```python
from bs4 import BeautifulSoup
print("library imported")
```
terminal에 library imported가 print 된다.

## 3. 크롤링 코드

### 3-1. 객체 초기화
```python
def main():
    #객체 초기화, 뒤에있는 parser가 핵심: python에서 접근 가능하게 만들어줌
    soup = BeautifulSoup(open("data/index.html"), "html.parser")
    print(soup)

if __name__ == "__main__":
    main()
```
함수를 만들어 html file을 열고 그 file을 parser로 python이 읽을 수 있는 형태로 가져온다.

<실행 화면>
```python

library imported
<!DOCTYPE html>

<html>
<head>
<meta charset="utf-8"/>
<title>Crawl This Page</title>
</head>
<body>
<div class="cheshire">
<p>Don't crawl this.</p>
</div>
<div class="elice">
<p>Hello, Python Crawling!</p>
</div>
</body>
</html>

Process finished with exit code 0
```
읽어 오는 것 까지가 끝

### 3-2. 원하는 객체 뽑아내기 : HTML tag로
```python
# /c/../Crawring/venv/Scripts/python
# -*- Encoding : UTF-8 -*-

from bs4 import BeautifulSoup

print("library imported")


def main():
    # 객체 초기화, 뒤에있는 parser가 핵심: python에서 접근 가능하게 만들어줌
    soup = BeautifulSoup(open("data/index.html"), "html.parser")
    #원하는 data 출력
    print(soup.find("div").get_text()) #find_all 쓰면 get_text가 안된다.
    #저장(Excel:pandas, DB)

if __name__ == "__main__":
    main()
```
<실행 화면>
```python
library imported

Don't crawl this.

Process finished with exit code 0
```
● .find("div") : div tag를 뽑아오는 구문
● .get_text() : div tag를 삭제하고 text만 뽑아옴
● .find_all("div") : get text()가 안먹는다.

### 3-3. 원하는 객체 뽑아내기 : class name으로
```python

def main():
    # 객체 초기화
    soup = BeautifulSoup(open("data/index2.html"), "html.parser")
    # 원하는 data 출력
    print(soup.find("div", class_ = "elice").find("p").get_text())
    # 저장(Excel:pandas, DB)

if __name__ == "__main__":
    main()
```

### 3-3. 원하는 객체 뽑아내기 : id 로
```python

def main():
    # 객체 초기화
    soup = BeautifulSoup(open("data/index3.html"), "html.parser")
    # 원하는 data 출력
    print(soup.find("div", id = "main").find("p").get_text())
    # 저장(Excel:pandas, DB)

if __name__ == "__main__":
    main()
```
### 4. data 뽑아내기
● data 뽑아내는 거는 google colab에서 진행

### 4-1. data file 받아오기
● Data file은 [여기](http://data.ex.co.kr/)에서 무료로 받을 수 있다.
● 인증키는 받아서 사용해야 되는데, [여기](https://data.ex.co.kr/openapi/apikey/requestKey)에서 정보를 입력하고 받아오면 된다. 
● 인증키를 받았다면 google colab 열고 진행
● 인증키는 입력한 메일로 오기도 하고 창이 팝업 창이 뜨기도 해서 메일 주소를 잘 입력하고 팝업 차단을 해제해 두어야 한다.
```python
import requests
key = "*본인의 인증키 숫자를 넣는다*"
url = "http://data.ex.co.kr/openapi/trtm/realUnitTrtm?key=`인증키여기`&type=json&iStartUnitCode=101&iEndUnitCode=103"

responses = requests.get(url)
```
<실행 화면>
```python
<Response [200]>
```
인증키를 성공적으로 넣으면 위와 같은 <실행 화면>이 나온다.

### 4-2. responses로 json file 만들기
```python
json = responses.json()
```
<실행 화면>
```python
{'code': 'SUCCESS',
 'count': 602,
 'message': '인증키가 유효합니다.',
 'numOfRows': 10,
 'pageNo': 1,
 'pageSize': 61,
 'realUnitTrtmVO': [{'efcvTrfl': '18',
   'endUnitCode': '103 ',
   'endUnitNm': '수원신갈',
   'iEndUnitCode': None,
   'iStartEndStdTypeCode': None,
   'iStartUnitCode': None,
   'numOfRows': None,
   'pageNo': None,
   'startEndStdTypeCode': '2',
   'startEndStdTypeNm': '도착기준통행시간',
   'startUnitCode': '101 ',
   'startUnitNm': '서울',
   'stdDate': '20220103',
   'stdTime': '00:25',
   'sumTmUnitTypeCode': None,
   'tcsCarTypeCode': '1',
   'tcsCarTypeDivCode': '1',
   'tcsCarTypeDivName': '소형차',
   'tcsCarTypeName': '1종',
   'timeAvg': '7.466666666666667',
   'timeMax': '9.216',
   'timeMin': '5.800'},
  {'efcvTrfl': '53',
   'endUnitCode': '103 ',
   'endUnitNm': '수원신갈',
   'iEndUnitCode': None,
   'iStartEndStdTypeCode': None,
   'iStartUnitCode': None,
   'numOfRows': None,
   'pageNo': None,
   'startEndStdTypeCode': '2',
   'startEndStdTypeNm': '도착기준통행시간',
   'startUnitCode': '101 ',
   'startUnitNm': '서울',
   'stdDate': '20220103',
   'stdTime': '00:30',
   'sumTmUnitTypeCode': None,
   'tcsCarTypeCode': '1',
   'tcsCarTypeDivCode': '1',
   'tcsCarTypeDivName': '소형차',
   'tcsCarTypeName': '1종',
   'timeAvg': '7.466666666666667',
   'timeMax': '9.283',
   'timeMin': '5.783'},
  {'efcvTrfl': '14',
   'endUnitCode': '103 ',
   'endUnitNm': '수원신갈',
   'iEndUnitCode': None,
   'iStartEndStdTypeCode': None,
   'iStartUnitCode': None,
   'numOfRows': None,
   'pageNo': None,
   'startEndStdTypeCode': '2',
   'startEndStdTypeNm': '도착기준통행시간',
   'startUnitCode': '101 ',
   'startUnitNm': '서울',
   'stdDate': '20220103',
   'stdTime': '00:35',
   'sumTmUnitTypeCode': None,
   'tcsCarTypeCode': '1',
   'tcsCarTypeDivCode': '1',
   'tcsCarTypeDivName': '소형차',
   'tcsCarTypeName': '1종',
   'timeAvg': '7.416666666666667',
   'timeMax': '8.400',
   'timeMin': '6.050'},
  {'efcvTrfl': '15',
   'endUnitCode': '103 ',
   'endUnitNm': '수원신갈',
   'iEndUnitCode': None,
   'iStartEndStdTypeCode': None,
   'iStartUnitCode': None,
   'numOfRows': None,
   'pageNo': None,
   'startEndStdTypeCode': '2',
   'startEndStdTypeNm': '도착기준통행시간',
   'startUnitCode': '101 ',
   'startUnitNm': '서울',
   'stdDate': '20220103',
   'stdTime': '00:40',
   'sumTmUnitTypeCode': None,
   'tcsCarTypeCode': '1',
   'tcsCarTypeDivCode': '1',
   'tcsCarTypeDivName': '소형차',
   'tcsCarTypeName': '1종',
   'timeAvg': '7.516666666666667',
   'timeMax': '9.283',
   'timeMin': '5.966'},
  {'efcvTrfl': '41',
   'endUnitCode': '103 ',
   'endUnitNm': '수원신갈',
   'iEndUnitCode': None,
   'iStartEndStdTypeCode': None,
   'iStartUnitCode': None,
   'numOfRows': None,
   'pageNo': None,
   'startEndStdTypeCode': '2',
   'startEndStdTypeNm': '도착기준통행시간',
   'startUnitCode': '101 ',
   'startUnitNm': '서울',
   'stdDate': '20220103',
   'stdTime': '00:45',
   'sumTmUnitTypeCode': None,
   'tcsCarTypeCode': '1',
   'tcsCarTypeDivCode': '1',
   'tcsCarTypeDivName': '소형차',
   'tcsCarTypeName': '1종',
   'timeAvg': '7.5',
   'timeMax': '8.800',
   'timeMin': '5.750'},
  {'efcvTrfl': '11',
   'endUnitCode': '103 ',
   'endUnitNm': '수원신갈',
   'iEndUnitCode': None,
   'iStartEndStdTypeCode': None,
   'iStartUnitCode': None,
   'numOfRows': None,
   'pageNo': None,
   'startEndStdTypeCode': '2',
   'startEndStdTypeNm': '도착기준통행시간',
   'startUnitCode': '101 ',
   'startUnitNm': '서울',
   'stdDate': '20220103',
   'stdTime': '00:50',
   'sumTmUnitTypeCode': None,
   'tcsCarTypeCode': '1',
   'tcsCarTypeDivCode': '1',
   'tcsCarTypeDivName': '소형차',
   'tcsCarTypeName': '1종',
   'timeAvg': '7.416666666666667',
   'timeMax': '8.800',
   'timeMin': '5.766'},
  {'efcvTrfl': '8',
   'endUnitCode': '103 ',
   'endUnitNm': '수원신갈',
   'iEndUnitCode': None,
   'iStartEndStdTypeCode': None,
   'iStartUnitCode': None,
   'numOfRows': None,
   'pageNo': None,
   'startEndStdTypeCode': '2',
   'startEndStdTypeNm': '도착기준통행시간',
   'startUnitCode': '101 ',
   'startUnitNm': '서울',
   'stdDate': '20220103',
   'stdTime': '00:55',
   'sumTmUnitTypeCode': None,
   'tcsCarTypeCode': '1',
   'tcsCarTypeDivCode': '1',
   'tcsCarTypeDivName': '소형차',
   'tcsCarTypeName': '1종',
   'timeAvg': '7.433333333333334',
   'timeMax': '8.350',
   'timeMin': '5.750'},
  {'efcvTrfl': '87',
   'endUnitCode': '103 ',
   'endUnitNm': '수원신갈',
   'iEndUnitCode': None,
   'iStartEndStdTypeCode': None,
   'iStartUnitCode': None,
   'numOfRows': None,
   'pageNo': None,
   'startEndStdTypeCode': '2',
   'startEndStdTypeNm': '도착기준통행시간',
   'startUnitCode': '101 ',
   'startUnitNm': '서울',
   'stdDate': '20220103',
   'stdTime': '01  ',
   'sumTmUnitTypeCode': None,
   'tcsCarTypeCode': '1',
   'tcsCarTypeDivCode': '1',
   'tcsCarTypeDivName': '소형차',
   'tcsCarTypeName': '1종',
   'timeAvg': '7.55',
   'timeMax': '10.183',
   'timeMin': '5.750'},
  {'efcvTrfl': '30',
   'endUnitCode': '103 ',
   'endUnitNm': '수원신갈',
   'iEndUnitCode': None,
   'iStartEndStdTypeCode': None,
   'iStartUnitCode': None,
   'numOfRows': None,
   'pageNo': None,
   'startEndStdTypeCode': '2',
   'startEndStdTypeNm': '도착기준통행시간',
   'startUnitCode': '101 ',
   'startUnitNm': '서울',
   'stdDate': '20220103',
   'stdTime': '01:00',
   'sumTmUnitTypeCode': None,
   'tcsCarTypeCode': '1',
   'tcsCarTypeDivCode': '1',
   'tcsCarTypeDivName': '소형차',
   'tcsCarTypeName': '1종',
   'timeAvg': '7.625',
   'timeMax': '10.183',
   'timeMin': '6.600'},
  {'efcvTrfl': '3',
   'endUnitCode': '103 ',
   'endUnitNm': '수원신갈',
   'iEndUnitCode': None,
   'iStartEndStdTypeCode': None,
   'iStartUnitCode': None,
   'numOfRows': None,
   'pageNo': None,
   'startEndStdTypeCode': '2',
   'startEndStdTypeNm': '도착기준통행시간',
   'startUnitCode': '101 ',
   'startUnitNm': '서울',
   'stdDate': '20220103',
   'stdTime': '01:05',
   'sumTmUnitTypeCode': None,
   'tcsCarTypeCode': '1',
   'tcsCarTypeDivCode': '1',
   'tcsCarTypeDivName': '소형차',
   'tcsCarTypeName': '1종',
   'timeAvg': '7.683333333333334',
   'timeMax': '8.250',
   'timeMin': '7.500'}]}
```
● json 객체에 responses 함수를 이용하여 json형태의 file을 담고
● cars : 내가 찾고 싶은 부분을 file의 형태에서 찾아서 넣는다.
● file의 구조와 내가 찾고 싶은 부분을 알고 있어야 원하는 정보를 넣을 수 있다.

### 4-3. json file에서 원하는 정보 빼오기
● 반복되는 'realUnitTrtmVO'를  dictionarly에 접근하여
  정보를 빼보자.
```python
cars = json["realUnitTrtmVO"]
```
<실행 화면>
```python
[{'efcvTrfl': '18',
  'endUnitCode': '103 ',
  'endUnitNm': '수원신갈',
  'iEndUnitCode': None,
  'iStartEndStdTypeCode': None,
  'iStartUnitCode': None,
  'numOfRows': None,
  'pageNo': None,
  'startEndStdTypeCode': '2',
  'startEndStdTypeNm': '도착기준통행시간',
  'startUnitCode': '101 ',
  'startUnitNm': '서울',
  'stdDate': '20220103',
  'stdTime': '00:25',
  'sumTmUnitTypeCode': None,
  'tcsCarTypeCode': '1',
  'tcsCarTypeDivCode': '1',
  'tcsCarTypeDivName': '소형차',
  'tcsCarTypeName': '1종',
  'timeAvg': '7.466666666666667',
  'timeMax': '9.216',
  'timeMin': '5.800'},
 {'efcvTrfl': '53',
  'endUnitCode': '103 ',
  'endUnitNm': '수원신갈',
  'iEndUnitCode': None,
  'iStartEndStdTypeCode': None,
  'iStartUnitCode': None,
  'numOfRows': None,
  'pageNo': None,
  'startEndStdTypeCode': '2',
  'startEndStdTypeNm': '도착기준통행시간',
  'startUnitCode': '101 ',
  'startUnitNm': '서울',
  'stdDate': '20220103',
  'stdTime': '00:30',
  'sumTmUnitTypeCode': None,
  'tcsCarTypeCode': '1',
  'tcsCarTypeDivCode': '1',
  'tcsCarTypeDivName': '소형차',
  'tcsCarTypeName': '1종',
  'timeAvg': '7.466666666666667',
  'timeMax': '9.283',
  'timeMin': '5.783'},
 {'efcvTrfl': '14',
  'endUnitCode': '103 ',
  'endUnitNm': '수원신갈',
  'iEndUnitCode': None,
  'iStartEndStdTypeCode': None,
  'iStartUnitCode': None,
  'numOfRows': None,
  'pageNo': None,
  'startEndStdTypeCode': '2',
  'startEndStdTypeNm': '도착기준통행시간',
  'startUnitCode': '101 ',
  'startUnitNm': '서울',
  'stdDate': '20220103',
  'stdTime': '00:35',
  'sumTmUnitTypeCode': None,
  'tcsCarTypeCode': '1',
  'tcsCarTypeDivCode': '1',
  'tcsCarTypeDivName': '소형차',
  'tcsCarTypeName': '1종',
  'timeAvg': '7.416666666666667',
  'timeMax': '8.400',
  'timeMin': '6.050'},
 {'efcvTrfl': '15',
  'endUnitCode': '103 ',
  'endUnitNm': '수원신갈',
  'iEndUnitCode': None,
  'iStartEndStdTypeCode': None,
  'iStartUnitCode': None,
  'numOfRows': None,
  'pageNo': None,
  'startEndStdTypeCode': '2',
  'startEndStdTypeNm': '도착기준통행시간',
  'startUnitCode': '101 ',
  'startUnitNm': '서울',
  'stdDate': '20220103',
  'stdTime': '00:40',
  'sumTmUnitTypeCode': None,
  'tcsCarTypeCode': '1',
  'tcsCarTypeDivCode': '1',
  'tcsCarTypeDivName': '소형차',
  'tcsCarTypeName': '1종',
  'timeAvg': '7.516666666666667',
  'timeMax': '9.283',
  'timeMin': '5.966'},
 {'efcvTrfl': '41',
  'endUnitCode': '103 ',
  'endUnitNm': '수원신갈',
  'iEndUnitCode': None,
  'iStartEndStdTypeCode': None,
  'iStartUnitCode': None,
  'numOfRows': None,
  'pageNo': None,
  'startEndStdTypeCode': '2',
  'startEndStdTypeNm': '도착기준통행시간',
  'startUnitCode': '101 ',
  'startUnitNm': '서울',
  'stdDate': '20220103',
  'stdTime': '00:45',
  'sumTmUnitTypeCode': None,
  'tcsCarTypeCode': '1',
  'tcsCarTypeDivCode': '1',
  'tcsCarTypeDivName': '소형차',
  'tcsCarTypeName': '1종',
  'timeAvg': '7.5',
  'timeMax': '8.800',
  'timeMin': '5.750'},
 {'efcvTrfl': '11',
  'endUnitCode': '103 ',
  'endUnitNm': '수원신갈',
  'iEndUnitCode': None,
  'iStartEndStdTypeCode': None,
  'iStartUnitCode': None,
  'numOfRows': None,
  'pageNo': None,
  'startEndStdTypeCode': '2',
  'startEndStdTypeNm': '도착기준통행시간',
  'startUnitCode': '101 ',
  'startUnitNm': '서울',
  'stdDate': '20220103',
  'stdTime': '00:50',
  'sumTmUnitTypeCode': None,
  'tcsCarTypeCode': '1',
  'tcsCarTypeDivCode': '1',
  'tcsCarTypeDivName': '소형차',
  'tcsCarTypeName': '1종',
  'timeAvg': '7.416666666666667',
  'timeMax': '8.800',
  'timeMin': '5.766'},
 {'efcvTrfl': '8',
  'endUnitCode': '103 ',
  'endUnitNm': '수원신갈',
  'iEndUnitCode': None,
  'iStartEndStdTypeCode': None,
  'iStartUnitCode': None,
  'numOfRows': None,
  'pageNo': None,
  'startEndStdTypeCode': '2',
  'startEndStdTypeNm': '도착기준통행시간',
  'startUnitCode': '101 ',
  'startUnitNm': '서울',
  'stdDate': '20220103',
  'stdTime': '00:55',
  'sumTmUnitTypeCode': None,
  'tcsCarTypeCode': '1',
  'tcsCarTypeDivCode': '1',
  'tcsCarTypeDivName': '소형차',
  'tcsCarTypeName': '1종',
  'timeAvg': '7.433333333333334',
  'timeMax': '8.350',
  'timeMin': '5.750'},
 {'efcvTrfl': '87',
  'endUnitCode': '103 ',
  'endUnitNm': '수원신갈',
  'iEndUnitCode': None,
  'iStartEndStdTypeCode': None,
  'iStartUnitCode': None,
  'numOfRows': None,
  'pageNo': None,
  'startEndStdTypeCode': '2',
  'startEndStdTypeNm': '도착기준통행시간',
  'startUnitCode': '101 ',
  'startUnitNm': '서울',
  'stdDate': '20220103',
  'stdTime': '01  ',
  'sumTmUnitTypeCode': None,
  'tcsCarTypeCode': '1',
  'tcsCarTypeDivCode': '1',
  'tcsCarTypeDivName': '소형차',
  'tcsCarTypeName': '1종',
  'timeAvg': '7.55',
  'timeMax': '10.183',
  'timeMin': '5.750'},
 {'efcvTrfl': '30',
  'endUnitCode': '103 ',
  'endUnitNm': '수원신갈',
  'iEndUnitCode': None,
  'iStartEndStdTypeCode': None,
  'iStartUnitCode': None,
  'numOfRows': None,
  'pageNo': None,
  'startEndStdTypeCode': '2',
  'startEndStdTypeNm': '도착기준통행시간',
  'startUnitCode': '101 ',
  'startUnitNm': '서울',
  'stdDate': '20220103',
  'stdTime': '01:00',
  'sumTmUnitTypeCode': None,
  'tcsCarTypeCode': '1',
  'tcsCarTypeDivCode': '1',
  'tcsCarTypeDivName': '소형차',
  'tcsCarTypeName': '1종',
  'timeAvg': '7.625',
  'timeMax': '10.183',
  'timeMin': '6.600'},
 {'efcvTrfl': '3',
  'endUnitCode': '103 ',
  'endUnitNm': '수원신갈',
  'iEndUnitCode': None,
  'iStartEndStdTypeCode': None,
  'iStartUnitCode': None,
  'numOfRows': None,
  'pageNo': None,
  'startEndStdTypeCode': '2',
  'startEndStdTypeNm': '도착기준통행시간',
  'startUnitCode': '101 ',
  'startUnitNm': '서울',
  'stdDate': '20220103',
  'stdTime': '01:05',
  'sumTmUnitTypeCode': None,
  'tcsCarTypeCode': '1',
  'tcsCarTypeDivCode': '1',
  'tcsCarTypeDivName': '소형차',
  'tcsCarTypeName': '1종',
  'timeAvg': '7.683333333333334',
  'timeMax': '8.250',
  'timeMin': '7.500'}]
```

### 4-4. csv file로 출력

● pandas를 이용하여 dictionarly, json file을 dataFrame, csv file로 변환
```python
import pandas as pd
dt = []
for car in cars:
  dic_df = {}
  dic_df["data"] = car["stdDate"]
  dic_df["time"] = car["stdTime"]
  dic_df["destination"] = car["endUnitNm"]
  dt.append(dic_df)

pd.DataFrame(dt).to_csv("temp.csv",index = False, encoding="euc-kr")
```
Encoding의 경우 해당 json file의 documents를 봐야함.

google과 같은 기업에서 API를 받아와서 사용 하는 것도 가능 하므로
앞으로 이 기술은 무궁무진한 발전 가능성이 있을 것으로 보임 ^^

