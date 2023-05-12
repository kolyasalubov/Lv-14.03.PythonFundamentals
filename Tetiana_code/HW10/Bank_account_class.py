class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__account_holder = account_holder       
        self.__balance = balance

    @property
    def account_holder(self):
        return self.__account_holder

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.__balance