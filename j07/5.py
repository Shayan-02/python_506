i = 200 # start
while i > 0: # end
    print(i, end="\t")
    i -= 1 # step

print()
print("-"*50)

for j in range(200, 0,-2):
    if j == 130:
        j -= 10
        continue
    print(j, end="\t")