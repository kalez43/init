user_input = input("Type in your yearly salary = ")

salary = float(user_input)

tax = 0.18

income = salary - (salary * tax)

print("This is your remaining yearly gross income:")
print(income)
print("You should have majored in Economics.")
