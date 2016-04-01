"""
Unit tests on the view module.

"""

import pytest
from tergraw import view
from tergraw.constant import REWRITABLE_LETTERS


@pytest.fixture()
def row_view():
    # create the view                                  0123456789
    return {(0, y): letter for y, letter in enumerate("   X    X ")}

@pytest.fixture()
def col_view():
    # create the view                                  0123456789
    return {(x, 0): letter for x, letter in enumerate("   X    X ")}


def test_letter_rewrittable():
    assert 'X' not in REWRITABLE_LETTERS
    assert ' ' in REWRITABLE_LETTERS


def test_next_row_on_row_view_beg(row_view):
    assert view.next_unwrittable_on_row(row_view, (0, 0)) == 3

def test_next_row_on_row_view_first(row_view):
    assert view.next_unwrittable_on_row(row_view, (3, 0)) == 3

def test_next_row_on_row_view_mid(row_view):
    assert view.next_unwrittable_on_row(row_view, (4, 0)) == 8

def test_next_row_on_row_view_end(row_view):
    assert view.next_unwrittable_on_row(row_view, (9, 0)) is None

def test_prev_row_on_row_view_beg(row_view):
    assert view.previous_unwrittable_on_row(row_view, (2, 0)) is None

def test_prev_row_on_row_view_mid(row_view):
    assert view.previous_unwrittable_on_row(row_view, (7, 0)) == 3

def test_prev_row_on_row_view_end(row_view):
    assert view.previous_unwrittable_on_row(row_view, (9, 0)) == 8


def test_next_col_on_col_view_beg(col_view):
    assert view.next_unwrittable_on_col(col_view, (0, 0)) == 3

def test_next_col_on_col_view_first(col_view):
    assert view.next_unwrittable_on_col(col_view, (0, 3)) == 3

def test_next_col_on_col_view_mid(col_view):
    assert view.next_unwrittable_on_col(col_view, (0, 4)) == 8

def test_next_col_on_col_view_end(col_view):
    assert view.next_unwrittable_on_col(col_view, (0, 9)) is None

def test_prev_col_on_col_view_beg(col_view):
    assert view.previous_unwrittable_on_col(col_view, (0, 2)) is None

def test_prev_col_on_col_view_mid(col_view):
    assert view.previous_unwrittable_on_col(col_view, (0, 7)) == 3

def test_prev_col_on_col_view_end(col_view):
    assert view.previous_unwrittable_on_col(col_view, (0, 9)) == 8
