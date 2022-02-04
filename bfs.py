class Node:
    def __init__(self, name):
        self.name = name
        self.adj_list = []


def bfs(start_node, accept):
    queue = []
    visited = {}
    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if not visited.get(node.name):
            visited[node.name] = True
            accept(node)
            for neighbors in node.adj_list:
                queue.append(neighbors)


def test():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.adj_list = [b, c]
    b.adj_list = [c, e]
    c.adj_list = [d, f]
    d.adj_list = []
    e.adj_list = [f]
    f.adj_list = []

    traverse_result = []
    bfs(a, lambda node: traverse_result.append(node.name))
    assert sorted(traverse_result) == ['a', 'b', 'c', 'd', 'e', 'f']
