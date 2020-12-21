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

    # TODO: Implementar esse teste para refatorar cats.py:31
    assert recent_used_populated.pop(0) == "file3"
    assert recent_used_populated.pop(1) == "file2"
    assert recent_used_populated.pop(2) == "file1"


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
    put at the top of the list
    """
    duplicate = recent_used_populated[0]
    recent_used_populated.append(duplicate)

    assert recent_used_populated.pop() == duplicate


def test_popped_items_are_kept(recent_used_populated):
    """
    After accessing the top of the list through the
    `pop` method, the item should be kept on
    the list
    """
    top = recent_used_populated.pop()
    assert recent_used_populated.pop() == top


def test_history_is_bounded():
    """
    Can we add a limit to the history's size?
    """
    bounded = RecentUsed(limit=2)
    assert isinstance(bounded, RecentUsed)


def test_history_bound_is_respected():
    """
    After going over the limit, the oldest element
    must be removed and the newest one be added
    """
    bounded = RecentUsed(limit=2)
    bounded.append("file1")
    bounded.append("file2")
    bounded.append("file3")

    assert len(bounded) == 2


def test_can_clean_history(recent_used_populated):
    """
    Test if we can clean the whole history
    """
    recent_used_populated.clear()

    assert len(recent_used_populated) == 0


def test_equality():
    """
    Can we compare two histories?
    """

    history_a = RecentUsed(limit=3)
    history_b = RecentUsed(limit=3)
    history_c = RecentUsed(limit=4)

    for h in (history_a, history_b, history_c):
        h.append("file1")
        h.append("file2")

    assert history_a == history_b
    assert history_b != history_c


def test_json_serialization(recent_used_populated):
    """
    Can we save and restore an history from a json string?
    """
    serialized = recent_used_populated.to_json()
    assert serialized == '{"data": ["file1", "file2", "file3"], "limit": null}'

    history = RecentUsed.from_json(serialized)
    assert history == recent_used_populated
