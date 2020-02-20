# Mutable Types
from datetime import date


# Working with datetime objects
print('Working with datetime')
today = date(2019, 9, 30) # Representing a day as a "number"
freedom = date(2019, 12, 19)
time_difference = freedom - today # Representing the number of days between 2 dates
print(time_difference)
print(today.year) # Prints an attribute: 2019
print(today.strftime('%A, %B %d')) # Can present the date in another format


# Treating strings are objects
print('\nWorking with strings are objects')
sample = 'Hello'
print(sample.upper()) #HELLO
print(sample.swapcase()) #hELLO
print(sample.isalpha()) #Prints True
print(sample.endswith('lo')) #Prints True

'''
Brief Notes about Strings
- Strings are represented by ASCII code
- Layout was chosen to support sorting by character code
-Unicode standard includes 137,994 characters and 150 scripts

'''

# Mutable Objects: Lists
suits = ['a','b','c','d']
suits.pop() # ['a','b','c']
suits.remove('b') # ['a','c']

# Mutable Objects: Dictionaries
numerals = {'I': 1, 'V': 5}
numerals['X'] = 10 #{'I': 1, 'V': 5, 'X': 10}
numerals.pop('V') # {'I': 1, 'X': 10}

'''
Mutable types
- Same object can change value throughout description
- Only mutable types can change
- All objects that refer to the same object are affected by mutation
- Only objects that can change: lists and dictionaries
= Function can change the value of an object in its scope
'''

# Tuples
tup = (2,3,4,5) # Parantheses are technically not necessarily
print(t[0], t[2]) #2 4
print(t[:3]) #(2, 3, 4)
tup2 = tuple([2,3,4,5]) # Can make a tuple from a list
ugly = (2,) # Makes a tuple of length 1
print(tup * 2) # (2,3,4,5,2,3,4,5)

# Tuples can't append or assign because they're not mutable
# Tuples can be a key in a dictionary
tuple_dict = {(2,3): 'value'} # Dictionary with a tuple

'''
Notes
- Objects: represent some value in a meaningful way
- The end result of today.strftime depends on the method, object, and parameters that are passed
- Data and behavior together create abstractions
- Objects can also represent properties, interactions, & processes
- The "type" of object is called a class
- Object Oriented programs: method of organizing large programs
    - Uses different syntax to amke things easier
- In Python, every value is an object
    -All objects have attributes
    - Object methods can make life easier
- Contrast: Functions do 1 thing; objects do many things
- Previously, if objects aren't modified, compound value is the total of its pieces
    0Compound data is made up of the pieces of which makes it up
'''
