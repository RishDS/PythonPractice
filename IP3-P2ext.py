import os
from typing import Dict, List, Optional

class UCLAIP:
    """
    Class for managing a vocabulary list.
    """
    def __init__(self,fName:str) -> None: 
        """
        Initialize the class with a file name.

        Args:
            file_name: The name of the file to read from.
        """
        self.fName = fName

    def numLines(self) -> int:
        """
        Read the file and return the number of lines in it.

        Returns:
            The number of lines in the file.
        """
        try:
            with open(self.fName, 'r') as infile: 
                lineList = infile.readlines()
            return len(lineList)-1
        except Exception as e:
            raise Exception(f"Failed to read file: {e}")
    
    def countTerms(self) -> int:
        """
        Prompt the user to enter the number of terms they would like to add to the vocabulary list.

        Returns:
            The number of terms to add.
        """
        while True:
            try:
                cTerms = int(input(f'How many would you like to add? ')) # ask user to input the number of terms
                assert cTerms >0 # validate that the entered number is positive
                return cTerms
            except ValueError:
                print(f'Error. Please enter an integer.')
            except AssertionError:
                print(f'Error. Please enter a positive number.')
            except Exception as e:
                raise Exception(f"Failed to get number of terms: {e}")
    
    def createDict(self, keys: List[str], values: List, default_value=None) -> dict:
        """
        Create a dictionary from a list of keys and values. If the number of keys exceeds the number of values,
        the remaining keys will be paired with the default_value parameter.

        Args:
            keys (List[str]): A list of keys to be used in the dictionary.
            values (List): A list of values to be used in the dictionary.
            default_value: A default value to be used when there are more keys than values.

        Returns:
            dict: A dictionary where each key is paired with the corresponding value from the values list.
        """
        orgDict = {}
        with open(self.fName, 'r') as f:
            for line in f:
                fields = line.strip().split('\t')
                if len(fields) != 2:
                    print(f"Skipping line '{line.strip()}' - invalid format")
                    continue
                keys, values = fields
                orgDict[keys.strip()] = values.strip()
        return orgDict

    def dictUpdate(self, cTerms: int, myDict: Dict[str,str]) -> Dict[str,str]:
        """
        Prompts the user to enter new terms and their definitions, and updates the input dictionary.

        Parameters:
        count (int): The number of terms to be added
        my_dict (dict): The dictionary to be updated

        Returns:
        dict: The updated dictionary
        """
        for i in range(1,cTerms+1):
            newTerm = input(f'Term #{i}: ') # ask user to enter new term
            if newTerm in myDict.keys(): # check if the new term is already present in the orgDictionary
                choice = input(f'Warning! This term is already in the vocabulary list. Update definition (Y/N)? ') # ask user if they want to update the definition
                if choice.upper() == 'Y': # check if the user wants to update the definition
                    myDict[newTerm] = input(f'Definition #{i}: ') # if yes, ask user to input the new definition and add it to the orgDictionary
                else:
                    continue # if no, continue to the next iteration of the loop
            else:
                myDict[newTerm] = input(f'Definition #{i}: ') # if the term is not already present in the orgDictionary, ask user to input the new definition and add both to the orgDictionary
        return myDict
    
    def printDict(self, myDict: Dict[str,str]):
        """
        Prints the dictionary in a formatted way where each line contains a term and its definition.

        Parameters:
        my_dict (dict): The dictionary to be printed
        """
        try:
            print ("\n".join(f'{term} - {definition}' for term, definition in myDict.items()))
        except AttributeError:
            print("The dictionary is empty.")
        except KeyError:
            print("The first key and value are not present in the dictionary.") 


    def saveFile(self, myDict: Dict[str,str]):
        """
        Prompts the user to enter a file name and saves the dictionary to a file with the entered name.

        Parameters:
        my_dict (dict): The dictionary to be saved
        """
        newFileName = input(f'\nWhat would you like to save the file as? ') # ask user to enter the name of the file to be saved
        with open(newFileName,'w',encoding='utf-8') as f:
            for term, definition in myDict.items():
                f.write(f'{term}\t{definition}\n')


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
