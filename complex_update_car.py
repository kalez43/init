"""
author: kalez43@github.com
description: This program opens a .csv file that contains information about different cars. It uses prompts to assist
the user input information on a new car and adds it to the existing file.
"""
# Opens file carlist.csv and creates list car_info based on data in file
with open("../carlist.csv", "r") as car_list:
    car_info = []
    car_rows = car_list.readlines()
    for row in car_rows:
        vals = row.strip().split(',')
        new_tuple = (vals[0], vals[1], vals[2], vals[3])
        car_info.append(new_tuple)
print(car_info)


# Allows user input to add to list car_info
def add_info():
    car_make = input("Car make:")  # user inputs car info
    car_model = input("Car model:")
    car_year = input("Year:")
    car_price = '$' + input("Price:")
    new_row = (car_make, car_model, car_year, car_price)  # creates tuple using user input
    car_info.append(new_row)  # adds tuple to end of list
    return car_info


add_info()  # runs function that allows user to add to list

print(car_info)

# Write in carlist.csv file (auto open with excel), writes list into spreadsheet after user updates to list
with open("../carlist.csv", "w") as car_file:
    for lin in car_info:
        car_row = '{}, {}, {}, {}'.format(lin[0], lin[1], lin[2], lin[3])
        car_file.write(car_row)
        car_file.write("\n")
