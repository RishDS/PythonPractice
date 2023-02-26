#Rishbha Godara - Jan 26 2023 - Individual Programming 1 (Part 2) extension

#prompt the user for a general category of things and ask them for five things to put in that category
category = input("Let's create a list of 5 things. Think of a general category.\nWhat category of things should we store? ")
ctg_lst = list()
#for loop to capture user inputs of the five things they wish to put in the above category into a list
i = 1
for i in range (1,6):
    ctg_lst.append(input(str(category)+" "+str(i)+": "))

#ask the user to enter a number between 1 and 5 and based on their numeric input (n), print the n-th item in the sorted list
num = eval(input("Pick a number between 1 and 5: "))
num= num-1
ctg_lst.sort()
print(f"\nYou picked {ctg_lst[num]}!")

#print the sorted list
print(f"The sorted list is: \n{ctg_lst}")

#prompt the user for a character and print a list of booleans reflecting whether the user-entered character is in each element of the list
var1 = input("Pick a character: ")
result = list()
i = 0
for i in range (5):
    result.append(var1.lower() in ctg_lst[i].lower())
print(result)

