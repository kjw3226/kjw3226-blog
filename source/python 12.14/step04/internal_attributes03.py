# /c/ProgramData/Anaconda3/python
# -*- coding:utf-8 -*-

class BetterDate:
    _MAX_DAYS = 30
    _MAX_MONTHS = 12

    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day


    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    def _is_valid(self):
        return (self.day <= BetterDate._MAX_DAYS) and \
               (self.month <= BetterDate._MAX_MONTHS)

