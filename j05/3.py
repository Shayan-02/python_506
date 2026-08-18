n = int(input("enter a number: "))

if n % 2:
    print("odd")
else:
    print("even")

print("odd" if n % 2 else "even")