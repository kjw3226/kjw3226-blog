# /c/ProgramData/Anaconda3/python
# -*- coding:utf-8 -*-

class Parent:
    def talk(self):
        print("Parent talking!")

class Son(Parent):
    def talk(self):
        print("Son talking!")

class Daughter(Parent):
    def talk(self):
        print("Daughter talking!")
        Parent.talk(self)

if __name__ == "__main__":
    pat, son, daughter = Parent(), Son(), Daughter()
    for obj in (pat, son, daughter):
        obj.talk()