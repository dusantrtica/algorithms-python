from heap import Heap


class Node:
    def __init__(self, name):
        self.name = name
        self.adj_list = []


def bellman_ford_shortest_path(start_node, other_nodes_with_edges):
    def get_all_vertices_and_edges():
        _vertices = {start_node.name}
        all_edges = list(
            map(lambda x: [x.name, [(y[0].name, y[1]) for y in x.adj_list]], [start_node, *other_nodes_with_edges]))
        _edges = []
        for edge in all_edges:
            u = edge[0]
            _vertices.add(u)
            others = edge[1]
            for v, cost in others:
                _vertices.add(v)
                _edges.append((u, v, cost))
        return _vertices, _edges

    visited = {}
    predecessors = {}
    distances = {
        start_node.name: 0
    }

    def get_distance(node_name):
        if node_name in distances:
            return distances.get(node_name)
        return float('inf')

    vertices, edges = get_all_vertices_and_edges()

    for vertex in vertices:
        for (u, v, cost) in edges:
            distance_to_u = get_distance(u)
            if distance_to_u + cost < get_distance(v):
                distances[v] = distance_to_u + cost
                predecessors[v] = u

    return distances, predecessors


def test_shortest_path():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')

    a.adj_list = [(b, 5), (h, 8), (e, 9)]
    b.adj_list = [(d, 15), (c, 12), (h, 4)]
    c.adj_list = [(d, 3), (g, 11)]
    d.adj_list = [(g, 9)]
    e.adj_list = [(h, 5), (f, 4), (g, 20)]
    f.adj_list = [(c, 1), (g, 13)]
    g.adj_list = []
    h.adj_list = [(c, 7), (f, 6)]

    expected_costs = {
        'a': 0,
        'b': 5,
        'c': 14,
        'd': 17,
        'e': 9,
        'f': 13,
        'g': 25,
        'h': 8
    }

    expected_paths = {
        'b': 'a',
        'c': 'f',
        'd': 'c',
        'e': 'a',
        'f': 'e',
        'g': 'c',
        'h': 'a'
    }

    costs, paths = bellman_ford_shortest_path(a, [b, c, d, e, f, g, h])

    assert costs == expected_costs
    assert paths == expected_paths


def test_negative_weights():
    a = Node('a')
    b = Node('b')
    c = Node('c')

    a.adj_list = [(b, 5), (c, 2)]
    b.adj_list = [(c, -10)]
    c.adj_list = []

    expected_costs = {
        'a': 0,
        'b': 5,
        'c': -5
    }

    expected_paths = {
        'b': 'a',
        'c': 'b'
    }

    costs, paths = bellman_ford_shortest_path(a, [b, c])

    assert costs == expected_costs
    assert paths == expected_paths
