---
title: Google Cloud Platfrom1(구글 클라우드 플랫폼1)
tag: Google Cloud Platfrom1(구글 클라우드 플랫폼1)
date: 2022-01-20
categories:	SQL
----
 오늘은 '구글'의 '빅 쿼리'라는 걸 새롭게 배웠다.
 '엄청 편리하다.'라는 느낌을 많이 받은 시간이었다.

맨 먼저 'Google Cloud Platform' 을 검색하거나 '구글 클라우드'를 검색하면
'Google 클라우드 플랫폼' 사이트가 뜨는데 이곳에 들어간다.

그리고 회원가입을 진행한다.

가입이 완료되면 '무료로 시작하기'를 클릭하면 그 다음 부터는 모든 서비스를 이용할 수 있다.

밑의 사진들은 오늘 실습한 '빅 쿼리'와 'Data studio'의 화면을 캡처한 

사진들이다.

![google Big Query](https://user-images.githubusercontent.com/96108301/150300677-5b6e0987-667c-4b34-b54d-37fb79bf0163.PNG)

위와 같은 화면에서 'Big Query'가 잘 작동하는지 

확인하기 위해 

쿼리문을 좀 써준다.

```python
SELECT count(*) FROM `bigquery-public-data.covid19_public_forecasts.county_14d`
```
```python
SELECT EXTRACT(YEAR FROM starttime) AS year,
    EXTRACT(MONTH FROM starttime) AS month,
    COUNT(starttime) AS number_one_way
FROM
    `bigquery-public-data.new_york_citibike.citibike_trips`
WHERE
    start_station_name != end_station_name
GROUP BY year, month
ORDER BY year ASC, month ASC
```
```python
SELECT * FROM `bq-sampleabc.basketball.mascots` LIMIT 10;
```
정상 동작하는 것이 확인되면 된다.


![google data studio1](https://user-images.githubusercontent.com/96108301/150300668-d2a4d036-cd5a-4cdb-91c8-ea635dea0b3b.PNG)

![google data studio2](https://user-images.githubusercontent.com/96108301/150300671-029cbaae-1754-43fe-af16-d13af02c3553.PNG)

