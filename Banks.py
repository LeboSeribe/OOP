class BankAccount:
    def __init__(self,balance,interestrate,monthlyfee,customer):
        self.balance =balance
        self.interestrate = interestrate
        self.monthlyfee = monthlyfee
        self.customer = customer

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    

    def withdraw(self,amount):
        if self.balance <= 0:
            return 'insufficient funds'
        else:
            self.balance -= amount
    def transfer(self,amount):
        self.balance -= amount
        return self.balance

    def finish_month(self):
        self.balance = self.balance + self.balance*self.interestrate/12 - self.monthlyfee
        return self.balance


class Bank():
  
    def __init__(self,accounts):
      # it has to be encapsulated
        self.__accounts = accounts
        


    def withdraw(self,bank_account_number,amount,password):
        # The length of the account number has to be ten
        if len(bank_account_number) == 10:
            account = self.__accounts.get(bank_account_number)

            # check the account number
            if account is None:
                raise Exception("Account does not exist.")

            # check the password
            if account.customer.check_password(password) is False:
                raise Exception("wrong password")
        else:
            raise Exception("invalid account number")


        account.withdraw(amount)
        return account.balance



    def deposit(self,bank_account_number,amount):
        if len(bank_account_number) == 10:
            account = self.__accounts.get(bank_account_number)

            # check the account number
            if account is None:
                raise Exception("Account does not exist.")

        else:
            raise Exception("invalid account number")

        account.deposit(amount)
        return account.balance



    def transfer(self,bank_account_number,amount,password):


        if len(bank_account_number) == 10:
            account = self.__accounts.get(bank_account_number)

            # check the account number
            if account is None:
                raise Exception("Account does not exist.")

            # check the password
            if account.customer.check_password(password) is False:
                raise Exception("wrong password")
        else:
            raise Exception("invalid account number")


        account.transfer(amount)
        return account.balance




class Customer:
    def __init__(self, secret_password):
        self.__secret_password = secret_password

    def set_password(self, new_password):
        self.__secret_password = new_password

    def check_password(self, password):
        return self.__secret_password == password

