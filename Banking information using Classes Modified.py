class Bank(object):
    name = ""
    acctno = 0
    initial_bal = 0.0
    amt = 0

    def accept(self):
        print("Enter name, Acctno,and Initial Balance:")
        self.name = input()
        self.acctno = int(input())
        self.initial_bal = float(input())
        
        print("Customer Details")
        print(self.name)
        print(self.acctno)
        print(self.initial_bal)

    def deposit(self):
        print("Enter amount to be deposited:")
        self.amt = int(input())
        self.initial_bal = self.initial_bal + self.amt
        print("Updated balance is", self.initial_bal)

    def withdraw(self):
        print("Enter amount to be withdrawn:")
        self.amt = int(input())
        self.initial_bal = self.initial_bal - self.amt
        print("Updated balance is", self.initial_bal)

        
b1 = Bank()
b1.accept()
b1.withdraw()
b1.deposit()
