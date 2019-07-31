"""
Author: kalez43@github.com
Description: This is a random number generator for a six sided die.
"""

import random
roll = 0

while roll < 7:
    roll = random.randrange(1, 7)
    print(roll)
    roll_again = input("Would you like to roll again? Type '1' for yes and '0' for no: ")
    roll_again = int(roll_again)
    if roll_again < 1:
        print("Thanks for playing!")
        break
