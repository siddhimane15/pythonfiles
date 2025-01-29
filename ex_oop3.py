class account:

    def __init__(self,accont_no):

        self.balance = 0
        self.account_no = accont_no
    
    def deposit(self,amount):

        if amount > 0:

            self.balance += amount

            print(f"Credit: Rs. {amount} Current Balance: Rs. {self.balance}")

        else:

            print("Invalid Amount! Please check the deposit amount...")

    def withdrawal(self,amount):

        if amount > 0:
            self.balance -=amount

            print(f"debit: Rs. {amount} current balance: Rs. {self.balance}")

        else:

            print("Invalid Amount! Please check the withdrawal amount...")

    def check_balance(self):

        print(f"account no: {self.account_no} current balance: Rs. {self.balance}")


class SavingsAccount(account):
    def __init__(self, interest, account_no):
        super().__init__(account_no)

        self.balance=0
        self.interest=interest

    def balance_with_interest(self):
        interest_amount = self.balance * self.interest
        self.deposit(interest_amount)
        print(f"Current Balance: {self.balance}")


siddhi = account('0105553522')
siddhi.deposit(1500)
siddhi.withdrawal(71)
siddhi.check_balance()
#siddhi.balance_with_interest()

papa = SavingsAccount(0.07, '0105522001')
papa.check_balance()
papa.deposit(10000)
papa.balance_with_interest()







        

    


