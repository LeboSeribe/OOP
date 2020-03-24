class Customer:
    def __init__(self, secret_password):
        self.__secret_password = secret_password

    def set_password(self, new_password):
        self.__secret_password = new_password
        

    def check_password(self, password):
        return self.__secret_password == password