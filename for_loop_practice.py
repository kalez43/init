questions = ["What is 1 + 1?", "What is 2 + 2?"]
answers = [2, 4]

for question in questions:
    print(question)
    user_answer = input("Type answer and press enter ==> ")
    user_answer = int(user_answer)
    if user_answer == int(answers[0]) or user_answer == answers[1]:
        print("Well done!")
        continue
    else:
        print("Sorry, that is incorrect")
        break

print('***')

letters = "three"
numbers = [0, 1, 2, letters, 4, 5, 6]

for num in numbers:
    print(num)

print('***')

colors = ["green", "blue", "pink", "yellow", "orange"]

for color in colors:
    n = colors[-1]
    if color == n:
        print(color)

