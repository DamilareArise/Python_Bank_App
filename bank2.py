
from bank import Bank
import random

class Bank_Branch(Bank):
    def __init__(self):
        super().__init__()
        self.name = input("Bank name: ")
        self.account_No = str(random.randint(2300000000, 2399999999))
        self.landing_page()
        

bank_branch = Bank_Branch()
       
        
# myfile = open("C:\\python-works\\Banks\\bank2.py", mode= "rt") 
# print(myfile.read())

# import sys
# import random
# class bank:
#     def __init__(self):
#         self.account_num = str(random.randint(2300000000, 2399999999))


#     def landing_page(self):
#         print("""
#         Welcome to Mtp Bank plc

#         1. Sign in 
#         2. Sign up
#         3. Exit
        
#         """)
#         user = input("Option: ")
#         if user == "1":
#             self.signin()+
#         elif user == "2":
#             self.signup()
#         elif user == "3":
#             sys.exit()

#     def signup(self):
#         self.full_name = input("Full Name: ")
#         self.email = input("Email: ")
#         self.username = input("Username: ")
#         self.password = input("password: ")
#         print(f"Your Account, with account number {self.account_num} has been created successfully, kindly login")
#         self.signin()

#     def signin(self):

#         username = input("Username: ")
#         password = input("password: ")

#         if username == self.username and password == self.password:
#             self.landing_page2()
        
#         else:
#             print("wrong username or password")

#             self.landing_page()

#     def landing_page2(self):
