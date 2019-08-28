"""
author: kalez43@github.com
description: for Rafid
"""

rafid_dict = {'Smart': 0, 'Quiet': 0, 'Studious': 0, 'Pious': 0, 'Funny': 0, 'Grumpy': 0}
yes_list = []
no_list = []
for ky in rafid_dict.keys():
    answer_val = input("Is Rafid {}? Answer 'yes or 'no'.".format(ky))
    if answer_val == 'yes':
        rafid_dict[ky] = 'YES'
        yes_list.append(ky)
    if answer_val == 'no':
        rafid_dict[ky] = 'NO'
        no_list.append(ky)
print("Rafid is {}.".format(str(yes_list)))
print("He is not {}.".format(str(no_list)))
print(rafid_dict)

