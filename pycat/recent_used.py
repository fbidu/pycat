# pylint:disable=missing-module-docstring, too-many-ancestors

from collections import UserList
from json import dumps


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

        super().__init__()

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

    def pop(self, i=-1):
        """
        Returns the most recently accessed item without
        removing it.
        """
        return self[i]

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
        data = self.__dict__
        del data["set"]

        return dumps(data)
