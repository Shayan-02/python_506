sumnumbers = 0
tedad = 0
while True:
    a = int(input("enter a number: "))
    if a < 0:
        break
    else:
        sumnumbers = sumnumbers + a # sumnumbers += a
        tedad += 1


avg = sumnumbers/tedad
# if int(avg) == avg:
#     print(int(avg))
# else:
#     print(f"{avg:.2f}")

print(int(avg) if int(avg) == avg else f"{avg:.2f}")