#!/usr/bin/env python3

# Accept a positive integer on the command line
# and compute its prime factorization. Print
# the prime factors on a single line, separated
# by whitespace.

import sys


def is_prime(n):
    """
    Return True if the given integer is prime, False
    otherwise.

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(9)
    False
    >>> is_prime(10)
    False
    """
    if n < 2:
        return False

    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, n):
        if n % i == 0:
            return False
    
    return True


def factorize(n):
    """
    Yield the prime factors of the given integer.

    >>> list(factorize(9))
    [3, 3]
    >>> list(factorize(15))
    [3, 5]
    >>> list(factorize(81))
    [3, 3, 3, 3]
    """
    if is_prime(n):
        yield n

    for f in range(2, n):
        if n % f != 0:
            continue

        yield from factorize(f)
        yield from factorize(n // f)
        break


if __name__ == "__main__":
    number = int(sys.argv[1])
    factors = factorize(number)
    print(" ".join((str(f) for f in factors)))

