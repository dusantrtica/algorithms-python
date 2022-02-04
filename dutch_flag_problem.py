import unittest


def dutch_flag(input):
    zeroes_count = 0
    ones_count = 0
    twos_count = 0
    for i in input:
        if i == 0:
            zeroes_count += 1
        elif i == 1:
            ones_count += 1
        elif i == 2:
            twos_count += 1

    for i in range(len(input)):
        if zeroes_count > 0:
            input[i] = 0
            zeroes_count -= 1
        elif ones_count > 0:
            input[i] = 1
            ones_count -= 1
        elif twos_count > 0:
            input[i] = 2
            twos_count -= 1

    return input


class Test(unittest.TestCase):
    def test_case1(self):
        self.assertListEqual([0, 0, 1, 1, 2], dutch_flag([2, 1, 0, 1, 0]))


if __name__ == '__main__':
    unittest.main()
