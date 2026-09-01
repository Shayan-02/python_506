a = [1, "ali", True, 3.14,]
b = list((1, 2, "reza", 25, 1.5))
s = "salam"
print(type(a))

print(len(s))

a += b

print("-"*20)
for i in range(len(a)):
    if type(a[i]) == float:
        print(a[i], end="\t")