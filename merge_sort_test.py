def merge(a, b):
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    k = 0
    l = [0] * (m + n)
    while i < n and j < m:
        if a[i] < b[j]:
            l[k] = a[i]
            i += 1
        else:
            l[k] = b[j]
            j += 1
        k += 1

    while i < n:
        l[k] = a[i]
        k += 1
        i += 1
    while j < m:
        l[k] = b[j]
        j += 1
        k += 1

    return l


def merge_sort(nums):
    n = len(nums)
    if n < 2:
        return nums

    mid = n // 2
    left_arr = merge_sort(nums[0:mid])
    right_arr = merge_sort(nums[mid:n])

    return merge(left_arr, right_arr)


def test_1():
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == merge_sort(nums)


def test_2():
    nums = [23, 6, -1, 0, 12, 8, 3, 1]
    sorted_nums = sorted(nums)
    assert sorted_nums == merge_sort(nums)
