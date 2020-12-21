"""
(re) implementations of UNIX's `cat`
"""
from .recent_used import RecentUsed


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

        self.history = RecentUsed()

    def __call__(self, *args):
        filenames = []

        for filename in args:
            if filename.startswith("$"):
                index = int(filename[1:])
                filenames.append(self.history.pop(-1 - index))
            else:
                filenames.append(filename)

        self.history.extend(filenames)
        return self.strategy(*filenames)

    @staticmethod
    def simple(*filenames):
        """
        Simple cat implementation using `open` and `print`.
        Prints to stdout the contents of `filename`
        """
        for filename in filenames:
            with open(filename) as f:
                print(f.read(), end="")

    @staticmethod
    def sys_write(*filenames):
        """
        Simple cat implementation using `sys.stdout` and `write`.
        Prints to stdout the contents of `filename`
        """
        from sys import stdout

        for filename in filenames:
            with open(filename) as f:
                stdout.write(f.read())
