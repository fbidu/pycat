"""
(re) implementations of UNIX's `cat`
"""


class Cat:
    """
    Cat implements different strategies for the `cat` UNIX command.

    ## Usage

    >>> cat = Cat()
    >>> cat("filename")
    """

    def __init__(self, strategy="simple"):
        try:
            self.strategy = getattr(self, strategy)
        except AttributeError as e:
            raise Exception(f"Invalid {strategy=}") from e

    def __call__(self, *args):
        return self.strategy(*args)

    @staticmethod
    def simple(*filenames):
        """
        Simple cat implementation using `open` and `print`.
        Prints to stdout the contents of `filename`
        """
        for filename in filenames:
            with open(filename) as f:
                print(f.read(), end="")
