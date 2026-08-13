number = int(input("enter a number: "))

# way 1
# if number == 0: # ham type # ham meghdar
#     print("zero")
# elif number % 2 == 0:
#     print("even")
# # elif number % 2 == 1:
# else:
#     print("odd")

# way 2
if number == 0:
    print("zero")
else:
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

