import unittest
from stack import Stack


class StackWithMax:
    def __init__(self):
        self.stack = Stack()
        self.max_values_stack = Stack()

    def push(self, data):
        if self.stack.stack_size() == 0:
            self.max_values_stack.push(data)
        else:
            self.max_values_stack.push(max(self.max_values_stack.peek(), data))

        self.stack.push(data)

    def pop(self):
        self.max_values_stack.pop()
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def stack_size(self):
        return self.stack.stack_size()

    @property
    def max(self):
        return self.max_values_stack.peek()

class MyTestCase(unittest.TestCase):
    def test_max_stack(self):
        stack = StackWithMax()

        stack.push(2) # 2 max = 2
        self.assertEqual(2, stack.max)

        stack.push(1) # 2, 1 -> max = 2
        self.assertEqual(2, stack.max)

        stack.push(4) # 2, 1, 4, max = 4
        self.assertEqual(4, stack.max)

        stack.push(0) # 2, 1, 4, 0, max = 4
        self.assertEqual(4, stack.max)

        stack.push(5) # 2, 1, 4, 0, 5, max = 5
        self.assertEqual(5, stack.max)

        stack.pop() # 2, 1, 4, 0, max = 4
        self.assertEqual(4, stack.max)

        stack.pop() # 2, 1, 4, max = 4
        self.assertEqual(4, stack.max)

        stack.pop() # 2, 1, max = 2
        self.assertEqual(2, stack.max)

        stack.pop() # 2
        self.assertEqual(2, stack.max)

if __name__ == '__main__':
    unittest.main()
