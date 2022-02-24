---
title: text mainig python (machine learning)
tag: text mainig python (machine learning)
date: 2021-12-17
categories:	Python Machine Learning
---
<데이터 불러오기>
```python
# ---- 데이터 불러오기 ----

library(ggplot2) # 시각화 코드
# install.packages("dplyr")
# install.packages("tidyr")
library(dplyr) # 데이터 가공
library(reshape) # 데이터 가공 <-- tidyr
library(readr) # 파일 입출력


raw_reviews = read_csv("data/Womens Clothing E-Commerce Reviews.csv") %>% select(-1)

# raw_reviews <- raw_reviews %>% select(-1)
glimpse(raw_reviews)

colnames(raw_reviews) <- c("ID", "Age", "Title", "Review", "Rating", "Recommend", "Liked", "Division", "Dept", "Class")

glimpse(raw_reviews) 

# age 리뷰 작성한 고객의 연령
# Title, Review Text 리뷰 제목, 내용
# Rating: 고객이 부여한 평점
# Recommend IND: 추천 여부
# Positive Feedback Count: 좋아요 수치
# Division, Dept, Class --> 상품의 대분류 정보
```
<데이터 전처리>
```python
# ---- 데이터 전처리 ----
# 결측치 확인
colSums(is.na(raw_reviews))

table(raw_reviews$Age)

age_group = cut(as.numeric(raw_reviews$Age), 
                breaks = seq(10, 100, by = 10), 
                include.lowest = TRUE, 
                right = FALSE, 
                labels = paste0(seq(10, 90, by = 10), "th"))

age_group[1:10]

# 새로운 변수 추가
raw_reviews$age_group = age_group
table(raw_reviews$age_group)

# 감성 사전 데이터셋 변환
summary(raw_reviews$Liked)
table(raw_reviews$Liked)

# 층화추출? / 임의추출
idx = sample(1:nrow(raw_reviews), nrow(raw_reviews) * 0.1, replace = FALSE)

raw_reviews2 = raw_reviews[idx, ] 

raw_reviews2 %>% 
  mutate(pos_binary = ifelse(Liked > 0, 1, 0)) %>% # 이산형 변수로 변환
  select(Liked, pos_binary) -> pos_binary_df

pos_binary_df$pos_binary <- as.factor(pos_binary_df$pos_binary)

table(pos_binary_df$pos_binary) # 0 부정, 1 긍정

# ---- 키워드 데이터셋 생성
REVIEW_TEXT = as.character(raw_reviews2$Review)
REVIEW_TEXT = tolower(raw_reviews2$Review)

# 단어를 이어 붙인 후, 토큰화된 단어들로 문장 재구성
library(tokenizers)

TEXT_Token = c()
for(i in 1:length(REVIEW_TEXT)) {
  token_words = unlist(tokenize_word_stems(REVIEW_TEXT[i]))
  Sentence = ""
  
  for (tw in token_words) {
    Sentence = paste(Sentence, tw)
  }
  
  TEXT_Token[i] = Sentence
  
}
```
<텍스트 전처리>
```python
# ---- 텍스트 전처리
library(tm)

Corpus_token = Corpus(VectorSource(TEXT_Token))
Corpus_tm_token = tm_map(Corpus_token, removePunctuation)
Corpus_tm_token = tm_map(Corpus_token, removeNumbers)
Corpus_tm_token = tm_map(Corpus_token, removeWords, c(stopwords("English")))


#TDM과 DTM 의 차이 (TDM :term Document Matrix)
# T=ODF . DTM = CountVectprozor(in Python)
DTM_Token = DocumentTermMatrix(Corpus_tm_token)
DTM_Matrix_Token = as.matrix(DTM_Token)

# 상위 키워드 추출
# quantile() 함수 활용
top_1_pct = colSums(DTM_Matrix_Token) > quantile(colSums(DTM_Matrix_Token), probs = 0.99)

DTM_Matrix_Token_selected = DTM_Matrix_Token[, top_1_pct]

ncol(DTM_Matrix_Token_selected)

#Error
DTM_df = as.data.frame(DTM_Matrix_Token_selected)
DTM_df

pos_final_df = cbind(pos_binary_df, DTM_df)

glimpse(pos_final_df)


#희소행렬 문제가 나타나게 된다.

ncol(pos_final_df)
```
<훈련,검증용 데이터 분류>
```python
# ---- 훈련 검증용 데이터 분류 ----
set.seed(1234)
idx = sample(1:nrow(pos_final_df), nrow(pos_final_df) * 0.7, replace = FALSE)
train = pos_final_df[idx, ]
test = pos_final_df[-idx, ]
```
<로지스틱 회귀 모형 개발 (Logistic Regression Model Develop)>
```python
# --- 로지스틱 회귀 모형 개발 ---

start_time = Sys.time()

glm_model = step(glm(pos_binary ~ .,
                     data = train[-1],
                     family = binomial(link = "logit")),
                 direction = "backward") # 후진소거법

End_time = Sys.time()
difftime(End_time, start_time, units = "secs")
```
Step: AIC=2202.56
 - Logistic regression 안의 평가 기준
 - 낮을 수록 좋다.

```python
Step: AIC=2202.2
pos_binary ~ love + veri + just + size + dress + fit + will +
back + like + tri + flatter + top + length + realli + shirt +
materi
```
<실행 화면>

![AIC_LogisticR](https://user-images.githubusercontent.com/96108301/147807053-3c8c740c-0b89-4823-978c-aaa9167099c4.png)

<모형 성능 측정>

```python
# ---- 모형 성능 측정 ----
# install.packages("pROC")
library(pROC)
preds = predict(glm_model, newdata = test, type = "response")
roc_glm = roc(test$pos_binary, preds)
plot.roc(roc_glm, print.auc=TRUE)
```
<실행 화면>

![R_calssification_pROC](https://user-images.githubusercontent.com/96108301/147807155-1428650c-cfbb-41d0-aad2-1d0760bacfca.png)

<정리>
1. 정형 데이터 가져 오기 
2. 정형 데이터 가공
    - 좋아요 수를 활용하여 긍정/부정 data 나눔
3. 정형 데이터 분리 : 텍스트 데이터 따로 분리 
4. 텍스트 데이터 처리 (전처리, 토큰화, 코퍼스, DTM)
5. 텍스트 데이터 + 기존 data 합침
6. ML 모형 진행 (다른 모형을 진행 해도 된다. )

지금까지 배운 내용이 어렵다면 python 으로만 하는 것도
나쁘지 않다.
