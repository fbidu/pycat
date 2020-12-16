"""
(re) implementations of UNIX's `cat`
"""


def simple(*filenames):
    """
    Simple cat implementation using `open` and `print`.
    Prints to stdout the contents of `filename`
    """
    for filename in filenames:
        with open(filename) as f:
            print(f.read(), end="")
