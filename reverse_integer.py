import unittest


def reverse(num):
    rev_num = 0

    while num > 0:
        rem = num % 10
        rev_num = rev_num * 10 + rem
        num = num // 10

    return rev_num


class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(1234, reverse(4321))

    def test_case2(self):
        self.assertEqual(21, reverse(12))

    def test_case3(self):
        self.assertEqual(4, reverse(4))

    def test_case4(self):
        self.assertEqual(4, reverse(40))


if __name__ == '__main__':
    unittest.main()
