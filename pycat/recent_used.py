# pylint:disable=missing-module-docstring, too-many-ancestors

from collections import UserList


class RecentUsed(UserList):
    """
    RecentUsed remembers last recently opened files
    """

    def __init__(self, data=None):
        if not data:
            data = []

        self.data = data

        super().__init__()

    def append(self, item) -> None:
        if not item in self:
            return super().append(item)
