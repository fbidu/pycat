"""
(re) implementations of UNIX's `cat`
"""


def simple(filename):
    """
    Simple cat implementation using `open` and `print`.
    Prints to stdout the contents of `filename`
    """
    with open(filename) as f:
        print(f.read(), end="")
