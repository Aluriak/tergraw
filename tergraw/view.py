"""
Definition relative to a view, ie a defaultdict containing
the view of the graph.

"""
from operator import itemgetter
from collections import defaultdict
from .constant import REWRITABLE_LETTERS


def clean(matrix):
    """Return a copy of given matrix where keys associated
    to space values are discarded"""
    return defaultdict(lambda: ' ', {
        k: v for k, v in matrix.items() if v != ' '
    })


def build(matrix):
    """Yield lines generated from given matrix"""
    max_x = max(matrix, key=lambda t: t[0])[0]
    min_x = min(matrix, key=lambda t: t[0])[0]
    max_y = max(matrix, key=lambda t: t[1])[1]
    min_y = min(matrix, key=lambda t: t[1])[1]
    yield from (
        # '{}:'.format(j).ljust(4) + ''.join(matrix[i, j] for i in range(min_x, max_x+1))
        ''.join(matrix[i, j] for i in range(min_x, max_x+1))
        for j in range(min_y, max_y+1)
    )


def next_unwrittable_on_row(view, coords):
    """Return position of the next (in row) letter that is unwrittable"""
    x, y = coords
    maxx = max(view.keys(), key=itemgetter(0))[0]
    for offset in range(x + 1, maxx):
        letter = view[offset, y]
        if letter not in REWRITABLE_LETTERS:
            return offset
    return None


def next_unwrittable_on_col(view, coords):
    """Return position of the next letter (in column) that is unwrittable"""
    x, y = coords
    maxy = max(view.keys(), key=itemgetter(1))[1]
    for offset in range(y + 1, maxy):
        letter = view[x, offset]
        if letter not in REWRITABLE_LETTERS:
            return offset
    return None


def previous_unwrittable_on_row(view, coords):
    """Return position of the previous (in row) letter that is unwrittable"""
    x, y = coords
    minx = -1
    for offset in range(x - 1, minx, -1):
        letter = view[offset, y]
        if letter not in REWRITABLE_LETTERS:
            return offset
    return None


def previous_unwrittable_on_col(view, coords):
    """Return position of the previous (in column) letter that is unwrittable"""
    x, y = coords
    miny = -1
    for offset in range(y - 1, miny, -1):
        letter = view[x, offset]
        if letter not in REWRITABLE_LETTERS:
            return offset
    return None
