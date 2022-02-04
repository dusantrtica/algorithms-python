import unittest


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 0


class AVLTree:
    def __init__(self):
        # we can access root node exclusively
        self.root = None

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

    def get_predecessor(self, data):
        nodes_in_path = self.search(data)
        node = nodes_in_path[-1]
        if node.left is not None:
            node = node.left
            while True:
                if node.right:
                    node = node.right
                else:
                    return node

        for node in nodes_in_path[::-1]:
            if node.data < data:
                return node
        return None

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left)
        elif data > node.data:
            self.remove_node(data, node.right)
        else:
            # we have found the node we want to remove
            # case 1 - node is leaf node
            if node.left is None and node.right is None:
                parent = node.parent
                if parent is not None and parent.left == node:
                    parent.left = None
                if parent is not None and parent.right == node:
                    parent.right = None

                if parent is None:
                    self.root = None

                del node

                self.handle_violation(parent)
            # case 2 - one children
            elif node.left is None and node.right is not None:
                parent = node.parent

                if parent is not None:
                    if parent.left == node:
                        parent.left = node.right
                    if parent.right == node:
                        parent.right = node.right
                else:
                    self.root = node.right
                node.right.parent = parent
                del node

                self.handle_violation(parent)
            elif node.right is None and node.left is not None:
                parent = node.parent
                if parent is not None:
                    if parent.left == node:
                        parent.left = node.left
                    if parent.right == node:
                        parent.right = node.left
                else:
                    self.root = node.left

                node.left.parent = parent
                del node

                self.handle_violation(parent)

            else: # node has 2 children
                predecessor = self.get_predecessor(node.left)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.remove_node(data, predecessor)

    def calc_height(self, node):
        if node is None:
            return -1
        return node.height

    def calculate_balance(self, node):
        if node is None:
            return 0
        return self.calc_height(node.left) - self.calc_height(node.right)

    def violation_helper(self, node):
        balance = self.calculate_balance(node)
        if balance > 1:
            # left right heavy situation, left rotation on parent + right rotation on grandparent
            if self.calculate_balance(node.left) < 0:
                self.rotate_left(node.left)

            # this is the right rotation on grandparent (if left-left heavy , that's single right rotation)
            self.rotate_right(node)

        if balance < -1:
            if self.calculate_balance(node.right) > 0:
                self.rotate_right(node.right)
            self.rotate_left(node)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data, node)
                node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1

        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data, node)
                node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1

        # check if avl properties are violated or not
        self.handle_violation(node)

    def handle_violation(self, node):
        # check the nods from the node we have inserted up to root node
        while node is not None:
            node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
            self.violation_helper(node)
            node = node.parent

    def rotate_right(self, node):
        temp_left = node.left
        t = temp_left.right

        temp_left.right = node
        node.left = t
        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left
        temp_left.parent = temp_parent

        if temp_left.parent is not None and temp_left.parent.left == node:
            temp_left.parent.left = temp_left
        if temp_left.parent is not None and temp_left.parent.right == node:
            temp_left.parent.right = temp_left

        if node == self.root:
            self.root = temp_left

        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        temp_left.height = max(self.calc_height(temp_left.left), self.calc_height(temp_left.right)) + 1

    def rotate_left(self, node):
        temp_right = node.right
        t = temp_right.left

        temp_right.left = node
        node.right = t
        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right
        temp_right.parent = temp_parent

        if temp_right.parent is not None and temp_right.parent.left == node:
            temp_right.parent.left = temp_right

        if temp_right.parent is not None and temp_right.parent.right == node:
            temp_right.parent.right = temp_right

        if node == self.root:
            self.root = temp_right

        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        temp_right.height = max(self.calc_height(temp_right.left), self.calc_height(temp_right.right)) + 1



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
