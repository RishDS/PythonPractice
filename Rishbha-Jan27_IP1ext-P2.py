#Rishbha Godara - Jan 26 2023 - Individual Programming 1 (Part 2) extension

#prompt the user for a general category of things and ask them for five things to put in that category
category = input("Hello there! I'm a list creating program. \n\nWhat would you like to create a list of? ")
ctg_lst = []

#while loop to capture user inputs of the five things they wish to put in the above category into a list
print(f"\nOK. Please enter values into your list of {category}:\n")
i = 0
while 1:
    i+=1
    item = input(str(category) + " "+ str(i) + ": ")
    if item == "":
        break
    ctg_lst.append(item)
x = len(ctg_lst)

#edge case: is statement to stop further compiling if no elements in the list
if x == 0:
    print("\nYou did not enter any item.\nExiting...")
    exit()

print(f"\nGreat! You have {x} elements in your list.")
ctg_lst.sort()
#print the sorted list
print(f"\nYour sorted list is: \n{ctg_lst}")

#ask the user to enter a number between 1 and list length and based on their numeric input (n), print the n-th item in the sorted list
num = eval(input("\nPick a number between 1 and " + str(x) + ": "))
j=0
while 1:
    j+=1
    if num not in range(1,x+1):
        num = eval(input("Input Error!! \nPlease pick a number between 1 and " + str(x) + ": "))
    else:
        break
num -=1
print(f"\nYou picked {ctg_lst[num]}!")

#prompt the user to check if a character(s) exists in the list and print a list of booleans reflecting whether the user-entered character is in each element of the list
var1 = input("\nDo you want to check if something exists in your list? Enter your character(s): ")
result = list()
i = 0
for i in range (x):
    result.append(var1.lower() in ctg_lst[i].lower())
print(result)
    