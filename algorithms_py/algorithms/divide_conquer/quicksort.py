def quicksort(nums):
    """Quicksort implementation.

    Arguments
        nums: An unsorted array of numbers.

    Returns
        A sorted array of numbers.
    """
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
