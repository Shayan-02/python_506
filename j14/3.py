"""
import random
import random as r
from random import randint
from random import randint, choice
from random import choice as c
"""
# import libraries
from random import *


# function
def guess(num):
    if num == correct_number:
        print("you guessed correctly")
        return True
    elif num > correct_number:
        print("you guessed too high")
    elif num < correct_number:
        print("you guessed too low")


# variable
start = int(input("enter start number: "))
end = int(input("enter end number: "))
correct_number = randint(start, end)

# main function
def main():
    chances = 5
    while chances:
        guess_number = int(input(f"enter guess number{5 - chances + 1}: "))
        if guess(guess_number):
            break
        else:
            chances -= 1
    else:
        print("Game Over")

main()