# Lecture-Composition

'''
Notes
- Linked List: either empty or 1 value + the rest of the linked list
    - Way of representing a sequence as a first element + its remaining elements
- Linked lists have 2 attributes: first + rest
- An example: 3, 4, 5
    - Link instance: first-3, rest-Link instance: first 4, rest-Link instance: first: 5, rest: empty
- Linked list is a pair (linked list isn't a specific class in Python)
    - Can represent the different components however best suits the class
    - By convention, the empty list is represented as a slash
- When constructing a linked list, the remaining list should default to empty
- Linked list tend to be more efficient
    - Adding elements to the beginning can share memory
- @<attribute> decorator can be used to designate whenever the attribute is assigned

'''

class Link:
    empty = () # Creates an empty tuple--could also be None or any value we choose it to be
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link) # Ensures that what's passed in can become a linked list
        self.first = first
        self.rest = rest # Default value is empty

    @property # When this function is referred to, it's automatically called when looking up an instance
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value
        

s = Link(3, Link(4, Link(5, Link.empty))) # Should correspond to 3, 4, 5
s.first # 3
s.rest.first # 4
t = Link(2, s) # Allows us to add an element at the beginning of the linked list
t.rest.first = 7 # Now refers to 2, 7, 4, 5
t.rest.rest = Link.empty # Now refers to 2, 7, 4
# We are able to "get rid" of any element
v = Link(1, Link(Link(2, Link(3)), Link(4))) # [1, [2, 3], 4]-creating a nested linked list


# What if we wanted to be able to access a value that isn't inheriting there?
''' Using the property decorator'''

j = Link(3, Link(4, Link(5)))



# Tree Abstraction Review
'''
Notes
- A tree has a root label and a list of branches
- Branch is a tree, a leaf has no branches
- Trees can be represented as a class
'''

class Tree:
    def __init__(self, label, branches = []):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches) # Ensures everything is a list
    def is_leaf(self):
        return not self.branches


'''
- Previously, we had a data abstraction for trees
- Now, we can use dot notation to get all these components of a tree
- Class representation just makes things easier
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
        
'''

'''
Other stuff to try myself
1. Get the height of a tree
2. Get a list of the leaves of a tree
3. Construct a fibonacci tree based off of the tree class
'''


# Constructing class version of a fibonacci tree

def fib_tree(n): # n being the nth fibonacci number
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left_tree = fib_tree(n-1)
        right_tree = fib_tree(n-2)
        return Tree(left_tree.label + right_tree.label, [left_tree, right_tree])

# Make a list of the leaves of a tree
''' With an assignment statement'''
def leaves(t):
    leaves = []
    if not t.branches:
        return leaves.append(t.label)
    for b in t.branches:
        return leaves(b)

''' Without an assignment statement'''
# Check to see if this method is valid
def new_leaves(t):
    if not t.branches:
        return [t.label]
    for b in t.branches:
        return [].extend(leaves(b))

# Get the height of a tree
def height(t):
    if not t.branches:
        return 0
    else:
        branches = []
        for b in t.branches:
            branches.append(height(b))
    return 1 + max(branches)

'''
Notes to self about finding the height
- Base case: if t is a leaf, then it has no height
- Otherwise, we construct a list of the heights of the branches
- Afterward, we get the maximum of the height of the branches?
    - Add one each time we get to the root and count back up
'''


# Testing pruning a tree

# Somehow I magically got this right first try???
def prune(t, n):
    '''Prune sub-trees whose label value is n'''
    t.branches = [b for b in t.branches if t.label != n]
    for b in t.branches:
        prune(b, n)


'''
Notes to self about pruning
- Use list comprehension to parse through all the branches of a tree
- Check to see if the label matches that which we want to prune
    - If it does, then we don't keep that branch
    - If it doesn't, then we keep that branch and go through the branches of the branch
- Recursive call the pruning on the remaining branches
'''






