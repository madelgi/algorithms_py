def insertion_sort(nums):
    """Insertion sort implementation.

    Argument:
        An array of unsorted numbers.

    Returns:
        An array of sorted numbers.
    """
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1

    return nums
