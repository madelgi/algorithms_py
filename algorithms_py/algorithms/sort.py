def bubble_sort(nums):
    """Bubble sort implementation.
    """
    compare_len = len(nums)
    while compare_len > 1:
        for i in range(compare_len - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        compare_len -= 1

    return nums


def insertion_sort(nums):
    """Insertion Sort implementation.
    """
    list_len = len(nums)
    for i in range(1, list_len):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1

    return nums


def merge_sort(nums):
    """Merge sort implementation.
    """
    list_len = len(nums)
    if list_len < 2:
        return nums

    left = []
    right = []
    mid = list_len/2
    for x in nums[:mid]:
        left.append(x)
    for x in nums[mid:]:
        right.append(x)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    """Helper function for merge sort.
    """
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    if left != []:
        result += left
    if right != []:
        result += right
    return result


def quicksort(nums):
    def quicksort_help(nums, start, end):
        if start < end:
            part = partition(nums, start, end)


def partition(nums, lo, hi):
    pivot = nums[hi]
    i = lo
    for j in range(lo, hi):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i]
