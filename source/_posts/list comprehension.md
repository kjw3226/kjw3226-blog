---
title: list comprehension
tag: list comprehension
date: 2021-11-10
categories:	Python
    
---
-Comprehension이란 
 iterable한 오브젝트를 생성하기 위한 방법중 하나로 파이썬에서 사용할 수 있는 유용한 기능중 하나이다.
 파이썬에는 다음과 같은 크게 네 가지 종류의 Comprehension이 있다.

 -List Comprehension (LC)
 -Set Comprehension (SC)
 -Dict Comprehension (DC)
 -Generator Expression (GE)

 Generator의 경우 comprehension과 형태는 동일하지만 특별히 expression이라고 부른다.

 그럼 이제 각각의 경우에 대해 간단히 살펴보자. 

 <for문을 활용한 list comprehension>
 List Comprehension은 리스트 안에서 for 문과 if 문을 이용하여 보다 편리하게 리스트를 작성하고 처리할 수 있게 해줄 수 있다. 
 List Comprehension의 기본 구조는 다음과 같다.

 ![list comprehension structure 1](https://user-images.githubusercontent.com/93234783/141088564-15228dcc-0017-4f2f-9afe-e2713978cacf.PNG)

 ![List Comprehension1](https://user-images.githubusercontent.com/93234783/141107585-75071139-3d77-4745-81af-824f8e4602ea.PNG)
 
 ![List Comprehension2](https://user-images.githubusercontent.com/93234783/141107632-9f1c563b-aac4-4e62-a067-1efacabe018f.PNG)

 ![List Comprehension3](https://user-images.githubusercontent.com/93234783/141107684-fa9bd45d-3c58-4145-9bca-a2c36eb17c51.PNG)

 <단일 if 문을 포함한 List Comprehension>

 if 문은 for 문 뒤에 나오면 된다. 만약 range(5)에서 짝수만 리스트로 작성하려면 아래와 같이 하면 된다.


![List Comprehension4](https://user-images.githubusercontent.com/93234783/141107743-5ab39f74-fbaf-4dd3-8d02-719a80706308.PNG)


![List Comprehension5](https://user-images.githubusercontent.com/93234783/141107803-a86dff68-a531-4f01-bd07-d50b4de53b53.PNG)


 [i for i in range(5)]의 결과가 [0,1,2,3,4]인데 이 중 if i%2 == 0 조건이 추가된다면, 

 이는 2로 나눈 나머지가 0이면 해당 i를 리스트에 생성하라는 의미이므로 [0,2,4]만 리스트에 나타나게 되는 것이다.

 마찬가지로, [i for i in range(5)]의 결과가 [0,1,2,3,4]인데 이 중 if i%2 == 1 조건이 추가된다면, 

 이는 2로 나눈 나머지가 1이면 해당 i를 리스트에 생성하라는 의미이므로 [1,3]만 리스트에 나타나게 되는 것이다.

 <if와 else문을 포함한 List Comprehension>

 if 문에 else를 추가하여 리스트를 생성할 수 있다. 만약에 [0,1,2,3,4] 중 짝수는 모두 리스트에 포함시키고 홀수일 경우에는 None을 리스트에 포함시키려고 한다면 아래와 같이 하면 된다.

 ![list comprehension structure 2](https://user-images.githubusercontent.com/93234783/141088564-15228dcc-0017-4f2f-9afe-e2713978cacf.PNG)

 else가 추가되는 경우에는 if~else문이 i와 for 사이에 위치하여야 한다는 점에 유의하기 바란다.


 ![List Comprehension6](https://user-images.githubusercontent.com/93234783/141108021-1448b29c-5a98-4084-a6b0-572425e4c675.PNG)


 <중첩 for문을 포함한 List Comprehension>

 for 문을 중첩하여 List Comprehension을 만들 수 있다. '1 - 5' 사이의 숫자에 각각 '7 - 9' 숫자를 곱한 결과를 리스트에 나타내고 싶다면 아래와 같이 하면 된다.



 ![List Comprehension7](https://user-images.githubusercontent.com/93234783/141108161-822dddc9-dac6-42c4-b5de-849cd44d6bb7.PNG)

 for 문 뒤에 for 문을 계속 쓰는 경우 앞의 for 문의 원소에 대해서 그 다음 for 문의 원소를 순차적으로 적용한 결과가 
 리스트에 나타나게 된다. 상기 사례를 도식화해서 나타내면 아래와 같다.

 ![list comprehension structure 3](https://user-images.githubusercontent.com/93234783/141088564-15228dcc-0017-4f2f-9afe-e2713978cacf.PNG)

 [ ( 변수를 활용한 값 ) for ( 사용할 변수 이름 ) in ( 순회할 수 있는 값 )] --> 이런 식으로 조건식을 매우 간단하게 표현할 수 있는 것이 'List Comprehension'이다.

