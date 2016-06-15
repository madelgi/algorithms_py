def bubble_sort(nums):
    """Bubble sort implementation.
    """
    compare_len = len(nums) - 1
    while compare_len > 0:
        for i in range(compare_len):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        compare_len -= 1

    return nums
