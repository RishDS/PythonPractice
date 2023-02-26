#Rishbha Godara - Jan 26 2023 - Individual Programming 1 (Part 1) extension

def inches_to_feet_inches(inches):
    # convert inches to feet and inches
    feet = inches // 12
    inches = inches % 12
    return feet, inches

def compare_height (height):
    if height >= 0:
        return 1
    else:
        return 0

#capturing person details
first_name = input("Enter the first person's name: ")
first_height = float(input("Enter " + first_name +"'s height in inches: "))

second_name = input("Enter the second person's name: ")
second_height = float(input("Enter " + second_name +"'s height in inches: "))

# calculate difference in height and its absolute value
height_diff = first_height - second_height
height_diff = round(height_diff, 2)
height_diff_abs = abs(height_diff)

# convert heights to feet-inches
first_height_ft, first_height_in = inches_to_feet_inches(first_height)

second_height_ft, second_height_in = inches_to_feet_inches(second_height)


#print output
if compare_height (height_diff) == 1:
    print(f"{first_name} is {height_diff_abs} inches taller than {second_name}")
else:
    print(f"{second_name} is {height_diff_abs} inches taller than {first_name}")

import math as m
print(f"{first_name} is {m.floor(first_height_ft)}\'{round(first_height_in,1)}\" tall.")
print(f"{second_name} is {m.floor(second_height_ft)}\'{round(second_height_in,1)}\" tall.")

