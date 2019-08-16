"""

author: kalez43@github.com
description: some practice with non-mutating methods on strings
"""

rafid = "I am the best coder in the world."
print(rafid)

r_up = rafid.upper()
print(r_up)

r_low = r_up.lower()
print(r_low)

r_amt = rafid.count("e")
print(r_amt)

r_let = "e"
r_amt_e = rafid.count(r_let)
print(r_amt_e)

print(rafid.index("e"))
print(rafid.index("the"))

print(rafid.strip())

print(rafid.replace("best", "worst"))
raf_excit = rafid.replace(".", "!")

new_rafid = "Rafid often says '{}'".format(raf_excit)
print(new_rafid)


