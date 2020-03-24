## Import classes from files

from Bank import Bank
from Bank_Account import Bank_Account
from Customers import Customer

## Instance for Bank_Account

bank_account = Bank_Account(1000,0.12,50,'john')
print(bank_account.deposit(0))
print(bank_account.withdraw(1000))
print(bank_account.transfer(10000))
print(bank_account.finish_month())
## Instance for Customers

john = Customer(1234)
jane = Customer(2468)
print(john.check_password(1234)) ##customer.check_password(password)
print(jane.check_password(5656)) ##customer.check_password(password)

## The data of customers' bank accounts

                                                    ## if len(bank_account_number) == 10
accounts = {                                        ## account = self.__accounts.get(bank_account_number)
"0123456789":Bank_Account(1000, 0.12, 50, jane),    ## account.customer.check_password(password)
"1123456789":Bank_Account(1290, 0.15, 50, john),          ## bank_account_number is a key in a dictionary
"1223456789":Bank_Account(1000, 0.12, 50, jane)
}

nedbank = Bank(accounts)                            ## account.balance  ## balance is an attribute of Bank_Account
print(nedbank.withdraw("1223456789", 1000, 2468))      ## Access the instance attributes  ## Balance is updated accordingly 
print(nedbank.deposit("1223456789",500)) 
print(nedbank.withdraw("0123456789", 1000, 2468))                 ## with deposit,withdraw and transfer
print(nedbank.transfer("0123456789",3000,2468))



