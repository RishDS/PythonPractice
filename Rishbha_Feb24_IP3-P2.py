import os
from IPfunctions import UCLAIP

ipf = UCLAIP()

##Example 3
fName = input(f'Please enter a file name: ')
pathHead, fName = os.path.split(fName)
#extension
'''if not os.path.exists(fName):
    print("File not found!")'''
nTerms = ipf.numLines(fName)
input(f'There are {nTerms} terms in this vocabulary list. Would you like to add more (Y/N)? ')
'''input(f'How many would you like to add? 1.5')
input(f'Error. Please enter an integer.')
input(f'How many would you like to add? -4')
input(f'Error. Please enter a positive number.')
input(f'How many would you like to add? one')
input(f'Error. Please enter an integer.')
input(f'How many would you like to add? 2')
input(f'Term #1: break')
input(f'Warning! This term is already in the vocabulary list. Update definition (Y/N)? Y')
input(f'Definition #1: Used to exit a loop')
input(f'Term #2: if')
input(f'Definition #2: Conditionally executes a block of code')
input(f'Would you like to add more terms (Y/N)? Y')
input(f'How many would you like to add? 0')
input(f'Would you like to add more terms (Y/N)? N')
input(f'There are 11 terms in the new vocabulary list.')
input(f'')
input(f'break - Used to exit a loop')
input(f'continue - Used to skip the current block, and return to the "for" or "while" statement')
input(f'dictionary - A mutable associative array (or dictionary) of key and value pairs. ')
input(f'float - An immutable floating point number.')
input(f'immutable - Cannot be changed after its created.')
input(f'int - An immutable integer of unlimited magnitude.')
input(f'pass - Needed to create an empty code block')
input(f'set - Unordered set, contains no duplicates')
input(f'string - Can include numbers, letters, and various symbols and be enclosed by either double or single quotes')
input(f'while - Executes a block of code as long as its condition is true.')
input(f'if - Conditionally executes a block of code')
input(f'')
input(f'What would you like to save the file as? mynewvocablist.txt')'''