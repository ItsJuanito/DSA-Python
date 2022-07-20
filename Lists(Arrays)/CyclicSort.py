
def cyclicSort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums

print([2, 3, 1, 4, 5])
print(cyclicSort([2, 3, 1, 4, 5]))