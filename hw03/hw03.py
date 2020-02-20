HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def num_sevens(n):
    """Returns the number of times 7 appears as a digit of n.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_sevens',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    elif n % 10 == 7:
        return 1 + num_sevens(n//10)
    return num_sevens(n//10)



def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    '''
    counter = 1
    dir = 1
    ping_pong_num = 1
    while counter != n:
        ping_pong_num += dir
        temp = ping_pong_num
        while !temp:
            if temp % 10 == 7:
                ping_pong_num *= -1
        if ping_pong_num % 7 == 0:
            pingpong_num *= -1
        counter += 1
    '''

    # Check to see if there is a digit 7
    def hasSeven(num):
        if not num:
            return False
        elif num % 10 == 7:
            return True
        return hasSeven(num//10)

    # Check if direction should be switched
    def meetSevenCondition(num):
        return hasSeven(num) or num % 7 == 0

    # Switch or don't switch direction based on current value
    def changeDirection(num, dir):
        if meetSevenCondition(num):
            return -dir
        return dir

    # Change the value of N based on its previous direction?
    def changeN(initial_value, prev_dir):
        if initial_value == n:
            return prev_dir
        return prev_dir + changeN(initial_value + 1, changeDirection(initial_value, prev_dir))

    return changeN(1, 1)







def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"\

    # Determine if it's a denomination of two
    def denomination_two(num):
        if num == 1:
            return True
        elif num % 2 == 1:
            return False
        return denomination_two(num//2)

    # Determine the highest denomination of two less than amount
    def max_of_two(num):
        if num == 0:
            return -1
        return 1 + max_of_two(num//2)

    # Use the partition algorithm
    def partition_with_denomination(num, up_to):
        if num == 0:
            return 1
        elif num < 0:
            return 0
        elif up_to == 0:
            return 0
        else:
            first_partition = partition_with_denomination(num-up_to, up_to)
            second_partition = partition_with_denomination(num, up_to//2)
            return first_partition + second_partition
    return partition_with_denomination(amount, 2**max_of_two(amount))

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x # Ensure x is not mutated
    [1, [2, 3], 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> x
    [[1, [1, 1]], 1, [1, 1]]
    """
    "*** YOUR CODE HERE ***"

    '''
    for elem in lst:
        if type(elem) == list:
            return False
    return True
    '''
    cleaned_list = []
    for elem in lst:
        if type(elem) != list:
            cleaned_list.append(elem)
            #print(cleaned_list)
        else:
            cleaned_list = cleaned_list + flatten(elem)
    return cleaned_list



###################
# Extra Questions #
###################

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
