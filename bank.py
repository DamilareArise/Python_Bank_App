
import mysql.connector as sql
import time
import sys
import random
import datetime as dt


mycon = sql.connect(host='127.0.0.1', user='root', passwd='', database='mybank_db')
# mycursor = mycon.cursor()

# mycursor.execute("DROP TABLE customer_details")

# mycursor.execute("CREATE TABLE customer_details (customer_ID INT(4) PRIMARY KEY AUTO_INCREMENT, full_name VARCHAR(40), address VARCHAR(20), phone_no VARCHAR(12), username VARCHAR(10) UNIQUE, pin INT(4), account_no VARCHAR(12) UNIQUE, account_balance FLOAT(20))")



# mycursor.execute("CREATE TABLE Transaction_table (transaction_id INT(4) PRIMARY KEY AUTO_INCREMENT, date_time DATETIME(6), amount FLOAT(20), transaction_type VARCHAR(20), beneficiary_acc VARCHAR(12), sender_acc VARCHAR(12), reciever_account VARCHAR(12), account_no VARCHAR(12))")


# self.mycursor.execute('SHOW TABLES')
# for table in self.mycursor:
#     print(table)


class Bank:
    def __init__(self):
        self.name = "Lolla Bank Plc"
        self.account_No = str(random.randint(2200000000, 2299999999))
        self.account_balance = float(0)
        self.time = dt.datetime.now()
        self.mycursor = mycon.cursor()
        print(self.time)
        self.landing_page()

    def landing_page(self):

        print(f"Welcome to {self.name}".center(100))
        time.sleep(1)

        print("""
        1. Signin
        2. Signup
        3. Quit 
        
        """)

        user = input("Input option: ")
        if user.strip() == "1":
            self.signin()
        elif user.strip() == "2":
            self.signup()
        elif user.strip() == "3":
            self.quit()
        else:
            print("invalid input")
            time.sleep(2)
            self.landing_page()
 
    def signup(self):
       

        print('''
        Signup >>>
        ''')

        full_name = input("Full Name: ")
        address = input("Address: ")
        phone_no = input("Phone Number: ")
        username =input("Enter Prefered Username: ")
        pin =input("Enter your four(4)digit pin: ")

        try:
            query = "INSERT INTO customer_details (full_name, address, phone_no, username, pin, account_no, account_balance) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (full_name,  address, phone_no, username, pin, self.account_No, self.account_balance )
            self.mycursor.execute(query, val)
            mycon.commit()
        except:
            print("Username Taken, enter another")
            self.signup()
        else:
            print("Please wait...")
            time.sleep(2)
            print(f'''
            Congratulations your account as been created successfully.
            Your account number is {self.account_No} 
            
            Kindly Login >>>

            ''')    
            self.signin()    

    def signin(self):
       

        print('''
        Loading...
        ''')
        time.sleep(1)
    
        self.inp_username = input("Username >> ")
        self.inp_pin = input("Pin >> ")

        query2 = "SELECT full_name, account_no, account_balance, pin FROM customer_details WHERE username = %s AND pin = %s"
        val2 = (self.inp_username, self.inp_pin )
        self.mycursor.execute(query2, val2)
        details = self.mycursor.fetchall()
        try:
            self.name_user = details[0][0]
            self.number_user = details[0][1]
            self.balance_user = details[0][2]
            self.pin_user = details[0][3]
        except:
            print("Wrong username or password ")
            user = input("Press 'ENTER' to retry or '1' to go back to menu: ")
            while user != "1":
                self.signin()
            self.landing_page()
        else:
            print('''
        loading...  
            ''')
            time.sleep(1)
            print(f'Welcome {self.name_user} with account number {self.number_user}, Your account balance is ${self.balance_user}')
            self.landing_page2()
              
    def landing_page2(self):
        print("""

        1. Deposit                  4. Airtime
        2. Withdrawal               5. Check balance
        3. Transfer                 6. Logout
        7. Exit                     8. Check History
        
        """)

        try:

            option = int(input('Your option: '))
        except ValueError:
            print("Invalid input")
            self.landing_page2()

        else:
                
            if option == 1:
                self.deposit()
            elif option == 2:
                self.withdrawal()
            elif option == 3:
                self.transfer()
            elif option == 4:
                self.airtime()    
            elif option == 5:
                self.account_bal()
            elif option == 6:
                self.landing_page()
            elif option == 7:
                self.quit()
            elif option == 8:
                self.history()
            else:
                print("Invalid input")
                self.landing_page2()
        
    def quit(self):
        sys.exit()
    
    def history(self):
        mycon = sql.connect(host='127.0.0.1', user='root', passwd='', database='mybank_db')
        
        query = "SELECT  date_time, amount, transaction_type, reciever_account  FROM Transaction_table WHERE account_no = %s "
        val = (self.number_user, )
        self.mycursor.execute(query, val)
        details = self.mycursor.fetchall()
        
        for each_detail in details:
            print(f"Date&Time:{each_detail[0]}, Amount:{each_detail[1]}, Transaction Type:{each_detail[2]}, Beneficiary Account/Phone:{each_detail[3]}")
        mycon.close()
        time.sleep(1)
        user = input("Press 'ENTER' to continue or '1' to exit: ")
        while user.strip() != "1":
            self.landing_page2()
        self.quit()

    def account_bal(self):
        mycon = sql.connect(host='127.0.0.1', user='root', passwd='', database='mybank_db')

        query2 = "SELECT account_balance FROM customer_details WHERE username = %s AND pin = %s"
        val2 = (self.inp_username, self.inp_pin )
        self.mycursor.execute(query2, val2)
        details = self.mycursor.fetchall()
        mycon.close()
        time.sleep(1)
        print(f"Your account balance is ${details[0][0]}")
        time.sleep(1)

        self.landing_page2()

    def airtime (self):
        mycon = sql.connect(host='127.0.0.1', user='root', passwd='', database='mybank_db')

        query = "SELECT account_balance FROM customer_details WHERE username = %s AND pin = %s"
        val2 = (self.inp_username, self.inp_pin )
        self.mycursor.execute(query, val2)
        details = self.mycursor.fetchall()

        try:
            user = float(input(f"Input amount: "))
            num = (input(f"Input Phone number:"))
        except:
            print("Invalid Input")
            self.airtime()
        else:
            if details[0][0] < user:
                print('''

                Insufficient fund..

                ''')
                time.sleep(1)
                self.landing_page2()
            else:
                new_balance = details[0][0] - user 
                query = "UPDATE customer_details SET account_balance =%s WHERE pin = %s"
                val = (new_balance, self.inp_pin)
                self.mycursor.execute(query, val)
                mycon.commit()

                time_now = dt.datetime.now()
                query3 = "INSERT INTO Transaction_table (date_time, amount, transaction_type, sender_acc, reciever_account, account_no) VALUES(%s, %s, %s, %s, %s, %s)"
                val3 = (time_now, user, "Airtime",  self.number_user, num, self.number_user)
                self.mycursor.execute(query3, val3)
                mycon.commit()
                mycon.close()

                print(f"{num} has being credited with ${user} at {time_now}")
                time.sleep(1)
                self.landing_page2()

    def deposit(self):
        mycon = sql.connect(host='127.0.0.1', user='root', passwd='', database='mybank_db')
        
        det = {"1":50.0, "2":100.0, "3":500.0, "4":1000.0}
        print ("""
    
        1> $50                      2> $100
        3> $500                     4> $1000
        5> Others                   6> Back

        """)

        user = input('Input Your option: ')

        
        if user == "5":
            try:
                request = float(input("Input amount: "))
            except:
                print("Invalid input..")
                self.deposit()
        elif user == "6":  
            time.sleep(1)
            self.landing_page2()
        else:
            try:
                request = det[user] 
            except:
                print("Invalid input..")
                self.deposit()

        query2 = "SELECT account_balance FROM customer_details WHERE username = %s AND pin = %s"
        val2 = (self.inp_username, self.inp_pin )
        self.mycursor.execute(query2, val2)
        details = self.mycursor.fetchall()
        

        new_balance = details[0][0] + request

        query = "UPDATE customer_details SET account_balance =%s WHERE username = %s"
        val = (new_balance, self.inp_username)
        self.mycursor.execute(query, val)
        

        time.sleep(1)
        print(f"You've successfully deposited ${request} at {self.time}, Your account balance is ${new_balance}")

        time_now = dt.datetime.now()
        query3 = "INSERT INTO Transaction_table (date_time, amount, transaction_type, sender_acc, reciever_account, account_no) VALUES(%s, %s, %s, %s, %s, %s)"

        val3 = (time_now, request, "Deposit",  self.number_user, self.number_user, self.number_user)
        self.mycursor.execute(query3, val3)
        mycon.commit()
        mycon.close()

        time.sleep(1)
        self.landing_page2()   
                
    def withdrawal(self):
        mycon = sql.connect(host='127.0.0.1', user='root', passwd='', database='mybank_db')

        det = {"1":50.0, "2":100.0, "3":500.0, "4":1000.0}
        print ("""
    
        1> $50                      2> $100
        3> $500                     4> $1000
        5> Others                   6> Back

        """)

        user = input('Input Your option: ')

        
        if user == "5":
            try:
                request = float(input("Input amount: "))
            except:
                print("Invalid input..")
                self.withdrawal()
        elif user == "6":  
            time.sleep(1)
            self.landing_page2()
        else:
            try:
                request = det[user] 
            except:
                print("Invalid input..")
                self.withdrawal()

        query2 = "SELECT account_balance FROM customer_details WHERE username = %s AND pin = %s"
        val2 = (self.inp_username, self.inp_pin )
        self.mycursor.execute(query2, val2)
        details = self.mycursor.fetchall()
        
        if request > details[0][0]:
            print("Insufficient fund")
            time.sleep(1)
            self.landing_page2()

        else:
            new_balance = details[0][0] - request

            query = "UPDATE customer_details SET account_balance =%s WHERE username = %s"
            val = (new_balance, self.inp_username)
            self.mycursor.execute(query, val)
            
            time.sleep(1)
            time_now = dt.datetime.now()
            print(f"You've successfully withdraw ${request} at {time_now}, Your account balance is ${new_balance}")

            query3 = "INSERT INTO Transaction_table (date_time, amount, transaction_type, sender_acc, reciever_account, account_no) VALUES(%s, %s, %s, %s, %s, %s)"
            val3 = (time_now, request, "Withdrawal",  self.number_user, self.number_user, self.number_user)
            self.mycursor.execute(query3, val3)
            mycon.commit()
            mycon.close()
            time.sleep(1)
            self.landing_page2()

    def transfer(self):
        mycon = sql.connect(host='127.0.0.1', user='root', passwd='', database='mybank_db')

        query = "SELECT account_no, full_name  FROM customer_details"
        self.mycursor.execute(query)
        info = self.mycursor.fetchall()

        print("Please wait...")
        time.sleep(1)

        print("Available accounts are;")
        accounts = {}
        for all in info: 
            accounts.update({all[1]:all[0]})
        print(accounts)

        time.sleep(2)
        
        user = input("Input recipient account number: ")
        
        if user.strip() == self.number_user:
            print("Error..!, You can't transfer to self.")
            time.sleep(2)
            user_1 = input("Press 'ENTER' to retry or '1' to go back to menu: ")
            while user_1 != "1":
                self.transfer()
            self.landing_page2()
            
        else:
            query = "SELECT full_name, account_balance, account_no FROM customer_details WHERE account_no=%s"
            val = (user, )
            self.mycursor.execute(query, val)
            info2 = self.mycursor.fetchall() 

            query2 = "SELECT account_balance, account_no FROM customer_details WHERE username = %s AND pin = %s"
            val2 = (self.inp_username, self.inp_pin )
            self.mycursor.execute(query2, val2)
            details = self.mycursor.fetchall()  

            try:
                amount = float(input(f"How much are you sending to {info2[0][0]}: "))
            except:
                print("Invalid input")
                time.sleep(2)
                user_1 = input("Press 'ENTER' to retry or '1' to go back to menu: ")
                while user_1 != "1":
                    self.transfer()
                self.landing_page2()
                
            else:
                if details[0][0] < amount:
                    print("Insufficient Fund")
                    time.sleep(1)
                    self.landing_page2()
                else:
                    
                    new_balance = details[0][0] - amount 

                    query3 = "UPDATE customer_details SET account_balance =%s WHERE account_no = %s"
                    val3 = (new_balance, details[0][1])
                    self.mycursor.execute(query3, val3)
                    mycon.commit()
                
                    recipient_balance = info2[0][1] + amount
                    query4 = "UPDATE customer_details SET account_balance =%s WHERE account_no = %s"
                    val4 = (recipient_balance, user)
                    self.mycursor.execute(query4, val4)
                    mycon.commit()
                    
                    time.sleep(1)
                    time_now = dt.datetime.now()

                    print(f"You've successfully Transferred ${amount} to {info2[0][0]} at {time_now}. Your account balance is ${new_balance}")

                    query5 = "INSERT INTO Transaction_table (date_time, amount, transaction_type, sender_acc, reciever_account, account_no) VALUES(%s, %s, %s, %s, %s, %s)"
                    val5 = (time_now, amount, "Transfer",  self.number_user, info2[0][2], self.number_user)
                    self.mycursor.execute(query5, val5)
                    mycon.commit()

                    query6 = "INSERT INTO Transaction_table (date_time, amount, transaction_type, sender_acc, reciever_account, account_no) VALUES(%s, %s, %s, %s, %s, %s)"
                    val6 = (time_now, amount, "Transfer",  self.number_user, info2[0][2], info2[0][2])
                    self.mycursor.execute(query6, val6)
                    mycon.commit()
                    mycon.close()

                    time.sleep(1)
                    self.landing_page2()
                    
atm = Bank()


