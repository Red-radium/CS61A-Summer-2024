def count_occurrences(t, n, x):
    """Return the number of times that x is equal to one of the
    first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(t, 3, 10)
    2
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(u, 1, 3)  # Only iterate over 3
    1
    >>> count_occurrences(u, 3, 2)  # Only iterate over 2, 2, 2
    3
    >>> list(u)                     # Ensure that the iterator has advanced the right amount
    [1, 2, 1, 4, 4, 5, 5, 5]
    >>> v = iter([4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5])
    >>> count_occurrences(v, 6, 6)
    2
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for _ in range(n):
        if next(t) == x:
            count += 1
    return count


def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.

    >>> for num in hailstone(10):
    ...     print(num)
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    # while True:
    #     if n == 1:
    #         yield n
    #         return
    #     elif n % 2 == 0:
    #         yield n
    #         n = n // 2
    #     else:
    #         yield n
    #         n = n * 3 + 1
    if n == 1:
        yield 1
    elif n % 2 == 0:
        yield n
        yield from hailstone(n // 2)
    else:
        yield n
        yield from hailstone(n * 3 + 1)


def merge(incr_a, incr_b):
    """Yield the elements of strictly increasing iterables incr_a and incr_b, removing
    repeats. Assume that incr_a and incr_b have no repeats. incr_a or incr_b may or may not
    be infinite sequences.

    >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    >>> def big(n):
    ...    k = 0
    ...    while True: yield k; k += n
    >>> m = merge(big(2), big(3))
    >>> [next(m) for _ in range(11)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    iter_a, iter_b = iter(incr_a), iter(incr_b)
    next_a, next_b = next(iter_a, False), next(iter_b, False)
    "*** YOUR CODE HERE ***"
    while next_a is not None or next_b is not None:
        if next_a is not None and (next_b is None or next_a < next_b):
            yield next_a
            next_a = next(iter_a, None)
        elif next_b is not None and (next_a is None or next_b < next_a):
            yield next_b
            next_b = next(iter_b, None)
        else:
            yield next_a
            next_a, next_b = next(iter_a, None), next(iter_b, None)
