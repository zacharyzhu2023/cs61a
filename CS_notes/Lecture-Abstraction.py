from operator import getitem # Allows us to "index" a list
from math import gcd

# Abstraction example
def mul_rational(x,y):
    return rational(numer(x) * numer(y), denom(x)*denom(y))

def add_rational(x,y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def equal_rational(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

'''
Notes
- The function numer(num) and denom(num) aren't defined, but we don't necessarily need them
- We just need to understand what they're intended to do to implement abstraction

'''


# New functions defined to implement the previously abstracted methods
def rational(n, d):
    """ Take in 2 integers and represent them as a fraction through a list"""
    return [int(n/gcd(n,d)), int(d/gcd(n,d))]

def numer(x):
    """ x is a list constructed through the rational function
    numer should return the numerator of this 'fraction' """
    return x[0]

def denom(x):
    ''' Same criteria applies as above, but returns the denominator'''
    return x[1]

print(mul_rational([3,4],[2,7]))

# How can we use data abstraction to reduce a number to lowest terms?
'''
Additional Comments
- Using abstraction allows you to change one component without messing everything else up
- Easier to gauge through implementation
- It's also possible to represent these numbers as functions, instead of as lists
'''


# List Operations
print("Working with list operations")
pair = [1, 2] # Referred to as a list literal
print(pair)
x, y = pair # x now equals the first element, y equals the second-process is called unpacking
print(x, y) # Should print 1 2

pair[0] # Expression evaluates to 1
print(getitem(pair, 0)) # Does exactly the same thing as above


# Learning to work with dictionaries
print("Now Working with Dictionaries")
d = {1: 'I', 5: 'V', 10: 'X'} # There is a key that corresponds to a value
print(d[1], d[5]) # It's possible to find the value in a dictionary that corresponds to the key
d.keys() # Way to find the explicit values of a key
d.values() # Way to find all the values in a dictionary
print(list(d.items())) # Provides an ordered list of the items of a dictionary
e = {1: ['I','i'], 5: 'V', 10: 'X'} # Work around to get one key in a dictionary to associate with multiple values
f = {str(k): v for k, v in d.items()} # Method for modifying all the keys of a dictionary using an already existing one
print(f) # The dictionary with a string version of the original keys
g = {1: {2:'hi'}, 3: {'hello': 5}} # It's possible to have a compound dictionary
print('Now operating with compound dictionaries')
print(g[1]) # A key can go to a dictionary, but a dictionary can't go to a key
print(g[3]['hello'])
h = {v: k for k, v in d.items()} # v, k refer to the key and values in a dictionary
print('Inverting a dictionary: ', h)
print(d.get('C', 0)) # Searches for a key in a dictionary, if not there, return 0



"""
Notes on Dictionaries
- Dictionaries are useful to use b/c they're optimized for finding keys
- It's possible to use a list of lists, but the computation requires lists vs a built-in function
- Keys of dictionaries can be any data type, same with output (input should not be a key)
- A dictionary is typically used to find values from keys
- If you repeat a key in a dictionary, Python automatically only keeps the first instance
- Dictionaries are unordered
- Dictinoary restrictions: keys cannot be a dictionary nor a dictionary (anything mutable)
"""
