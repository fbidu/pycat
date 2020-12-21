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

    def __init__(self, strategy="simple", history_limit=10, keep_history=True):
        try:
            self.strategy = getattr(self, strategy)
        except AttributeError as e:
            raise Exception(f"Invalid {strategy=}") from e
        self.keep_history = keep_history

        if self.keep_history:
            self._setup_history(history_limit)

    def _setup_history(self, history_limit):
        """
        Sets up the history backend

        Args:
            history_limit (int): How much entries to keep in history
        """
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

    def _parse_filenames(self, _filenames):
        """Parses a list of filenames. If any of them is in the format
        of `#x`, the filename is swapped with the x-th most recent
        accessed item in history. If history is disabled and any
        filename contains this format, an error will be raised.

        Args:
            _filenames (list): List of filenames to be parsed

        Raises:
            Exception: When any filename starts with # and `keep_history`
                is false, an exception is raised

        Returns:
            list: A list of parsed filenames
        """
        filenames = []

        if any(f.startswith("#") for f in _filenames) and not self.keep_history:
            raise Exception("History is disabled")

        for filename in _filenames:
            if filename.startswith("#"):
                index = int(filename[1:])
                filenames.append(self.history.pop(index))
            else:
                filenames.append(filename)
        return filenames

    def _write_history(self, filenames):
        """Writes filenames to history and saves it to a file.

        Args:
            filenames (list): List of files to be add to history.
        """
        if self.keep_history:
            self.history.extend(filenames)

            with open(self.history_path, "w") as history_data:
                history_data.write(self.history.to_json())

    def __call__(self, *args, **kwargs):
        filenames = self._parse_filenames(args)
        self._write_history(filenames)
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
