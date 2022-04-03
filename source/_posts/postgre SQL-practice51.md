---
title: postgre SQL-practice51
tag: postgre SQL-practice51
date: 2022-04-03
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'7장  17강 데이터를 조합해서 새로운 데이터 만들기'의

'1. IP 주소를 기반으로 국가와 지역 보완하기'로 넘어갔으며

페이지 408 ~ 414를 참고하였다.

액션 로그의 IP 주소로 국가와 지역 정보를 추출하는 쿼리문
```python
SELECT
   a.ip
 , l.continent_name
 , l.country_name
 , l.city_name
 , l.time_zone
FROM
   action_log AS a
 LEFT JOIN
   mst_city_ip AS i
   ON a.ip::inet << i.network
 LEFT JOIN
  mst_locations AS l
  ON i.geoname_id = l.geoname_id
;
```

PostgreSQL 이외의 미들웨어에서 IP 주소를 다루는 방법은 6강 6절에서

소개했습니다. 네트워크 범위의 최소/최대 IP 주소를 계산하고, 비교

가능한 형식으로 변환해야 다양하게 활용할 수 있습니다. CSV 파일의

데이터를 전처리 해주는 'GeoIP2 CSV Format Converter' 등의 

도구가 있으므로 한번 살펴보기 바랍니다.

(데이터 분석을 위한 SQL 레시피-7장 데이터 활용의

정밀도를 높이는 분석 기술 17강 데이터를 조합해서

새로운 데이터 만들기 페이지 414 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어