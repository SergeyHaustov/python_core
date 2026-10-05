class CreditCard:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance

    def show_info(self):
        print(f"Номер счета: {self.__account_number}"
              f"\nБаланс: {self.__balance}")


first_account = CreditCard(account_number=123456789, balance=1000)
second_account = CreditCard(account_number=987654321, balance=2000)
third_account = CreditCard(account_number=987654322, balance=3000)

first_account.deposit(100)
second_account.deposit(200)
third_account.withdraw(100)

first_account.show_info()
second_account.show_info()
third_account.show_info()
