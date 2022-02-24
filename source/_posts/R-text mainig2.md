---
title: R-Text Mining2(R-텍스트 마이닝2)
tag: R-Text Mining2(R-텍스트 마이닝2)
date: 2021-12-14
categories:	R
---
어제에 이어서 오늘도 '텍스트 마이닝'을 

실습 했다.

아래는 시작 전 해야 하는 작업들이다.

<MeCab 설치>
'Mecab-ko' 형태소 분석기 사용 위해서는 Rcppmecab 패키지가 있어야함.

설치를 위한 URL: [URL][https://github.com/junhewk/RcppMeCab/blob/master/README_kr.md]

해당 깃허브에서 설치해야 할 파일을 다운로드 받은 후,

![RcppMeCab_zipfiles](https://user-images.githubusercontent.com/96108301/147801420-7654b2d7-8fa3-498e-9167-aa72bf048b68.png)

- 압축 해제 시에 C drive 에서 mecab folder 생성
- 오른쪽 버튼 클릭 후 여기에 압출풀기를 선택하면 쉽다.

이 과정에서

![Rcppmecab](https://user-images.githubusercontent.com/96108301/147801479-20edbe9d-d72d-4777-b4c3-a793a6dd2826.png)

위의 file 내의 폴더 형태와, file 명, 경로 가 같지 않으면 다음과 같은 에러가 난다.
```python
Exception:
list()
```
- 경로, file명 등을 확인 하기 바란다.

<오류 해결 참조> ![URL][https://github.com/junhewk/RcppMeCab/issues/12]

이제 'Mecab'을 'R-studio'를 이용해 'R'에 설치하자
```python
# library(remotes)
remotes::install_github("junhewk/RcppMeCab", force = TRUE)

library(RcppMeCab)
```
- RcppMeCab 설치 확인 (형태소 분리기)
한글을 써 본다.
```python
text1 = "안녕하세요?!"
pos(sentence = text1)

text2 = enc2utf8(text1)
pos(sentence = text2)
```
그러면 이렇게 실행 화면이 나타난다.
```python
text2 = enc2utf8(text1)

pos(sentence = text2)

$안녕하세요?!

[1] “안녕/NNG” “하/XSV” “세요/EP+EF” “?/SF” “!/SF”
```
오늘은 이렇게만 실습을 하였다.

더 자세한 실습 자료는 [URL][source/Lecture/text_mining] 
여기에 가면 있다.