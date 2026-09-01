start = int(input("enter start: "))
end = int(input("enter end: "))

for i in range(start, end+1):
    if i % 3 == 0 and i % 5:
        print(i, end=" ")