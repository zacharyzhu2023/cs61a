# Lecture-Objects

'''
Notes
- Object oriented programming: method to organize programs
    - Also groups relevant info/behavior
- Each object has its own local state (characteristics)
- Class: describes the general behavior of instances/objects of it
- Analogy of a bank account: Account class, bank accounts have balance
& someone who holds the account
    -In this class, the behaviors should all work the same way
- Methods are functions defined in suite of a class statement
- <expression>.<name>
    - Expression can be any valid Python expression
    - <name> must be a simple name
- Functions are different from bound methods
'''


# Bank Account Class-Abstract behavior
"""
a = Account('John')
a.holder # 'John'
a.balance # 0
a.deposit(15) # 15
a.withdraw(10) # 5
a.balance # 5
a.withdraw(10) # 'Insufficient funds'
"""


'''
Notes on creating a class
class <name>:
    <suite>
- Class statement creates the class & binds it to the first frame of environment
- Assignment/def statements in suite create attributes of the class
'''

class Clown:
    nose = 'big and red'
    def dance():
        return 'No thanks'

# Looking at the general characteristics of a class
print(Clown.nose)
print(Clown.dance())

class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            return self.balance
        return 'Insufficient Funds'
    # Making a class attribute
    interest = 0.02
    
        
a = Account('Jim')
print(a.balance) # 0
print(a.holder) # 'Jim'

b = Account('Jack') # Each call to account creates a new instance from the same class
print(b.balance) # 0
print(b.deposit(15)) # 15
print(b.withdraw(3)) # 12

print(type(b.interest))
print(a.interest)

'''
- First, it creates a new instance of a class
- __init__ method of a class is called with self along with additional arguments
provided in the call expression
'''

'''
Evaluating dot expression
- Evaluate expression to the left of the dor (should give an object)
- Name is matched against instance attributes; if exists, value retuned
    - Otherwise, name is looked up in a class
- The returned function/method is then evaluated
'''




