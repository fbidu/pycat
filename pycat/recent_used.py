# pylint:disable=missing-module-docstring, too-many-ancestors

from collections import UserList


class RecentUsed(UserList):
    """
    RecentUsed remembers last recently opened files
    """

    def __init__(self, data=None, limit=None):
        if not data:
            data = []

        self.data = data
        self.set = set(data)
        self.limit = limit

        super().__init__()

    def append(self, item) -> None:
        if self.limit and len(self) == self.limit:
            self.set.remove(self[0])
            del self[0]

        if item in self.set:
            self.remove(item)
        else:
            self.set.add(item)

        super().append(item)

    def pop(self, i=-1):
        return self[i]
