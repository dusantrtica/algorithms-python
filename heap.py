import unittest


class Heap:
    def __init__(self, cmp_fn):
        self.cmp = cmp_fn
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        item_index = len(self.heap) - 1

        self.fix_up(item_index)

    def fix_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.cmp(self.heap[index], self.heap[parent_index]) > 0:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    def peek(self):
        return self.heap[0]

    def poll(self):
        max_item = self.peek()
        last_item_index = len(self.heap) - 1
        self.heap[last_item_index], self.heap[0] = self.heap[0], self.heap[last_item_index]
        del self.heap[last_item_index]
        self.fix_down(0)
        return max_item

    def fix_down(self, index):
        left_child_idx = index * 2 + 1
        right_child_idx = index * 2 + 2
        size = len(self.heap)
        largest_index = index

        if left_child_idx < size and self.cmp(self.heap[left_child_idx], self.heap[index]) > 0:
            largest_index = left_child_idx

        if right_child_idx < size and self.cmp(self.heap[right_child_idx], self.heap[largest_index]) > 0:
            largest_index = right_child_idx

        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)

    def is_empty(self):
        return len(self.heap) == 0


def is_min_heap(input):
    """
    :param heap: collection of items
    :return: True if the collection satisfies min heap properties, otherwise False
    """
    size = len(input)

    def is_leaf(index):
        return index >= size

    def is_heap_satisfied(parent_idx):
        if is_leaf(parent_idx):
            return True

        left_child_idx = parent_idx * 2 + 1
        right_child_idx = parent_idx * 2 + 2

        is_left_child_ok = is_leaf(left_child_idx) or input[parent_idx] < input[left_child_idx]
        is_right_child_ok = is_leaf(right_child_idx) or input[parent_idx] < input[right_child_idx]

        return is_right_child_ok and \
               is_left_child_ok and \
               is_heap_satisfied(left_child_idx) and \
               is_heap_satisfied(right_child_idx)

    if len(input) == 0 or len(input) == 1:
        return True

    return is_heap_satisfied(0)


def is_min_heap_iter(input):
    size = len(input) // 2
    for i in range(size):
        if input[i] > input[2 * i + 1] or input[i] > input[2 * i + 2]:
            return False

    return True


def max_to_min_heap(input):
    size = len(input)

    def fix_down(index):
        left_child_idx = 2 * index + 1
        right_child_idx = 2 * index + 2

        smallest_index = index
        if left_child_idx < size and input[left_child_idx] < input[index]:
            smallest_index = left_child_idx

        if right_child_idx < size and input[right_child_idx] < input[smallest_index]:
            smallest_index = right_child_idx

        if smallest_index != index:
            input[index], input[smallest_index] = input[smallest_index], input[index]
            fix_down(smallest_index)

    for i in range((len(input) - 2) // 2, -1, -1):
        fix_down(i)

    return input


class MyTestCase(unittest.TestCase):
    def test_heap(self):
        heap = Heap(lambda x, y: x - y)
        self.assertTrue(heap.is_empty())
        heap.insert(4)
        heap.insert(3)
        heap.insert(5)
        heap.insert(10)
        heap.insert(2)
        heap.insert(12)

        self.assertEqual(12, heap.poll())
        self.assertEqual(10, heap.poll())
        self.assertEqual(5, heap.poll())
        self.assertEqual(4, heap.poll())
        self.assertEqual(3, heap.poll())
        self.assertEqual(2, heap.poll())
        self.assertTrue(heap.is_empty())

    def test_is_min_heap(self):
        self.assertTrue(is_min_heap([1, 2, 3, 4, 5, 6, 7]))
        self.assertTrue(is_min_heap([1, 10, 4, 17, 20, 7, 9]))
        self.assertFalse(is_min_heap([4, 5, 2]))
        self.assertFalse(is_min_heap([1, 10, 4, 17, 3]))

    def test_is_min_heap_iter(self):
        self.assertTrue(is_min_heap_iter([1, 2, 3, 4, 5, 6, 7]))
        self.assertTrue(is_min_heap_iter([1, 10, 4, 17, 20, 7, 9]))
        self.assertFalse(is_min_heap_iter([4, 5, 2]))
        self.assertFalse(is_min_heap_iter([1, 10, 4, 17, 3]))

    def test_max_to_min_heap(self):
        self.assertTrue(is_min_heap(max_to_min_heap([10, 9, 8, 7, 6, 5, 4, 3])))
        self.assertTrue(is_min_heap(max_to_min_heap([10, 9, 8])))


if __name__ == '__main__':
    unittest.main()
