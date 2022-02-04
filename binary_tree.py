import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __eq__(self, other):
        if self is None and other is None:
            return True

        if other is None and self is not None:
            return False
        if other is not None and self is None:
            return False

        data_equal = self.data == other.data
        left_equal = self.left == other.left
        right_equal = self.right == other.right

        return data_equal and left_equal and right_equal

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data)

    def search(self, data):
        if self.root.data == data:
            return [self.root]
        nodes_in_path = []
        self.search_for_node(self.root, data, nodes_in_path)
        return nodes_in_path

    def search_for_node(self, node, data, nodes_in_path):
        nodes_in_path.append(node)
        if data < node.data:
            self.search_for_node(node.left, data, nodes_in_path)
        elif data > node.data:
            self.search_for_node(node.right, data, nodes_in_path)

    def successor(self, data):
        nodes_in_path = self.search(data)
        node = nodes_in_path[-1]
        if node.right is not None:
            node = node.right
            while True:
                if node.left is not None:
                    node = node.left
                else:
                    return node.data
        for node in nodes_in_path[::-1]:
            if node.data > data:
                return node.data
        return None

    def predecessor(self, data):
        nodes_in_path = self.search(data)
        node = nodes_in_path[-1]
        if node.left is not None:
            node = node.left
            while True:
                if node.right:
                    node = node.right
                else:
                    return node.data

        for node in nodes_in_path[::-1]:
            if node.data < data:
                return node.data
        return None

    def height_of_tree(self, node):
        if node is None:
            return 0
        left_height = self.height_of_tree(node.left)
        right_height = self.height_of_tree(node.right)

        return 1 + max(left_height, right_height)

    @property
    def height(self):
        if self.root is None:
            return 0
        return self.height_of_tree(self.root)

    def __eq__(self, other):
        r1 = self.root
        r2 = other.root
        return r1 == r2


class MyTestCase(unittest.TestCase):
    def test_insert(self):
        tree = BinaryTree()
        tree.insert(10)

        expected = BinaryTree()
        expected.root = Node(10)

        self.assertEqual(expected, tree)

        tree.insert(12)
        expected.root.right = Node(12)
        self.assertEqual(expected, tree)

        tree.insert(8)
        expected.root.left = Node(8)
        self.assertEqual(expected, tree)

        tree.insert(9)
        expected.root.left.right = Node(9)
        self.assertEqual(expected, tree)

    def test_successor(self):
        tree = BinaryTree()
        tree.root = Node(32)
        tree.root.left = Node(10)
        tree.root.left.left = Node(1)
        tree.root.left.right = Node(19)
        tree.root.left.right.left = Node(16)
        tree.root.left.right.right = Node(23)
        tree.root.right = Node(55)
        tree.root.right.left = Node(40)
        tree.root.right.right = Node(79)

        self.assertEqual(40, tree.successor(32))
        self.assertEqual(55, tree.successor(40))
        self.assertEqual(79, tree.successor(55))
        self.assertEqual(None, tree.successor(79))
        self.assertEqual(32, tree.successor(23))
        self.assertEqual(19, tree.successor(16))
        self.assertEqual(10, tree.successor(1))
        self.assertEqual(23, tree.successor(19))
        self.assertEqual(16, tree.successor(10))

    def test_predecessor(self):
        tree = BinaryTree()
        tree.root = Node(32)
        tree.root.left = Node(10)
        tree.root.left.left = Node(1)
        tree.root.left.right = Node(19)
        tree.root.left.right.left = Node(16)
        tree.root.left.right.right = Node(23)
        tree.root.right = Node(55)
        tree.root.right.left = Node(40)
        tree.root.right.right = Node(79)

        self.assertEqual(23, tree.predecessor(32))
        self.assertEqual(40, tree.predecessor(55))
        self.assertEqual(55, tree.predecessor(79))
        self.assertEqual(19, tree.predecessor(23))
        self.assertEqual(10, tree.predecessor(16))
        self.assertEqual(None, tree.predecessor(1))
        self.assertEqual(16, tree.predecessor(19))

    def test_height(self):
        tree = BinaryTree()
        self.assertEqual(0, tree.height)

        tree.root = Node(32)
        self.assertEqual(1, tree.height)

        tree.root.left = Node(10)
        tree.root.left.left = Node(1)
        self.assertEqual(3, tree.height)

        tree.root.left.right = Node(19)
        tree.root.left.right.left = Node(16)
        tree.root.left.right.right = Node(23)
        self.assertEqual(4, tree.height)

        tree.root.right = Node(55)
        tree.root.right.left = Node(40)
        tree.root.right.right = Node(79)
        self.assertEqual(4, tree.height)

if __name__ == '__main__':
    unittest.main()
