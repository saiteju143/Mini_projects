

class Payment:
    def __init__(self,amount):
        self.amount=amount
    def Process_payment(self):
        print("Processing amount")

        
class CreditCardPayment(Payment):
   
    def Process_payment(self):
        print("CreditCardPayment processing amount:" , self.amount)

    
class UPIPayment(Payment):
    def Process_payment(self):
        print("UPIPayment processing amount:" , self.amount)
    
class NetBankingPayment(Payment):
    def Process_payment(self):
        print("NetBankingPayment processing amount:" , self.amount)
    
class WalletPayment(Payment):
    def Process_payment(self):
        print("WalletPayment processing amount:" , self.amount)
    

credit_card=CreditCardPayment(5000)
upi=UPIPayment(1500)
net_banking=NetBankingPayment(2000)
wallet=WalletPayment(1200)

credit_card.Process_payment()
upi.Process_payment()
net_banking.Process_payment()
wallet.Process_payment()