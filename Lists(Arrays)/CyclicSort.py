
def cyclicSort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums

nums = [3, 1, 5, 4, 2]
print(cyclicSort(nums))
nums2 = [2, 6, 4, 3, 1, 5]
print(cyclicSort(nums2))
nums3 = [1, 5, 6, 4, 3, 2]
print(cyclicSort(nums3))
