class Bank_Account:
    def __init__(self,balance,interestrate,monthlyfee,customer):
        self.balance =balance
        self.interestrate = interestrate
        self.monthlyfee = monthlyfee
        self.customer = customer

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    

    def withdraw(self,amount):
        if self.balance < amount:
            return 'insufficient funds'
        else:
            self.balance -= amount
            return self.balance

    def transfer(self,amount):
        if self.balance < amount:
            return 'insufficient funds'
        else:
            self.balance -= amount
            return self.balance

    def finish_month(self):
        self.balance = self.balance + self.balance*self.interestrate/12 - self.monthlyfee
        return self.balance


    