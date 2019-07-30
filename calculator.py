"""
Author: kalez43@github.com
Description: This is a basic calculator for gross yearly income.
"""

user_input = input("Type in your yearly salary = ")

salary = float(user_input)
tax = 0.18


def income_calculation():
    return salary - (salary * tax)


print("This is your remaining yearly gross income:")
print(income_calculation())

user_input = input("Type in the percentage you'd like to go towards savings = ")

savings = float(user_input)


def yearly_savings():
    return income_calculation() * (savings/100)


print("This is your yearly savings:")
print(yearly_savings())


if income_calculation() < 50000:
    print("You should have majored in Economics.")
else:
    print("You overachiever, you!")
