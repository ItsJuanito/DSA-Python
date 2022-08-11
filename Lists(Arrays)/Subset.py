
def find_subsets(nums):
    subset = []
    subset.append([])

    for n in nums:
        for i in range(len(subset)):
            temp = subset[i].copy()
            temp.append(n)
            subset.append(temp)
    return subset

nums = [1, 3]
print(find_subsets(nums))
nums2 = [1, 5, 3]
print(find_subsets(nums2))
