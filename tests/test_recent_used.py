from pycat.recent_used import RecentUsed


def test_recent_used_instantiation():
    """
    Can we create a new recent used instance?
    """
    recent_used = RecentUsed()
    assert isinstance(recent_used, RecentUsed)


def test_recent_used_initially_empty():
    """
    A new RecentUsed instance must be empty
    """
    recent_used = RecentUsed()
    assert len(recent_used) == 0


def test_recent_used_accepts_filename():
    """
    Can we register a new 'opened' filename?
    """
    recent_used = RecentUsed()
    recent_used.append("file1")
