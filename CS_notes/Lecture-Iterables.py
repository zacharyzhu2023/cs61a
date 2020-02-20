# Iterators and Generators


'''
Notes on Iterators
- Container can provide an iterator that accesses elements in order
    - Used iter(iterable) -> returns iterator over elements of an iterable value
    - next(iterator) -> returns the next element in an iterator
- The iterator knows the values within the list
- Next is simply called using the iterator
- Cannot iterate beyond the length of a list (stop at the last element)
- Programming note: avoid changing an iterable while using the iterator for it
- Iterable value: value that is passed to iter to produce an iterator
- Iterator-Returned from iter and passed to next; are mutable
- Dictionary/keys/values/items are all iterable values
    - Dictionary items are are not super predictable
- Does the iter(iterable) change when next is called? With reference to the pointer
'''



# Calling iterator/next on a list
print('Iterating over a list')
s = [3,4,5]
t = iter(s) # t is a position that accesses a position in t
print(next(t)) # 3-Gives you the current element in s, and then advances to the next element
print(next(t)) # 5-Next time, it accesses the next element
u = iter(s)
print(next(u)) # A new iterator, so it starts over at 3
print(next(t)) # 5-Original iterator accesses the current position in the previous iterator


# Iterating over a dictionary
print('Iterating over a dictionary')
d = {'one': 1, 'two': 2}
for k in d.keys():
    print(k) # one, two

for v in d.values():
    print(v) #1, 2

k = iter(d.keys())
print(next(k)) # one
print(next(k)) # two

# Iterating over a range
print('Iterating over a range')
r = range(3,6)
t = iter(r)
print(next(t)) # 3
print(next(t)) # 4

# Possible to use go through an iterator with a for loop, but uses up the iterator
for i in t:
    print(i)

# For Statements
print('For statements')
newD = {'one':1, 'two': 2}
v = iter(d.values())
print(next(v)) # 1
for something in v:
    print(something) # Only prints 2, because the iterator has "looked" at the original value


# Built-in iterator functions
'''
map(func, iterable)-Iterates over func(x) for x in iterable
filter(func, iterable)-Iterates over x in iterable if func(x)
zip(first_iter, second_iter)-Iterates over co-indexed (x,y) pairs
list(iterable)-Will create a list containing all the elements in an iterable
'''

# Utilizing max which uses an iterator

print('Working with more built-in iterators')
def double(x):
    return 2 * x

print(list(map(double, [3,4,5]))) # Iterates over the list and then doubles the contents
m = map(double, range(3,9)) # Creates  built in map object, delaying the computation
print(next(m)) # Nows it calls next on the first element of m
print(list(m)) # Iterates over the remaining elements of m with the function

# Generators

# Generators don't have to return 1 value
# Yield can yield as many values as you want
print('Working with generators')
def plus_minus(x):
    yield x
    yield -x

t = plus_minus(3)
print(next(t)) # 3
print(next(t)) # -3
print(list(plus_minus(3)) # Will give the list of all the yields of the functoin

"""
Notes
- A generator function yields a value, instead of returning one
- Generator function yields as many times as you want
- Generator is an iterator created from the generator function
    - When you get the result of a yield, you have flexibility with what to do with it
        - The result of a yield can take any data form (int, str, etc.)

"""


def a_then_b(a,b):
    for x in a:
        yield x
    for x in b:
        yield x

def a_then_b(a,b):
    yield from a
    yield from b


