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
        self.from_bank_account_number = from_bank_account_number
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
    

p2 = Bank(1234567891,1345678922,500,1000)
print('The balances of the sender and reciever respectively are:',format(p2.transfer(1234567890,1000575911,200)))


class customer:
    def __init__(self,account_number,balance,password):
        self.account_number = account_number
        self.balance = balance
        self.password = password
        
        

    def  withdraw(self,amount):
        password = int(input('password'))
        if password == '1234':
            return withdraw()
        else:
            return 'no'    
        # print('please input pin',password)
        if self.balance <= 0:
            return 'insufficient funds'
        else:    
            self.balance -=amount
            return self.balance

    # def   deposit(self,bank_account_number,amount):
        # pass
    
    # def transfer(self,fromBankAccountNumber,toBankAccountNumber,amount,secretPassword):
        # pass
p3 = customer(1,1000,1234)
print(p3.withdraw(100))


         
