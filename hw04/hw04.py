def hailstone(n):
    """Q1: Yields the elements of the hailstone sequence starting at n.
       At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        yield 1
        yield from hailstone(1)
    elif n % 2 == 0:
        yield n
        yield from hailstone(n // 2)
    else:
        yield n
        yield from hailstone(3 * n + 1)


def merge(a, b):
    """Q2:
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    "*** YOUR CODE HERE ***"
    a0 = next(a)
    b0 = next(b)
    while True:
        if a0 < b0:
            yield a0
            a0 = next(a)
        elif a0 == b0:
            yield a0
            a0 = next(a)
            b0 = next(b)
        else:
            yield b0
            b0 = next(b)


def perms(seq):
    """Q3: Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> p = perms([100])
    >>> type(p)
    <class 'generator'>
    >>> next(p)
    [100]
    >>> try: # Prints "No more permutations!" if calling next would cause an error
    ...     next(p)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(perms([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(perms((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(perms("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"
    if len(seq) == 1:
        yield [seq[0]]
    else:
        for perm in perms(seq[1:]):
            for i in range(len(perm) + 1):
                yield perm[:i] + [seq[0]] + perm[i:]


def yield_paths(t, value):
    """Q4: Yields all possible paths from the root of t to a node with the label
    value as a list.

    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> print_tree(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(yield_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = yield_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = tree(0, [tree(2, [t1])])
    >>> print_tree(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = yield_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    if label(t) == value:
        yield [label(t)]
    for b in branches(t):
        for a in yield_paths(b,value):
            yield [label(t)] + a


class Minty:
    """A mint creates coins by stamping on years. The update method sets the mint's stamp to Minty.present_year.
    >>> mint = Minty()
    >>> mint.year
    2021
    >>> dime = mint.create('Dime')
    >>> dime.year
    2021
    >>> Minty.present_year = 2101  # Time passes
    >>> nickel = mint.create('Nickel')
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Minty.present_year = 2176     # More time passes
    >>> mint.create('Dime').worth()    # 10 cents + (75 - 50 years)
    35
    >>> Minty().create('Dime').worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    """
    present_year = 2021

    def __init__(self):
        self.update()

    def create(self, type):
        "*** YOUR CODE HERE ***"
        return Coin(self.year, type)    

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = self.present_year

class Coin:
    cents = 50

    def __init__(self, year, type):
        "*** YOUR CODE HERE ***"
        self.year = year
        if type == 'Dime':
            self.type = 10
        else:
            self.type = 5

    def worth(self):
        "*** YOUR CODE HERE ***"
        if Minty.present_year - self.year - 50 <= 0:
            return self.type
        return self.type + (Minty.present_year - self.year - 50)


class VendingMachine():
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    stock = 0
    balance = 0
    
    def __init__(self, product, price):
        self.product = product
        self.price = price
    
    def restock(self, amount):
        self.stock += amount
        return 'Current {} stock: {}'.format(self.product,self.stock)

    def add_funds(self, amount):
        if self.stock != 0:
            self.balance += amount
            return 'Current balance: ${}'.format(self.balance)
        else:
            return 'Nothing left to vend. Please restock. Here is your ${}.'.format(amount)
    def vend(self):
        if self.stock == 0:
            return 'Nothing left to vend. Please restock.'
        elif self.balance < self.price:
            return 'Please add ${} more funds.'.format(self.price - self.balance)
        elif self.balance == self.price:
            self.stock -= 1
            self.balance = 0
            return 'Here is your {}.'.format(self.product)
        else:
            change = self.balance - self.price
            self.balance = 0
            self.stock -= 1
            return 'Here is your {} and ${} change.'.format(self.product,change)


# Tree Data Abstraction

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

