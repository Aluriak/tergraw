"""
Constants definition.

"""
from enum import Enum


# DEFAULT_GRAPHVIZ_PROG = 'neato'
# DEFAULT_GRAPHVIZ_PROG = 'twopi'
# DEFAULT_GRAPHVIZ_PROG = 'dot'
DEFAULT_GRAPHVIZ_PROG = 'fdp'  # best results so far

class Direction(Enum):
    Up, Right, Down, Left = range(4)

CORNER_UPRIGHT, CORNER_UPLEFT     = '└', '┘'
CORNER_DOWNRIGHT, CORNER_DOWNLEFT = '┌', '┐'
BAR_UPDOWN, BAR_LEFT_RIGHT = '│', '─'
REWRITABLE_LETTERS = (' ',)

# {current direction, next direction: character to be printed}
CHARACTER = {  # {current direction, next direction: character to be printed}
    (Direction.Down, Direction.Right) : CORNER_UPRIGHT,
    (Direction.Left, Direction.Up)    : CORNER_UPRIGHT,

    (Direction.Right, Direction.Up)  : CORNER_UPLEFT,
    (Direction.Down, Direction.Left) : CORNER_UPLEFT,

    (Direction.Up, Direction.Right)  : CORNER_DOWNRIGHT,
    (Direction.Left, Direction.Down) : CORNER_DOWNRIGHT,

    (Direction.Right, Direction.Down) : CORNER_DOWNLEFT,
    (Direction.Up, Direction.Left)    : CORNER_DOWNLEFT,

    (Direction.Up, Direction.Up)       : BAR_UPDOWN,
    (Direction.Right, Direction.Right) : BAR_LEFT_RIGHT,
    (Direction.Down, Direction.Down)   : BAR_UPDOWN,
    (Direction.Left, Direction.Left)   : BAR_LEFT_RIGHT,
}

# '↳ ↲ ↱ ↰ ↵ '
# '↗ ↖ ↙ ↘'
# {current direction, next direction: oriented arrow to be printed}
ORIENTATION = {
    (Direction.Down, Direction.Right) : '↳',  # or ↘
    (Direction.Left, Direction.Up)    : '⬑',  # or ↖

    (Direction.Right, Direction.Up)  : '⬏',  # or ↗
    (Direction.Down, Direction.Left) : '↲',  # or ↙

    (Direction.Up, Direction.Right)  : '↱',  # or ↗
    (Direction.Left, Direction.Down) : '⬐',  # or ↙

    (Direction.Right, Direction.Down) : '⬎',  # or ↘
    (Direction.Up, Direction.Left)    : '↰',  # or ↖

    (Direction.Up, Direction.Up)       : '↑',
    (Direction.Right, Direction.Right) : '→',
    (Direction.Down, Direction.Down)   : '↓',
    (Direction.Left, Direction.Left)   : '←',
}

# START_ORIENTATION = {
    # (Direction.Down, Direction.Right) : '↳',  # or ↘
    # (Direction.Left, Direction.Up)    : '↥',  # or ↖

    # (Direction.Right, Direction.Up)  : '↥',  # or ↗
    # (Direction.Down, Direction.Left) : '↲',  # or ↙

    # (Direction.Up, Direction.Right)  : '↱',  # or ↗
    # (Direction.Left, Direction.Down) : '↧',  # or ↙

    # (Direction.Right, Direction.Down) : '↴',  # or ↘
    # (Direction.Up, Direction.Left)    : '↰',  # or ↖

    # (Direction.Up, Direction.Up)       : '↥',
    # (Direction.Right, Direction.Right) : '↦',
    # (Direction.Down, Direction.Down)   : '↧',
    # (Direction.Left, Direction.Left)   : '↤',
# }
