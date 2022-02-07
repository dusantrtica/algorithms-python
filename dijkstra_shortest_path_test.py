import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.adj_list = []


class NodeInTraversal(Node):
    def __init__(self):
        self.visited = False
        self.predecessor = None
        self.min_distance = float('inf')

    def __lt__(self, other):
        return self.min_distance < other.min_distance


def dijkstra_shortest_path(start_node):
    visited = {}
    predecessors = {}
    distances = {}
    heap = []

    heapq.heappush(heap, start_node)

    return {}, {}


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
        'b': ['a', 'b'],
        'c': ['a', 'e', 'f', 'c'],
        'd': ['a', 'e', 'f', 'c', 'd'],
        'e': ['a', 'e'],
        'f': ['a', 'e', 'f'],
        'g': ['a', 'e', 'f', 'c', 'g'],
        'h': ['a', 'h']
    }

    costs, paths = dijkstra_shortest_path(a)

    assert costs == expected_costs
    assert paths == expected_paths
