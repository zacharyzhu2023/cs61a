



'''
Working with lists/while loops/for loops/recursion

1. Write a function using recursion that allows you to find factorials
factorial(1) --> 1
factorial(2) --> 2
factorial(5) --> 120

2. Create a recursive function that counts the number of 5's in the digits of a number
numFives(388552) --> 2
numFives(28883) --> 0
numFives(175555) --> 4

'''

def function(x):
    ''' Takes in an positive integer x '''

    if x == 0:
        return x
    else:
        print(x)
        function(x-1)

function(5)


def elementsOfAString(s):
    ''' Print out each of the individual characters in a string using recursion'''
    if len(s) == 0:
        return ''
    else:
        print(s[0], s[1:])
        elementsOfAString(s[1:])

elementsOfAString('some arbitrary string')



def calcBond(one, two):
    greaterElement = max(one, two)
    smallerElement = min(one, two)
    if greaterElement - smallerElement >= 1.7:
        return 'ionic'
    else:
        return 'covalent'


x = 10
if x == 5:
    if True:
        pass
    elif x == 10:
        print('True statement')



