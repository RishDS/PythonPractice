#Rishbha Godara - Feb 10 2023 - Individual Programming 2 (Part 2)

import os
import os
import csv

# convert function takes filepath as an argument, opens the file and reads it into a list of rows.
# Then, it makes each row in the spreadsheet have the same number of columns based on the length of the longest row.
# After that, it calculates the longest entry in each column, and pads each entry in the same column with spaces to make each column have the same length as the longest entry.
# Finally, it writes the updated data back to the file and renames the file with a '.txt' extension.
def convert(filepath):
    with open(filepath) as fp:
        data = []
        reader = csv.reader(fp, skipinitialspace=True)
        for row in reader:
            data.append(row)
    # make spreadsheet rows consistent length, based on longest row
    max_len_row = len(max(data, key=len))

    for row in data:
        if len(row) < max_len_row:
            append_number = max_len_row - len(row)
            for i in range(append_number):
                row.append('')
        # create dictionary of number of columns
        longest = {}

    for times in range(len(data[0])):
        longest[times] = 0
    # get longest entry for each column
    for sublist_index, sublist in enumerate(data):
    
        for column_index, element in enumerate(sublist):
            if longest[column_index] < len(element):
                longest[column_index] = len(element)

    # make each column as long as the longest entry
    for sublist_index, sublist in enumerate(data):
        for column_index, element in enumerate(sublist):
            if len(element) < longest[column_index]:
                amount_to_append = longest[column_index] - len(element)
                data[sublist_index][column_index] += (' ' * amount_to_append)

    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for row in data:
            writer.writerow(row)

    path, ext = os.path.splitext(filepath)
    newfilepath = path + '.txt'
    os.rename(filepath, newfilepath)
    return newfilepath
    
# numLines function takes filename as an argument, opens the file and reads it into a list of lines, then returns the number of lines.
def numLines(fName):
    infile = open(fName, 'r') # open the file and read it *** can add exception handling for empty rows or corrupted file
    lineList = infile.readlines() # into a list of lines
    infile.close()
    return len(lineList)

# copyData function takes two filenames as arguments, opens the original file and reads its data, then writes that data to the new file.
def copyData(orgFile, newFile):
    infile = open(orgFile,'r')
    fileData = infile.read()
    outfile = open(newFile,'w')
    outfile.write(fileData)
    infile.close()
    outfile.close()
# append_pData function takes new filename and person data as arguments, opens the new file in append mode and writes the person data to the file.
def append_pData(newFile,persondata):
    infile = open(newFile, 'a')
    infile.write(persondata)
    infile.close()

# Code to collect personal information of a person and store it in a file
def record_pData():
    frName = input("First Name: ")
    lsName = input("Last Name: ")
    age = input("Age: ")
    occ = input("Occupation: ")
    height = input("Height (in inches): ")
    weight = input("Weight (in pounds): ")
    lifestyle = int(input("Lifestyle (1-sedentary, 2-moderate, 3-active): "))
    lifestyle_headers = {"1":"Sedentary","2":"Moderate","3":"Active"}
    pData = f"\n{frName},{lsName},{age},{occ},{height},{weight},{lifestyle_headers[lifestyle]}"
    return pData

# main program
print("Hello.")  # prints a greeting message
boolValidFile = False
while not boolValidFile:
    fName = input("Please enter a roster file: ")
    try:
        fName = os.path.normpath(fName)
        numEntries = numLines(fName)-1
        boolValidFile = True
    except FileNotFoundError:
        print("The file could not be found. Please enter a valid file name.")

fName = os.path.normpath(fName)  # normalizes the file path
numEntries = numLines(fName)-1  # calculates the number of entries in the file
boolCreate = input("There are " + str(numEntries) + " names in this file. Would you like to enter additional names? (Y/N) ")  # prompts user to enter additional names if there are any existing names in the file
if boolCreate.upper() == 'Y':  # checks if the user entered 'Y'
    newfile = open('newfilename.csv', 'x')  # opens a new file 'newfilename.csv' in exclusive creation mode
    tempName = newfile.name  # stores the name of the newly created file
    copyData(fName,tempName)  # copies data from the original file to the new file
    newEntries = int(input("How many more names? "))  # collects the number of new entries the user wants to add
    for i in range(1,newEntries+1):  # iterates for each new entry
        print(f"----- Person {i} -----")  # prints a message indicating the entry number
        persondata = record_pData()  # calls the `record_pData` function to collect personal data for each entry
        append_pData(tempName,persondata)  # appends the personal data to the newly created file
        print("-------------------------")  # prints a separator line after each entry
    newFileName = input("Save new roster file as: ")  # collects the name the user wants to save the newly created file as
    conv_tempName = convert(tempName)  # converts the name of the new file to a different format
    os.rename(conv_tempName,newFileName)  # renames the new file with the name specified by the user
    print("File saved!")  # prints a message indicating the file was saved successfully
else:
    print('You\'re done.')  # prints a message indicating that the user is done and no additional names were added to the file
