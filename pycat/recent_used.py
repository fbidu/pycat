# pylint:disable=missing-module-docstring
class RecentUsed:
    """
    RecentUsed remembers last recently opened files
    """

    def __init__(self, data=None):
        if not data:
            data = []

        self.data = data

    def __len__(self):
        return 0

    def append(self, item):
        """
        Adds a new file to the history
        """
        self.data.append(item)
