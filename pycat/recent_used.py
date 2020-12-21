# pylint:disable=missing-module-docstring, too-many-ancestors

from collections import UserList
from json import dumps, loads


class RecentUsed(UserList):
    """
    RecentUsed remembers most recently opened files.
    """

    def __init__(self, data=None, limit=None):
        if not data:
            data = []

        self.data = data
        self.set = set(data)
        self.limit = limit

        super().__init__(initlist=data)

    @classmethod
    def from_json(cls, data):
        """
        Given a valid JSON string in `data` creates a new instance
        """
        data_ = loads(data)
        return cls(**data_)

    def append(self, item):
        """
        Adds a new item to the history.

        If the history's len is equal to `limit`,
        it removes the oldest item and inserts the new one.
        """
        if self.limit and len(self) == self.limit:
            self.set.remove(self[0])
            del self[0]

        if item in self.set:
            self.remove(item)
        else:
            self.set.add(item)

        super().append(item)

    def extend(self, other) -> None:
        for item in other:
            self.append(item)

    def pop(self, i=0):
        """
        Returns the most recently accessed item without
        removing it.

        Arguments:
             i {integer} - The index to be popped, relative to the most recent
                           access. That is:

                            * `i=0` returns the most recent entry.
                            * `i=1` returns the second most recent entry.
                            * `i=2` returns the third most recent entry and so on

        >>> r = RecentUsed()
        >>> r.append("file1")
        >>> r.append("file2")

        >>> r.pop()
        'file2'

        >>> r.pop(0)
        'file2'

        >>> r.pop(1)
        'file1'
        """
        return self[-1 - i]

    def __eq__(self, o):
        """
        Two RecentUsed objects are the same if they:
            - Have the same data stored

            AND

            - Have the same limit
        """
        return self.data == o.data and self.limit == o.limit

    def to_json(self):
        """
        Returns a JSON representation of the current object
        """
        data = self.__dict__.copy()
        if "set" in data:
            del data["set"]

        return dumps(data)
