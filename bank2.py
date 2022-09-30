from bank import Bank
import random

class Bank_Branch(Bank):
    def __init__(self):
        super().__init__()
        self.name = input("Bank name: ")
        self.account_No = str(random.randint(2300000000, 2399999999))
        self.landing_page()
        

bank_branch = Bank_Branch()
       
        
