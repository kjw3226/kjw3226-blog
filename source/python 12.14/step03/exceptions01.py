# /c/Program Files/anaconda3/envs/python-P/step03
# -*- coding: utf-8 -*-

def error01():
    a = 10
    a / 0
    # ZeroDivisionError: division by zero

def error02():
    a = [1, 2, 3, 4, 5]
    a[10]
    # IndexError: list index out of range

def error03():
    a = 1000
    a + "안녕"
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'

def error04():
    a = 1000
    a + b
    # NameError: name 'b' is not defined

if __name__ == "__main__":
    error01()
    error02()
    error03()
    error04()

    print("Program is done")

# 크롤링 코드 작성
# "https://sports.news.naver.com/news?oid=109&aid=00045260" + "83" # 페이지 없음

# 크롤링 코드 멈춤

# URL: https://sports.news.naver.com/news?oid=109&aid=0004526080
