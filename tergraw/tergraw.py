"""
Implementation of graph printing routines.

"""
import itertools
from collections import defaultdict

from .constant import (Direction, DEFAULT_GRAPHVIZ_PROG, CHARACTER,
                       ORIENTATION, REWRITABLE_LETTERS)
from . import graphutils
from . import view


def _is_up(source, target):
    return source[1] - target[1] > 0
def _is_right(source, target):
    return source[0] - target[0] < 0
def _is_down(source, target):
    return source[1] - target[1] < 0
def _is_left(source, target):
    return source[0] - target[0] > 0

# iter of (predicate, source position transform, edge character):
DIRECTIONS = (
    (_is_up,    (lambda s: (s[0], s[1] - 1)), Direction.Up),
    (_is_right, (lambda s: (s[0] + 1, s[1])), Direction.Right),
    (_is_down,  (lambda s: (s[0], s[1] + 1)), Direction.Down),
    (_is_left,  (lambda s: (s[0] - 1, s[1])), Direction.Left),
)


@graphutils.process_input_graph
def create_layout(graph, graphviz_prog=DEFAULT_GRAPHVIZ_PROG):
    """Return {node: position} for given graph"""
    graphviz_layout = graphutils.graphviz_layout(graph, prog=graphviz_prog)
    # print('GRAPHIZ LAYOUT:', graphviz_layout)
    layout = {k: (int(x // 10), int(y // 10))
              for k, (x, y) in graphviz_layout.items()}
    # apply an offset for layouts to get all position >= 0
    max_x = max(layout.values(), key=lambda t: t[0])[0]
    min_x = min(layout.values(), key=lambda t: t[0])[0]
    max_y = max(layout.values(), key=lambda t: t[1])[1]
    min_y = min(layout.values(), key=lambda t: t[1])[1]
    offset_x = - min(0, min_x)
    offset_y = - min(0, min_y)
    return {
        node: (offset_x + x, offset_y + y)
        for node, (x, y) in layout.items()
    }


@graphutils.process_input_graph
def pretty_view(graph, oriented=False, construction=False,
                graphviz_prog=DEFAULT_GRAPHVIZ_PROG):
    """Yield strings, printable view of given graph"""
    layout = create_layout(graph, graphviz_prog=graphviz_prog)
    matrix_view = defaultdict(lambda: ' ')

    # Add the edge to the view

    # print('GRAPH EDGES:', tuple(graph.edges()))
    # print('LAYOUT:', layout)

    edges = ((layout[source], layout[target])
             for source, target in graph.edges())
    # print('EDGES:', tuple(edges))

    for source, target in edges:
        previous_edge_char = None
        previous_position = source
        while source != target:
            for is_dir, transform, edge_char in DIRECTIONS:
                first_loop = previous_edge_char is None
                if is_dir(source, target):
                    previous_source = source
                    source = transform(source)
                    if not first_loop:  # first loop: no previous char
                        char = CHARACTER[previous_edge_char, edge_char]
                        if not isinstance(char, str):
                            char = char.value
                        matrix_view[previous_source] = char
                        if construction:
                            old = defaultdict(lambda: ' ', matrix_view)
                            yield view.build(matrix_view)
                        assert isinstance(matrix_view[previous_source], str)
                    if source != target:
                        previous_edge_char = edge_char
                    previous_position = previous_source
                    break  # for loop ; don't test the remain directions

        if oriented:
            matrix_view[previous_position] = ORIENTATION[previous_edge_char, edge_char]
        if construction:
            yield view.build(matrix_view)

    # mark the place where nodes labels will be added
    # for node, coords in layout.items():
        # matrix_view[coords] = node[0]
    # Add the node labels to the view
    # matrix_view = view.clean(matrix_view)
    for node, (x, y) in layout.items():
        if len(node) == 1:
            matrix_view[x, y] = node
            continue
        row_min, row_max = (view.previous_unwrittable_on_row(matrix_view, (x, y)),
                            view.next_unwrittable_on_row(matrix_view, (x, y)))
        col_min, col_max = (view.previous_unwrittable_on_col(matrix_view, (x, y)),
                              view.next_unwrittable_on_col(matrix_view, (x, y)))
        # print('NODE ' + node + ':',
              # '→row: [{};{}]'.format(row_min, row_max).ljust(20),
              # '↓col: [{};{}]'.format(col_min, col_max))
        print_coords = [itertools.count(x), itertools.cycle((y,))]
        if row_min is None:  # write left to right, end at (x, y)
            if row_max is None or row_max > (x + len(node) / 2):  # enough space at the right
                factor = 2
            else:
                factor = 1
            print_coords[0] = tuple(
                x - (len(node) // factor) + offset + 1
                for offset in range(len(node))
            )
            # print('DEBUG 1:', y, len(node), print_coords[0])
        elif row_max is None:  # write left to right, beginning at (x, y)
            if row_min < (x - len(node) / 2):  # enough space at the left
                factor = 1
            else:
                factor = 0
            print_coords[0] = tuple(
                x + offset - (len(node) // 2) * factor
                for offset in range(len(node))
            )
            # print('DEBUG 2:', print_coords[0])
        elif (row_max - row_min) > len(node) + 1:  # write left to right, if enough place
            print_coords[0] = tuple(
                x + offset
                for offset in range(len(node))
            )
            # print('DEBUG 3:', print_coords[0])

        elif col_min is None:  # write up to down, end at (x, y)
            if col_max is None or col_max > (x + len(node) / 2):  # enough space at the right
                factor = 2
            else:
                factor = 1
            print_coords = (itertools.cycle((x,)), tuple(
                y - (len(node) // factor) + offset + 1
                for offset in range(len(node))
            ))
            # print('DEBUG 4:', y, len(node), print_coords[1])
        elif col_max is None:  # write up to down, beginning at (x, y)
            if col_min < (x - len(node) / 2):  # enough space at the left
                factor = 1
            else:
                factor = 0
            print_coords = (itertools.cycle((x,)), tuple(
                y + offset - (len(node) // 2) * factor
                for offset in range(len(node))
            ))
            # print('DEBUG 5:', print_coords[1])
        elif (col_max - col_min) > len(node) + 1:  # write up to down, if enough place
            print_coords = (itertools.cycle((x,)), tuple(
                y + offset
                for offset in range(len(node))
            ))
            # print('DEBUG 6:', print_coords[1])
        else:  # not enough space
            if (row_max - row_min) > (col_max - col_min):
                # more space on Y axis
                node = node[:row_max - row_min]  # cut the node
                print_coords = (itertools.cycle((x,)), tuple(
                    x + offset
                    for offset in range(len(node))
                ))
                # print('DEBUG 7:', print_coords[1])
            else:
                # more space on X axis
                node = node[:col_max - col_min]  # cut the node
                print_coords[0] = tuple(
                    x + offset
                    for offset in range(len(node))
                )
                # print('DEBUG 8:', print_coords[0])

        for letter, i, j in zip(node, *print_coords):
            matrix_view[i, j] = letter




    if construction:
        yield view.build(matrix_view)
    else:
        yield from view.build(matrix_view)
