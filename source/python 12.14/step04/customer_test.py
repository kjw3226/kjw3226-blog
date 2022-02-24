# /c/ProgramData/Anaconda3/python
# -*- coding:utf-8 -*-

from customer05 import Customer

if __name__ == "__main__":
    cust = Customer("Belinda Lutz", 2000)
    cust.balance = 3000
    print(cust.balance)
    cust.balance = -1000
    print(cust.balance)