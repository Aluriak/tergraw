"""
Definition of utilitary routines working on graphs.

Define also the interface with networkx module.

"""

from functools import wraps
import networkx as nx


def dict_to_nx(graph, oriented=False):
    """Return an nx.Graph equivalent of given {node: succs}"""
    nxg = nx.DiGraph() if oriented else nx.Graph()
    for node, succs in graph.items():
        for succ in succs:
            nxg.add_edge(node, succ)
    return nxg


def process_input_graph(func):
    """Decorator, ensuring first argument is a networkx graph object.
    If the first arg is a dict {node: succs}, a networkx graph equivalent
    to the dict will be send in place of it."""
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        input_graph = args[0]
        if isinstance(input_graph, nx.DiGraph):
            return func(*args, **kwargs)
        else:
            nx_graph = dict_to_nx(args[0], oriented=True)
            args = [nx_graph] + list(args[1:])
            return func(*args, **kwargs)
    return wrapped_func


def graphviz_layout(nx_graph, prog):
    """Return the layout computed for given networkx (Di)Graph instance"""
    return nx.nx_pydot.graphviz_layout(nx_graph, prog=prog)
