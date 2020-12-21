"""
(re) implementations of UNIX's `cat`
"""
from json.decoder import JSONDecodeError
from pathlib import Path

from .recent_used import RecentUsed


class Cat:
    """
    Cat implements different strategies for the `cat` UNIX command.

    ## Usage

    >>> cat = Cat()
    >>> cat("filename")
    """

    def __init__(self, strategy="simple", history_limit=10):
        try:
            self.strategy = getattr(self, strategy)
        except AttributeError as e:
            raise Exception(f"Invalid {strategy=}") from e

        self.history_path = Path.home() / ".pycat_history.json"

        if self.history_path.is_file():
            try:
                with open(self.history_path, "r") as history_data:
                    self.history = RecentUsed.from_json(history_data.read())
            except JSONDecodeError:
                self.history_path.unlink()
                self.history = RecentUsed(limit=history_limit)
        else:
            self.history = RecentUsed(limit=history_limit)

    def __call__(self, *args, **kwargs):
        filenames = []

        for filename in args:
            if filename.startswith("$"):
                index = int(filename[1:])
                filenames.append(self.history.pop(index))
            else:
                filenames.append(filename)

        self.history.extend(filenames)

        with open(self.history_path, "w") as history_data:
            history_data.write(self.history.to_json())

        if kwargs.get("dry_run"):
            return None

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
