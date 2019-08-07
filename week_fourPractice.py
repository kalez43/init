"""
author: kalez43@github.com
description: This is practice for various mutation methods for lists.
"""
# list
first_list = ['cow', 'pig', 'chicken', 'goat', 'goose', 'sheep']

print("first list")
print(first_list)

print("count 'cow'")
print(first_list.count('cow'))  # prints number of iterations of 'cow' in list

print("remove 'chicken'")
first_list.remove('chicken')  # removes 'chicken' from list
print(first_list)

print("index 'sheep'")
print(first_list.index('sheep'))  # tells you what position "sheep" is in list

print("insert 'horse'")
first_list.insert(0, 'horse')  # inserts element into list at specified position
print(first_list)

print("insert 'chicken'")
first_list.insert(2, 'chicken')  # another insert putting 'chicken' back in
print(first_list)

print("slicing = second list")
second_list = first_list[0:-1]  # makes a new list using slice of old list (ends up the same)
print(second_list)

print("pop first list")
first_list.pop()  # removes last element in list and returns it
print(first_list)

print("first list == second list")
print(first_list == second_list)  # asks whether the lists are equivalent

print("first list is second list")
print(first_list is second_list)  # asks whether the lists are the same object

print("sort first list")
first_list.sort()  # sorts elements in list (alphabetically or numerically lowest to highest)
print(first_list)

print("pop(-3) first list")
print(first_list.pop(-3))  # removes element from specific position and returns that element
print(first_list)

print("reverse second list")
second_list.reverse()  # reverses the list
print(second_list)

print("concatenate lists and rename best list")
best_list = first_list + second_list  # makes new list from both lists
print(best_list)

print("sort best list")
best_list.sort()  # alphabetizes best list
print(best_list)

print('*****')

animals = []  # create new list


# function to duplicate best list into animals
def duplicate_list():
    for item in best_list:
        animals.append(item)


print("duplicate list 'animals'")
duplicate_list()  # run function and print list 'animals'
print(animals)

print("duplicate list 'better animals'")
better_animals = best_list[0:]  # simpler way to duplicate list
print(better_animals)


# function to remove duplicates from best list
def remove_duplicates():
    for x in range(1, len(animals)):
        if animals[x-1] == animals[x]:
            best_list.remove(animals[x])


remove_duplicates()  # run the function

print("")
print("Best List without duplicates:")
print(best_list)

# automate the function so it can be used with other lists in next file
