floor = 0

a = input()

for i in range(len(a)):
    if a[i].lower() == "u":
        floor += 1
    elif a[i].lower() == "d":
        floor -= 1

print(floor)