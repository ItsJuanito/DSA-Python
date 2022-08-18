def find_max_in_bitonic_array(nums):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if mid == len(nums) - 1:
            return nums[mid]
        if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            start = mid + 1
        else:
            if mid - 1 >= 0 and nums[mid] > nums[mid - 1]:
                return nums[mid]
            elif mid == 0:
                return nums[mid]
            else:
                end = mid - 1

nums = [1, 3, 8, 12, 4, 2]
print(find_max_in_bitonic_array(nums))