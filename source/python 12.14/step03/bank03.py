# /c/Program Files/anaconda3/envs/python-P/step03
# -*- coding: utf-8 -*-

# 프로젝트 4개월
# 1개월 환경세팅, 미팅, 요구 사항 미팅
# 2개월 날코딩 (프레임워크 위주로 코드 짬) / 자동화 (x)
# 1개월 문서 작업, 코드 리팩토링 (기초문법*****)

class Bank:

    def __init__(self, cust_id, name, balance = 0):
        self.cust_id, self.name, self.balance = cust_id, name, balance

    def __str__(self):
        cust_str = """
        Customer:
            cust_id : {cust_id}
            name : {name}
            balance : {balance}
        """.format(cust_id = self.cust_id, name = self.name, balance = self.balance)

        return cust_str

if __name__ == "__main__":
    bank_cust = Bank(123, "Kim")
    print(bank_cust)