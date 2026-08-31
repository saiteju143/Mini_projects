

class BankAccount:
    def __init__(self,acc_number,holder_name,balance):
        self.acc_number=acc_number
        self.holder_name=holder_name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
    def display_balance(self):
        return self.balance
    def account_details(self):
        print("Acc_num:" , self.acc_number)
        print("Holder_name:" , self.holder_name)
        print("Balance:" , self.balance)

class SavingsAccount(BankAccount):
    def __init__(self,acc_number,holder_name,balance,interest_rate):
        super().__init__(acc_number,holder_name,balance)
        self.interest_rate=interest_rate

class CurrentAccount(BankAccount):
    def __init__(self,acc_number,holder_name,balance,overdraft_limit):
        super().__init__(acc_number,holder_name,balance)
        self.overdraft_limit=overdraft_limit
        print("Over_draft:",self.overdraft_limit)

class SalaryAccount(BankAccount):
    def __init__(self,acc_number,holder_name,balance,employer,monthly_salary):
        super().__init__(acc_number,holder_name,balance)
        self.employer=employer
        self.monthly_salary=monthly_salary
        print("Employer name:",self.employer)
        print("Monthly_Salary:" , self.monthly_salary)


savings1 = SavingsAccount("S101", "Teju", 50000, 6.5)
savings2 = SavingsAccount("S102", "Anu", 40000, 7.0)

current1 = CurrentAccount("C101", "Rahul", 30000, 20000)

salary1 = SalaryAccount("SAL101", "Priya", 60000, "ABC Company", 70000)


# Demonstrate inherited behavior

savings1.deposit(5000)
savings1.display_balance()
savings1.account_details()

current1.deposit(3000)
current1.display_balance()
current1.account_details()

salary1.deposit(10000)
salary1.display_balance()
salary1.account_details()



        



