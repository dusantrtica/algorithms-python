from collections import deque

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


def partition_hoare(nums, left, right):
    pivot_index = (left + right) // 2
    pivot = nums[pivot_index]
    i = left
    j = right
    while True:
        if i >= j:
            return i
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        swap(nums, i, j)

    return i


def quicksort(nums, left, right, partition_fn=partition):
    if left >= right:
        return

    pivot_index = partition_fn(nums, left, right)
    quicksort(nums, left, pivot_index - 1)
    quicksort(nums, pivot_index + 1, right)


def quicksort_iter(nums):
    n = len(nums)
    stack = deque()

    stack.append((0, n-1))

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        pivot_index = partition(nums, left, right)
        stack.append((left, pivot_index-1))
        stack.append((pivot_index + 1, right))


def test_quicksort():
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    quicksort(nums, 0, len(nums) - 1)
    assert nums == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_quicksort_case2():
    nums = [23, 6, -1, 0, 12, 8, 3, 1]
    sorted_nums = sorted(nums)
    quicksort(nums, 0, len(nums) - 1)
    assert nums == sorted_nums


def test_quicksort_hoare():
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    quicksort(nums, 0, len(nums) - 1, partition_fn=partition_hoare)
    assert nums == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_quicksort_case2_hoare():
    nums = [23, 6, -1, 0, 12, 8, 3, 1]
    sorted_nums = sorted(nums)
    quicksort(nums, 0, len(nums) - 1, partition_fn=partition_hoare)
    assert nums == sorted_nums


def test_quicksort_iter1():
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    quicksort_iter(nums)
    assert nums == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_quicksort_iter2():
    nums = [23, 6, -1, 0, 12, 8, 3, 1]
    sorted_nums = sorted(nums)
    quicksort_iter(nums)
    assert nums == sorted_nums
