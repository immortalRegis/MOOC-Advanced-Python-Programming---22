# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name: str, account_number: int, balance: float):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
        
        self.__service_charge()

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        charge = self.__balance * 0.01
        self.__balance -= charge







