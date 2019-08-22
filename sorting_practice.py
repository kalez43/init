"""
author: kalez43@github.com
description: practice with sorting
"""

lst = {'Chevy': 2, 'Mazda': 6, 'Toyota': 10, 'Honda': 4, 'Subaru': 1}

alphabetical_keys = sorted(lst)
print(alphabetical_keys)

sorted_values = sorted(lst, key=lambda k: lst[k])
print(sorted_values)


def stock_lst(current_lst):
    highest_amt = sorted(current_lst, key=lambda k: current_lst[k], reverse=True)
    for x in highest_amt:
        print("Make: {}; Amount in stock: {}".format(x, current_lst[x]))


stock_lst(lst)
