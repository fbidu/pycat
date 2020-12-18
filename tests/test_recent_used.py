"""
Tests for the RecentUsed class
"""
import pytest

from pycat.recent_used import RecentUsed

# pylint:disable=redefined-outer-name
@pytest.fixture
def recent_used():
    """
    Returns a new RecentUsed instance for each test
    """
    return RecentUsed()


def test_recent_used_instantiation(recent_used):
    """
    Can we create a new recent used instance?
    """
    assert isinstance(recent_used, RecentUsed)


def test_recent_used_initially_empty(recent_used):
    """
    A new RecentUsed instance must be empty
    """
    assert len(recent_used) == 0


def test_recent_used_accepts_filename(recent_used):
    """
    Can we register a new 'opened' filename?
    """
    recent_used.append("file1")

    # after adding, `len` should increase
    assert len(recent_used) == 1


def test_recent_used_accepts_filename(recent_used):
    """
    Can we register a new 'opened' filename?
    """
    recent_used.append("file1")

    # after adding, `len` should increase
    assert len(recent_used) == 1


def test_file_index(recent_used):
    """
    Can we access files in the history by
    their index?
    """
    recent_used.append("file1")
    recent_used.append("file2")
    recent_used.append("file3")

    assert recent_used[0] == "file1"
    assert recent_used[1] == "file2"
    assert recent_used[2] == "file3"


def test_pop_returns_latest_file(recent_used):
    """
    Can we `pop` the latest file?
    """
    recent_used.append("file1")
    recent_used.append("file2")
    recent_used.append("file3")

    assert recent_used.pop() == "file3"
