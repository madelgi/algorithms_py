def merge_sort(nums):
    """Merge sort implementation.

    Arguments
        nums: An unsorted array of numbers.

    Returns
        A sorted array of numbers.
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
