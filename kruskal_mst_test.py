import pytest

class Node:
    def __init__(self, rank, node_id, parent=None):
        self.rank = rank
        self.node_id = node_id
        self.parent = parent


class DisjointSetNaive:
    def __init__(self, vertices):
        self.sets = set(vertices)

    def find(self, node):
        for vertex_set in self.sets:
            if node in vertex_set:
                return vertex_set[0]
        return None

    def merge(self, node1, node2):
        set1 = None
        set2 = None

        for vertex_set in self.sets:
            if node1 in vertex_set:
                set1 = vertex_set
            if node2 in vertex_set:
                set2 = vertex_set
        if set1 == set2:
            return

        new_set = set1 + set2
        self.sets.remove(set1)
        self.sets.remove(set2)

        self.sets.add("".join(sorted(new_set)))


def kruskal(edges, disjoint_set):
    # sort edges with regards of edge weight
    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    edges_in_mst = []
    for (u, v, weight) in sorted_edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            edges_in_mst.append((u, v, weight))
            disjoint_set.merge(u, v)

    return sorted(edges_in_mst, key=lambda edge: edge[0])


def test_spanning_tree():
    graph = [
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
    ]

    mst = kruskal(graph, DisjointSetNaive(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
    expected_mst = [
        ('a', 'b', 2),
        ('b', 'd', 3),
        ('b', 'e', 3),
        ('c', 'd', 1),
        ('c', 'f', 2),
        ('d', 'g', 5)
    ]

    assert mst == expected_mst


def test_disjoint_set_naive():
    vertices = ['a', 'b', 'c', 'd', 'e']
    disjoint_set = DisjointSetNaive(vertices)
    assert disjoint_set.find('a') == 'a'
    assert disjoint_set.find('b') == 'b'
    assert disjoint_set.find('x') is None

    disjoint_set.merge('a', 'a')
    assert disjoint_set.sets == {'a', 'b', 'c', 'd', 'e'}
    assert disjoint_set.find('b') == 'b'

    disjoint_set.merge('a', 'b')
    assert disjoint_set.sets == {'ab', 'c', 'd', 'e'}
    assert disjoint_set.find('b') == 'a'

    disjoint_set.merge('b', 'c')
    assert disjoint_set.sets == {'abc', 'd', 'e'}
    assert disjoint_set.find('c') == 'a'
    assert disjoint_set.find('d') == 'd'

    disjoint_set.merge('a', 'c')
    assert disjoint_set.sets == {'abc', 'd', 'e'}

    disjoint_set.merge('e', 'c')
    assert disjoint_set.sets == {'abce', 'd'}

    disjoint_set.merge('a', 'e')
    assert disjoint_set.sets == {'abce', 'd'}

    disjoint_set.merge('a', 'd')
    assert disjoint_set.sets == {'abcde'}
    assert disjoint_set.find('d') == 'a'
