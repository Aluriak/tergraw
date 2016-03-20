"""
Unit tests about the main API.

"""
import pytest
from tergraw import pretty_view


def test_str_output():
    graph = {'a': {'b', 'c'}, 'd': {'b', 'e'}, 'f': {'g'}}
    for line in pretty_view(graph):
        assert isinstance(line, str)

