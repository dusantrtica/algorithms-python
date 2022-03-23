def bubble_sort(nums):
    n = len(nums)
    while True:
        is_sorted = True
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                is_sorted = False
        if is_sorted:
            break

    return nums


# better in cases in which 'write' is more expensive
def selection_sort(nums):
    n = len(nums)
    for left in range(n):
        min_index = left
        for i in range(left, n):
            if nums[i] < nums[min_index]:
                min_index = i
        nums[min_index], nums[left] = nums[left], nums[min_index]
    return nums


def selection_sort_recursive(nums):
    if not nums:
        return
    min_index = 0
    for i in range(len(nums)):
        if nums[i] < nums[min_index]:
            min_index = i
    nums[0], nums[min_index] = nums[min_index], nums[0]

    selection_sort_recursive(nums[1:])


# adaptive, online algorithm
def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    return nums


def test_bubble_sort():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_selection_sort():
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_insertion_sort():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_insertion_sort_rec():
    nums = [5, 4, 3, 2, 1]
    selection_sort_recursive(nums)
    assert nums == [1, 2, 3, 4, 5]