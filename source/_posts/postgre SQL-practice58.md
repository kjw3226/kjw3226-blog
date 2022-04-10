---
title: postgre SQL-practice58
tag: postgre SQL-practice58
date: 2022-04-10
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'7장  19강 데이터 중복 검출하기'의

'1. 마스터 데이터에서 중복 검출하기'로 넘어갔으며

페이지 440 ~ 444을 참고하였다.


키의 중복을 확인하는 쿼리문
```python
SELECT
   COUNT(1) AS total_num
 , COUNT(DISTINCT id) AS key_num
FROM
 mst_categories
;
```


키가 중복되는 레코드의 값 확인하는 쿼리문
```python
SELECT
   id
 , COUNT(*) AS record_num
 
 --데이터를 배열로 집약하고, 쉼표로 구분된 문자열로 변환하기
 --■PostgreSQL, BigQuery의 경우는 string_agg 사용하기
 , string_agg(name,  ',') AS name_list
 , string_agg(stamp, ',') AS stamp_list
 --■Redshift의 경우는 listagg 사용하기
 --, listagg(name,  ',') AS name_list
 --, listagg(stamp, ',') AS stamp_list
 --■Hive, SparkSQL의 경우는 collesct_list와 concat_ws 사용하기
 --, concat_ws(',', collect_list(name )) AS name_list
 --, concat_ws(',', collect_list(stamp )) AS stamp_list
FROM
 mst_categories
GROUP BY id
HAVING COUNT(*) > 1 -- 중복된 ID 확인하기
;
```

윈도 함수를 사용해서 중복된 레코드를 압축하는 쿼리문
```python
WITH
mst_categories_with_key_num AS (
 SELECT
	*
	-- ID 중복 세기
  , COUNT(1) OVER(PARTITION BY id) AS key_num
 FROM
	mst_categories
)
SELECT
 *
FROM
 mst_categories_with_key_num
WHERE
 key_num > 1 -- ID가 중복되는 경우 확인하기
;
```

마스터 데이터의 ID가 중복되는 경우는 기본적으로 어떤 실수 또는 오류가

원인일 수 있습니다. 이러한 때는 일단 마스터 데이터를 클렌징하기 바랍니다.

여러 번의 데이터 로드가 원인이라면, 데이터 로드 흐름을 수정하거나 또는 

매번 데이터를 지우고 새로 저장하는 방법을 사용하여 여러 번 데이터를 

로드해도 같은 실행 결과가 보증되게 만들기 바랍니다.

마스터 데이터가 도중에 갱신되어 새로운 데이터와 오래된 데이터가 중복된

경우에는 새로운 데이터만 남기거나, 타임스탬프를 포함해서 유니크 키를 

구성하는 방법도 생각해 볼 수 있습니다.

(데이터 분석을 위한 SQL 레시피-7장 데이터 활용의

정밀도를 높이는 분석 기술 19강 데이터 중복 검출하기 444 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어
