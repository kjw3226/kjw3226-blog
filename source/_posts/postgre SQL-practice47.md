---
title: postgre SQL-practice47
tag: postgre SQL-practice47
date: 2022-03-30
categories:	SQL
---
'예제 코드'는 여기서 다운 받아 실행하면 된다.

['SQL CODE'](source/Lecture/sql recipes for data analysis/sql recipes for data analysis example code)

'6장  15강 사이트 내의 사용자 행동 파악하기

8. 페이지 완독률 집계하기'

로 넘어갔으며, 페이지는 387 ~ 390을 참고하였다.


완독률을 집계하는 쿼리문
```python
SELECT
   url
 , action
 , COUNT(1) AS count
 , 100.0
   * COUNT(1)
   / SUM(CASE WHEN action = 'view' THEN COUNT(1) ELSE 0 END)
      OVER(PARTITION BY url)
   AS action_per_view
FROM read_log
GROUP BY
 url, action
ORDER BY
 url, count DESC
;
```

EC 사이트에서는 상품 상세 정보 아래에 '추천 상품'을 출력하는 모듈, 

뉴스 사이트에서는 기사 마지막에 '관련 기사'를 출력하는 모듈이 설치

되어 있는 경우가 많습니다.

이러한 모듈은 일반적으로 상품 정보와 기사를 끝까지 읽어야 보이므로,

해당 페이지의 완독률이 낮으면 모듈을 아무리 설치해도 의미가 없습니다.

따라서 이러한 모듈을 사용할 때는 페이지의 완독률을 확인하고,

모듈의 효과가 충분히 효과가 발생할지 고민해보기 바랍니다.

(데이터 분석을 위한 SQL 레시피-6장 웹사이트에서의

행동을 파악하는 데이터 추출하기 15강 페이지 390 中)

[SQL recipes for data analysis](source/image/sql recipes for data analysis-correction.jpg)

참고 도서 : 데이터 분석을 위한 SQL 레시피

저자 : 가나키 나가토, 다미야 나오토

출판사 : 한빛미디어

