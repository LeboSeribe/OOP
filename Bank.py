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
        if account.balance <= amount:
            return 'insufficient funds'
        else:
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
        if account.balance <= amount:
            return 'insufficient funds'
        else:
            return account.balance
        

        