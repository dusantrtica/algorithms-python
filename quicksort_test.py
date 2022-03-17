def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


def partition(nums, left, right):
    pivot_index = (left + right) // 2
    swap(nums, pivot_index, right)

    i = left
    for j in range(left, right):  # range does not include latest element
        if nums[j] < nums[right]:
            swap(nums, i, j)
            i += 1
    swap(nums, i, right)
    return i


def quicksort(nums, left, right):
    if left >= right:
        return

    pivot_index = partition(nums, left, right)
    quicksort(nums, left, pivot_index - 1)
    quicksort(nums, pivot_index + 1, right)


def test_quicksort():
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    quicksort(nums, 0, len(nums) - 1)
    assert nums == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_quicksort_case2():
    nums = [23, 6, -1, 0, 12, 8, 3, 1]
    sorted_nums = sorted(nums)
    quicksort(nums, 0, len(nums) - 1)
    assert nums == sorted_nums
