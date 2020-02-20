# Lecture-Representation


# repr/str
'''
Notes
- Object value should behave like the data it represents
- A string representation of itself must be usable in programs but also in language
- Python has 2 string representations"
    - Has str representation legible to humans
    - Has repr representation legible to Python
    - str/repr are often the same
- Result of repr(value) is what Python prints in an interactive session
'''

print(repr(12e12)) # 12000000000000.0
12e12 # Evaluates to the same thing as above

from fractions import Fraction
half = Fraction(1,2) # Build a fraction from a numerator and denominator
print(repr(half)) # Fraction(1, 2)
print(str(half)) # 1/2
print(half) # Same as the result of the str(value)

sample = 'Hello World'
print(repr(sample)) # 'Hello World'
print(sample) # Hello World
print(str(sample)) # Hello World
repr(sample) # Evaluates to: "'Hello World'"
eval(repr(sample)) # Evaluates to: 'Hello World'
'''
Notes to self
- sample is obviously a string
- repr(sample) makes a string of a string
- Meanwhile, since sample is already a string, str returns the original string
    - Similar to list(expression) when expression is already a list
- eval(expression) requires a valid Python expression
'''

# Polymorphic Functions

'''
Notes
- Polymorphic function: Function that applies to many different forms of data
    - Example: str/repr, since they can apply to any object
- repr invokes the argument __repr__ on its argument
    - Manages to ignore an instance attribute __repr__ and default to class attributes
- str invokes the argument __str__ on its argument
    - Ignores the instance attribute __str__
    = Looks for __str__ attribute, but then goes to repr
- str is a class, not a function
'''
half.__repr__() # Evaluates to: 'Fraction(1,2)'
half.__str__() # Evaluates to: '1/2'

'''
def repr(x):
    return type(x).__repr__(x)
- Looks up the type of the argument
- type(x) returns a class
- Then, the __repr__ argument is called from the class on x
'''

class Bear:
    def __repr__(self):
        return 'Bear()'
oski = Bear()
print(oski) # Bear()
print(str(oski)) # Bear()
print(repr(oski)) # Bear()
print(oski.__str__()) # Bear()
print(oski.__repr__()) # Bear()


class OtherBear:
    def __init__(self):
        self.__repr__ = lambda: 'oski bear'
        self.__str__ = lambda: 'this bear'
    def __repr__(self):
        return 'OtherBear()'
    def __str__(self):
        return 'another bear'
    
new_oski = OtherBear()
print(new_oski) # another bear
print(str(new_oski)) # another bear
print(repr(new_oski)) # OtherBear()
print(new_oski.__str__()) # this bear
print(new_oski.__repr__()) # oski bear

'''
Notes about the OtherBear class
- First, we created an instance of this class
- When printing out an instance, defaults to class __str__ method
- str(instance of OtherBear) uses the class method
- repr(instance of OtherBear) uses the class method
- instance of OtherBear.__repr__() uses the instance method defined in __init__
= instance of OtherBear.__str__() uses the instance method defined in __init__ as well

'''

# Making another repr function
'''
def repr(x):
    return type(x).__repr__(x)

def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
    else:
        return repr(x)
'''

# Interfaces
'''
Notes
- Looks up attributes on each other
'''

class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d
    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)
    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)
    def __float__(self):
        return self.numer/self.denom
    def __add__(self, other):
        # Account for three cases: other is int, other is float, other is an instance of Ratio
        if isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, int):
            n = self.numer + other * self.denom
            d = self.denom
        elif isinstance(other, float):
            return float(self) + other # Return a float directly, not a ratio
        g = gcd(n,d)
        return Ratio(n//g, d//g)

    __radd__ = __add__ # Right side addition is the same as 
            

def gcd(n,d):
    while n != d:
        n, d = min(n, d), abs(n-d)
    return n

half = Ratio(1,2)
print(half) # Prints 1/2 because it uses the __str__ method to print
half # Evaluates to Ratio(1/2) since it's an instance


# Special Method Names
'''
Notes
- Certain names are special because they have built-in behavior
- These names start & end with two underscores
- Example: __init__
    - Invoked automatically when object is constructed
- Another example: __repr__ used to display an object as an expression
- __add__ used to add on object to another
- __bool__ converts an object to True/False
- __float__ converts object to float

'''
a, b, c = 0, 1, 2
a + b # Evaluates to: 1
bool(a), bool(b) # Evaluates to: (False, True)
a.__add__(b) # Does the same thing as a + b
a.__bool__(), b.__bool__() # Still evaluates to: (False, True)











