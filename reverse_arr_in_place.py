import unittest


def reverse(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return

    for i in range(n-1):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]


class Test(unittest.TestCase):
    def test_case1(self):
        arr = [1, 2, 3]
        reverse(arr)
        self.assertEqual([3, 2, 1], arr)

    def test_case2(self):
        arr = [1, 2]
        reverse(arr)
        self.assertEqual([2, 1], arr)

    def test_case3(self):
        arr = [1]
        reverse(arr)
        self.assertEqual([1], arr)

    def test_case3(self):
        arr = []
        reverse(arr)
        self.assertEqual([], arr)


if __name__ == '__main__':
    unittest.main()
