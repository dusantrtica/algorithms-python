from functools import reduce
from heap import Heap
class Graph(list):
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for item in self:
            if item not in other:
                return False
        return True


def edges_by_vertex(graph):
    def add_edge_to_vertex_map(edge, map):
        (u, v, cost) = edge
        if u in map:
            map[u].append((v, cost))
        else:
            map[u] = [(v, cost)]

    vertices = {}
    reduce(lambda edge: add_edge_to_vertex_map(edge, vertices), graph)
    return vertices


def prim_mst(graph):
    visited = set()
    heap = Heap(lambda e1, e2: e1[2] - e2[2])
    for u, edges_from_u in edges_by_vertex(graph).items():
        if u not in visited:
            visited.add(u)
        for edge in edges_from_u:
            pass

    mst = []
    return mst


def test_prim_mst():
    graph = Graph([
        ('a', 'b', 1),
        ('a', 'c', 2),
        ('a', 'd', 12),
        ('b', 'd', 4),
        ('b', 'e', 7),
        ('b', 'g', 8),
        ('c', 'd', 6),
        ('c', 'f', 3),
        ('d', 'f', 5),
        ('d', 'e', 2),
        ('e', 'f', 4),
        ('e', 'g', 9),
        ('f', 'g', 2)
    ])

    expected_mst = Graph([
        ('a', 'b', 1),
        ('a', 'c', 2),
        ('b', 'd', 4),
        ('c', 'f', 3),
        ('d', 'e', 2),
        ('e', 'f', 4),
        ('f', 'g', 2)
    ])

    assert prim_mst(graph) == expected_mst


def test_prim_another_graph():
    graph = Graph([
        ('a', 'b', 2),
        ('a', 'c', 6),
        ('a', 'e', 5),
        ('a', 'f', 10),
        ('b', 'd', 3),
        ('b', 'e', 3),
        ('c', 'd', 1),
        ('c', 'f', 2),
        ('d', 'e', 4),
        ('d', 'g', 5),
        ('f', 'g', 5)
    ])

    mst = prim_mst(graph)
    expected_mst = [
        ('a', 'b', 2),
        ('b', 'd', 3),
        ('b', 'e', 3),
        ('c', 'd', 1),
        ('c', 'f', 2),
        ('d', 'g', 5)
    ]

    assert mst == expected_mst
