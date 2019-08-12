"""
author: kalez43@github.com
description: small practice for loops
"""
# lists of questions and their respective answers
questions = ["What is 1 + 1?", "What is 2 + 2?", "What is 3 * 3?"]
answers = [2, 4, 9]

# for loop asking each question
for current in range(0, len(questions)):
    current_question = questions[current]  # assigns current question so we can compare later
    current_answer = answers[current]  # assigns current answer so we can compare later
    print(questions[current])  # prints current question
    user_answer = int(input("Type answer and press enter ==> "))  # asks user to answer current question
    if user_answer == current_answer:  # evaluates whether user input is correct
        print("Well done!")  # prints success message
        continue  # continues the loop
    else:
        print("Sorry, that is incorrect.")  # prints failure message
        break  # stops the loop


# creates function that prints a row of stars
def stars():
    print('***')


stars()  # prints row of stars

# lists
letters = "three"
numbers = [0, 1, 2, letters, 4, 5, 6]


# creates function for printing each item in the list 'numbers'
def print_list():
    for num in numbers:
        print(num)


print_list()  # prints the ist 'numbers'

stars()  # prints row of stars

# list
colors = ["green", "blue", "pink", "yellow", "orange"]


# function that runs a for loop to print an item of the list 'colors' if it matches item position of n
def print_color():
    for color in colors:
        n = colors[-1]
        if color == n:
            print(color)


print_color()  # runs function

