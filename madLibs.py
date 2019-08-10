"""
author: kalez43@github.com
description: This is a short Mad Libs game
"""
words = []


# asks the user for inputs and puts them into a list
def create_list():
    inputs = ["Adjective: ", "Object: ", "Name: ", "Verb: ", "Number: ", "Body part: ", "Adverb: "]
    for x in inputs:
        word = input(x)  # asks for each input
        word = word.upper()  # makes each input all caps
        words.append(word)  # puts each input into a list


create_list()  # runs the function


# This prints the story with the user inputs added in
print("""A """ + words[0] + """ man was walking down the street carrying his favorite """ + words[1] + """ when a car
hit a puddle and it was completely drenched. 'Oh no!' he exclaimed. 'My wife """ + words[2] + """ will
 """ + words[3] + """ me, she's already replaced it """ + words[4] + """ times!' He shook his """ + words[5] + """ sadly 
and walked home """ + words[6] + """.""")
