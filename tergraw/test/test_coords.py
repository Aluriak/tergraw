"""
Unit testing of coordinates related functions.

"""
from tergraw.tergraw import _is_up, _is_down, _is_right, _is_left



def test_up():
    assert     _is_up((0, 1), (0, 0))
    assert not _is_up((0, 0), (0, 1))

def test_right():
    assert     _is_right((0, 0), (1, 0))
    assert not _is_right((1, 0), (0, 0))

def test_down():
    assert     _is_down((0, 0), (0, 1))
    assert not _is_down((0, 1), (0, 0))

def test_left():
    assert     _is_left((1, 0), (0, 0))
    assert not _is_left((0, 0), (1, 0))
