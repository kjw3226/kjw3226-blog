# /c/Program Files/anaconda3/envs/python-P/step03
# -*- coding: utf-8 -*-
# != __ne__()
# >= __ge__()
# <= __le__()
# > __gt__()
# < __lt__()

class Bank:

    # instance attribute
    def __init__(self, cust_id, balance=0):
        self.balance = balance
        self.cust_id = cust_id

    # instance method
    def withdraw(self, amount):
        self.balance -= amount

    def __eq__(self, other):
        print("__eq()__ is called")
        return self.cust_id == other.cust_id

    def __ne__(self, other):
        print("__eq()__ is called")
        return self.cust_id != other.cust_id


if __name__ == "__main__":
    account01 = Bank(123, 1000)
    account02 = Bank(123, 1000)
    account03 = Bank(456, 1000)
    print(account01 == account02)
    print(account02 == account03)
    print(account01 == account03)
