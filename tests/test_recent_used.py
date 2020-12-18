from pycat.recent_used import RecentUsed


def test_recent_used_instantiation():
    recent_used = RecentUsed()
    assert isinstance(recent_used, RecentUsed)


def test_recent_used_initially_empty():
    recent_used = RecentUsed()
    assert len(recent_used) == 0
