from functools import reduce
from heap import Heap


class Graph(list):
    def __eq__(self, other):
        def reverse(item):
            (u, v, cost) = item
            return (v, u, cost)

        for item in self:
            if item not in other and reverse(item) not in other:
                return False
        return True


def edges_by_vertex(graph):
    def add_edge_to_vertex_map(edge, vertex_map):
        (u, v, cost) = edge
        if u in vertex_map:
            vertex_map[u].append(edge)
        else:
            vertex_map[u] = [edge]

        if v in vertex_map:
            vertex_map[v].append((v, u, cost))
        else:
            vertex_map[v] = [(v, u, cost)]

    vertices = {}
    for edge in graph:
        add_edge_to_vertex_map(edge, vertices)
    return vertices


def prim_jarnik_mst(graph):
    vertex_map = edges_by_vertex(graph)
    unvisited = set(vertex_map.keys())
    heap = Heap(lambda e1, e2: e2[2] - e1[2])
    mst = []
    total_cost = 0
    start_vertex = list(unvisited)[0]

    while unvisited:
        # consider all edges of actual vertex
        for (u, v, cost) in vertex_map[start_vertex]:
            if v in unvisited:
                heap.insert((u, v, cost))

        (u, v, cost) = heap.poll()

        if v in unvisited:
            mst.append((u, v, cost))
            total_cost += cost
            start_vertex = v
            unvisited.remove(v)

    return Graph(mst)

"""
simpathy - razumevanje, imam razumevanja
phrase - sintagma
false friends: simpathy and simpatija - znace razlicite stvari
cognate - many cognates: 
don't want to water it down or to dilute from it
dear implies initimacy and familiarity
mistank
"""

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
        ('c', 'f', 3),
        ('d', 'e', 2),
        ('e', 'f', 4),
        ('f', 'g', 2)
    ])

    assert prim_jarnik_mst(graph) == expected_mst


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

    mst = prim_jarnik_mst(graph)
    expected_mst = Graph([
        ('a', 'b', 2),
        ('b', 'd', 3),
        ('b', 'e', 3),
        ('c', 'd', 1),
        ('c', 'f', 2),
        ('f', 'g', 5)
    ])

    assert expected_mst == mst
