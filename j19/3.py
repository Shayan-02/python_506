class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def info(self): return f"username : {self.name}\nbalance: {self.balance}$"
    
    def show_balance(self): return f"balance: {self.balance}$"
    
    def variz(self, amount):
        if amount > 0:
            self.balance += amount
            print(amount, "$ variz shod")
        else: print("invalid amount\nvariz nashod")
        # self.show_balance()
        
    def bardasht(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            print(amount, "$ bardasht shod")
        else: print("invalid amount\nbardasht nashod")


b1 = BankAccount("reza", 1000)
print(b1.info())

b1.variz(500)
print(b1.show_balance())

b1.variz(-3000)
print(b1.show_balance())

b1.bardasht(-5000)
print(b1.show_balance())
