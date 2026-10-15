class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def info(self):
        return f"username : {self.name}\nbalance: {self.__balance}$"

    def show_balance(self):
        return f"balance: {self.__balance}$\n\n"

    def variz(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"{amount} $ variz shod\n{self.show_balance()}"
        else:
            print("invalid amount\nvariz nashod")
        return self.show_balance()

    def bardasht(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(amount, "$ bardasht shod")
        else:
            print("invalid amount\nbardasht nashod")


b1 = BankAccount("reza", 1000)
print(b1.info())

print(b1.variz(500))
# print(b1.show_balance())

# print(b1.variz(-3000))
# print(b1.show_balance())

# b1.bardasht(-5000)
# print(b1.show_balance())

# b1.balance = 10000

# print(b1.show_balance())

# b1.bardasht(5000)
# print(b1.show_balance())

# print(b1.__balance)
