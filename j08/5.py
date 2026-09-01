num = int(input())
strnum = str(num)

for i in range(len(strnum)):
    print(f"{strnum[i]}: {int(strnum[i]) * strnum[i]}")