from heap import Heap


class Node:
    def __init__(self, name):
        self.name = name
        self.adj_list = []


def dijkstra_shortest_path(start_node):
    visited = {}
    predecessors = {}
    distances = {
        start_node.name: 0
    }

    def get_distance(node_name):
        if node_name in distances:
            return distances.get(node_name)
        return float('inf')

    heap = Heap(lambda node2, node1: get_distance(node1.name) - get_distance(node2.name))

    heap.insert(start_node)

    while not heap.is_empty():
        actual_vertex = heap.poll()
        if actual_vertex.name in visited:
            continue
        for (neighbour_node, cost_to_neighbour) in actual_vertex.adj_list:
            new_distance = get_distance(actual_vertex.name) + cost_to_neighbour
            if new_distance < get_distance(neighbour_node.name):
                distances[neighbour_node.name] = new_distance
                predecessors[neighbour_node.name] = actual_vertex.name
                heap.insert(neighbour_node)
        visited[actual_vertex.name] = True

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

    costs, paths = dijkstra_shortest_path(a)

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

    costs, paths = dijkstra_shortest_path(a)

    assert costs == expected_costs
    assert paths == expected_paths
