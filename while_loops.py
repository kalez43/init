"""
author: kalez43@github.com
description: practicing while loops
"""


def sort_lst():
    num_lst = []
    num_in = int(input("Number you would like to count to: "))
    for x in range(1, num_in + 1):
        num_lst.append(x)
    f = 0
    even_lst = []
    odd_lst = []
    while f < len(num_lst):
        if num_lst[f] % 2 == 0:
            even_lst.append(num_lst[f])
        else:
            odd_lst.append(num_lst[f])
        f += 1
    print('Here is the highest number you asked for: ' + str(num_in))
    print('This is your list of even numbers:')
    print(even_lst)
    print('This is your list of odd numbers:')
    print(odd_lst)


sort_lst()
