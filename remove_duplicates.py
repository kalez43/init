"""
author: kalez@github.com
description: This function takes a list and sorts it and removes duplicates.
"""


def stars():
    print("****")


orig_list = [2, 3, 4, 2, 5, 6, 8, 4, 10, 2, 6, 3, 7, 5, 9, 10, 1, 1, 3]
print(orig_list)

stars()


def remove_duplicates():
    orig_list.sort()
    print(orig_list)
    stars()
    list_copy = orig_list[0:]
    print(list_copy)
    for x in range(1, len(list_copy)):
        if list_copy[x] == list_copy[x-1]:
            orig_list.remove(list_copy[x])
    stars()
    print(orig_list)


remove_duplicates()
