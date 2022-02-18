class Node:
    def __init__(self, rank, node_id, parent=None):
        self.rank = rank
        self.node_id = node_id
        self.parent = parent


class DisjointSet:
    def __init__(self, edges):
        sets = {}
        for edge in edges:
            sets.add(edge[0])
            sets.add(edge[1])
        self.root_nodes = [Node(0, v) for v in sets]

    def find(self, node):
        current_node = node
        while current_node.parent is not None:
            current_node = current_node.parent

        # apply path compression
        root = current_node
        current_node = node

        while current_node is not root:
            temp = current_node.parent
            current_node.parent = root
            current_node = temp

        return root.node_id

    def merge(self, node1, node2):
        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:
            return


def kruskal(graph):
    # sort edges with regards of edge weight
    sorted(graph, lambda edge: edge[2])
    disjoint_set = DisjointSet(graph)
    return []


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

    mst = kruskal(graph)
    expected_mst = [
        ('a', 'b', 2),
        ('b', 'd', 3),
        ('b', 'e', 3),
        ('c', 'd', 1),
        ('c', 'f', 2),
        ('f', 'g', 5)
    ]

    assert mst == expected_mst
