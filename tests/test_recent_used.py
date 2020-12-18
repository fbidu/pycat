"""
Tests for the RecentUsed class
"""
import pytest

from pycat.recent_used import RecentUsed

# pylint:disable=redefined-outer-name
@pytest.fixture
def recent_used():
    """
    Returns a new empty RecentUsed instance for each test
    """
    return RecentUsed()


@pytest.fixture
def recent_used_populated():
    """
    Returns a new RecentUsed instance with items registered
    """
    recent_used = RecentUsed()
    recent_used.append("file1")
    recent_used.append("file2")
    recent_used.append("file3")

    return recent_used


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


def test_file_index(recent_used_populated):
    """
    Can we access files in the history by
    their index?
    """
    assert recent_used_populated[0] == "file1"
    assert recent_used_populated[1] == "file2"
    assert recent_used_populated[2] == "file3"


def test_pop_returns_latest_file(recent_used_populated):
    """
    Can we `pop` the latest file?
    """
    assert recent_used_populated.pop() == "file3"


def test_duplicated_file_is_unique(recent_used_populated):
    """
    After opening a duplicated file, it should be
    present in the list only once
    """
    duplicate = recent_used_populated[0]
    recent_used_populated.append(duplicate)

    assert recent_used_populated.count(duplicate) == 1


def test_duplicated_file_goes_to_top(recent_used_populated):
    """
    After opening a duplicated file, it should be
    present in the list only once
    """
    duplicate = recent_used_populated[0]
    recent_used_populated.append(duplicate)

    assert recent_used_populated.pop() == duplicate
