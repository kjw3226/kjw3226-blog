# /c/ProgramData/Anaconda3/python
# -*- coding:utf-8 -*-

from properties04 import Employee

if __name__ == "__main__":

    emp = Employee("Miriam Azari", 3000)
    print(emp.salary)

    emp.salary = 6000 # <= @salary.setter
    print(emp.salary)
    emp.salary = 1000