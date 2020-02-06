print("Welcome to the IndianSwiss")
class banking:
    def __init__(self):
        custName = input("Enter the customer name:")
        self.amount=5000
        print("The Amount you have in your A/C is 5000")

    def withdraw(self):
        self.withdraw=int(input("To be withdrawn:"))
        print("The amount to want to withdraw is:",self.withdraw)
        self.amount=self.amount-self.withdraw
        return self.amount

    def deposit(self):
        self.deposit=int(input("To be deposited:"))
        print("The amount to want to deposit is:",self.deposit)
        self.amount=self.amount+self.deposit
        return self.amount
    
    

for i in range(2):
    bankuser1=banking()
    print(bankuser1.withdraw())
    print(bankuser1.deposit())
