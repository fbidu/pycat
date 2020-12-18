# pylint:disable=missing-module-docstring

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
