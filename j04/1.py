num1 = int(input("enter first number: "))
op = input("enter an operator (+, -, *, /): ")
num2 = int(input("enter second number: "))

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op =="-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Cannot divide by zero")
else:
    print("enter a vakid operator")
