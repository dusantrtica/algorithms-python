import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.prev_node = None
        self.next_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node

    def insert_first(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            node.next_node = self.head
            self.head.prev_node = node
            self.head = node

    def __eq__(self, other):
        actual_node = self.head
        other_node = other.head
        while True:
            if actual_node is None and other_node is None:
                return True

            if actual_node is None and other_node is not None:
                return False
            if other_node is None and actual_node is not None:
                return False

            if other_node.data != actual_node.data:
                return False

            actual_node = actual_node.next_node
            other_node = other_node.next_node


class MyTestCase(unittest.TestCase):
    def test_insert(self):
        l = DoublyLinkedList()
        l.insert(10)

        exp = DoublyLinkedList()
        exp.head = Node(10)
        exp.tail = exp.head
        self.assertEqual(exp, l)


if __name__ == '__main__':
    unittest.main()
