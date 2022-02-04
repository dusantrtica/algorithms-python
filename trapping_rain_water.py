import unittest


def trapping_rain_water(heights):
    n = len(heights)
    if n < 3:
        return 0

    max_left = [0] * n
    max_right = [0] * n
    water_by_position = [0] * n

    for i in range(1, n):
        max_left[i] = max(max_left[i-1], heights[i-1])

    for i in range(n-2, -1, -1):
        max_right[i] = max(max_right[i+1], heights[i+1])

    for i in range(n):
        water_at_curr_pos = min(max_left[i], max_right[i]) - heights[i]
        water_by_position[i] = water_at_curr_pos if water_at_curr_pos > 0 else 0

    return sum(water_by_position)


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(7, trapping_rain_water([4, 1, 3, 1, 5]))

    def test2(self):
        self.assertEqual(3, trapping_rain_water([2, 1, 3, 1, 4]))

    def test3(self):
        self.assertEqual(8, trapping_rain_water([1, 0, 2, 1, 3, 1, 2, 0, 3]))

    def test4(self):
        self.assertEqual(9, trapping_rain_water([4, 2, 0, 3, 2, 5]))


if __name__ == '__main__':
    unittest.main()
