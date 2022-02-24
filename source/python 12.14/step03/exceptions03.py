# /c/Program Files/anaconda3/envs/python-P/step03
# -*- coding: utf-8 -*-
# 클래스
# __init__ <--- set_name, set_balanace
# __eq__, __ne__, etc
# 상속, 다형성


class SalaryExcept(ValueError): pass # 상속
class TipExcept(SalaryExcept): pass # 상속

class Employee:

    # class attribute
    MIN_SALARY = 20000
    MAX_BONUS = 10000

    # instance attribute
    def __init__(self, name, salary = 30000):
        self.name = name
        if salary < Employee.MIN_SALARY:
            raise SalaryExcept("급여가 너무 낮아요!")
        self.salary = salary

    # instance method
    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            print("보너스가 너무 많습니다!")
        elif self.salary + amount < Employee.MIN_SALARY:
            print("보너스 지급 후의 급여도 매우 낮아요!")
        else:
            self.salary += amount

if __name__ == "__main__":
    emp = Employee("Evan", salary=20000)
    try:
        emp.give_bonus(70000)
    except SalaryExcept:
        print("Salary 오류가 감지됨")
    try:
        emp.give_bonus(-100000)
    except TipExcept:
        print("Tip 오류 감지됨")
