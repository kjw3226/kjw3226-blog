# /c/Program Files/anaconda3/envs/python-P/step03
# -*- coding: utf-8 -*-

class Bank:

    # cust_id, balance = 0
    def __init__(self, cust_id, balance = 0):
        self.cust_id, self.balance = cust_id, balance


    # withdraw method
    def withdraw(self, amount):
        self.balance -= amount

    # eq
    def __eq__(self, other):
        print("__eq()__ is called")
        return (self.cust_id == other.cust_id) and (type(self) == type(other))

class Phone:

    def __init__(self, cust_id):
        self.cust_id = cust_id

    def __eq__(self, other):
        return self.cust_id == other.cust_id

if __name__ == "__main__":
    account01 = Bank(1234)
    phone01 = Phone(1234)

    print(account01 == phone01)