import unittest


def is_palindrom(word):
    n = len(word)

    for i in range(int(n/2)):
        if word[i] != word[n-i-1]:
            return False

    return True


class Test(unittest.TestCase):
    def test_case1(self):
        self.assertTrue(is_palindrom("anavolimilovana"))

    def test_case2(self):
        self.assertTrue(is_palindrom("dulejelud"))

    def test_case3(self):
        self.assertFalse(is_palindrom("neki obican tekst"))


if __name__ == '__main__':
    unittest.main()
