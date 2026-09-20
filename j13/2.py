lst = [1, 2, 3]

def sum_numbers(a):
    # tedad, sumofnumbers = 1, 0
    # while True:
    #     number = input(f"enter number{tedad}: ")
    #     if number == "":
    #         break
    #     else:
    #         sumofnumbers += int(number)
    #         tedad += 1
    # return sumofnumbers
    sumofnumbers = 0
    for i in a:
        sumofnumbers += i
    return sumofnumbers



print(sum_numbers())
print(sum_numbers(1))
print(sum_numbers(1, 2))
print(sum_numbers(1, 2, 3))
print(sum_numbers(1, 2, 3, 4))
# print(sum_numbers(lst))