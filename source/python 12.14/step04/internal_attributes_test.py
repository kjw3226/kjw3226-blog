# /c/ProgramData/Anaconda3/python
# -*- coding:utf-8 -*-

from internal_attributes03 import BetterDate

if __name__ == "__main__":
    bd1 = BetterDate(2021, 4, 30)
    print(bd1._is_valid())
    bd2 = BetterDate(2021, 6, 45)
    print(bd2._is_valid())

