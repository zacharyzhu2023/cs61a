# Lecture-Efficiency
'''
Notes
- One example of tree recursion could be computing fibonacci numbers
    - This was inefficient because there was a lot of repetition with recursive calls
- Efficiency measures how many steps are required to reach the desired result

'''

# Generate fibonacci numbers with tree recursion
def fib(n):
    #print('call: ' + str(n))
    if n <= 1:
        return n
    return fib(n-2) + fib(n-1)

# Count the number of recursive calls
def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

fib = count(fib)
fib(5)
print(fib.call_count) # 15-the fibonacci function is called 15 times
fib(5)
print(fib.call_count) # 30-called again 15 times


# Memoization


def memo(f):
    cache = {} # Dictionary that memorizes results
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized


fib = count(fib)
counted_fib = fib
fib = memo(fib)
fib = count(fib)
fib(10)
print(counted_fib.call_count)
print(fib.call_count)


# Exponentiation
'''
Notes
- Goal: one more multiplication lets use double problem size
- The normal definition of exp has linear time
- The second definition of exp_fast has logarithmic time
'''

# Raise b to the power of n through multiplication
# This isn't as efficient as it could be: multiplies n times
# Uses: b * b ** (n-1)
def exp(b,n):
    if n == 0:
        return 1
    return b * exp(b, n-1)

# if n = 0: 1, if n % 2 == 0: b ** (1/2n) ** 2, if n % 2 == 1: b * b ** (n-1)

def exp_fast(b,n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return exp_fast(b, n//2) ** 2
    else:
        return b * exp_fast(b, n - 1)

# Orders of Growth
'''
- Quadratic time-Functions that process all pairs of values in a sequence of length n
Example:
    def overlap(a,b):
        count = 0
        for item in a:
            for n in b:
                if item == n:
                    count += 1
        return count
- This takes a * b computations
- Exponential time: amount of work t do "one more" multiplies work to do n by a constant factor
    - This greatly increases over time

a * b^(n+1) = (a * b^n) * b --> exponential growth
a * (n+1) ^2 = (a * n^2) + a * (2n+1) --> Quadratic growth
a * (n+1) = a * n + a --> Linear growth
a * ln(2*n) = (a * ln(n)) + a * ln(2) --> Logarithnmic growth

Exponential growth-Incrementing n multiplies time by constant
Quadratic growth means incrementing n increases time by n times a constant
Linear Grwoth means n increases time by a constant
Logarithmic growth means doubling n increments time by a constant

'''


# Space
'''
- Space is linearly dependent on the number of elements in a container
- Space is also dependent on the number of frames necessary during evaluation
- Memory used for values/frames can be recycled, however
- Environment is active is function is curretnly being evaluated but nothign has been returned
- Parent environments of functions named in active environments are also considered active
'''













