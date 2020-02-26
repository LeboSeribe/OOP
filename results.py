from Banks import Bank
from Banks import BankAccount
from Banks import Customer
john = Customer(1234)
jane = Customer(2468)

all_ccounts = { "0123456789": BankAccount(0.12, 50, 1000, jane),
            "1123456789":BankAccount(0.15, 50, 1290, john),
            "1223456789":BankAccount(0.12, 50, 1000, jane)
            }

nedbank = Bank(all_ccounts)
print(nedbank.withdraw("1223456789", 5000, 2468))
print(nedbank.deposit("1223456789",5000))
print(nedbank.transfer("0123456789",200,2468))
 ## I dont understand, isnt it that the balance has to be updated through out