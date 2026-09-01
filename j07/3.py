from random import randint

start = int(input("enter start range: "))
end = int(input("enter end range: "))

c = randint(start, end)

i = 1
while i <= 5:
    print(f"guess {i}")
    guess = int(input(f"enter a number between {start} and {end}: "))
    if guess == c:
        print("you win")
        break
    elif guess > c:
        print("enter a lower number")
    else:
        print("enter a higher number")
    print("-"*30)
    print(f"you have {5 -i} chances")
    i += 1