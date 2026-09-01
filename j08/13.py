floor = 0

a = input()

for i in a:
    if i.lower() == "u":
        floor += 1
    elif i.lower() == "d":
        floor -= 1

print(floor)