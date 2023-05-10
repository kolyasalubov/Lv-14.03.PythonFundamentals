# QUESTION 1
# Create a program that models a zoo. The program should have a base
# class Animal that stores the animal's name, species, and number of legs.
# The class should have a method make_sound that returns a string indicating
# the sound the animal makes. The make_sound method should be overriden
# in the subclasses to return a sound specific to each type of animal.
# Then, create three subclasses of Animal: Mammal, Bird, and Reptile.
# Each of these subclasses should inherit the name, species, and number
# of legs from the Animal class. For the Mammal class, add a method
# give_birth and return "Roar" for make_sound method.
# For the Bird class, add a method lay_eggs and return "Squawk"
# for make_sound method. For the Reptile class, add a method shed_skin
# and return "Hiss" for make_sound method.

class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def make_sound(self):
        pass


class Mammal(Animal):
    def give_birth(self):
        pass

    def make_sound(self):
        return "Roar"


class Bird(Animal):
    def lay_eggs(self):
        pass

    def make_sound(self):
        return "Squawk"


class Reptile(Animal):
    def shed_skin(self):
        pass

    def make_sound(self):
        return "Hiss"


# QUESTION 2
# Create a class "BankAccount" that implements encapsulation.
# The class should have the following attributes:
# account_number (string); account_holder (string);
# balance (float).
# The class should have the following methods:
# deposit(amount) - a method that allows the account holder
# to deposit money into the account;
# withdraw(amount) - a method that allows the account holder
# to withdraw money from the account (write "Insufficient funds"
# if money doesn't enough);
# check_balance() - a method that returns the current balance of the account.
# The class should also have the following restrictions:
# account_number should not be accessible from outside the class
# balance should not be directly accessible from outside the class,
# it should only be accessible through the methods deposit() and withdraw()
# account_holder should be accessible from outside the class but should not be modifiable.

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    @property
    def account_holder(self):
        return self.__account_holder
