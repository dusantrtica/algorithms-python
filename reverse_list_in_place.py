import unittest
from linked_list import LinkedList, Node


def reverse_list(linked_list):
    if linked_list.head is None or linked_list.head.nextNode is None:
        return

    new_next_node = None
    curr_head = linked_list.head
    while curr_head is not None:
        tmp_next_node = curr_head.nextNode
        curr_head.nextNode = new_next_node
        new_next_node = curr_head
        curr_head = tmp_next_node

    linked_list.head = new_next_node


class MyTestCase(unittest.TestCase):
    def test_empty_list(self):
        l = LinkedList()
        reverse_list(l)
        self.assertEqual(l, LinkedList())

    def test_single_element_list(self):
        l = LinkedList()
        l.head = Node(10)
        reverse_list(l)
        expected = LinkedList()
        expected.head = Node(10)
        self.assertEqual(expected, l)

    def test_two_element(self):
        l = LinkedList()
        l.head = Node(10)
        l.head.nextNode = Node(11)
        expected = LinkedList()
        expected.head = Node(11)
        expected.head.nextNode = Node(10)
        reverse_list(l)
        self.assertEqual(expected, l)

    def test_three_element(self):
        l = LinkedList()
        l.head = Node(10)
        l.head.nextNode = Node(11)
        l.head.nextNode.nextNode = Node(12)
        expected = LinkedList()
        expected.head = Node(12)
        expected.head.nextNode = Node(11)
        expected.head.nextNode.nextNode = Node(10)
        reverse_list(l)
        self.assertEqual(expected, l)


if __name__ == '__main__':
    unittest.main()
