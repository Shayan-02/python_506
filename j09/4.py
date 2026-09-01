a = input().split()

# a1 = int(a[0])
# a2 = int(a[1])

# print(a1 + a2)

s = 0
for i in range(len(a)):
    s += int(a[i])

print(s)