class BankAccount:
    def __init__(self,balance,interestrate,monthlyfee):
        self.balance =balance
        self.interestrate = interestrate
        self.monthlyfee = monthlyfee

    def deposit(self,dep):
        self.balance += dep
        return self.balance
    

    def withdraw(self,draw):
        if self.balance <= 0:
            return 'insufficient funds'
        else:
            self.balance -= draw

    def finish_month(self):
        self.balance = self.balance + self.balance*self.interestrate/12 - self.monthlyfee
        return self.balance
# finish_month(1)
     


p1= BankAccount(0,0.12,60)
# p1.deposit(200)
print(p1.withdraw(50))
print(p1.finish_month())
    
class Bank:
    def __init__(self,from_bank_account_number,to_bank_account_number,from_balance,to_balance):
      
        while True:
            self.from_bank_account_number = str(from_bank_account_number)
            try:
                if len(self.from_bank_account_number) ==10 and int(self.from_bank_account_number):
                    return self.from_bank_account_number
                else:
                    print('wrong')
                    continue
            except ValueError:
                print('digits') 
               

        self.to_bank_account_number = to_bank_account_number
        self.from_balance = from_balance
        self.to_balance = to_balance

    def withdraw(self,amount):
        if self.from_balance <= 0:
            return 'insufficient funds'
        else:    
            self.from_balance -=amount

    def deposit(self,amount):
        self.from_balance += amount
        return self.from_balance 

    def transfer(self,from_bank_account_number,to_bank_account_number, amount):
        self.from_balance -=amount
        self.to_balance += amount
        return [self.from_balance,self.to_balance]
    

           

p2 = Bank(1,2,500,1000)
print('The balances of the sender and reciever respectively are:',format(p2.transfer(1234567890,1000575911,200)))
# print('The balances of the sender and reciever respectively are:'.format(print(p2.transfer(1234567890,1000575911,200))) 
    
         
