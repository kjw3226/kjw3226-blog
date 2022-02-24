# /c/ProgramData/Anaconda3/python
# -*- coding:utf-8 -*-

class Employee:
    def __init__(self, name, new_salary):
        self._salary = new_salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Invalid salary")
        self._salary = new_salary

