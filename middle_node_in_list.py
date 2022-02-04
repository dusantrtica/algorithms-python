import unittest
from linked_list import LinkedList, Node


def find_middle_node(linked_list):
    curr_node = linked_list.head
    faster_node = curr_node.nextNode if curr_node is not None else None
    while faster_node is not None:
        curr_node = curr_node.nextNode
        faster_node = faster_node.nextNode
        if faster_node is not None:
            faster_node = faster_node.nextNode

    return curr_node.data


class MyTestCase(unittest.TestCase):
    def test_1(self):
        l = LinkedList()
        l.head = Node(10)
        l.head.nextNode = Node(11)
        l.head.nextNode.nextNode = Node(12)
        self.assertEqual(11, find_middle_node(l))

    def test_2(self):
        l = LinkedList()
        l.head = Node(10)
        l.head.nextNode = Node(11)
        l.head.nextNode.nextNode = Node(12)
        l.head.nextNode.nextNode.nextNode = Node(13)
        l.head.nextNode.nextNode.nextNode.nextNode = Node(14)
        self.assertEqual(12, find_middle_node(l))


if __name__ == '__main__':
    unittest.main()
