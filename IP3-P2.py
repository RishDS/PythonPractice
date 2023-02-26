#Rishbha Godara - Feb 24 2023 - Individual Programming 3 (Part 2)

import os

class UCLAIP:

    def __init__(self,fName): #Initialize the class with a file name.
        self.fName = fName

    def numLines(self): #Read the file and returns the number of lines in it.
        infile = open(self.fName, 'r') # open the file and read it *** can add exception handling for empty rows or corrupted file
        lineList = infile.readlines() # into a list of lines
        infile.close()
        return len(lineList)-1
    
    def countTerms(self): #Prompt the user to enter the number of terms they would like to add to the vocabulary list
        while True:
            try:
                cTerms = int(input(f'How many would you like to add? ')) # ask user to input the number of terms
                assert cTerms >0 # validate that the entered number is positive
                break
            except ValueError:
                print(f'Error. Please enter an integer.')
            except AssertionError:
                print(f'Error. Please enter a positive number.')
        return cTerms #return the entered value after validating that it is a positive integer
    
    def createDict(self): #Read the file and create a orgDictionary where the keys are the terms and the values are the definitions.
        orgDict = {}
        with open(self.fName, 'r') as f:
            for line in f:  # Loop through each line in the file
                (key, value) = line.strip().split('\t') # Extract the word and its meaning from the line and add it to the orgDict orgDictionary
                orgDict[key.strip()] = value.strip()
        return orgDict

    def dictUpdate(self, cTerms, myDict): #Prompt the user to enter new terms and their definitions, and update the input orgDictionary.
        for i in range(1,cTerms+1):
            newTerm = input(f'Term #{i}: ') # ask user to enter new term
            if newTerm in myDict.keys(): # check if the new term is already present in the orgDictionary
                boolvar = input(f'Warning! This term is already in the vocabulary list. Update definition (Y/N)? ') # ask user if they want to update the definition
                if boolvar.upper() == 'Y': # check if the user wants to update the definition
                    dTemp1 = {newTerm: input(f'Definition #{i}: ')} # if yes, ask user to input the new definition and add it to the orgDictionary
                    myDict.update(dTemp1)
                else:
                    continue # if no, continue to the next iteration of the loop
            else:
                dTemp2 = {newTerm: input(f'Definition #{i}: ')} # if the term is not already present in the orgDictionary, ask user to input the new definition and add both to the orgDictionary
                myDict.update(dTemp2)
        newDict = myDict
        return newDict
    
    def printDict(self, myDict): #Print the orgDictionary in a formatted way where each line contains a term and its definition
        myKeys = list(myDict.keys())
        del myKeys[0]
        myValues  = list(myDict.values())
        del myValues[0]
        print ("\n".join("{0} - {1}".format(a, b) for a, b in zip(myKeys, myValues)))

    def saveFile(self, myDict): #Prompt the user to enter a file name and save the orgDictionary to a file with the entered name
        newFileName = input(f'\nWhat would you like to save the file as? ') # ask user to enter the name of the file to be saved
        with open(newFileName,'w',encoding='utf-8') as f:
            dataset = ("{0}\t{1}".format(a, b) for a, b in zip(myDict.keys(), myDict.values()))
            for line in dataset:
                f.write(str(line) + "\n")


# Main Program


# Prompt the user to enter a file name
while True:
    fName = input("Please enter a file name: ")
    if os.path.isfile(fName):
        break
    else:
        print(f"The file '{fName}' does not exist. Please try again.")

ipf = UCLAIP(fName)
nTerms = ipf.numLines()

while True:
    addMore = input(f'There are {nTerms} terms in this vocabulary list. Would you like to add more (Y/N)? ')
    if addMore.upper() == 'Y':
        countTerms = ipf.countTerms()
        orgDict = ipf.createDict()
        newDict = ipf.dictUpdate(countTerms,orgDict)
        while True:
            addMore = input("Do you want to add more terms? (Y/N)").strip()
            if addMore.upper() == 'Y':
                countTerms = ipf.countTerms()
                newDict = ipf.dictUpdate(countTerms,newDict)
            elif addMore.upper() == 'N':
                break
            else:
                print("Invalid input. Please enter Y or N.")
        keyCount = len(newDict)-1
        print(f'There are {keyCount} terms in the new vocabulary list.\n')
        ipf.printDict(newDict)
        ipf.saveFile(newDict)
        break
    elif addMore.upper() == 'N':
        orgDict = ipf.createDict()
        keyCount = len(orgDict)-1
        print(f'The vocabulary list:\n')
        ipf.printDict(orgDict)
        ipf.saveFile(orgDict)
        break
    else:
        print("Invalid input. Please enter Y or N.")
