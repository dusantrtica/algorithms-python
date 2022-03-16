import random


def bogo_sort(nums):
    def is_sorted():
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True

    # Fisher-Yates approach: we generate a new permutation in O(N)
    def shuffle():
        for i in range(len(nums) - 2, -1, -1):
            j = random.randint(0, i + 1)
            nums[i], nums[j] = nums[j], nums[i]

    while not is_sorted():
        shuffle()

    return nums


def test():
    assert bogo_sort([3, 2, 1, 5, 7]) == [1, 2, 3, 5, 7]
    assert bogo_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
