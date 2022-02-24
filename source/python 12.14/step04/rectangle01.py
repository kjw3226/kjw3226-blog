# /c/ProgramData/Anaconda3/python
# -*- coding:utf-8 -*-

class Rectangle:
    def __init__(self, h, w):
        self.h, self.w = h, w

# Define a Square class
class Square(Rectangle):
    def __init__(self, w):
        self.h, self.w = w, w

