a = input().split()
b = input().split()

counter = 0
for i in range(8):
    if a[i] == b[i] == "1":
        counter += 1


print(a)
print(b)
print(counter)