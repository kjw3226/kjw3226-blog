---
title: How to convert a dictionary to a Json file
tag: How to convert a dictionary to a Json file
date: 2022-05-17
categories:	Everyday life (일상 생활)
----

오늘은 'dictionary(딕셔너리형)' 파일을 

'Jason(제이슨 형)' 파일로 

변환하는 법을 

공부했다.

아래 코드는 오늘 실습한 코드들이다.

```python
<JSON을 Dictionary 로 간단하게 변환>

import json

json_example = '{"olivia": {"gender": "female", "age": 25, "hobby": ["reading", "music"]}, "Tyler": {"gender": "male", "age": 28, "hobby": ["development", "painting"]}}'

dict_example = json.loads(json_example) # Convert json to dict


print("JSON Type : ", type(json_example))
print("JSON : ", json_example)
print("Dictionary Type : ", type(dict_example))
print("Dictionary : ", dict_example)


# Output
# JSON Type :  <class 'str'>
# JSON :  {"olivia": {"gender": "female", "age": 25, "hobby": ["reading", "music"]}, "Tyler": {"gender": "male", "age": 28, "hobby": ["development", "painting"]}}
# Dictionary Type :  <class 'dict'>
# Dictionary :  {'olivia': 
```

반대로는

```python
<Dictionary 를 JSON으로 간단하게 변환>

import json

dict_example = {
  "olivia" : {
    "gender": "female",
    "age" : 25,
    "hobby" : ["reading", "music"]
  },
  "Tyler" : {
    "gender": "male",
    "age" : 28,
    "hobby" : ["development", "painting"]
  }
}

json_example = json.dumps(dict_example) # Convert dict to json


print("Dictionary Type : ", type(dict_example))
print("Dictionary : ", dict_example)
print("JSON Type : ", type(json_example))
print("JSON : ", json_example)


# Output
# Dictionary Type :  <class 'dict'>
# Dictionary :  {'olivia': {'gender': 'female', 'age': 25, 'hobby': ['reading', 'music']}, 'Tyler': {'gender': 'male', 'age': 28, 'hobby': ['development', 'painting']}}
# JSON Type :  <class 'str'>
# JSON :  {"olivia": {"gender": "female", "age": 25, "hobby": ["reading", "music"]}, "Tyler": {"gender": "male", "age": 28, "hobby": ["development", "painting"]}}
```

그리고 

아래 코드는 파일을 저장하는 코드다.

```python
# json 모듈 로드
import json

persons = [
	{'name':'Han Byungik', 'age':35, 'hobby':'game'},
    {'name':'Park junkyu', 'age':34, 'hobby':'walk'},
    {'name':'Lee hyunbok', 'age':37, 'hobby':'talk'},
    {'name':'Yoon hyejun', 'age':37, 'hobby':'sleep'},
    {'name':'Han bin', 'age':39, 'hobby':'soccer'},
]

# json 파일로 저장
with open('persons.json', 'w') as f : 
	json.dump(persons, f, indent=4)
```
