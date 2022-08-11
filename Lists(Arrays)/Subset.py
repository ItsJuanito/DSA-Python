
def find_subsets(nums):
    # create a subsets list
    subsets = []
    # append an empty set to the list
    subsets.append([])
    # loop through each element in nums
    for n in nums:
        # loop through each element in subset
        for i in range(len(subsets)):
            # copy the ith element and store it in temp list
            temp = subsets[i].copy()
            # append the current element to the temp list
            temp.append(n)
            # add the temp list to the subset
            subsets.append(temp)
    # return the subset
    return subsets

nums = [1, 3]
print(find_subsets(nums))
nums2 = [1, 5, 3]
print(find_subsets(nums2))
