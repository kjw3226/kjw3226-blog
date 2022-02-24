# /c/ProgramData/Anaconda3/python
# -*- coding:utf-8 -*-

class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError("Invalid Balance")
        self._balance = new_bal

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_bal):
        if new_bal < 0:
            raise ValueError("Invalid balance!")
        self._balance = new_bal
        print("Setter method is called")
