class BankAccount(object):
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self._account_holder = account_holder
        self.__balance = balance
      
    @property
    def account_holder(self):
        return self._account_holder
        
    def deposit(self, amount):
        self.__balance+=amount
    
    def withdraw(self, amount):
        if amount <=  self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
            
    def check_balance(self):
        return self.__balance
    



my_account = BankAccount("123456789", "John Doe", 1000.0)
print(my_account.account_holder)

try:
    _ = my_account.account_number
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

try:
    _ = my_account.balance
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

print(my_account.check_balance())

my_account.deposit(500.0)
print(my_account.check_balance())

my_account.withdraw(250.0)
print(my_account.check_balance())

try:
    my_account.account_holder = "Jane Doe"
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

my_account.withdraw(5000.0)
    
    
    
    

        