"""
author: kalez43@github.com
description: This is a text-based game. The goal is to make the best decisions in order to allow Marley (dog) to
retrieve a cake off of the counter without Kayleigh (her human) catching her.
"""


# Space between story strings
def space():
    print("")


def stars():
    space()
    print("* * * * *")
    space()


# Enter function between story telling strings
def enter():
    space()
    x = 0
    while x < 1:
        x += 1
        user_input = input("Click here then press enter ==>")
        if user_input == "":
            continue
        else:
            break


# Intro
space()
print("Marley's Cake Adventure")
stars()
print("""Marley is a very hungry hound! Cake is her favorite food, and Kayleigh has just placed a freshly baked birthday
cake on the counter to cool. Help Marley retrieve the cake without Kayleigh noticing!""")
space()
print("""Click where prompted and press enter to move to the next segment. Answer prompts to give Marley the best 
chance of succeeding. And don't forget to be quiet!""")
enter()
stars()
print("""You are a medium sized dog named Marley. You are lying on your dog bed watching Kayleigh, your human, bake a 
cake in the kitchen. Your dog bed is behind the couch and 18 feet away from the kitchen counter.""")
enter()
stars()
print("Kayleigh places the cake on the counter and walks 20 feet away to sit down on the couch.")
space()
print("""You notice that she is facing away from the counter, and is reading a book. Her attention should be 
filled for now.""")
enter()
stars()


def decision1():
    print("""You can:
          1. Stand and walk 2 feet towards the counter
          2. Listen for more information""")
    answer = input("Type 1 or 2, then press enter ==> ")
    answer = int(answer)
    space()
    if answer == 1:
        print("""Kayleigh hears your nails clicking on the floor. She gets up and admonishes you for moving towards the 
        cake. You go back to your bed in shame.""")
        # fail()
    else:
        print("""The sweet smell of the cake beckons you, but you pause to listen before making any moves. You notice that 
        you don't hear Kayleigh turning the pages of her book. She must be listening, in case you try for the cake! You 
        decide to wait, and after a few moments you hear her turn the page.""")


decision1()




