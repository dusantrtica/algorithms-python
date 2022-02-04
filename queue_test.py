import unittest

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    @property
    def size(self):
        return len(self.queue)

class MyTestCase(unittest.TestCase):
    def test_test_queue(self):
        queue = Queue()
        self.assertEqual(0, queue.size)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(3, queue.size)

        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())

        self.assertEqual(0, queue.size)


if __name__ == '__main__':
    unittest.main()
