a = 10
b = 20
c = 30

if a >= b and b > c:
    print("1")
elif a < b and b == c:
    print("2")
elif a > b and b < c:
    print("3")
elif a < b and b < c:
    print("4")
elif a == 10:
    print("5")

print("-"*30)

if a > b or b > c:
    print("1")
elif a > b or b < c:
    print("2")
elif a < b or b < c:
    print("3")