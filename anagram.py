import unittest


def is_anagram(s, t):
    return len(s) == len(t) and sorted(s) == sorted(t)


class Test(unittest.TestCase):
    def test_case1(self):
        self.assertTrue(is_anagram("restful", "fluster"))


unittest.main()
