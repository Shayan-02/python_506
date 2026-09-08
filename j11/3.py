def calculate_floor(string):
    # floor = 0
    # for i in range(4):
    #     if string[i].lower() == "u":
    #         floor += 1
    #     elif string[i].lower() == "d":
    #         floor -= 1
    # return floor
    floor = 0
    for i in string:
        if i.lower() == "u":
            floor += 1
        elif i.lower() == "d":
            floor -= 1
    return floor

f = input()
print(calculate_floor(f))