"""
Implementation of graph printing routines.

"""
from collections import defaultdict

from .constant import Direction, DEFAULT_GRAPHVIZ_PROG, CHARACTER, ORIENTATION
from . import graphutils


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
def pretty_view(graph, oriented=False, graphviz_prog=DEFAULT_GRAPHVIZ_PROG):
    """Yield strings, printable view of given graph"""
    layout = create_layout(graph, graphviz_prog=graphviz_prog)
    matrix_view = defaultdict(lambda: ' ')

    # Add the edge to the view

    # iter of (predicate, source position transform, edge character):
    directions = (
        (_is_up,    (lambda s: (s[0], s[1] - 1)), Direction.Up),
        (_is_right, (lambda s: (s[0] + 1, s[1])), Direction.Right),
        (_is_down,  (lambda s: (s[0], s[1] + 1)), Direction.Down),
        (_is_left,  (lambda s: (s[0] - 1, s[1])), Direction.Left),
    )

    # print('GRAPH EDGES:', tuple(graph.edges()))
    # print('LAYOUT:', layout)

    edges = ((layout[source], layout[target])
             for source, target in graph.edges())
    # print('EDGES:', tuple(edges))

    for source, target in edges:
        previous_edge_char = None
        previous_position = source
        while source != target:
            for is_dir, transform, edge_char in directions:
                first_loop = previous_edge_char is None
                if is_dir(source, target):
                    previous_source = source
                    source = transform(source)
                    if not first_loop:  # first loop: no previous char
                        char = CHARACTER[previous_edge_char, edge_char]
                        if not isinstance(char, str):
                            char = char.value
                        matrix_view[previous_source] = char
                        assert isinstance(matrix_view[previous_source], str)
                    if source != target:
                        previous_edge_char = edge_char
                    previous_position = previous_source
                    break  # for loop ; don't test the remain directions

        if oriented:
            matrix_view[previous_position] = ORIENTATION[previous_edge_char, edge_char]

    # Add the node to the view
    for node, (x, y) in layout.items():
        for offset, letter in enumerate(node):
            coords = offset + x, y
            if coords not in matrix_view:
                matrix_view[coords] = letter
            elif matrix_view[coords] in REWRITABLE_LETTERS:
                matrix_view[coords] = letter
            else:  # not printable
                break

    return _build_view(matrix_view)


def _build_view(matrix):
    """Yield lines generated from given matrix"""
    max_x = max(matrix, key=lambda t: t[0])[0]
    min_x = min(matrix, key=lambda t: t[0])[0]
    max_y = max(matrix, key=lambda t: t[1])[1]
    min_y = min(matrix, key=lambda t: t[1])[1]
    yield from (
        ''.join(matrix[i, j] for i in range(min_x, max_x+1))
        for j in range(min_y, max_y+1)
    )


def _is_up(source, target):
    return source[1] - target[1] > 0
def _is_right(source, target):
    return source[0] - target[0] < 0
def _is_down(source, target):
    return source[1] - target[1] < 0
def _is_left(source, target):
    return source[0] - target[0] > 0
