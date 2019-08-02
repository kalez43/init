"""
author: kalez43@github.com
description: A coin flip generator utilizing the random module and a list.
"""

import random

text = ["Heads", "Tails"]

flip = random.random()

if flip < 0.5:
    print(text[0])
else:
    print(text[1])

