# Lecture-Inheritance



# Review of Classes
'''
Notes
- All objects have attributes
- Classes are objects, so they have attributes
    - Instance Attribute: Attribute of an instance
    - Class Attribute: Attribute of a class  of an instance
- Methods are both functions and class attributes
- Bound methods are objects-first parameter self bound to an instance

'''

class Account:
    interest = 0.02 # Example of a class attribute
    def __init__(self, holder):
        # holder/balance are examples of instance attributes
        self.holder = holder
        self.balance = 0
    def withdraw(self, amount);
        self.balance -= amount
        return self.balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance

tom_account = Account('Tom')
tom_account.interest = 0.08 # This interest is now a instance attribute (bound to tom_account)
Account.interest = 0.04 # Example of a class attribute assignment



# Inheritance

'''
Notes
- Inheritance: method for relating classes together
    - Commonly used with two similar classes that have some specialization
    - Specialized class my have same attributes along with a special behavior
    - Specify the differences from the base class and everything else stays the same

Syntax:
    class <name> (<base class>):
        <suite>
    - The class <name> inherits from the base class
    - The subclass still shares the attributes of the base class

- For a subclass, looking up a name in the class:
    - Check first to see if the class has an attribute value
    - Otherwise look the name up in the base class to see if it exists

'''

checking_account = CheckingAccount('Tom')
ch.interest # 0.01-Lower interest rate
ch.deposit(20) # 20-Deposits work the same way
ch.withdraw(5) # 14-Withdrawals now incur a $1 fee

class CheckingAccount(Account):
    interest = 0.01
    withdrawal_fee = 1
    def withdraw(self, amount):
        # Using Account.withdraw avoids the recursive call
        return Account.withdraw(self, amount + self.withdraw_fee)


# Object-Oriented Design

'''
Notes
- Avoid repetition, use existing implementations when possible
- Overriddden attributes are still class objects (and can be accessed as such)


'''

class Bank:
    # Don't inherit from account, because it contains accounts
    # Will open accounts
    
    def __init__(self):
        self.accounts = []

    # Open different types of accounts
    def open_account(self, name, amount, type_account = Account):
        account = type_account(name)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    # Pay interest to accounts
    def pay_interest(self):
        for account in self.accounts:
            account.deposit(account.interest * account.balance)

    # Check to see if the bank has sufficient accounts to not "close"
    def too_big_to_fail(self):
        return len(self.accounts) > 1
    
john = bank.open_account('John', 10)
jack = bank.open_account('Jack', 5, CheckingAccount)
bank.pay_interest()
john.balance # 10.2
bank.too_big_to_fail # True


# Attributes Lookup Practice

class A:
    z = -1
    def f(self, x):
        return B(x-1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)

class C(B):
    def f(self, x):
        return x


a = A()
b = B()
b.n = 5

'''
C(2).n -->
    - No init method in class C, so it looks it up in class B
    - Sees an init method in the base class, passing in 2 to B's init method
    - self.z is then set to self.f(y)
        - Since self is the instance of C in this case, it looks up the f method in class C
        - This method returns the value passed into C, which is 2
        - self.z = 2
    - First, looks for n for the specific instance -cannot find it
    - Then, it looks for n in the current class, which is C -cannot find it here either
    - After, it looks for n in the base class, which is B -then finds it, n = 4
    
a.z == C.z -->
    - a.z = -1
        - For all instances of A, z is a class attribute, equaling to -1
    - C.z
        - This is looking for a class attribute of C
        - Looks from the current class up through class A, finally finding z = -1
    - Therefore, this evaluates to True
    
a.z == b.z -->
    - a.z = -1, as proven above
    - b.z
        - An instance of B is created, passing in 1 in the __init__ method
            - self.z = self.f(1)
            - Looks for f in B as an instance of f, but then goes to A as the base class
                - self.f(y) passes in 1 --> return B(0)
                - Creates a new instance of B, passing in 0
                    - self.z = C(y+1)
                    - Creates a new instance of C, passing in 1
                    - Since C doesn't have a constructor, the __init__ of B is used
                        - As a result, self.z is an instance of B
    -a.z (an integer), cannot be equal to b.z, an instance of B
                
    - As a result, this returns False

'''

# Multiple Inheritance
''' Occurs when a class has multiple base classes'''

'''
Notes
- A class may inherit from multiple base classes in Python
'''

class SavingsAccount(Account):
    deposit_fee = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)
    

'''
We want to creat a new account:
    _ Interest rate of 1%
    - $1 fee for withdrawals
    - $2 for deposits
    - Free dollar when opening an account
'''

def AdvertisedAccount(SavingsAccount, CheckingAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1


deal_account = AdvertisedAccount('John')
deal_account.balance # 1, because of the init method
deal.deposit(20) # 19, because it inherits the deposit method from savings account
deal.withdraw(10) # 7, because it inherits the withdraw method from checking account















    

