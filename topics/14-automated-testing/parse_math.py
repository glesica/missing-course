from typing import List, Union


def parse_math(expr: str) -> List[Union[str, int]]:
    """
    Parse a mathematical expression consisting of integers
    and simple arithmetic operators (+, -, *, /) into a list
    of integers (representing the operands) and strings
    (representing the operators). An exception is thrown if
    the given string is an invalid expression.

    >>> parse_math('')
    []
    >>> parse_math('0')
    [0]
    >>> parse_math('+')
    ['+']
    >>> parse_math(0)
    Traceback (most recent call last):
     ...
    Exception: invalid expression
    >>> parse_math(None)
    Traceback (most recent call last):
     ...
    Exception: invalid expression
    >>> parse_math('!')
    Traceback (most recent call last):
     ...
    Exception: invalid expression
    >>> parse_math('1.0')
    Traceback (most recent call last):
     ...
    Exception: invalid expression
    >>> parse_math('4+2')
    [4, '+', 2]
    >>> parse_math('4 2 +')
    [4, 2, '+']
    >>> parse_math(' 4\t+ 2\t')
    [4, '+', 2]
    >>> parse_math('4 + 2 / 1')
    [4, '+', 2, '/', 1]
    >>> parse_math('-1')
    ['-', 1]
    >>> parse_math('10')
    [10]
    >>> parse_math('+-*/')
    ['+', '-', '*', '/']
    """
    pass
