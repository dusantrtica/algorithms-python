def count_sort(nums):
    smallest_value = min(nums)
    counts = [0 for _ in range(smallest_value, max(nums) + 1)]
    for num in nums:
        counts[num - smallest_value] += 1

    sorted_nums = []
    for index, count_num in enumerate(counts):
        for _ in range(count_num):
            sorted_nums.append(index + smallest_value)

    return sorted_nums


def test_count_sort_1():
    assert count_sort([4, 4, 3, 1, 1, 2]) == [1, 1, 2, 3, 4, 4]


def test_sort_negative():
    assert count_sort([-4, 1, 3, 2, 3, 2, -1]) == [-4, -1, 1, 2, 2, 3, 3]


def test_sort_big_gap():
    assert count_sort([100, 1, 2, 101]) == [1, 2, 100, 101]
