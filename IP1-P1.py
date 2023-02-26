#Rishbha Godara - Jan 26 2023 - Individual Programming 1 (Part 1)

#capturing person heights in variables height1, height2 and their difference in height_diff
height1 = eval(input('Person 1 Height: '))
height2 = eval(input('Person 2 Height: '))
height_diff = height1-height2
#converting the input to feet and inches
feet1=height1//12
inch1=height1%12
feet2=height2//12
inch2=height2%12
#printing output
print("Person 1 is ", height_diff," inches taller than Person 2." )
print("Person 1 is ",feet1,"\'",inch1,"\".", sep = "")
print("Person 2 is ",feet2,"\'",inch2,"\".", sep = "")

