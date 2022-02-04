class Node:
    def __init__(self, name):
        self.name = name
        self.adj_list = []


def dfs(start_node, accept):
    stack = []
    visited = {}
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if not visited.get(node.name):
            visited[node.name] = True
            accept(node)
            for neighbor in node.adj_list:
                stack.append(neighbor)

def dfs_rec(node, accept, visited = {}):
    if node.name in visited:
        return
    accept(node)
    visited[node.name] = True
    for neighbor in node.adj_list:
        if neighbor.name not in visited:
            dfs_rec(neighbor, accept, visited)

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
    dfs(a, lambda node: traverse_result.append(node.name))
    assert sorted(traverse_result) == ['a', 'b', 'c', 'd', 'e', 'f']

def test_dfs_nondirected():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.adj_list = [b, c]
    b.adj_list = [a, c, e]
    c.adj_list = [a, b, d, f]
    d.adj_list = [c]
    e.adj_list = [b, f]
    f.adj_list = [c, e]

    traverse_result = []
    dfs(a, lambda node: traverse_result.append(node.name))
    assert sorted(traverse_result) == ['a', 'b', 'c', 'd', 'e', 'f']

def test_dfs_rec_nondirected():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.adj_list = [b, c]
    b.adj_list = [a, c, e]
    c.adj_list = [a, b, d, f]
    d.adj_list = [c]
    e.adj_list = [b, f]
    f.adj_list = [c, e]

    traverse_result = []
    visited = {}
    dfs_rec(a, lambda node: traverse_result.append(node.name), visited)
    assert sorted(traverse_result) == ['a', 'b', 'c', 'd', 'e', 'f']
