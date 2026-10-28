from tkinter import messagebox

a = input("variz | bardasht: ")

balance = 100
amount = 200

if a == "bardasht":
    if balance < amount:
        # raise ValueError("mojoodi kafi nist")
        messagebox.showerror("error", "mojoodi kafi nist")
    balance -= amount

print(balance)