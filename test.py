from abstract import *

def factorize(n, k = 2):
    if n == k:
        return 1
    elif n < k:
        return 0
    elif n%k != 0:
        return factorize(n,k+1)
    return factorize(n//k,k)+factorize(n,k+1)


def subsequences(lst):
    if lst == []:
        return [[]]
    without_first = subsequences(lst[1:])
    with_first = [[lst[0]] + rest for rest in subsequences(lst[1:])]
    return without_first+with_first


def prune(t):
    assert isinstance(t, Tree)
    def prune_level(t, d):
        if d%2 == 0:
            t.branches = [b for b in t.branches if b.label>=t.label]
        else:
            t.branches = [b for b in t.branches if b.label<=t.label ]
        for b in t.branches:
            prune_level(b, d+1)
    prune_level(t, 0)
    
class LearnableContent():
    def __init__(self,title, author) -> None:
        self.titel = title
        self.author = author
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
    
class Video(LearnableContent):
    license = 'CC-BY-NC-SA'
    def __init__(self, title, author, num_seconds) -> None:
        super().__init__(title, author)
        self.num_seconds = num_seconds
    def __str__(self):
        return f"{self.title} by {self.author} ({self.num_seconds} seconds)"
    
def link_insert(lnklst, value, before):
    if lnklst is Link.empty:
        return Link.empty
    elif lnklst.first == before:
        return Link(value, lnklst)
    else:
        return Link(lnklst.first, link_insert(lnklst.rest, value, before))
    
def most_common(s):
    pass

class SparseList():
    def __init__(self,s) -> None:
        self.n = len(s)
        self.common = most_common(s)
        self.others = {i:s[i] for i in range(self.n) if s[i] != self.common}
    
    def item(self, i):
        if i >= self.n:
            return 'out of range'
        elif i in self.others:
            return self.others[i]
        else:
            return self.common
        
    def items(self):
        return [self.item(i) for i in range(self.n)]
    
def link_insert(lnklst, value, before):
    if lnklst is Link.empty:
        return Link.empty
    elif lnklst.first == before:
        return Link(value, lnklst)
    else:
        return Link(lnklst.first, link_insert(lnklst.rest, value, before))
    
    
def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth)
    level have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    def helper(t, need_reverse):
        if t.is_leaf():
            return
        new_label = [b.label for b in t.branches[::-1]]
        for i in range(len(t.branches)):
            curr_branche = t.branches[i]
            helper(curr_branche, not need_reverse)
            if need_reverse:
                t.branches.label = new_label[i]
    return helper(t, True)