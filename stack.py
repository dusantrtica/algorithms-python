import unittest


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def stack_size(self):
        return len(self.stack)


class MyTestCase(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        self.assertEqual(0, stack.stack_size())
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(3, stack.stack_size())
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())

        self.assertEqual(0, stack.stack_size())


if __name__ == '__main__':
    unittest.main()
