from logging import logMultiprocessing
import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __eq__(self, other):
        if other == self:
            return True
        return self.data == other.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        actual = self.head
        while actual.nextNode is not None:
            actual = actual.nextNode

        actual.nextNode = new_node

    def __eq__(self, other):
        head1 = self.head
        head2 = other.head

        while True:
            if head1 is None and head2 is not None:
                return False
            if head2 is None and head1 is not None:
                return False

            if head1 is None and head2 is None:
                return True

            if head1.data != head2.data:
                return False

            head1 = head1.nextNode
            head2 = head2.nextNode

    def remove(self, data):
        if self.head is None:
            return

        actual_node = self.head
        prev_node = None

        while actual_node is not Node and actual_node.data != data:
            prev_node = actual_node
            actual_node = actual_node.next

        if actual_node is None:
            return

        if prev_node is None:
            self.head = self.head.nextNode
        else:
            prev_node.nextNode = actual_node.nextNode


class TestListEquality(unittest.TestCase):
    def test_insert_start1(self):
        l1 = LinkedList()
        l2 = LinkedList()
        self.assertEqual(l1, l2)

    def test_insert_start2(self):
        l1 = LinkedList()
        l1.insert_start(10)

        l2 = LinkedList()
        l2.head = Node(10)
        self.assertEqual(l1, l2)

    def test_insert_start3(self):
        l1 = LinkedList()
        l1.insert_start(10)
        l1.insert_start(12)

        l2 = LinkedList()
        l2.head = Node(12)
        l2.head.nextNode = Node(10)
        self.assertEqual(l1, l2)

    def test_insert_end1(self):
        l1 = LinkedList()
        l1.insert_end(10)

        l2 = LinkedList()
        l2.head = Node(10)
        self.assertEqual(l1, l2)

    def test_insert_end2(self):
        l1 = LinkedList()
        l1.insert_end(10)
        l1.insert_end(12)

        l2 = LinkedList()
        l2.head = Node(10)
        l2.head.nextNode = Node(12)
        self.assertEqual(l1, l2)

    def test_remove_from_empty_list(self):
        l1 = LinkedList()
        l1.remove(10)
        self.assertEqual(LinkedList(), l1)

    def test_remove(self):
        l1 = LinkedList()
        l1.head = Node(10)
        l1.remove(10)
        self.assertEqual(l1, LinkedList())

    def test_remove_first_elem(self):
        l1 = LinkedList()
        l1.head = Node(10)
        l1.head.nextNode = Node(12)
        l1.remove(10)

        l2 = LinkedList()
        l2.head = Node(12)
        self.assertEqual(l1, l2)

    def remove_other_cases(self):
        l1 = LinkedList()
        l1.head = Node(10)
        l1.head.nextNode = Node(11)
        l1.head.nextNode.nextNode = Node(12)

        l1.remove(11)

        l2 = LinkedList()
        l2.head = Node(10)
        l2.head.nextNode = Node(12)
        self.assertEqual(l1, l2)

        l1.remove(12)
        l2 = LinkedList()
        l2.head = Node(10)
        self.assertEqual(l1, l2)


if __name__ == '__main__':
    unittest.main()
